Alerts API
==========

.. _get-alerts:

GET /alerts
-----------

.. _get-alert-id:

GET /alert/<id>
---------------

Resource URL
++++++++++++

http://host:port/api/alert/:id

Parameters
++++++++++

+---------------+-------------+--------------------------------------+
| Parameter     | Description | Example                              |
+===============+=============+======================================+
| :id           | Alert ID    | 22c656fa-02bd-4dde-a761-2218d90338b1 |
| `mandatory`   |             |                                      |
+---------------+-------------+--------------------------------------+

Example Request
+++++++++++++++

GET http://host:port/api/alert/22c656fa-02bd-4dde-a761-2218d90338b1

.. code-block:: json

    {
      "status": "ok",
      "total": 1,
      "alert": {
        "origin": "alert-pinger/alerta01",
        "text": "Node did not respond to ping or timed out within 15 seconds",
        "lastReceiveTime": "2014-04-07T21:17:28.536Z",
        "receiveTime": "2014-04-04T14:49:49.879Z",
        "trendIndication": "moreSevere",
        "rawData": "PING 10-252-167-58 (10.252.167.58) 56(84) bytes of data.\n\n--- 10-252-167-58 ping statistics ---\n16 packets transmitted, 0 received, 100% packet loss, time 15000ms",
        "previousSeverity": "unknown",
        "event": "PingFailed",
        "group": "Ping",
        "severity": "major",
        "service": [
          "Network"
        ],
        "id": "22c656fa-02bd-4dde-a761-2218d90338b1",
        "environment": "development",
        "type": "serviceAlert",
        "status": "open",
        "repeat": true,
        "tags": [],
        "createTime": "2014-04-04T14:49:49.865Z",
        "lastReceiveId": "bc3f26d7-9aa3-404f-9e80-a8e25030ee13",
        "resource": "10-252-167-58:icmp",
        "duplicateCount": 4650,
        "correlate": [
          "PingFailed",
          "PingSlow",
          "PingOK",
          "PingError"
        ],
        "value": "100% packet loss",
        "timeout": 86400,
        "attributes": {},
        "history": [
          {
            "updateTime": "2014-04-04T14:49:49.865Z",
            "severity": "major",
            "text": "Node did not respond to ping or timed out within 15 seconds",
            "value": "100% packet loss",
            "event": "PingFailed",
            "id": "22c656fa-02bd-4dde-a761-2218d90338b1"
          },
          {
            "status": "open",
            "text": "new alert status change",
            "updateTime": "2014-04-04T14:49:49.879Z",
            "event": "PingFailed",
            "id": "22c656fa-02bd-4dde-a761-2218d90338b1"
          }
        ]
      }
    }

.. _post-alert:

POST /alert
-----------

.. _delete-alert-id:

DELETE /alert/<id>
------------------

.. _post-alert-id-status:

POST /alert/<id>/status
-----------------------

.. _post-alert-id-tag:

POST /alert/<id>/tag
--------------------

.. _post-alert-id-untag:

POST /alert/<id>/untag
----------------------

.. _get-alerts-history:

GET /alerts/history
-------------------

.. _get-alerts-count:

GET /alerts/count
-----------------

.. _get-alerts-top10:

GET /alerts/top10
-----------------

.. _get-environments:

GET /environments
-----------------

.. _get-services:

GET /services
-------------

.. _post-pagerduty:

POST /pagerduty
---------------