.. _plugins:

Plug-ins
========

Plugins
-------

`Plugin extensions`_ are an easy way of adding new features to Alerta that meet
a specific end-user requirement.

.. _Plugin extensions: https://en.wikipedia.org/wiki/Plug-in_(computing)

Core
~~~~

`Core plugins`_ ship with the Alerta server. The default enabled plugins are
``remote_ip``, ``reject``, ``heartbeat``, ``blackout`` and ``forwarder``.

.. _Core plugins: https://github.com/alerta/alerta/tree/master/alerta/plugins

* `Remote IP`_ - extract remote IP address from request headers and add to alert attributes
* `Reject`_ - reject alerts before processing. used to enforce custom alert format policies
* `Heartbeat`_ - convert missed heartbeats into alerts
* `Blackout`_ - suppression handler that will drop alerts that match a blackout period
* `Forwarder`_ - forward alerts to other Alerta servers or external systems
* `Escalate`_ - escalate alert severity based on how long the alert has been open
* `Timeout`_ - auto-expire stale alerts
* `Acked By`_ - track which user acknowledged an alert

.. _Remote IP: https://github.com/alerta/alerta/blob/master/alerta/plugins/remote_ip.py
.. _Reject: https://github.com/alerta/alerta/blob/master/alerta/plugins/reject.py
.. _Heartbeat: https://github.com/alerta/alerta/blob/master/alerta/plugins/heartbeat.py
.. _Blackout: https://github.com/alerta/alerta/blob/master/alerta/plugins/blackout.py
.. _Forwarder: https://github.com/alerta/alerta/blob/master/alerta/plugins/forwarder.py
.. _Escalate: https://github.com/alerta/alerta/blob/master/alerta/plugins/escalate.py
.. _Timeout: https://github.com/alerta/alerta/blob/master/alerta/plugins/timeout.py
.. _Acked By: https://github.com/alerta/alerta/blob/master/alerta/plugins/acked_by.py

Contrib
~~~~~~~

`Contributed plugins`_ are available for popular tools and services:

.. _Contributed plugins: https://github.com/alerta/alerta-contrib/tree/master/plugins

**Messaging & Chat**

* DingTalk_ - send alerts to DingTalk groups
* HipChat_ - send alerts to HipChat room
* Matrix_ - send alerts to Matrix rooms
* Mattermost_ - send alerts to Mattermost channels
* `MS Teams`_ - send alerts to Microsoft Teams channels
* Rocketchat_ - send alerts to Rocket.Chat channels
* Slack_ - send alerts to Slack channels
* `Telegram Bot`_ - send alerts to Telegram channels

**Incident Management**

* AlertOps_ - send alerts to AlertOps
* GoAlert_ - send alerts to GoAlert
* `Jira Plugin`_ - create Jira tickets from alerts
* OpsGenie_ - send alerts to OpsGenie
* `PagerDuty Plugin`_ - send alerts to PagerDuty (webhooks used to receive callbacks)

**Monitoring & Metrics**

* InfluxDB_ - send alerts to InfluxDB for graphing with Grafana
* `Prometheus Silencer`_ - silence alerts in Prometheus Alertmanager if ack'ed in Alerta
* OP5_ - send alerts to OP5 Monitor
* Zabbix_ - send alerts to Zabbix

**Notifications**

* `Pushover.net`_ - send alerts to Pushover.net
* `Twilio SMS`_ - send alerts via SMS using Twilio

**Queues & Pub/Sub**

* AMQP_ - publish alerts to an AMQP fanout topic after processing
* `Google Pub/Sub`_ - publish alerts to Google Cloud Pub/Sub
* `AWS SNS`_ - publish alerts to SNS topic after processing

**Logging & Status**

* Cachet_ - create incidents for display on Cachet status page
* `Logstash/Kibana`_ - send alerts to logstash agent after processing
* `Syslog Logger`_ - send alerts via syslog

**Alert Processing**

* Enhance_ - add new information to an alert based on existing information
* `GeoIP Location`_ - use remote IP address to add location data
* `Normalise`_ - ensure alerts are formatted in a consistent manner

