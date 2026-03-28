.. _tutorial 8 webhooks:

Webhook Integrations
====================

In this tutorial, you will learn how to use Alerta webhooks to
receive alerts from Prometheus Alertmanager, Grafana, and other
tools that can send HTTP POST requests.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Understand webhook URLs`_
  * `Step 2: Configure Prometheus Alertmanager`_
  * `Step 3: Configure Grafana`_
  * `Step 4: Test with curl`_
  * `Next Steps`_

Overview
--------

Alerta provides built-in webhook receivers that accept HTTP POST
requests at ``/api/webhooks/<provider>`` and translate provider-specific
payloads into Alerta alerts. This means the sending tool does not
need to know the Alerta alert format -- it sends its native payload
and the webhook handler does the translation.

Built-in webhooks include ``prometheus``, ``grafana``, ``pagerduty``,
``cloudwatch``, ``pingdom``, ``stackdriver``, and many more.

Prerequisites
-------------

Before you begin, you should have:

  * A running Alerta server (see :ref:`tutorial 10`)
  * An Alerta API key with ``write:alerts`` scope
  * Prometheus and Alertmanager installed (for Step 2)
  * Grafana installed (for Step 3)

.. _Step 1:

Step 1: Understand webhook URLs
-------------------------------

All webhook URLs follow the same pattern::

    POST http://alerta.example.com:8080/api/webhooks/<provider>?api-key=<YOUR_API_KEY>

The ``<provider>`` name determines which webhook handler processes the
incoming payload. For example:

  * ``/api/webhooks/prometheus`` -- Prometheus Alertmanager
  * ``/api/webhooks/grafana`` -- Grafana alerts
  * ``/api/webhooks/cloudwatch`` -- AWS CloudWatch alarms

The API key can be passed as a query parameter (``?api-key=``) or
in the ``Authorization`` header (``Authorization: Key <api-key>``).

.. _Step 2:

Step 2: Configure Prometheus Alertmanager
-----------------------------------------

The Prometheus webhook extracts ``severity``, ``environment``,
``service``, ``resource``, and ``event`` from alert labels. Any
remaining labels become tags, and annotations become attributes.

Edit the Alertmanager configuration file (``alertmanager.yml``)
to add an Alerta webhook receiver:

.. code-block:: yaml

    receivers:
      - name: alerta
        webhook_configs:
          - url: 'http://alerta.example.com:8080/api/webhooks/prometheus?api-key=your-api-key'
            send_resolved: true

    route:
      receiver: alerta
      group_by: ['alertname', 'instance']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 4h

You can control the Alerta severity and environment by adding
labels to your Prometheus alerting rules:

.. code-block:: yaml

    groups:
      - name: example
        rules:
          - alert: HighRequestLatency
            expr: http_request_duration_seconds{quantile="0.99"} > 1
            for: 10m
            labels:
              severity: warning
              environment: Production
              service: Web
            annotations:
              summary: "High request latency on {{ $labels.instance }}"
              description: "99th percentile latency is {{ $value }}s"

If no ``environment`` label is set, the webhook uses the server
default (``DEFAULT_ENVIRONMENT``, which defaults to ``Production``).

Reload Alertmanager to apply the configuration::

    $ curl -X POST http://localhost:9093/-/reload

.. _Step 3:

Step 3: Configure Grafana
--------------------------

Grafana can send alerts to Alerta using its built-in webhook
contact point.

In Grafana, navigate to **Alerting > Contact points** and create
a new contact point:

  * **Name:** Alerta
  * **Type:** Webhook
  * **URL:** ``http://alerta.example.com:8080/api/webhooks/grafana``
  * **HTTP Method:** POST
  * **Authorization Header:** ``Key your-api-key``

Then assign this contact point to a notification policy under
**Alerting > Notification policies**.

.. note:: Set ``GRAFANA_TAGS_AS_ATTRIBUTES = True`` in ``alertad.conf``
   (the default) to store Grafana alert tags as Alerta attributes. Set
   ``GRAFANA_TAGS_AS_TAGS = True`` if you prefer them as Alerta tags.

.. _Step 4:

Step 4: Test with curl
-----------------------

You can test the Prometheus webhook by sending a sample payload
directly with ``curl``:

.. code-block:: bash

    $ curl -X POST http://localhost:8080/api/webhooks/prometheus?api-key=your-api-key \
      -H 'Content-Type: application/json' \
      -d '{
        "status": "firing",
        "alerts": [{
          "status": "firing",
          "labels": {
            "alertname": "TestAlert",
            "severity": "warning",
            "instance": "web01:9090",
            "environment": "Development",
            "service": "Web"
          },
          "annotations": {
            "summary": "Test alert from curl"
          },
          "startsAt": "2024-01-01T00:00:00Z",
          "endsAt": "0001-01-01T00:00:00Z",
          "generatorURL": "http://prometheus:9090/graph"
        }]
      }'

Verify the alert was created::

    $ alerta query --filter resource=web01:9090

Next Steps
----------

  * :ref:`Troubleshooting <tutorial 9>`
  * :ref:`Kubernetes Deployment <tutorial 11>`
