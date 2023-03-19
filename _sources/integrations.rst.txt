.. _integrations_plugins:

.. spelling::

    Alertmanager
    Kibana
    Solarwinds
    Logstash
    Cloudwatch
    Chronograf
    Grafana
    Graylog
    Hipchat
    Kapacitor
    Nagios
    Oembed
    Opsweekly
    Sensu
    Stackdriver
    Telegraf
    Zabbix

Integrations & Plugins
======================

There are several different ways to integrate other alert sources into Alerta.

Firstly, existing :ref:`integrations <integrations>` with well known monitoring
tools like Nagios_, Zabbix_ and Sensu_ make use of the Alerta API and demonstrate
how to build integrations with other monitoring tools.

.. _Nagios: https://www.nagios.com
.. _Zabbix: http://www.zabbix.com
.. _Sensu: https://sensuapp.org

Secondly, there are built-in :ref:`webhooks <webhooks>` for
`AWS Cloudwatch <https://aws.amazon.com/cloudwatch/>`_,
`Pingdom <https://www.pingdom.com>`_, `PagerDuty <https://www.pagerduty.com/>`_,
`Google Stackdriver <https://cloud.google.com/stackdriver/>`_,
`Prometheus Alertmanager <https://prometheus.io/docs/alerting/alertmanager/>`_
and more which provide 'out-of-the-box' integrations for some of the most popular
monitoring systems available.

Thirdly, :ref:`alert severity indicators <widgets>` or widgets can be placed
on any web page using oEmbed_ for easy integration with existing dashboards.

.. _oEmbed: http://oembed.com/

Lastly, :ref:`plugins <plugins>` can be used to quickly and easily forward alerts
to or notify other systems like Slack or Hipchat.

.. contents:: Contents
   :local:
   :depth: 2

.. _integrations:

Integrations
------------

Core
~~~~

There are a few core integrations which have been developed to showcase how easy
it is to get alerts or events from other tools into Alerta. They are:

* `Nagios Event Broker`_ - forward host/service check results with suppression during downtime
* `InfluxData Kapacitor`_ - forward alerts for metric anomalies and dynamic thresholds
* `Zabbix Alert Script`_ - forward problems, acknowledged and OK events
* `Sensu Plugin`_ - forward Sensu events
* `Riemann Plugin`_ - generate alerts from thresholds defined against metric streams
* `Kibana Logging`_ - log alerts to Elasticsearch for historical visualisation of alert trends

.. _Nagios Event Broker: https://github.com/alerta/nagios-alerta
.. _InfluxData Kapacitor: https://docs.influxdata.com/kapacitor/latest/nodes/alert_node/#alerta
.. _Zabbix Alert Script: https://github.com/alerta/zabbix-alerta
.. _Sensu Plugin: https://github.com/alerta/sensu-alerta
.. _Riemann Plugin: https://github.com/alerta/riemann-alerta
.. _Kibana Logging: https://github.com/alerta/kibana-alerta

Contrib
~~~~~~~

There are several more integrations available in the `contrib`_ repo which may
be useful. They are:

* `Amazon SQS`_ - receive alerts from SQS that were sent using the SNS core plugin
* `E-mail`_ - send emails after a hold-time has expired (requires the `AMQP`_ message queue core plugin)
* Opsweekly_ - query Alerta to generate Opsweekly reports
* Pinger_ - generate ping alerts from list of network resources being pinged
* `SNMP Trap`_ - generate alerts from SNMPv1 and SNMPv2 sources
* Supervisor_ - trigger alerts and heartbeats based on process deamon events
* `Syslog Forwarder`_ - receive :RFC:`5424`, :RFC:`3164` syslog and Cisco_ syslog messages
* `URL monitor`_ - trigger alerts from web service query responses

.. _contrib: https://github.com/alerta/alerta-contrib
.. _Amazon SQS: https://github.com/alerta/alerta-contrib/tree/master/integrations/sqs
.. _E-mail: https://github.com/alerta/alerta-contrib/tree/master/integrations/mailer
.. _Opsweekly: https://github.com/alerta/alerta-contrib/tree/master/integrations/opsweekly
.. _Pinger: https://github.com/alerta/alerta-contrib/tree/master/integrations/pinger
.. _SNMP Trap: https://github.com/alerta/alerta-contrib/tree/master/integrations/snmptrap
.. _Supervisor: https://github.com/alerta/alerta-contrib/tree/master/integrations/supervisor
.. _Syslog Forwarder: https://github.com/alerta/alerta-contrib/tree/master/integrations/syslog
.. _Cisco: http://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html
.. _URL monitor: https://github.com/alerta/alerta-contrib/tree/master/integrations/urlmon

External
~~~~~~~~

Some third-party monitoring tools have built-in support for Alerta. They are:

