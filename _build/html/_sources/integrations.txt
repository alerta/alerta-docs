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

* `Amazon SQS`_
* AMQP
* `AWS Cloudwatch`_
* Opsweekly_
* Pinger
* SNMP Trap
* Supervisor_
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

.. _Amazon SQS: http://aws.amazon.com/sqs/
.. _AWS Cloudwatch: http://aws.amazon.com/cloudwatch/
.. _Opsweekly: https://codeascraft.com/2014/06/19/opsweekly-measuring-on-call-experience-with-alert-classification/
.. _Supervisor: http://supervisord.org/events.html