.. _AlertOps: https://github.com/alerta/alerta-contrib/tree/master/plugins/alertops
.. _AMQP: https://github.com/alerta/alerta-contrib/tree/master/plugins/amqp
.. _Cachet: https://github.com/alerta/alerta-contrib/tree/master/plugins/cachet
.. _DingTalk: https://github.com/alerta/alerta-contrib/tree/master/plugins/dingtalk
.. _Enhance: https://github.com/alerta/alerta-contrib/tree/master/plugins/enhance
.. _`GeoIP Location`: https://github.com/alerta/alerta-contrib/tree/master/plugins/geoip
.. _GoAlert: https://github.com/alerta/alerta-contrib/tree/master/plugins/goalert
.. _HipChat: https://github.com/alerta/alerta-contrib/tree/master/plugins/hipchat
.. _InfluxDB: https://github.com/alerta/alerta-contrib/tree/master/plugins/influxdb
.. _`Jira Plugin`: https://github.com/alerta/alerta-contrib/tree/master/plugins/jira
.. _Logstash/Kibana: https://github.com/alerta/alerta-contrib/tree/master/plugins/logstash
.. _Matrix: https://github.com/alerta/alerta-contrib/tree/master/plugins/matrix
.. _Mattermost: https://github.com/alerta/alerta-contrib/tree/master/plugins/mattermost
.. _`MS Teams`: https://github.com/alerta/alerta-contrib/tree/master/plugins/msteams
.. _Normalise: https://github.com/alerta/alerta-contrib/tree/master/plugins/normalise
.. _OP5: https://github.com/alerta/alerta-contrib/tree/master/plugins/op5
.. _OpsGenie: https://github.com/alerta/alerta-contrib/tree/master/plugins/opsgenie
.. _PagerDuty Plugin: https://github.com/alerta/alerta-contrib/tree/master/plugins/pagerduty
.. _`Prometheus Silencer`: https://github.com/alerta/alerta-contrib/tree/master/plugins/prometheus
.. _`Pushover.net`: https://github.com/alerta/alerta-contrib/tree/master/plugins/pushover
.. _`Google Pub/Sub`: https://github.com/alerta/alerta-contrib/tree/master/plugins/pubsub
.. _Rocketchat: https://github.com/alerta/alerta-contrib/tree/master/plugins/rocketchat
.. _Slack: https://github.com/alerta/alerta-contrib/tree/master/plugins/slack
.. _`AWS SNS`: https://github.com/alerta/alerta-contrib/tree/master/plugins/sns
.. _`Syslog Logger`: https://github.com/alerta/alerta-contrib/tree/master/plugins/syslog
.. _`Telegram Bot`: https://github.com/alerta/alerta-contrib/tree/master/plugins/telegram
.. _`Twilio SMS`: https://github.com/alerta/alerta-contrib/tree/master/plugins/twilio
.. _Zabbix: https://github.com/alerta/alerta-contrib/tree/master/plugins/zabbix

Plugin Lifecycle Hooks
~~~~~~~~~~~~~~~~~~~~~~

Plugins must implement the ``PluginBase`` abstract class. The following
lifecycle hooks are available:

**Required methods:**

``pre_receive(alert, **kwargs)``
    Called before an alert is saved to the database. Can modify and return the
    alert, or raise ``RejectException`` or ``BlackoutPeriod`` to reject it.

``post_receive(alert, **kwargs)``
    Called after an alert is saved. Used for sending notifications to external
    services. Should not modify the alert.

``status_change(alert, status, text, **kwargs)``
    Called when an alert status changes. Used to trigger actions on status
    transitions.

**Optional methods (raise ``NotImplementedError`` if not used):**

``take_action(alert, action, text, **kwargs)``
    Called before an action is taken on an alert. Can be used to trigger
    external actions or modify the alert before the action is applied.

``post_action(alert, action, text, **kwargs)``
    Called after an action has been applied to an alert and the status has been
    updated.

``take_note(alert, text, **kwargs)``
    Called when a note is added to an alert.

``delete(alert, **kwargs)``
    Called when an alert is deleted.
