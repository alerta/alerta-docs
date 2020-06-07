.. _heartbeat_format:

Heartbeat Format
================

Heartbeats received by Alerta conform to the following format.

.. _heartbeat_attributes:

Attributes
----------

The following heartbeat attributes are populated at source:

+----------------------+---------------------------------------------------------------------------------+
| Attribute            | Description                                                                     |
+======================+=================================================================================+
| ``id``               | globally unique random UUID                                                     |
+----------------------+---------------------------------------------------------------------------------+
| ``origin``           | name of monitoring component that generated the heartbeat                       |
+----------------------+---------------------------------------------------------------------------------+
| ``tags``             | set of tags in any format eg. ``aTag``, ``aDouble:Tag``, ``a:Triple=Tag``       |
+----------------------+---------------------------------------------------------------------------------+
| ``attributes``       | dictionary of key-value pairs                                                   |
+----------------------+---------------------------------------------------------------------------------+
| ``type``             | heartbeat type. only ``Heartbeat`` is currently supported                       |
+----------------------+---------------------------------------------------------------------------------+
| ``createTime``       | UTC date and time the heartbeat was generated in ISO 8601 format                |
+----------------------+---------------------------------------------------------------------------------+
| ``timeout``          | number of seconds before heartbeat is considered stale                          |
+----------------------+---------------------------------------------------------------------------------+

.. note:: Only ``origin`` is mandatory.

Attributes added when processing heartbeats
-------------------------------------------

+----------------------+---------------------------------------------------------------------------------+
| Attribute            | Description                                                                     |
+======================+=================================================================================+
| ``receiveTime``      | UTC date and time the heartbeat was received by the Alerta server daemon        |
+----------------------+---------------------------------------------------------------------------------+
| ``customer``         | assigned based on the owner of the API key used when submitting the heartbeat,  |
|                      | if "Customer Views" are enabled                                                 |
+----------------------+---------------------------------------------------------------------------------+

Example
-------

::

    {
      "attributes": {
        "environment": "Production", 
        "group": "Network", 
        "service": [
          "Core", 
          "HA"
        ], 
        "severity": "major"
      }, 
      "createTime": "2020-06-07T20:31:58.244Z", 
      "customer": null, 
      "href": "http://api.alerta.io/heartbeat/ea2f41e3-16c4-412f-aaf2-874e3c4c771b", 
      "id": "ea2f41e3-16c4-412f-aaf2-874e3c4c771b", 
      "latency": 0, 
      "maxLatency": 2000, 
      "origin": "cluster05", 
      "receiveTime": "2020-06-07T20:31:58.244Z", 
      "since": 91, 
      "status": "ok", 
      "tags": [
        "db05", 
        "dc2"
      ], 
      "timeout": 120, 
      "type": "Heartbeat"
    }
