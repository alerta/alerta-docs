.. _tutorial 3:

Use plugins to enhance Alerta
=============================

In this tutorial you will learn how to use simple plugins to add
powerful new features to Alerta to suit your environment.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Install a plugin`_
  * `Step 2: Write a plugin`_
  * `Step 3: Route alerts to plugins`_
  * `Next Steps`_

Overview
--------

Plugins are a simple but effective way of extending the functionality
of Alerta without having to modify the core source code. They are written
in python and are required to implement all methods of a base class.

They are pre-loaded into memory so do not require (and should avoid)
having to read local disk for performance reasons, though this is not
enforced. Any dependent network services should be aggressively timed-out
so as not to cause latency issues in the Alerta API if the downstream
service is unavailable or slow.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
where you installed Alerta as a uWsgi application served by nginx
on an Ubuntu Xenial server.

Step 1: Install a plugin
------------------------

To install a plugin you can either clone the git repository and
run ``python setup.py install`` from the plugin directory or you
can install the plugin directly using ``pip``.

For this tutorial use ``pip`` to install the ``geoip`` plugin::

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

The base class for plugins has three methods that **must** be implemented
and the ``__init__()`` method can optionally be implemented as well as long
as the Super class is also called.

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
count and returns ``True`` if alert severity changes has exceeded the thresholds.

.. code-block:: python

    import logging

    from alerta.app import db
    from alerta.app.exceptions import RateLimit
    from alerta.plugins import PluginBase

    LOG = logging.getLogger('alerta.plugins.transient')

    FLAPPING_COUNT = 2
    FLAPPING_WINDOW = 120  # seconds

    class TransientAlert(PluginBase):

        def pre_receive(self, alert):

            LOG.info("Detecting transient alerts...")
            if db.is_flapping(alert, window=FLAPPING_WINDOW, count=FLAPPING_COUNT):
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

The plugin above sets an attribute called ``flapping`` which can be used in other
plugins to perhaps not trigger an external notification for flapping alerts.

Alternatively, the alert could be rejected (using the ``RateLimit`` exception) or
any other appropriate action can be taken that suits your environment.

Step 3: Route alerts to plugins
-------------------------------

TBC

https://github.com/guardian/alerta/tree/master/contrib/routing

you are expected to change it before you install it. maybe i should make that more clear.

it could be slightly more complicated and actually be a useful starting point though.

sure. you should set debug output if you put DEBUG = True in the alertad.conf file.

.. routing
.. Send to Slack only if it has been received more than twice::
.. resend emails after x https://github.com/alerta/alerta-contrib/issues/64

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * :ref:`Use alert timeouts to expire stale alerts <tutorial 2>`
  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
