.. _alert_format:

Alert Format
============

Alerts received and sent by Alerta conform to a common alert format. All components of alerta use this message format and any external systems must produce or consume messages in this format also.

.. _alert_attributes:

Attributes
----------

The following alert attributes are populated at source:

+----------------------+---------------------------------------------------------------------------------+
| Attribute            | Description                                                                     |
+======================+=================================================================================+
| ``id``               | globally unique random UUID                                                     |
+----------------------+---------------------------------------------------------------------------------+
| ``resource``         | resource under alarm, deliberately not host-centric                             |
+----------------------+---------------------------------------------------------------------------------+
| ``event``            | event name eg. ``NodeDown``, ``QUEUE:LENGTH:EXCEEDED``, ``AppStatus``           |
+----------------------+---------------------------------------------------------------------------------+
| ``environment``      | effected environment, used to namespace the defined resource                    |
+----------------------+---------------------------------------------------------------------------------+
| ``severity``         | severity of alert (default ``normal``). see :ref:`severity_table` table         |
+----------------------+---------------------------------------------------------------------------------+
| ``correlate``        | list of related event names                                                     |
+----------------------+---------------------------------------------------------------------------------+
| ``status``           | status of alert (default ``open``). see :ref:`status_table` table               |
+----------------------+---------------------------------------------------------------------------------+
| ``service``          | list of effected services                                                       |
+----------------------+---------------------------------------------------------------------------------+
| ``group``            | event group                                                                     |
+----------------------+---------------------------------------------------------------------------------+
| ``value``            | event value eg. ``100%``, ``Down``, ``PingFail``, ``55ms``, ``ORA-1664``        |
+----------------------+---------------------------------------------------------------------------------+
| ``text``             | freeform text description                                                       |
+----------------------+---------------------------------------------------------------------------------+
| ``tags``             | set of tags in any format eg. ``aTag``, ``aDouble:Tag``, ``a:Triple=Tag``       |
+----------------------+---------------------------------------------------------------------------------+
| ``attributes``       | dictionary of key-value pairs                                                   |
+----------------------+---------------------------------------------------------------------------------+
| ``origin``           | name of monitoring component that generated the alert                           |
+----------------------+---------------------------------------------------------------------------------+
| ``type``             | alert type eg. snmptrapAlert, syslogAlert, gangliaAlert                         |
+----------------------+---------------------------------------------------------------------------------+
| ``createTime``       | UTC date and time the alert was generated in ISO 8601 format                    |
+----------------------+---------------------------------------------------------------------------------+
| ``timeout``          | number of seconds before alert is considered stale                              |
+----------------------+---------------------------------------------------------------------------------+
| ``rawData``          | unprocessed data eg. full syslog message or SNMP trap                           |
+----------------------+---------------------------------------------------------------------------------+

.. note:: Only ``event`` and ``resource`` are mandatory.

Attributes added when processing alerts
---------------------------------------

+----------------------+---------------------------------------------------------------------------------+
| Attribute            | Description                                                                     |
+======================+=================================================================================+
| ``duplicateCount``   | a count of the number of times this event has been received for a resource      |
+----------------------+---------------------------------------------------------------------------------+
| ``repeat``           | if duplicateCount is 0 or the alert status has changed then repeat is False,    |
|                      | otherwise it is True                                                            |
+----------------------+---------------------------------------------------------------------------------+
| ``previousSeverity`` | the previous severity of the same event for this resource. if no event or       |
|                      | ``correlate`` events exist in the database for this resource then it            |
|                      | will be ``unknown``                                                             |
+----------------------+---------------------------------------------------------------------------------+
| ``trendIndication``  | based on ``severity`` and ``previousSeverity`` will be one of ``moreSevere``,   |
|                      | ``lessSevere`` or ``noChange``                                                  |
+----------------------+---------------------------------------------------------------------------------+
| ``receiveTime``      | UTC date and time the alert was received by the Alerta server daemon            |
+----------------------+---------------------------------------------------------------------------------+
| ``lastReceiveId``    | the last alert ``id`` received for this event                                   |
+----------------------+---------------------------------------------------------------------------------+
| ``lastReceiveTime``  | the last time this alert was received. only different to receiveTime if the     |
|                      | alert is a duplicate                                                            |
+----------------------+---------------------------------------------------------------------------------+
| ``history``          | whenever an alert changes severity or status then a list of key alert           |
|                      | attributes are appended to the history log                                      |
+----------------------+---------------------------------------------------------------------------------+

