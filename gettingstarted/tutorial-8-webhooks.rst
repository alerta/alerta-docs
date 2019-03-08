.. _tutorial 8:

Use webhooks to extend Alerta
=============================

In this tutorial you will learn how to use custom webhooks to add
new integrations to Alerta to suit your environment.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Install a custom webhook`_
  * `Step 2: Write a custom webhook`_
  * `Next Steps`_

Overview
--------

Custom webhooks are a simple way of extending Alerta to support
additional monitoring tools without having to modify the core
source code. They are written in Python and are required to
implement a single method of a base class.

They are pre-loaded into memory and make available a new URL that
is then shared with the integrating system.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
where you installed Alerta as a uWsgi application served by nginx
on an Ubuntu Xenial server.

Step 1: Install a custom webhook
--------------------------------

To install a custom webhook you can either clone the git repository and
run ``python setup.py install`` from the plugin directory or you
can install the plugin directly using ``pip``.

For this tutorial use ``pip`` to install the ``sentry`` plugin::

    $ sudo pip install git+https://github.com/alerta/alerta-contrib.git#subdirectory=plugins/geoip

Modify the ``/etc/alertad.conf`` configuration file to enable the plugin
and use a different GeoIP lookup service than the default::

    $ sudo vi /etc/alertad.conf

::

    PLUGINS = ['reject','geoip']
    GEOIP_URL = 'http://ip-api.com/json'

Restart the uwsgi server so that Alerta API picks up the new configuration::

    $ sudo service uwsgi restart

Send a test alert and check that the attributes for the alert have been
populated with Geolocation information for the IP address of the
origin of the alert::

    $ alerta --debug send -r iot006 -e started -s normal -S IoT -E Production \
    -t 'iot006 has rebooted.'

.. code-block:: json

    {
      "alert": {
        "attributes": {
          "geoip": {
            "city": "Riga",
            "country_code": "LV",
            "country_name": "Latvia",
            "ip": "62.85.64.34",
            "latitude": 56.95,
            "longitude": 24.1,
            "metro_code": 0,
            "region_code": "RIX",
            "region_name": "Riga",
            "time_zone": "Europe/Riga",
            "zip_code": ""
          },
          "ip": "62.85.64.34"
        },
        "correlate": [],

.. note::

    The ``geoip`` plugin looks up the IP address that is passed to the
    Alerta API via the ``X-Forwarded-For`` HTTP header.

Step 2: Write a plugin
----------------------

The `base class for plugins`_ has three methods that **must** be implemented
and the ``__init__()`` method can optionally be implemented as well as long
as the Super class is also called.

.. _base class for plugins: http://docs.openstack.org/developer/stevedore/tutorial/creating_plugins.html#a-plugin-base-class

.. code-block:: python

    class ExamplePlugin(PluginBase):

        def __init__(self, name=None):

            # plugin-specific init goes here
            # if not required, leave "__init__()" out completely

            super(ExamplePlugin, self).__init__(name)

        def pre_receive(self, alert):

            # reject or modify an alert before it hits the database

            return alert

        def post_receive(self, alert):

            # after alert saved in database, forward alert to external systems

            return

        def status_change(self, alert, status, text):

            # triggered by external status changes, used by integrations

            return

Now that you know the basic implementation of a plugin you are going
to write one of your own to detect "flapping_" alerts.

.. _flapping: https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/flapping.html

To do this you are going to take advantage of the ``is_flapping()`` utility
method that takes an alert, a time window (in seconds) and a threshold
count and returns ``True`` if the number of alert severity changes
has exceeded the threshold.

.. code-block:: python

    import logging

    from alerta.exceptions import RateLimit
    from alerta.plugins import PluginBase

    LOG = logging.getLogger('alerta.plugins.transient')

    FLAPPING_COUNT = 2
    FLAPPING_WINDOW = 120  # seconds

    class TransientAlert(PluginBase):

        def pre_receive(self, alert):

            LOG.info("Detecting transient alerts...")
            if alert.is_flapping(window=FLAPPING_WINDOW, count=FLAPPING_COUNT):
                alert.severity = 'indeterminate'
                alert.attributes['flapping'] = True
                # uncomment following line to stop alerts from being processed
                # raise RateLimit("Flapping alert received more than %s times in %s seconds" % (FLAPPING_COUNT, FLAPPING_WINDOW))
            else:
                alert.attributes['flapping'] = False

            return alert

        def post_receive(self, alert):
            return

        def status_change(self, alert, status, text):
            return

The plugin above sets the severity to ``indeterminate`` and an attribute
called ``flapping`` (which can be used in other plugins to perhaps not
trigger an external notification for flapping alerts).

Alternatively, the alert could be rejected (using the ``RateLimit``
exception) or any other appropriate action can be taken that suits
your environment.

Copy the plugin code above, modifying it to suit your requirements, into
a file called ``alerta_transient.py`` and copy the following into another
file called ``setup.py``:

.. code-block:: python

    from setuptools import setup, find_packages

    version = '0.0.1'

    setup(
        name="alerta-transient",
        version=version,
        description='Example Alerta plugin for transient flapping alerts',
        url='https://github.com/alerta/alerta-contrib',
        license='Apache License 2.0',
        author='Your name',
        author_email='your.name@example.com',
        packages=find_packages(),
        py_modules=['alerta_transient'],
        install_requires=[],
        include_package_data=True,
        zip_safe=True,
        entry_points={
            'alerta.plugins': [
                'transient = alerta_transient:TransientAlert'
            ]
        }
    )

Next, install the plugin and add it to the list of enabled
plugins in the server configuration file, making sure to restart
uwsgi so that the Alerta server picks up the changes::

    $ sudo python setup.py install

::

    $ sudo vi /etc/alertad.conf

::

    PLUGINS = ['reject','transient']

Test the plugin by submitting multiple duplicate alerts in quick
succession. Depending on your implementation the Alerta server may
respond with a ``429 Rate Limited`` or update the alert with a
``flapping=True`` attribute.

Step 3: Route alerts to plugins
-------------------------------

By default, plugins are executed in the order in which they are
listed in the ``PLUGINS`` setting and all plugins are executed for
every alert.

In this step you are going to modify the default behaviour of plugins
by using a "routing" plugin to dynamically change which plugins
are run for an alert and in which order.

The most basic routing plugin is one that simply implements what is
the current behaviour. That is, it returns a list of the enabled
and loaded plugin entry points (not plugin names) of all the configured
plugins in the order they are listed.

.. code-block:: python

    def rules(alert, plugins):

        print(plugins)
        return plugins.values()

Copy the routing plugin code above into a file called ``routing.py``
and copy the following into a file called ``setup.py``:

.. code-block:: python

    from setuptools import setup, find_packages

    version = '0.0.1'

    setup(
        name="alerta-routing",
        version=version,
        description='Alerta routing rules for plugins',
        url='https://github.com/alerta/alerta-contrib',
        license='Apache License 2.0',
        author='Your name',
        author_email='your.name@example.com',
        packages=find_packages(),
        py_modules=['routing'],
        install_requires=[],
        include_package_data=True,
        zip_safe=True,
        entry_points={
            'alerta.routing': [
              'rules = routing:rules'
            ]
        }
    )

Next, install the routing plugin. There is no need to add it
to the ``alertad.conf`` file as it will be auto-detected. Do
not forget to restart uwsgi so that Alerta server picks up
the change though::

    $ sudo python setup.py install

Test the routing plugin by submitting an alert and the routing plugin
should print to stdout the order in which the plugins will be
executed. As a test, change the order of the listed ``PLUGINS``
in the ``alertad.conf`` file and confirm this is reflected in
the printed output.

Now that you have created a basic routing plugin the following
routing plugin simply demonstrates how to determine
which plugins should be executed for an alert at runtime. The
code below shows what to return if no plugins are wanted to be
executed, a subset of plugins should be executed, or all
configured plugins should be executed.

.. code-block:: python

    def rules(alert, plugins):

        if alert.text=='no plugins':
            return []
        elif alert.text=='reject only':
            return [plugins['reject']]
        elif alert.text=='all plugins':
            return plugins.values()

A more useful plugin would be one that doesn't call an external
notification like Slack_ unless an alert has been received at least
three times.

.. _Slack: https://github.com/alerta/alerta-contrib/tree/master/plugins/slack

.. code-block:: python

    def rules(alert, plugins):

        if alert.duplicate_count > 2:
            return [plugins['slack']]
        else:
            return []

The following routing plugin expands on the above but this time it
sends ``critical`` and ``major`` alerts to PagerDuty_ as well.

.. _PagerDuty: https://github.com/alerta/alerta-contrib/tree/master/plugins/pagerduty

.. code-block:: python

    def rules(alert, plugins):

        if alert.duplicate_count <= 2:
            return []
        elif alert.severity in ['critical', 'major']:
            return [plugins['slack'], plugins['pagerduty']]
        else:
            return [plugins['slack']]

Hopefully there are enough examples here to get you started developing
your own plugins. There are plenty of `contributed plugins`_ to refer to
and you are welcome to submit your plugins to the contrib repo for use
by the wider community.

.. _contributed plugins: https://github.com/alerta/alerta-contrib

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * :ref:`Use alert timeouts to expire stale alerts <tutorial 2>`
  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
