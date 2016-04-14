.. _integrations_plugins:

Integrations & Plugins
======================

There are several different ways to integrate other alert sources into Alerta.

Firstly, integrations with key open source monitoring tools like Nagios and Zabbix make use of the Alerta API and demonstrate how to build integrations with other monitoring tools.

Secondly, there are built-in webhooks for AWS Cloudwatch, Pingdom and PagerDuty which provide 'out-of-the-box' integrations for some of the most popular monitoring systems available.

Lastly, plugins can be used to quickly and easily forward alerts to or notify other systems like Slack or Hipchat.

.. _integrations:

Integrations
------------

Core
~~~~

There are a few core integrations which have been developed to showcase how easy it is to get alerts or events from other tools into Alerta. They are:

* `Nagios Event Broker`_ - forward host/service check results with suppression during downtime
* `Zabbix Alert Script`_ - forward problems, acknowledged and OK events
* `Sensu Plugin`_ - forward sensu events
* `Riemann Plugin`_ - generate alerts from thresholds defined against metric streams
* `Kibana Logging`_ - log alerts to Elasticsearch for historical visualisation of alert trends

.. _Nagios Event Broker: https://github.com/alerta/nagios-alerta
.. _Zabbix Alert Script: https://github.com/alerta/zabbix-alerta
.. _Sensu Plugin: https://github.com/alerta/sensu-alerta
.. _Riemann Plugin: https://github.com/alerta/riemann-alerta
.. _Kibana Logging: https://github.com/alerta/kibana-alerta

Contrib
~~~~~~~

There are several more integrations available in the `contrib`_ repo which may be useful. They are:

* `Amazon SQS`_ - receive alerts from SQS that were sent using the SNS core plugin
* `E-mail`_ - send emails after a hold-time has expired (requires the `AMQP`_ message queue core plugin)
* `AWS Cloudwatch`_ - receive cloudwatch alarms from SQS (deprecated, use the cloudwatch webhook instead)
* Opsweekly_ - query Alerta to generate Opsweekly reports
* Pinger_ - generate ping alerts from list of network resources being pinged
* `SNMP Trap`_ - generate alerts from SNMPv1 and SNMPv2 sources
* Supervisor_ - trigger alerts and heartbeats based on process deamon events
* Syslog_ - receive :RFC:`5424`, :RFC:`3164` syslog and Cisco_ syslog messages
* `URL monitor`_ - trigger alerts from web service query responses

.. _contrib: https://github.com/alerta/alerta-contrib
.. _Amazon SQS: https://github.com/alerta/alerta-contrib/tree/master/integrations/amazon-sqs
.. _E-mail: https://github.com/alerta/alerta-contrib/tree/master/integrations/mailer
.. _AWS Cloudwatch: https://github.com/alerta/alerta-contrib/tree/master/integrations/cloudwatch
.. _Opsweekly: https://github.com/alerta/alerta-contrib/tree/master/integrations/opsweekly
.. _Pinger: https://github.com/alerta/alerta-contrib/tree/master/integrations/pinger
.. _SNMP Trap: https://github.com/alerta/alerta-contrib/tree/master/integrations/snmptrap
.. _Supervisor: https://github.com/alerta/alerta-contrib/tree/master/integrations/supervisor
.. _Syslog: https://github.com/alerta/alerta-contrib/tree/master/integrations/syslog
.. _Cisco: http://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html
.. _URL monitor: https://github.com/alerta/alerta-contrib/tree/master/integrations/urlmon

.. _webhooks:

Webhooks
--------

`Webhook callbacks`_ are a way of integrating with other systems by triggering web callbacks to the Alerta server API when an event occurs.

.. _Webhook callbacks: https://en.wikipedia.org/wiki/Webhook

AWS CloudWatch
~~~~~~~~~~~~~~

Alerta can be configured to receive AWS CloudWatch alarms by subscribing the Alerta API endpoint to an SNS topic.

For details on how to set this up see the `Sending Amazon SNS Messages to HTTP/HTTPS Endpoints`_ page and in the `Endpoint` input box append :file:`/webhooks/cloudwatch` to the Alerta API URL.

**Example AWS CloudWatch Webhook URL**

:file:`https://alerta.example.com/api/webhooks/cloudwatch`

.. _Sending Amazon SNS Messages to HTTP/HTTPS Endpoints: http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html

Pingdom
~~~~~~~

Alerta can be configured to receive Pingdom URL check alerts by adding a webhook alerting endpoint that calls the Alerta API.