* elastalert_ - alerting on anomalies, spikes, or other patterns of interest from data in Elasticsearch
* netdata_ - a system for distributed real-time performance and health monitoring
* `Tick Stack`_ - designed to handle metrics and events using Telegraf, InfluxDB, Chronograf, and Kapacitor

.. _elastalert: https://elastalert.readthedocs.io/en/latest/ruletypes.html#alerta
.. _netdata: https://github.com/firehol/netdata/wiki/Alerta-monitoring-system
.. _Tick Stack: https://docs.influxdata.com/kapacitor/v1.5/event_handlers/alerta/

.. _bidirection integ:

Bi-directional
~~~~~~~~~~~~~~

Bi-directional integration is where the system integrating with Alerta
provides information that enables Alerta to link back to the originating
system, either via an external link or simply a hostname and reference ID.

There are several examples of this two-way integration and they mostly
take advantage of the flexible nature of the the ``tags`` and ``attributes``
alert attributes which can be used to keep track of the external reference.

**Usage**

In it's simplest form, pass the URL of the external system that generated
the alert in an attribute called ``externalUrl`` (or similar)::

    $ alerta send -E ... --attribute externalUrl=https://my.example.com/go?id=1234

Better still, surroud the URL with HTML markup to make the link clickable
in the web UI::

    $ alerta send -E ... --attribute externalUrl='<a href="https://my.example.com/go?id=1234">ref 1234</a>'

**Examples**

The following is a list of integrations, webbhooks and plugins that highlight
the use of bi-directional integration in different ways.

* AWS Cloudwatch webhook - includes the `SNS subscription confirmation`_ link in the text of the alert
* Zabbix integration & plugin - TBC
* Grafana webhook - includes `rule and image links`_ in Grafana alert attributes if available
* NewRelic webhook - includes `incident and runbook links`_ in NewRelic alerts
* PagerDuty webhook - includes the `incident URL`_ in alert history text when status changes
* Prometheus webhook - includes `external and generator URLs`_ in the alert attributes
* Zabbix integration - includes `moreInfo`_ link back to Zabbix console event trigger page in alert attribute

.. _SNS subscription confirmation: https://github.com/alerta/alerta/blob/master/alerta/webhooks/cloudwatch.py#L39-L40
.. _rule and image links: https://github.com/alerta/alerta/blob/master/alerta/webhooks/grafana.py#L39-L43
.. _incident and runbook links: https://github.com/alerta/alerta/blob/master/alerta/webhooks/newrelic.py#L33-L37
.. _incident URL: https://github.com/alerta/alerta/blob/master/alerta/webhooks/pagerduty.py#L18
.. _external and generator URLs: https://github.com/alerta/alerta/blob/master/alerta/webhooks/prometheus.py#L62-L65
.. _moreInfo: https://github.com/alerta/zabbix-alerta/blob/master/zabbix_alerta.py#L67

.. _webhooks:

Webhooks
--------

Webhooks are a way of integrating with other systems by triggering `HTTP callbacks`_
to the Alerta server API when an event occurs.

.. _HTTP callbacks: https://en.wikipedia.org/wiki/Webhook

.. contents:: Built-in Webhooks
   :local:
   :depth: 2

.. Note::
    If authentication is enforced, then an API key is needed to access the alerta API programatically and use the webhooks. 
    
    Please follow this page for more information on how to pass your api-key : https://docs.alerta.io/en/latest/authentication.html#api-keys

AWS CloudWatch
~~~~~~~~~~~~~~

Alerta can be configured to receive AWS CloudWatch alarms by subscribing the Alerta
API endpoint to an SNS topic.

For details on how to set this up see the `Sending Amazon SNS Messages to
HTTP/HTTPS Endpoints`_ page and in the `Endpoint` input box append
:file:`/webhooks/cloudwatch` to the Alerta API URL.

**Example AWS CloudWatch Webhook URL**

:file:`https://alerta.example.com/api/webhooks/cloudwatch`

**Example AWS CloudWatch Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/cloudwatch?api-key=xxxxx`

.. _Sending Amazon SNS Messages to HTTP/HTTPS Endpoints: http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html

Grafana
~~~~~~~

Alerta can be configured to receive Grafana alerts by adding a webhook
endpoint to the Notification Channels.

For details on how to set this up see `Grafana webhook`_ page and in the
`Endpoint URL` input box append :file:`/webhooks/grafana` to the Alerta API URL.

.. _Grafana webhook: http://docs.grafana.org/alerting/notifications/#webhook

**Example Grafana Webhook URL**

:file:`https://alerta.example.com/api/webhooks/grafana`

**The following parameters can be set in the url**
     environment, event_type, group, origin, service, severity, timeout

**Example Grafana Webhook URL with parameters**

:file:`https://alerta.example.com/api/webhooks/grafana?api-key=xxx&environment=Production&service=Web&timeout=3600`

Graylog
~~~~~~~

TBC

New Relic
~~~~~~~~~

Alerta can be configured to receive New Relic incidents by adding a webhook
endpoint to the Notification Channels.

