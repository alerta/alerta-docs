.. _server:

Server & API
============

The ``alertad`` server receives alerts from multiple sources, :ref:`correlates <correlation>`, :ref:`de-duplicates  <deduplication>` or :ref:`suppresses <blackouts>` them, and makes the alerts available via a RESTful_ JSON_ API.

.. _RESTful: http://apigee.com/about/resources/webcasts/restful-api-design-second-edition
.. _JSON: http://developers.squarespace.com/what-is-json/

Alerts can be intercepted as they are received to modify, enhance or reject them using :ref:`pre-receive hooks <pre_receive>`. Alerts can also be used to trigger actions in other systems after the alert has been processed using :ref:`post-receive hooks <post_receive>`.

There are several :ref:`integrations <integrations>` with popular monitoring tools available and :ref:`webhooks <webhooks>` can be used to trivially integrate with AWS Cloudwatch, Pingdom, and PagerDuty.

.. _event_processing:

Event Processing
----------------

Alerta comes `out-of-the-box` with key features designed to reduce the burden of alert management. When an event is received it it is processed in the following manner:

1. all plugins pre-receive hooks are run in alphabetical order, alert immediately rejected if any return a Reject Exception
2. alert is checked against any active blackout periods, alert suppressed if any match
3. alert is checked if duplicate, if so duplicate count ++, repeat=True
4. alert is checked if correlated, if so change severity and/or status etc
5. alert is added as new
6. all plugin post-receive hooks are run in alphabetical order
7. new or updated alert returned in reponse
8. timeout used to expire alerts from the console

Plug-ins
--------

Plug-ins are small python scripts that can run either before or after an alert is saved to the database. This is achieved by registering *pre-receive hooks* for transformers and *post-receive hooks* for downstream integration.

.. _transformers:

Transformers
~~~~~~~~~~~~

Using pre-receive hooks, plugins provide the ability to transform raw alert data from sources before alerts are created. For example, alerts can be *normalised* to ensure they all have specific attributes or tags or only have a specific value from a range of allowed values. This is demonstrated in the reject plugin that enforces an alert policy.

Plugins can also be used to *enhance* alerts, for example, to add Geo location data to alerts based on the sending IP address. See geoip plugin or a customer attribute based on information contained in the alert. See enhance plugin.

Downstream
~~~~~~~~~~

Using post-receive hooks, plugins can be used to provide downstream systems with alerts in realtime. For example, pushing alerts onto an AWS SNS topic, AMQP queue, logging to a Logstash/Kibana stack, or sending notifications to HipChat, Slack or Twilio.

.. _blackouts:

Blackout Periods
----------------


.. _deduplication:

De-Duplication
--------------

Same event/resource combination, same severity simply increases the duplicate count.


.. _correlation:

Simple Correlation
------------------

Same event/resource, different severity
Correlated list of related events. eg. NodeUp NodeDown

State-based Browser
-------------------

Alerts cleared, normal, ok change status to `closed`
auto status change (open->closed->open)
status / severity change & history log
duplicate count, repeat flag
previous severity & trend indication

Timeouts
--------


Heartbeats
----------


alerting on stale heartbeats



