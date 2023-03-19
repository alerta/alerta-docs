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

`Core plugins`_ have been developed as examples of common use-cases.

.. _Core plugins: https://github.com/alerta/alerta/tree/master/alerta/plugins

* `Reject`_ - reject alerts before processing. used to enforce custom alert format policies
* `Blackout`_ - suppression handler that will drop alerts that match a blackout period

.. _Reject: https://github.com/alerta/alerta/blob/master/alerta/plugins/reject.py
.. _Blackout: https://github.com/alerta/alerta/blob/master/alerta/plugins/blackout.py

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



custom error responses