.. _status_table:

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
| ``unknown``       | 9               |
+-------------------+-----------------+

.. _severity_table:

Alert Severities
----------------

The `Alarms in Syslog`_ :RFC:`5674` was referenced when defining alert severities.

+-------------------+---------------+--------+
| Severity          | Severity Code | Colour |
+===================+===============+========+
| ``critical``      | 1             | Red    |
+-------------------+---------------+--------+
| ``major``         | 2             | Orange |
+-------------------+---------------+--------+
| ``minor``         | 3             | Yellow |
+-------------------+---------------+--------+
| ``warning``       | 4             | Blue   |
+-------------------+---------------+--------+
| ``indeterminate`` | 5             | Green  |
+-------------------+---------------+--------+
| ``cleared``       | 5             | Green  |
+-------------------+---------------+--------+
| ``normal``        | 5             | Green  |
+-------------------+---------------+--------+
| ``ok``            | 5             | Green  |
+-------------------+---------------+--------+
| ``informational`` | 6             | Green  |
+-------------------+---------------+--------+
| ``debug``         | 7             | Purple |
+-------------------+---------------+--------+
| ``security``      | 8             | Grey   |
+-------------------+---------------+--------+
| ``unknown``       | 9             | Grey   |
+-------------------+---------------+--------+

.. _Alarms in Syslog: http://tools.ietf.org/html/rfc5674#section-2

History Entries
---------------


Example
-------

::

    {
      "resource": "web-elb-01",
      "event": "HttpServerError",
      "origin": "curl",
      "text": "The site is down.",
      "lastReceiveTime": "2015-03-01T23:34:30.635Z",
      "receiveTime": "2015-03-01T23:34:28.118Z",
      "trendIndication": "moreSevere",
      "href": "http://api.alerta.io/alert/f26b3695-0e67-402f-81be-ba966bcb9603",
      "rawData": "curl: (7) Failed connect to localhost:8080; Connection refused",
      "previousSeverity": "unknown",
      "group": "Web",
      "severity": "major",
      "service": [
        "example.com"
      ],
      "id": "f26b3695-0e67-402f-81be-ba966bcb9603",
      "environment": "Production",
      "type": "webAlert",
      "status": "closed",
      "repeat": true,
      "tags": [
        "eu-west-1",
        "AWS/EC2"
      ],
      "createTime": "2015-03-01T23:34:27.467Z",
      "lastReceiveId": "1637de1f-eac5-48dd-a4dd-8a10e4c89843",
      "duplicateCount": 1,
      "correlate": [
        "HttpServerError",
        "HttpServerOK"
      ],
      "value": "Bad Gateway (501)",
      "timeout": 86400,
      "attributes": {
        "city": "London",
        "region_code": "ENG",
        "region_name": "England",
        "ip": "86.156.104.171",
        "company": "ACME Corp",
        "time_zone": "Europe/London",
        "longitude": -0.124,
        "metro_code": 0,
        "latitude": 51.453,
        "country_code": "GB",
        "country_name": "United Kingdom",
        "zip_code": "SW2"
      },
      "history": [
        {
          "updateTime": "2015-03-01T23:34:27.467Z",
          "severity": "major",
          "text": "The site is down.",
          "value": "Bad Gateway (501)",
          "event": "HttpServerError",
          "id": "f26b3695-0e67-402f-81be-ba966bcb9603"
        },
        {
          "status": "ack",
          "text": "status change via console",
          "updateTime": "2015-03-02T02:49:10.297Z",
          "event": "HttpServerError",
          "id": "f26b3695-0e67-402f-81be-ba966bcb9603"
        },
        {
          "status": "closed",
          "text": "status change via console",
          "updateTime": "2015-03-02T02:49:11.719Z",
          "event": "HttpServerError",
          "id": "f26b3695-0e67-402f-81be-ba966bcb9603"
        }
      ]
    }



