.. _tutorial 3x:

Integration with Zabbix
=======================

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Zabbix Integration`
  * `Step 2: Prometheus Integration`
  * `Step 3: Influx Integration`
  * `Next Steps`_

Overview
--------

Configure Alerta to receive notifications from multiple Zabbix servers. Zabbix
severity levels and colours will be used.

Prerequisites
-------------

You have already installed Zabbix and Alerta.


Step 1: Zabbix
----------------------------------


    $ pip install zabbix-alerta
    $ grep AlertScripts
    $ ln -s `which zabbix-alerta` /usr/local/zabbix/alertscripts

Step 2: Prometheus
------------------------

To enable you to distinguish between different prometheus servers in each country I would either use the customer attribute (eg. customer=italy) or overload the environment attribute (eg. environment=italy:Production). In both cases the individual alerts will be correctly name spaced and considered as separate alerts for the same prometheus rule.

The customer would be defined by using API keys assigned to that customer. To set an environment for each country use the global config in the prometheus alertmanager, for example:

global:
  external_labels:
    environment: "italy:Production"
    service: "Prometheus"
    region: "eu-west-1"


Step 3: Influx
------------------------


Next Steps
----------
