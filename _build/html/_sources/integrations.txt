.. _integrations_plugins:

Integrations & Plugins
======================

There are several different ways to integrate other alert sources into Alerta. Integrations with key open source monitoring tools make use of the Alerta API and can form the starting points for integrating other lesser-known monitoring tools.

There are built-in webhooks for AWS Cloudwatch, Pingdom and PagerDuty. Plugins can be used to quickly and easily forward alerts to or notify other systems.

.. _integrations:

Integrations
------------

Core
~~~~

There are a few core integrations which have been developed to showcase how easy it is to quickly get alerts or events from other tools into Alerta. They are:

* `Nagios Event Broker`_ (C)
* `Zabbix Alert Script`_ (Python)
* `Sensu Plugin`_ (Ruby)
* `Riemann Plugin`_ (Clojure)

.. _Nagios Event Broker: https://github.com/alerta/nagios-alerta
.. _Zabbix Alert Script: https://github.com/alerta/zabbix-alerta
.. _Sensu Plugin: https://github.com/alerta/sensu-alerta
.. _Riemann Plugin: https://github.com/alerta/riemann-alerta

Contrib
~~~~~~~

There are several more integrations available in the `contrib`_ repo. They are:

* `Amazon SQS`_ - receive alerts from SQS that were sent using the SNS core plugin
* E-mail and PagerDuty integrations use the `AMQP`_ message queue core plugin
* `AWS Cloudwatch`_ - receive cloudwatch alarms from SQS (deprecated, use the cloudwatch webhook instead)
* Opsweekly_ - query Alerta to generate Opsweekly reports
* Pinger_ - generate ping alerts from list of network resources being pinged
* `SNMP Trap`_ - generate alerts from SNMPv1 and SNMPv2 sources
* Supervisor_ - trigger alerts and heartbeats based on process deamon events
* Syslog_ - receive RFC 5424, RFC 3164 syslog and Cisco syslog messages
* `URL monitor`_ - trigger alerts from web service query responses

.. _contrib: https://github.com/alerta/alerta-contrib

.. _Amazon SQS: https://github.com/alerta/alerta-contrib/tree/master/integrations/amazon-sqs
.. _AMQP: https://github.com/alerta/alerta-contrib/tree/master/integrations/amqp
.. _AWS Cloudwatch: https://github.com/alerta/alerta-contrib/tree/master/integrations/cloudwatch
.. _Opsweekly: https://github.com/alerta/alerta-contrib/tree/master/integrations/opsweekly
.. _Pinger: https://github.com/alerta/alerta-contrib/tree/master/integrations/pinger
.. _SNMP Trap: https://github.com/alerta/alerta-contrib/tree/master/integrations/snmptrap
.. _Supervisor: https://github.com/alerta/alerta-contrib/tree/master/integrations/supervisor
.. _Syslog: https://github.com/alerta/alerta-contrib/tree/master/integrations/syslog
.. _URL monitor: https://github.com/alerta/alerta-contrib/tree/master/integrations/urlmon

.. _webhooks:

Webhooks
--------

Webhooks are a popular and easy way of integrating with other systems to configuring API callbacks from other tools to the Alerta server API. When an alarm is triggered in Cloudwatch, an alert is generated in Pingdom or a alarm is acknowledged in PagerDuty, Alerta can be notified.

AWS Cloudwatch
~~~~~~~~~~~~~~

** go into detail here **

See Cloudwatch_webhook_

.. _Cloudwatch_webhook: http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html

Pingdom
~~~~~~~

** go into detail here **

See Pingdom_webhook_


.. _Pingdom_webhook: https://support.pingdom.com/Knowledgebase/Article/View/94/0/users-and-alerting-end-points

PagerDuty
~~~~~~~~~

** go into detail here **

See PagerDuty_webhook_

.. _PagerDuty_webhook: https://developer.pagerduty.com/documentation/rest/webhooks

.. _plugins:

Plugins
-------

Core
~~~~

* AMQP
* Enhance
* Logstash/Kibana
* Normalise
* Reject
* AWS SNS

** go into detail here **

Contrib
~~~~~~~

* `GeoIP Location`_
* HipChat_
* InfluxDB_
* PagerDuty_ -- send alerts to pagerduty (webhooks used to receive acks)
* `Pushover.net`_
* Slack_
* `Twilio SMS`_

.. _`GeoIP Location`: https://github.com/alerta/alerta-contrib/tree/master/plugins/geoip
.. _HipChat: https://github.com/alerta/alerta-contrib/tree/master/plugins/hipchat
.. _InfluxDB: https://github.com/alerta/alerta-contrib/tree/master/plugins/influxdb
.. _PagerDuty: https://github.com/alerta/alerta-contrib/tree/master/plugins/pagerduty
.. _`Pushover.net`: https://github.com/alerta/alerta-contrib/tree/master/plugins/pushover
.. _Slack: https://github.com/alerta/alerta-contrib/tree/master/plugins/slack
.. _`Twilio SMS`: https://github.com/alerta/alerta-contrib/tree/master/plugins/twilio
