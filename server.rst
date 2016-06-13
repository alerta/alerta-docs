.. _server:

Server & API
============

The Alerta API receives alerts from multiple sources, :ref:`correlates <correlation>`,
:ref:`de-duplicates  <deduplication>` or :ref:`suppresses <blackout periods>`
them, and makes the alerts available via a RESTful_ JSON_ API.

.. _RESTful: http://apigee.com/about/resources/webcasts/restful-api-design-second-edition
.. _JSON: http://developers.squarespace.com/what-is-json/

Alerts can be intercepted as they are received to modify, enhance or reject them
using :ref:`pre-receive hooks <prereceive>`. Alerts can also be used to trigger
actions in other systems after the alert has been processed using
:ref:`post-receive hooks <postreceive>` or following an alert
:ref:`status change <status_change>` for bi-directional integration.

There are several :ref:`integrations <integrations>` with popular monitoring tools
available and :ref:`webhooks <webhooks>` can be used to trivially integrate with
AWS Cloudwatch, Pingdom, and PagerDuty.

.. _event_processing:

Event Processing
----------------

Alerta comes `out-of-the-box` with key features designed to reduce the burden of
alert management. When an event is received it it is processed in the following
way:

1. all plugin pre-receive hooks are run in alphabetical order, an alert
   immediately rejected if any plugins return a Reject Exception
2. alert is checked against any active blackout periods, alert suppressed if any
   match
3. alert is checked if duplicate, if so duplicate count is increased and repeat
   set to `True`
4. alert is checked if correlated, if so change severity and/or status etc
5. alert is neither a duplicate or correlated so create new alert
6. all plugin post-receive hooks are run in alphabetical order
7. new or updated alert returned in response
8. timeout used to expire alerts from the console

Each of the above actions are explained in more detail in the following sections.

Plug-ins
--------

Plug-ins are small python scripts that can run either before or after an alert is
saved to the database, or before a status change update. This is achieved by
registering *pre-receive hooks* for transformers, *post-receive hooks* for
external notification and *status change hooks* for bi-directional integration.

.. _prereceive:

Transformers
~~~~~~~~~~~~

Using pre-receive hooks, plugins provide the ability to transform raw alert data
from sources before alerts are created. For example, alerts can be *normalised*
to ensure they all have specific attributes or tags or only have a specific value
from a range of allowed values. This is demonstrated in the `reject plugin`_
that enforces an alert policy.

.. _reject plugin: https://github.com/guardian/alerta/blob/master/alerta/plugins/reject.py

Plugins can also be used to *enhance* alerts  -- like the `Geo location plugin`_
which adds location data to alerts based on the remote IP address of the client,
or the generic `enhance plugin`_ which adds a ``customer`` attribute based on
information contained in the alert.

.. _Geo location plugin: https://github.com/alerta/alerta-contrib/blob/master/plugins/geoip/geoip.py
.. _enhance plugin: https://github.com/guardian/alerta/blob/master/alerta/plugins/enhance.py

.. _postreceive:

External Notification
~~~~~~~~~~~~~~~~~~~~~

Using post-receive hooks, plugin integrations can be used to provide downstream
systems with alerts in realtime for external notification. For example, pushing
alerts onto an `AWS SNS topic`_, `AMQP queue`_, logging to a `Logstash/Kibana`_
stack, or sending notifications to `HipChat`_, `Slack`_ or `Twilio`_ and many
more.

.. _AWS SNS topic: https://github.com/guardian/alerta/blob/master/alerta/plugins/sns.py
.. _AMQP queue: https://github.com/guardian/alerta/blob/master/alerta/plugins/amqp.py
.. _Logstash/Kibana: https://github.com/guardian/alerta/blob/master/alerta/plugins/logstash.py
.. _HipChat: https://github.com/alerta/alerta-contrib/blob/master/plugins/hipchat
.. _Slack: https://github.com/alerta/alerta-contrib/blob/master/plugins/slack
.. _Twilio: https://github.com/alerta/alerta-contrib/blob/master/plugins/twilio

.. _status_change:

Bi-directional Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Using status change hooks, plugins can be used to complete a two way integration
with an external system. That is, an external system like Prometheus Alertmanager
that generates alerts that are forwarded to Alerta can be updated when the status
of an alert changes in Alerta.

For example, if an operator "acknowledges" a Prometheus alert in the Alerta web
UI then a status change hook could silence_ the `corresponding alert in Alertmanager`_.
This requires that external systems provide enough information in the alert created
in Alerta for that alert to be uniquely identified at a later date.

.. _silence: https://prometheus.io/docs/alerting/alertmanager/#silences
.. _corresponding alert in Alertmanager: https://github.com/alerta/alerta-contrib/blob/master/plugins/prometheus/prometheus.py

.. _blackout periods:

Blackout Periods
----------------

An alert that is received during a :index:`blackout period <single: blackouts>`
is suppressed. That is, it is received by Alerta and a ``202 Accepted`` status
code is returned however this means that even though the alert has been accepted,
it won't be processed.