For details on how to set this up see `New Relic webhook`_ page and in the
`Endpoint URL` input box append :file:`/webhooks/newrelic` to the Alerta API URL.

.. _New Relic webhook: https://docs.newrelic.com/docs/alerts/new-relic-alerts/managing-notification-channels/notification-channels-controlling-where-send-alerts

**Example New Relic Webhook URL**

:file:`https://alerta.example.com/api/webhooks/newrelic`

**Example New Relic Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/newrelic?api-key=xxxxx`

PagerDuty
~~~~~~~~~

Alerta can be configured to receive PagerDuty incident-based webhooks -- any
change to the ``status`` or ``assigned_to_user`` of an incident will cause an
outgoing message to be sent.

For details on how to set this up see the `PagerDuty webhook`_ page and where it
requires the webhook URL append :file:`/webhooks/pagerduty` to the Alerta API URL.

**Example PagerDuty Webhook URL**

:file:`https://alerta.example.com/api/webhooks/pagerduty`

**Example PagerDuty Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/pagerduty?api-key=xxxxx`

.. _PagerDuty webhook: https://developer.pagerduty.com/documentation/rest/webhooks

Pingdom
~~~~~~~

Alerta can be configured to receive Pingdom URL check alerts by adding a webhook
alerting endpoint that calls the Alerta API.

For details on how to set this up see the `Pingdom webhook`_ page and in the
`webhook URL` input box append :file:`/webhooks/pingdom` to the Alerta API URL.

**Example Pingdom Webhook URL**

:file:`https://alerta.example.com/api/webhooks/pingdom`

**Example Pingdom Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/pingdom?api-key=xxxx`

.. _Pingdom webhook: https://support.pingdom.com/Knowledgebase/Article/View/94/0/users-and-alerting-end-points

Prometheus Alertmanager
~~~~~~~~~~~~~~~~~~~~~~~

Alerta can be configured as a webhook receiver in Alertmanager.

For details on how to set this up see the `Prometheus Config GitHub Repo`_

.. _Prometheus Config GitHub Repo: https://github.com/alerta/prometheus-config

Riemann
~~~~~~~

Alerta can be configured to receive Riemann events. The integration makes
no assumptions about the format of the Riemann events and consumes
standard events. If events are decorated with additional metadata (eg. tags,
environment, group, etc) then these will be used.

**Example Riemann Webhook URL**

:file:`https://alerta.example.com/api/webhooks/riemann`

**Example Riemann Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/riemann?api-key=xxxxx`

SeverDensity
~~~~~~~~~~~~

Alerta can be configured to receive SeverDensity alerts by adding a webhook
endpoint to the Notification Preferences.

For details on how to set this up see `SeverDensity webhook`_ page and in the
`Endpoint URL` input box append :file:`/webhooks/serverdensity` to the Alerta API URL.

.. _SeverDensity webhook: https://support.serverdensity.com/hc/en-us/articles/201017737-Setting-up-webhooks

**Example SeverDensity Webhook URL**

:file:`https://alerta.example.com/api/webhooks/serverdensity`

**Example SeverDensity Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/serverdensity?api-key=xxxxx`

Slack
~~~~~

TBC

Google Stackdriver
~~~~~~~~~~~~~~~~~~

Alerta can be configured to receive Google Stackdriver incidents by adding a
webhook endpoint to the notifications configuration.

For details on how to set this up see `Stackdriver webhook`_ page and in the
`ENDPOINT URL` input box append :file:`/webhooks/stackdriver` to the Alerta API URL.

**Example Stackdriver Webhook URL**

:file:`https://alerta.example.com/api/webhooks/stackdriver`

**Example Stackdriver Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/stackdriver?api-key=xxxxx`

.. _Stackdriver webhook: https://cloud.google.com/monitoring/support/notification-options#webhooks

Telegram
~~~~~~~~

Alerta can be configured to receive `Telegram callback queries`_ from the inline
buttons in the `Telegram Bot`_ plugin.

.. _Telegram callback queries: https://core.telegram.org/bots/api#callbackquery

For details on how to set this up see `Telegram Bot`_ page and for the
``TELEGRAM_WEBHOOK_URL`` setting append :file:`/webhooks/telegram` to the Alerta API URL.

**Example Telegram Webhook URL**

:file:`https://alerta.example.com/api/webhooks/telegram`

**Example Telegram Webhook URL with authentication**

:file:`https://alerta.example.com/api/webhooks/telegram?api-key=xxxxx`

.. _widgets:

Widgets
-------

Add an alert severity indicator (aka. widget) to any dashboard using the
Oembed API endpoint. The severity indicator is coloured with the maximum
severity for that alert query filter and has a count for the total number
of matching alerts for each severity.

Multiple severity indicators can be placed on the same page each for a
different environment, service or group. See the `example oembed web page`_.

.. _example oembed web page: https://github.com/alerta/alerta/blob/master/examples/oembed.html
