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

* `Amazon SQS`_ is this used to publish or receive alerts? even i don't know
* E-mail and PagerDuty via an `AMQP`_ message queue
* `AWS Cloudwatch`_ - how is this different to the cw webhook?
* Opsweekly_ - what is it?
* Pinger_ - generate alerts from list of nw resources being pinged. ICMP unreachable
* `SNMP Trap`_ - process SNMPv1, SNMPv2 but not SNMPv3. IPMI ???
* Supervisor_
* Syslog_ - BSD, Syslog and Cisco syslog
* `URL monitor`_ - probe URLs

.. _contrib: https://github.com/alerta/alerta-contrib

.. _Amazon SQS:
.. _AMQP: https://github.com/alerta/alerta-contrib/tree/master/integrations/amqp
.. _AWS Cloudwatch:
.. _Opsweekly: https://github.com/alerta/alerta-contrib/tree/master/integrations/opsweekly
.. _Pinger:
.. _SNMP Trap:
.. _Supervisor: https://github.com/alerta/alerta-contrib/tree/master/integrations/supervisor
.. _Syslog:
.. _URL monitor:

.. _webhooks:

Webhooks
--------

** webhooks are the thing **

AWS Cloudwatch
~~~~~~~~~~~~~~

** go into detail here **

See AwsCloudwatch_

Pingdom
~~~~~~~

** go into detail here **

See Pingdom_

.. _AwsCloudwatch: http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html
.. _Pingdom: https://support.pingdom.com/Knowledgebase/Article/View/94/0/users-and-alerting-end-points

PagerDuty
~~~~~~~~~

** go into detail here **

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
