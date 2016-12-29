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
      "origin": "macbook",
      "tags": [
        "foo",
        "bar",
        "baz"
      ],
      "createTime": "2015-10-03T00:00:59.055Z",
      "href": "http://api.alerta.io/heartbeat/a8b97056-8415-4b4f-83c8-e84ffcc676a3",
      "timeout": 300,
      "receiveTime": "2015-10-03T00:00:59.681Z",
      "type": "Heartbeat",
      "id": "a8b97056-8415-4b4f-83c8-e84ffcc676a3"
    }
