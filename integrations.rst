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

* `Nagios Event Broker`_ - host and service check with alert suppression during downtime
* `Zabbix Alert Script`_ - ???
* `Sensu Plugin`_ - ???
* `Riemann Plugin`_ - generate alerts from thresholds defined against metric streams

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

Webhooks are a way of integrating with other systems by triggering web callbacks to the Alerta server API when an event occurs.

AWS Cloudwatch
~~~~~~~~~~~~~~

** go into detail here **

See `Cloudwatch webhook`_

.. _Cloudwatch webhook: http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html

Pingdom
~~~~~~~

** go into detail here **

See `Pingdom webhook`_


.. _Pingdom webhook: https://support.pingdom.com/Knowledgebase/Article/View/94/0/users-and-alerting-end-points

PagerDuty
~~~~~~~~~

** go into detail here **

See `PagerDuty webhook`_

.. _PagerDuty webhook: https://developer.pagerduty.com/documentation/rest/webhooks

.. _plugins:

Plugins
-------

Core
~~~~

* AMQP - ???
* Enhance - ???
* Logstash/Kibana - ???
* Normalise - ???
* Reject - used to enforce custom alert format policies
* AWS SNS - ???

** go into detail here **

Contrib
~~~~~~~

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
