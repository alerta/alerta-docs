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
| ``resource``         | the resource under alarm, deliberately not host-centric                         |
+----------------------+---------------------------------------------------------------------------------+
| ``event``            | event name eg. ``NodeDown``, ``QUEUE:LENGTH:EXCEEDED``, ``AppStatus``           |
+----------------------+---------------------------------------------------------------------------------+
| ``environment``      | effected environment, used to namespace the defined resource                    |
+----------------------+---------------------------------------------------------------------------------+
| ``severity``         | severity of alert eg. ``critical`` see full list below                          |
+----------------------+---------------------------------------------------------------------------------+
| ``correlate``        | list of related event names                                                     |
+----------------------+---------------------------------------------------------------------------------+
| ``status`` *         | one of ``open``, ``ack``, ``closed``, or ``expired``                            |
+----------------------+---------------------------------------------------------------------------------+
| ``service``          | list of effected services                                                       |
+----------------------+---------------------------------------------------------------------------------+
| ``group``            | event group                                                                     |
+----------------------+---------------------------------------------------------------------------------+
| ``value``            | event value eg. 100%, Down, PingFail, 55ms, ORA-1664                            |
+----------------------+---------------------------------------------------------------------------------+
| ``text``             | freeform text description                                                       |
+----------------------+---------------------------------------------------------------------------------+
| ``tags``             | list of tags in any format eg. ``aTag``, ``aDouble:Tag``, ``a:Triple=Tag``      |
+----------------------+---------------------------------------------------------------------------------+
| ``attributes``       | dictionary of key-value pairs                                                   |
+----------------------+---------------------------------------------------------------------------------+
| ``origin``           | name of monitoring component that generated the alert                           |
+----------------------+---------------------------------------------------------------------------------+
| ``type``             | alert type eg. snmptrapAlert, syslogAlert, gangliaAlert                         |
+----------------------+---------------------------------------------------------------------------------+
| ``createTime``       | UTC date and time the alert was generated in ISO 8601 format                    |
+----------------------+---------------------------------------------------------------------------------+
| ``timeout``          | number of seconds before alert is deleted from database                         |
+----------------------+---------------------------------------------------------------------------------+
| ``rawData``          | unprocessed data eg. full syslog message or SNMP trap                           |
+----------------------+---------------------------------------------------------------------------------+

.. note:: Only ``event`` and ``resource`` are mandatory.

Alert attributes added when processing alerts
---------------------------------------------

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

Alert Severities
----------------

The `Alarms in Syslog`_ RFC was referenced when defining alert severities.

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



