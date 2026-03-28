.. _tutorial 4 customisation:

Customising Alerts
==================

In this tutorial you will learn how to customise alert severity levels,
colors, timeouts, correlation, and actions to fit your environment.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Custom Severity Levels`_
  * `Step 2: Custom Severity Colors`_
  * `Step 3: Alert Correlation`_
  * `Step 4: Alert De-duplication`_
  * `Step 5: Custom Attributes`_
  * `Step 6: Custom Actions`_
  * `Step 7: Alert Timeouts`_
  * `Next Steps`_

Overview
--------

Alerta ships with sensible defaults for severity levels, colors, and
timeouts, but most organisations need to adapt these to match existing
operational procedures. This tutorial walks through the main
customisation options available in the server configuration file
(``alertad.conf``).

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
or you have access to an Alerta server that you can send alerts to
using the ``alerta`` command-line tool.

Step 1: Custom Severity Levels
------------------------------

The default alarm model defines severities from ``security`` (most
severe) down through ``critical``, ``major``, ``minor``, ``warning``,
``informational``, to ``normal`` (least severe). You can override
the severity map by setting ``SEVERITY_MAP`` in ``alertad.conf``.

Each severity is assigned a numeric code -- lower numbers are more
severe::

    SEVERITY_MAP = {
        'critical': 1,
        'high': 2,
        'medium': 3,
        'low': 4,
        'ok': 5
    }
    DEFAULT_NORMAL_SEVERITY = 'ok'

Restart the server after making changes. Send a test alert with a
custom severity:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/alert -H 'Content-Type: application/json' -d '{
      "resource": "web01",
      "event": "HttpError",
      "environment": "Production",
      "service": ["Web"],
      "severity": "high",
      "text": "HTTP 500 errors detected."
    }'

Step 2: Custom Severity Colors
------------------------------

Pair custom severities with colors for the web console using
``COLOR_MAP``. Each severity maps to a ``severity`` color and a
``text`` color::

    COLOR_MAP = {
        'critical': {'severity': '#E74C3C', 'text': '#FFFFFF'},
        'high':     {'severity': '#E67E22', 'text': '#FFFFFF'},
        'medium':   {'severity': '#F1C40F', 'text': '#000000'},
        'low':      {'severity': '#3498DB', 'text': '#FFFFFF'},
        'ok':       {'severity': '#2ECC71', 'text': '#FFFFFF'}
    }

Step 3: Alert Correlation
-------------------------

Alert correlation groups related events so that a new event on the
same resource replaces an existing alert rather than creating a
duplicate. Set the ``correlate`` field to a list of related event
names when sending an alert:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/alert -H 'Content-Type: application/json' -d '{
      "resource": "web01",
      "event": "HttpError",
      "correlate": ["HttpError", "HttpOk"],
      "environment": "Production",
      "service": ["Web"],
      "severity": "major",
      "text": "HTTP 500 errors detected."
    }'

Now send the correlated clearing event:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/alert -H 'Content-Type: application/json' -d '{
      "resource": "web01",
      "event": "HttpOk",
      "correlate": ["HttpError", "HttpOk"],
      "environment": "Production",
      "service": ["Web"],
      "severity": "normal",
      "text": "HTTP service restored."
    }'

The second alert replaces the first because both events share a
``correlate`` list and target the same ``resource``.

Step 4: Alert De-duplication
----------------------------

When an alert is received that matches an existing alert on
``environment``, ``resource``, and ``event`` (and there is no
``correlate`` list), the alert is de-duplicated. The ``duplicateCount``
is incremented, the ``value`` and ``text`` are updated, and a history
entry is added if the value changed.

.. code-block:: console

  $ alerta send -r host01 -e DiskFull -s major -E Production -S System -t 'Disk 90% full.'
  $ alerta send -r host01 -e DiskFull -s major -E Production -S System -t 'Disk 95% full.'

  $ alerta query -r host01 --filter event=DiskFull
  # duplicateCount will show 1

Step 5: Custom Attributes
-------------------------

Alerts can carry arbitrary key-value attributes for enrichment.
Attributes are passed in the ``attributes`` field:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/alert -H 'Content-Type: application/json' -d '{
      "resource": "web01",
      "event": "HttpError",
      "environment": "Production",
      "service": ["Web"],
      "severity": "major",
      "text": "HTTP 500 errors detected.",
      "attributes": {
        "region": "EU",
        "team": "WebOps",
        "runbook": "https://wiki.example.com/runbooks/http-500"
      }
    }'

Custom attributes appear in the alert detail view in the web console
and can be used by plugins for routing or enrichment.

Step 6: Custom Actions
----------------------

Custom actions extend the set of operations available on alerts
beyond the built-in ``ack``, ``shelve``, and ``close``. Define
them in ``alertad.conf``::

    ACTIONS = ['escalate', 'createTicket']

Custom actions appear as buttons in the web console. Use a
post-receive plugin to implement the action logic. Trigger a custom
action via the API:

.. code-block:: console

  $ curl -XPUT http://localhost:8080/api/alert/ALERT_ID/action \
    -H 'Content-Type: application/json' -d '{"action": "escalate", "text": "Escalating to L2."}'

Step 7: Alert Timeouts
----------------------

Alerts expire automatically after a configurable timeout. The
default is 86400 seconds (24 hours). Override globally or per-alert::

    ALERT_TIMEOUT = 43200  # 12 hours globally

Or set the timeout on individual alerts:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/alert -H 'Content-Type: application/json' -d '{
      "resource": "web01",
      "event": "HttpError",
      "environment": "Production",
      "service": ["Web"],
      "severity": "major",
      "text": "HTTP 500 errors detected.",
      "timeout": 3600
    }'

Related timeouts include ``ACK_TIMEOUT`` (auto-unack after n seconds,
default 0 meaning disabled) and ``SHELVE_TIMEOUT`` (auto-unshelve,
default 7200 seconds).

Next Steps
----------

Now that you understand alert customisation, you might want to try
some of the following tutorials:

  * :ref:`Suppressing alerts using blackouts <tutorial 5>`
  * :ref:`Authentication and authorization <tutorial 6>`
