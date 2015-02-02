Integrations & Plugins
======================

There are several different ways to integrate other alert sources into Alerta. Integrations with key open source monitoring tools have been developed and provide good starting points for other, perhaps bespoke, monitoring tools.


Integrations
------------

Core
++++

There are a few core integrations which have been developed to showcase how easy it is to quickly get alerts or events from other tools into Alerta. They are:

* `Nagios Event Broker`_ (C)
* `Zabbix Alert Script`_ (Python)
* `Sensu Plugin`_ (Ruby)
* `Riemann Integration`_ (Clojure)

Contrib
+++++++

There are several more integrations available in the `contrib` repo. They are:

* Amazon SQS (Python)
* AMQP (Python)
* AWS Cloudwatch (Python)
* Opsweekly (PHP)
* Pinger (Python)
* SNMP Trap (Python)
* Supervisor (Python)
* Syslog
* URL monitor

Webhooks
--------

* AWS Cloudwatch
* Pingdom

Plugins
-------

Core
++++

* AMQP
* Enhance
* Logstash/Kibana
* Normalise
* Reject
* AWS SNS

Contrib
+++++++

* GeoIP Location
* HipChat
* InfluxDB
* Pushover.net
* Slack
* Twilio SMS


.. _Nagios Event Broker: https://github.com/alerta/nagios3-alerta
.. _Zabbix Alert Script: https://github.com/alerta/zabbix-alerta
.. _Sensu Plugin: https://github.com/alerta/sensu-alerta
.. _Riemann Integration: https://github.com/alerta/riemann-alerta
