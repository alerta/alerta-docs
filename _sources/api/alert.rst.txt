.. _alert format:

Alert Format
============

Alerts received and sent by Alerta conform to a common alert format.
All components of alerta use this message format and any external
systems must produce or consume messages in this format also.

.. _alert_attributes:

Attributes
----------

The following alert attributes are populated at source:

+-----------------+---------------------------------------------------------+
| Attribute       | Description                                             |
+=================+=========================================================+
| ``resource``    | resource under alarm, deliberately not host-centric     |
+-----------------+---------------------------------------------------------+
| ``event``       | event name eg. ``NodeDown``, ``QUEUE:LENGTH:EXCEEDED``  |
+-----------------+---------------------------------------------------------+
| ``environment`` | effected environment, used to namespace the resource    |
+-----------------+---------------------------------------------------------+
| ``severity``    | severity of alert (default ``normal``).                 |
|                 | see :ref:`severity table` table                         |
+-----------------+---------------------------------------------------------+
| ``correlate``   | list of related event names                             |
+-----------------+---------------------------------------------------------+
| ``status``      | status of alert (default ``open``).                     |
|                 | see :ref:`status table` table                           |
+-----------------+---------------------------------------------------------+
| ``service``     | list of effected services                               |
+-----------------+---------------------------------------------------------+
| ``group``       | event group used to group events of similar type        |
+-----------------+---------------------------------------------------------+
| ``value``       | event value eg. ``100%``, ``Down``, ``PingFail``,       |
|                 | ``55ms``, ``ORA-1664``                                  |
+-----------------+---------------------------------------------------------+
| ``text``        | freeform text description                               |
+-----------------+---------------------------------------------------------+
| ``tags``        | set of tags in any format eg. ``aTag``,                 |
|                 | ``aDouble:Tag``, ``a:Triple=Tag``                       |
+-----------------+---------------------------------------------------------+
| ``attributes``  | dictionary of key-value pairs                           |
+-----------------+---------------------------------------------------------+
| ``origin``      | name of monitoring component that generated the alert   |
+-----------------+---------------------------------------------------------+
| ``type``        | alert type eg. snmptrapAlert, syslogAlert, gangliaAlert |
+-----------------+---------------------------------------------------------+
| ``createTime``  | UTC date-time the alert was generated in ISO8601 format |
+-----------------+---------------------------------------------------------+
| ``timeout``     | number of seconds before alert is considered stale      |
+-----------------+---------------------------------------------------------+
| ``rawData``     | unprocessed data eg. full syslog message or SNMP trap   |
+-----------------+---------------------------------------------------------+

.. note:: Only ``event`` and ``resource`` are mandatory.

.. attention:: If the ``reject`` plugin is enabled (which it is by
    default) then alerts must have an ``environment`` attribute that
    is one of either ``Production`` or ``Development`` and it must
    define a ``service`` attribute. For more information on configuring
    or disabling this plugin see :ref:`plugin config`.

Attributes added when processing alerts
---------------------------------------

+----------------------+----------------------------------------------------+
| Attribute            | Description                                        |
+======================+====================================================+
| ``id``               | globally unique random UUID                        |
+----------------------+----------------------------------------------------+
| ``customer``         | assigned based on the owner of the API key used    |
|                      | when submitting the alert, if "Customer Views"     |
|                      | is enabled, or can be set if ``admin`` user        |
+----------------------+----------------------------------------------------+
| ``duplicateCount``   | a count of the number of times this event has been |
|                      | received for a resource                            |
+----------------------+----------------------------------------------------+
| ``repeat``           | if duplicateCount is 0 or the alert status has     |
|                      | changed then repeat is False, otherwise it is True |
+----------------------+----------------------------------------------------+
| ``previousSeverity`` | the previous severity of the same event for this   |
|                      | resource. if no event or ``correlate`` events      |
|                      | exist in the database for this resource then it    |
|                      | will be ``unknown``                                |
+----------------------+----------------------------------------------------+
| ``trendIndication``  | based on ``severity`` and ``previousSeverity``     |
|                      | will be one of ``moreSevere``, ``lessSevere`` or   |
|                      | ``noChange``                                       |
+----------------------+----------------------------------------------------+
| ``receiveTime``      | UTC datetime the alert was received by the         |
|                      | Alerta server daemon                               |
+----------------------+----------------------------------------------------+
| ``lastReceiveId``    | the last alert ``id`` received for this event      |
+----------------------+----------------------------------------------------+
| ``lastReceiveTime``  | the last time this alert was received. only        |
|                      | different to receiveTime if the alert is a         |
|                      | duplicate                                          |
+----------------------+----------------------------------------------------+
| ``updateTime``       | the last time the alert status changed. used to    |
|                      | calculate time remaining until an alert times out  |
+----------------------+----------------------------------------------------+
| ``history``          | whenever an alert changes severity or status then  |
|                      | a list of key alert attributes are appended to     |
|                      | the history log                                    |
+----------------------+----------------------------------------------------+

.. _status table:

Alert Status
------------

