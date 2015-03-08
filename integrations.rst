.. _integrations:

Integrations & Plugins
======================

There are several different ways to integrate other alert sources into Alerta. Integrations with key open source monitoring tools have been developed and provide good starting points for other, perhaps bespoke, monitoring tools.


Integrations
------------

Core
~~~~

There are a few core integrations which have been developed to showcase how easy it is to quickly get alerts or events from other tools into Alerta. They are:

* `Nagios Event Broker`_ (C)
* `Zabbix Alert Script`_ (Python)
* `Sensu Plugin`_ (Ruby)
* `Riemann Integration`_ (Clojure)

Contrib
~~~~~~~

There are several more integrations available in the `contrib`_ repo. They are:

* `Amazon SQS`_
* AMQP
* `AWS Cloudwatch`_
* Opsweekly_
* Pinger
* SNMP Trap
* Supervisor_
* Syslog
* URL monitor

.. _contrib: https://github.com/alerta/alerta-contrib

Webhooks
--------

POST, OPTIONS  /webhooks/cloudwatch  cloudwatch
HEAD, OPTIONS, GET  /webhooks/pingdom  pingdom

AWS Cloudwatch
~~~~~~~~~~~~~~

See AwsCloudwatch_

Pingdom
~~~~~~~

See Pingdom_

.. _AwsCloudwatch: http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html
.. _Pingdom: https://support.pingdom.com/Knowledgebase/Article/View/94/0/users-and-alerting-end-points


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

Contrib
~~~~~~~

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


oEmbed
------

Example
+++++++

From https://github.com/guardian/alerta/blob/master/examples/oembed.html

.. code:: html

  <!DOCTYPE html>
  <html lang="en">
  <head>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" />
    <link href='http://fonts.googleapis.com/css?family=Sintony:700' rel='stylesheet' type='text/css'>
  </head>
  <body>

  <div class="mobile-alerts">Loading...</div>

  <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  <script src="http://api.alerta.io/embed.js"></script>
  <script>
  $(function() {

    // $.alerta.defaults.endpoint = 'http://localhost:8080';
    // $.alerta.defaults.key = 'demo-key';
    // or
    $.alerta.defaults = {
        endpoint: 'http://api.alerta.io', // oEmbed endpoint becomes http://api.alerta.io/oembed.json
        key: 'demo-key'
    };

    $('.mobile-alerts').alerta('http://api.alerta.io/alerts/count?service=Mobile&status=open', {title:'Mobile Service'});

  });
  </script>
  </body>
  </html>

HEAD, OPTIONS, GET  /embed.js  embed_js
HEAD, OPTIONS, GET  /oembed.json  oembed


