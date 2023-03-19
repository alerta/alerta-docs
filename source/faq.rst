.. _faq:

Frequently Asked Questions
==========================

Alerta
------

Why can't I see any alerts in the web browser?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can send and query for alerts using the ``alerta`` CLI tool this
problem is almost certainly related to cross-origin browser errors. Open
up the Javascript developer console in your browser of choice and look
for CORS_ errors like::

    XMLHttpRequest cannot load http://api.alerta.io/alerts?status=open.
    No 'Access-Control-Allow-Origin' header is present on the requested
    resource. Origin 'http://web.alerta.io' is therefore not allowed access.

To fix this you can either serve the web UI from the `same origin`_ as
the API using a web server to :ref:`reverse proxy <reverse proxy>` the
web UI or ensure that the API server `allows the origin`_ where the
web UI is hosted by adding it to the :envvar:`CORS_ORIGINS` :ref:`server
configuration <CORS settings>` setting.

.. _CORS: https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
.. _same origin: https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
.. _allows the origin: https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Origin

Why do I need to set an ``environment`` and ``service`` when they are not mandatory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only ``resource`` and ``event`` are technically required to ensure that
Alerta can process alerts correctly. However, the "out-of-the-box" default
server setting for ``PLUGINS`` has the ``reject`` plugin enabled. This plugin
enforces an alert "policy" of requiring an ``environment`` attribute of either
``Production`` or ``Development`` and a value for the ``service`` attribute.

This is to encourage good habits early in defining useful alert attributes
that can be used to "namespace" alerts (this is what the ``environment``
attribute is for) and so that the web console can organise by ``environemnt``
and filter alerts by ``service``.

However, one of the principles of Alerta is not to enforce its view of the
world on users so the plugin can be :ref:`easily configured <plugin config>`,
:ref:`modified <tutorial 3>` or completely disabled. It's up to you.

Can I define custom severity codes and levels?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, you can now completely change the severity names, severity levels
and colours. See :ref:`webui` for more information.

How can I add a priority to an alert eg. High, Medium, Low?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use a custom attribute called ``priority`` when sending alerts to
Alerta::

    $ alerta send ... --attributes priority=high ...

Alerts of differing priority could be queried by ``alerta``
command-line tool using::

    $ alerta query --filters attributes.priority=high

Using the web console to sort alerts by priority as well as severity
would require some development effort.

What's the difference between `ack`, `close` and `delete`?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alerts are meant to auto-close when a corresponding `normal` or
`cleared` alert is received for that event-resource combination. If
no `normal` alert exists for a particular event (which may be the
case for alerts from log files or SNMP traps, for example) then the
alert will be deleted when the timeout period has expired. Alerts
timeout after 1 day by default but that is configurable on a
per-alert basis.

If, as an operator, you want to remove an event from view then you
can either `ack` the alert or DELETE it. If the alert is DELETED a
new alert with the same event-resource combination will trigger a
new notification email (if configured) whereas an `ack`'ed alert will
not.

Why don't you have a plugin or integration for X, where X is whatever you use in your job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We could spend countless hours writing plugins for everything and
never finish or we could focus on building an easily extensible
system with great documentation and let the end-user build the plugins
they need. Having said that, we have still created_ many_ `plugins`_
and integrations_ as working examples and we are not against writing
more if there is popular_ demand_. We are also happy to accept submissions.

What's this MongoDB "ServerSelectionTimeoutError"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the update to PyMongo 3.x multiprocessing_ applications "parent process
and each child process must create their own instances of MongoClient".

.. _multiprocessing: https://api.mongodb.com/python/current/faq.html#multiprocessing

For Apache WSGI applications, an example Apache "vhost" configuration for
the Alerta API would look like this::

    <VirtualHost *:8080>
      ServerName localhost
      WSGIDaemonProcess alerta processes=5 threads=5
      WSGIProcessGroup alerta
      WSGIApplicationGroup %{GLOBAL}
      WSGIScriptAlias / /var/www/api.wsgi
      WSGIPassAuthorization On
      <Directory /opt/alerta>
        Require all granted
      </Directory>
    </VirtualHost>

Full examples are available on GitHub_ and more information on why
this is necessary is available on stackoverflow_ and the PyMongo where
they discussion PyMongo in relation to forking_ and mod_wsgi_ site.

.. _GitHub: https://github.com/search?q=org%3Aalerta+WSGIApplicationGroup&type=Code
.. _stackoverflow: http://stackoverflow.com/questions/31030307/why-is-pymongo-3-giving-serverselectiontimeouterror
.. _forking: https://api.mongodb.com/python/current/faq.html#is-pymongo-fork-safe
.. _mod_wsgi: http://api.mongodb.com/python/current/examples/mod_wsgi.html

Does Alerta support Python 2.7 or Python 3?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alerta :ref:`Release 5.2 <release_5_2>` is the `last version`_ to support
Python 2.7 and from 31 August, 2018 it will only receive crtical bug fixes
and security patches.

Alerta :ref:`Release 6 <release_6_0>` supports Python 3.5+ and is recommended
for new production environments and existing installations should be switched
to Python 3 well before 1 January, 2020 when Python 2.7 becomes End-of-Life_.

.. _last version: https://github.com/alerta/alerta/issues/480
.. _created: https://github.com/alerta/nagios3-alerta
.. _many: https://github.com/alerta/alerta/tree/master/alerta/plugins
.. _plugins: https://github.com/alerta/alerta-contrib/tree/master/plugins
.. _integrations: https://github.com/alerta/alerta-contrib/tree/master/integrations
.. _popular: https://github.com/alerta/alerta/issues/74
.. _demand: https://github.com/alerta/alerta/issues/75
.. _End-of-Life: https://pythonclock.org/