For details on how to set this up see the `Pingdom webhook`_ page and in the `webhook URL` input box append :file:`/webhooks/pingdom` to the Alerta API URL.

**Example Pingdom Webhook URL**

:file:`https://alerta.example.com/api/webhooks/pingdom`

.. _Pingdom webhook: https://support.pingdom.com/Knowledgebase/Article/View/94/0/users-and-alerting-end-points

PagerDuty
~~~~~~~~~

Alerta can be configured to receive PagerDuty incident-based webhooks -- any change to the ``status`` or ``assigned_to_user`` of an incident will cause an outgoing message to be sent.

For details on how to set this up see the `PagerDuty webhook`_ page and where it requires the webhook URL append :file:`/webhooks/pagerduty` to the Alerta API URL.

**Example PagerDuty Webhook URL**

:file:`https://alerta.example.com/api/webhooks/pagerduty`

.. _PagerDuty webhook: https://developer.pagerduty.com/documentation/rest/webhooks

.. _stackdriver:

Google Stackdriver
~~~~~~~~~~~~~~~~~~

Alerta can be configured to receive Google Stackdriver incidents by adding a webhook endpoint to the notifications configuration.

For details on how to set this up see `Stackdriver webhook`_ page and in the `ENDPOINT URL` input box append :file:`/webhooks/stackdriver` to the Alerta API URL.

**Example Stackdriver Webhook URL**

:file:`https://alerta.example.com/api/webhooks/stackdriver`

.. _Stackdriver webhook: https://support.stackdriver.com/customer/portal/articles/1491775-configuring-webhooks

.. _plugins:

Plugins
-------

`Plugin extensions`_ are an easy way of adding new features to Alerta that meet a specific end-user requirement.

.. _Plugin extensions: https://en.wikipedia.org/wiki/Plug-in_(computing)

Core
~~~~

`Core plugins`_ have been developed as examples of common use-cases.

.. _Core plugins: https://github.com/guardian/alerta/tree/master/alerta/plugins

* `AMQP`_ - publish alerts to an AMQP fanout topic after processing
* `Enhance`_ - add new information to an alert based on existing information
* `Logstash/Kibana`_ - send alerts to logstash agent after processing
* `Normalise`_ - ensure alerts a formatted in a consistent manner
* `Reject`_ - reject alerts before processing. used to enforce custom alert format policies
* `AWS SNS`_ - publish alerts to SNS topic after processing

.. _AMQP: https://github.com/guardian/alerta/blob/master/alerta/plugins/amqp.py
.. _Enhance: https://github.com/guardian/alerta/blob/master/alerta/plugins/enhance.py
.. _Logstash/Kibana: https://github.com/guardian/alerta/blob/master/alerta/plugins/logstash.py
.. _Normalise: https://github.com/guardian/alerta/blob/master/alerta/plugins/normalise.py
.. _Reject: https://github.com/guardian/alerta/blob/master/alerta/plugins/reject.py
.. _AWS SNS: https://github.com/guardian/alerta/blob/master/alerta/plugins/sns.py

Contrib
~~~~~~~

`Contributed plugins`_ are made available for popular tools but implementation-specific requirements.

.. _Contributed plugins: https://github.com/alerta/alerta-contrib/tree/master/plugins

* `GeoIP Location`_ - use remote IP address to submitted alert to add location data
* HipChat_ - send alerts to HipChat room
* InfluxDB_ - send alerts to InfluxDB for graphing with Grafana
* PagerDuty_ - send alerts to PagerDuty (webhooks used to receive callbacks)
* `Pushover.net`_ - send alerts to Pushover.net
* Slack_ - send alerts to Slack room
* `Twilio SMS`_ - sene alerts via SMS using Twilio

.. _`GeoIP Location`: https://github.com/alerta/alerta-contrib/tree/master/plugins/geoip
.. _HipChat: https://github.com/alerta/alerta-contrib/tree/master/plugins/hipchat
.. _InfluxDB: https://github.com/alerta/alerta-contrib/tree/master/plugins/influxdb
.. _PagerDuty: https://github.com/alerta/alerta-contrib/tree/master/plugins/pagerduty
.. _`Pushover.net`: https://github.com/alerta/alerta-contrib/tree/master/plugins/pushover
.. _Slack: https://github.com/alerta/alerta-contrib/tree/master/plugins/slack
.. _`Twilio SMS`: https://github.com/alerta/alerta-contrib/tree/master/plugins/twilio
