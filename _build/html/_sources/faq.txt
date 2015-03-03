.. _faq:

Frequently Asked Questions
==========================

Alerta
------

Can I define custom severity codes and levels?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, though it is not recommended. There is nothing stopping you from using any string as the severity for a submitted alert. The only aspect of ``alerta`` that would not work as expected would be the ``trendIndication`` assigned to an alert that indicates whether it is more or less severe than the last alert for that ``resource`` and ``event``. To fix this, `severity code`_ mappings would need to be updated to include the new severity or to rename an existing one.

.. _`severity code`: https://github.com/guardian/alerta/blob/master/alerta/app/severity_code.py

How can I add a priority to an alert eg. High, Medium, Low?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use a custom attribute called ``priority`` when sending alerts to alerta::

    $ alerta send ... --attributes priority=high ...

Alerts of differing priority could be queried by ``alerta`` command-line tool using::

    $ alerta query --filters attributes.priority=high

Using the web console to sort alerts by priority as well as severity would require some development effort.

What's the difference between `ack`, `close` and `delete`?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alerts are meant to auto-close when a corresponding `normal` or `cleared` alert is received for that event-resource combination. If no `normal` alert exists for a particular event (which may be the case for alerts from log files, for example) then the alert will be deleted when the timeout period has expired. Alerts timeout after 1 day by default but that is configurable on a per-alert basis.

If, as an operator, you want to remove an event from view then you can either `ack` the alert or DELETE it. If the alert is DELETED a new alert with the same event-resource combination will trigger a new notification email (if configured) whereas an `ack`'ed alert will not.

Why don't you have a plug-in or integration for X, where X is whatever you use in your job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We could spend countless hours writing plug-ins for everything and never finish or we could focus on building an easily extensible system with great documentation and let the end-user build the plug-in they need. Having said that, we have still created_ many_ `plug-ins`_ and integrations_ as working examples and we are not against writing more if there is popular_ demand_. We are also happy to accept submissions.

.. _created: https://github.com/alerta/nagios3-alerta
.. _many: https://github.com/guardian/alerta/tree/master/alerta/plugins
.. _`plug-ins`: https://github.com/alerta/alerta-contrib/tree/master/plugins
.. _integrations: https://github.com/alerta/alerta-contrib/tree/master/integrations
.. _popular: https://github.com/guardian/alerta/issues/74
.. _demand: https://github.com/guardian/alerta/issues/75