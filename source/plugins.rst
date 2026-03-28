.. _plugins:

Plug-ins
========

.. _plugins:

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

More than two dozen `contributed plugins`_ are made available for popular tools. Some
of the most popular are:

.. _Contributed plugins: https://github.com/alerta/alerta-contrib/tree/master/plugins

* AMQP_ - publish alerts to an AMQP fanout topic after processing
* Cachet_ - create incidents for display on Cachet status page
* Enhance_ - add new information to an alert based on existing information
* `GeoIP Location`_ - use remote IP address to submitted alert to add location data
* HipChat_ - send alerts to HipChat room
* InfluxDB_ - send alerts to InfluxDB for graphing with Grafana
* `Logstash/Kibana`_ - send alerts to logstash agent after processing
* `Normalise`_ - ensure alerts a formatted in a consistent manner
* `PagerDuty Plugin`_ - send alerts to PagerDuty (webhooks used to receive callbacks)
* `Prometheus Silencer`_ - silence alerts in Prometheus Alertmanager if ack'ed in Alerta
* `Pushover.net`_ - send alerts to Pushover.net
* Slack_ - send alerts to Slack room
* `AWS SNS`_ - publish alerts to SNS topic after processing
* `Syslog Logger`_ - send alerts via syslog
* `Telegram Bot`_ - send alerts to Telegram channel
* `Twilio SMS`_ - send alerts via SMS using Twilio

.. _AMQP: https://github.com/alerta/alerta-contrib/tree/master/plugins/amqp
.. _Cachet: https://github.com/alerta/alerta-contrib/tree/master/plugins/cachet
.. _Enhance: https://github.com/alerta/alerta-contrib/tree/master/plugins/enhance
.. _`GeoIP Location`: https://github.com/alerta/alerta-contrib/tree/master/plugins/geoip
.. _HipChat: https://github.com/alerta/alerta-contrib/tree/master/plugins/hipchat
.. _InfluxDB: https://github.com/alerta/alerta-contrib/tree/master/plugins/influxdb
.. _Logstash/Kibana: https://github.com/alerta/alerta-contrib/tree/master/plugins/logstash
.. _Normalise: https://github.com/alerta/alerta-contrib/tree/master/plugins/normalise
.. _PagerDuty Plugin: https://github.com/alerta/alerta-contrib/tree/master/plugins/pagerduty
.. _Prometheus Silencer: https://github.com/alerta/alerta-contrib/tree/master/plugins/prometheus
.. _`Pushover.net`: https://github.com/alerta/alerta-contrib/tree/master/plugins/pushover
.. _Slack: https://github.com/alerta/alerta-contrib/tree/master/plugins/slack
.. _AWS SNS: https://github.com/alerta/alerta-contrib/tree/master/plugins/sns
.. _Syslog Logger: https://github.com/alerta/alerta-contrib/tree/master/plugins/syslog
.. _Telegram Bot: https://github.com/alerta/alerta-contrib/tree/master/plugins/telegram
.. _`Twilio SMS`: https://github.com/alerta/alerta-contrib/tree/master/plugins/twilio

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