Alerta defines many different alert attributes that can be used to group alerts
and it is these attributes that can be used to define blackout rules. For example,
to suppress alerts from an entire environment, service or group, or a combination
of these. However, it is possible to define blackout rules based only on resource
and event attributes for situations that require that level of granularity.

Tags can also be used to define a blackout rule which should allow a lot of
flexibility because tags can be added at source, using the ``alerta`` CLI, or
using a plug-in. Note that one or more tags can be required to match an alert
for the suppression to apply.

In summary, blackout rules can be any of:

* an entire environment eg. ``environment=Production``
* a particular resource eg. ``resource=host55``
* an entire service eg. ``service=Web``
* every occurrence of a specific event eg. ``event=DiskFull``
* a group of events eg. ``group=Syslog``
* a specific event for a resource eg. ``resource=host55 and event=DiskFull``
* all events that have a specific set of tags eg. ``tags=[ blackout, london ]``

Note that an ``environment`` is always required to be defined for a blackout rule.

.. _deduplication:

De-Duplication
--------------

When an alert with the same ``event``-``resource`` is received with the **same**
``severity``, the alert is de-duplicated.

This means that information from the de-duplicated alert is used to update key
attributes of the existing alert (like ``duplicateCount``, ``repeat`` flag,
``value``, ``text`` and ``lastReceiveTime``) and the new alert is not shown.

Alerts are sorted in the Alerta web UI by ``lastReceiveTime`` by default so that
the most recent alerts will be displayed at the top regardless of whether they
were new alerts or de-duplicated alerts.

.. _correlation:

Simple Correlation
------------------

Alerta implements what we call "simple correlation" -- as opposed to `complex
correlation`_ which is much_ more_ involved_. Simple correlation, in combination
with de-duplication, provides straight-forward and effective ways to reduce the
burden of managing an alert console.

With Alerta, there are two ways alerts can be correlated, namely:

1. when an alert with the same ``event``-``resource`` is received with a
  **different** ``severity``, then the alert is correlated.
2. when a alert with the same ``resource`` is received with an ``event`` in the
  ``correlate`` list of related events with **any** severity, then the alert is
  correlated.

.. _complex correlation: https://en.wikipedia.org/wiki/Complex_event_processing
.. _much: http://www.espertech.com/
.. _more: http://riemann.io/
.. _involved: http://www.drools.org/

In both cases, this means that information from the correlated alert is used to
update key attributes of the existing alert (like ``severity``, ``event``,
``value``, ``text`` and ``lastReceiveTime``) and the new alert is not shown.

.. _state based browser:

State-based Browser
-------------------

Alerta is called state-based because it will **automatically** *change the alert
status* based on the current and previous severity of alerts and subsequent user
actions.

The Alerta API will:

* only show the most recent state of any alert
* change the status of an alert to ``closed`` if a ``normal``, ``ok`` or
  ``cleared`` is received
* change the status of a ``closed`` alert to ``open`` if the event reoccurs
* change the status of an ``acknowledged`` alert to ``open`` if the new severity
  is higher than the current ``severity``
* update the ``severity`` and other key attributes of an alert when a more recent
  alert is received (see correlation_ and deduplication_)
* update the ``trendIndication`` attribute based on ``previousSeverity`` and
  current ``severity`` with either ``moreSevere``, ``lessSevere`` or ``noChange``
* update the ``history`` log following a ``severity`` or ``status`` change (see
  `alert history`_)

All of these automatic actions combine to ensure that important alerts are given
the priority they deserve.

.. note:: To take full advantage of the state-based browser it is recommended to
    implement the timeout of ``expired`` alerts using the :ref:`housekeeping`
    script.

Alert History
-------------

Whenever an alert status or severity changes, that change is recorded in the
alert :ref:`history <history>` log. This is to allow operations staff follow the
lifecycle of a particular alert, if necessary.

The alert history is visible in the *Alert Details* page of any alert and also
by using the ``alerta`` command-line tool ``history`` sub-command.

For example, it will show whether an alert status change happened as a result of
operator (external) action or an automatic correlation_ (auto) action.

Heartbeats
----------

An Alerta :ref:`heartbeat <Heartbeats>` is a periodic HTTP request sent to the
Alerta API to indicate normal operation of the origin of the heartbeat.

They can be used to ensure components of the Alerta monitoring system are
operating normally or sent from any other source. As well as an ``origin``
they include a ``timeout`` in seconds (after which they will be considered stale),
and optional ``tags``.

They are visible in the Alerta console (*About* page) and via the ``alerta``
command-line tool using the ``heartbeat`` sub-command to send them, and the
``heartbeats`` sub-command to view them.

Alerts can be generated from :index:`stale heartbeats <pair: heartbeat; stale>`
using ``alerta heartbeats --alert``.

.. _wiki: https://en.wikipedia.org/wiki/Heartbeat_(computing)
