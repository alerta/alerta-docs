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
configuration <CORS config>` setting.

.. _CORS: https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
.. _same origin: https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
.. _allows the origin: https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Origin

Can I define custom severity codes and levels?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, you can now completely change the severity names, severity levels
and colours. See :ref:`` for more information.

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
case for alerts from log files, for example) then the alert will
be deleted when the timeout period has expired. Alerts timeout after
1 day by default but that is configurable on a per-alert basis.

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

MongoDB errors ServerSelectionTimeoutError
WSGIApplicationGroup %{GLOBAL}

http://stackoverflow.com/questions/31030307/why-is-pymongo-3-giving-serverselectiontimeouterror

Does Alerta support Python 3?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, however due to dependencies on Flask the minimum version is
Python 3.4 and even then there may still be issues. For example,
running Flask apps as a WSGI application using Python 3 may be
problematic and so it is currently recommended_ to run Alerta using
Python 2.7 in production environments.

.. _recommended: http://flask.pocoo.org/docs/0.10/python3/#recommendations

.. _created: https://github.com/alerta/nagios3-alerta
.. _many: https://github.com/guardian/alerta/tree/master/alerta/plugins
.. _plugins: https://github.com/alerta/alerta-contrib/tree/master/plugins
.. _integrations: https://github.com/alerta/alerta-contrib/tree/master/integrations
.. _popular: https://github.com/guardian/alerta/issues/74
.. _demand: https://github.com/guardian/alerta/issues/75