+-------------------+-----------------+
| Status            | Status Code     |
+===================+=================+
| ``open``          | 1               |
+-------------------+-----------------+
| ``assign``        | 2               |
+-------------------+-----------------+
| ``ack``           | 3               |
+-------------------+-----------------+
| ``closed``        | 4               |
+-------------------+-----------------+
| ``expired``       | 5               |
+-------------------+-----------------+
| ``blackout``      | 6               |
+-------------------+-----------------+
| ``shelved``       | 7               |
+-------------------+-----------------+
| ``unknown``       | 9               |
+-------------------+-----------------+

.. _severity table:

Alert Severities
----------------

The `Alarms in Syslog`_ :RFC:`5674` was referenced when defining
alert severities.

+-------------------+---------------+--------+
| Severity          | Severity Code | Colour |
+===================+===============+========+
| ``security``      | 0             | Black  |
+-------------------+---------------+--------+
| ``critical``      | 1             | Red    |
+-------------------+---------------+--------+
| ``major``         | 2             | Orange |
+-------------------+---------------+--------+
| ``minor``         | 3             | Yellow |
+-------------------+---------------+--------+
| ``warning``       | 4             | Blue   |
+-------------------+---------------+--------+
| ``informational`` | 5             | Green  |
+-------------------+---------------+--------+
| ``debug``         | 6             | Purple |
+-------------------+---------------+--------+
| ``trace``         | 7             | Grey   |
+-------------------+---------------+--------+
| ``indeterminate`` | 8             | Silver |
+-------------------+---------------+--------+
| ``cleared``       | 9             | Green  |
+-------------------+---------------+--------+
| ``normal``        | 9             | Green  |
+-------------------+---------------+--------+
| ``ok``            | 9             | Green  |
+-------------------+---------------+--------+
| ``unknown``       | 10            | Grey   |
+-------------------+---------------+--------+

.. _Alarms in Syslog: http://tools.ietf.org/html/rfc5674#section-2

.. _history:

History Entries
---------------

History log entries can be for either severity or status changes.

+--------------------+------------------------------------------------------+
| Attribute          | Description                                          |
+====================+======================================================+
| ``id``             | alert id that history log entry relates to           |
+--------------------+------------------------------------------------------+
| ``event``          | event name of alert changing severity or status      |
+--------------------+------------------------------------------------------+
| ``severity``  (*)  | new severity of alert changing severity              |
+--------------------+------------------------------------------------------+
| ``status``    (+)  | new status of alert changing status                  |
+--------------------+------------------------------------------------------+
| ``value``     (*)  | event value of alert changing severity               |
+--------------------+------------------------------------------------------+
| ``text``           | text describing reason for severity or status change |
+--------------------+------------------------------------------------------+
| ``type``           | history type eg. ``action``, ``status``,             |
|                    | ``severity`` or ``value`` change                     |
+--------------------+------------------------------------------------------+
| ``updateTime``     | UTC date-time the alert triggering the change was    |
|                    | created                                              |
+--------------------+------------------------------------------------------+

.. note:: The ``severity`` and ``value`` attributes are only added to
    the history log for alerts with ``event`` changes (See ``*`` above).
    And the ``status`` attribute is only added to the history log for
    alerts with ``status`` changes (See ``+`` above).

Example
-------

::

    {
      "attributes": {
        "flapping": false,
        "ip": "127.0.0.1",
        "notify": true,
        "region": "EU"
      },
      "correlate": [
        "HttpServerError",
        "HttpServerOK"
      ],
      "createTime": "2018-01-27T21:00:12.999Z",
      "customer": null,
      "duplicateCount": 0,
      "environment": "Production",
      "event": "HttpServerError",
      "group": "Web",
      "history": [
        {
          "event": "HttpServerError",
          "href": "http://localhost:8080/alert/17d8e7ea-b3ba-4bb1-9c5a-29e60865f258",
          "id": "17d8e7ea-b3ba-4bb1-9c5a-29e60865f258",
          "severity": "major",
          "status": null,
          "text": "Site is down.",
          "type": "severity",
          "updateTime": "2018-01-27T21:00:12.999Z",
          "value": "Bad Gateway (501)"
        }
      ],
      "href": "http://localhost:8080/alert/17d8e7ea-b3ba-4bb1-9c5a-29e60865f258",
      "id": "17d8e7ea-b3ba-4bb1-9c5a-29e60865f258",
      "lastReceiveId": "17d8e7ea-b3ba-4bb1-9c5a-29e60865f258",
      "lastReceiveTime": "2018-01-27T21:00:13.070Z",
      "origin": "curl",
      "previousSeverity": "indeterminate",
      "rawData": null,
      "receiveTime": "2018-01-27T21:00:13.070Z",
      "repeat": false,
      "resource": "web01",
      "service": [
        "example.com"
      ],
      "severity": "major",
      "status": "open",
      "tags": [
        "dc1"
      ],
      "text": "Site is down.",
      "timeout": 86400,
      "trendIndication": "moreSevere",
      "type": "exceptionAlert",
      "value": "Bad Gateway (501)"
    }
