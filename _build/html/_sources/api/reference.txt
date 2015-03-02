API Reference
=============

.. contents:: Resource Types
   :local:
   :depth: 2

.. _alerts:

Alerts
------

.. _post_alert:

Send an alert
~~~~~~~~~~~~~

::

  POST /alert

Input
+++++

Only ``resource`` and ``event`` are required. See :ref:`Alert Attributes <alert_attributes>` for a full list of valid inputs.

Example
+++++++

::

    {
      "resource": "web01",
      "event": "HttpServerError",
      "environment": "Production",
      "severity": "major",
      "status": "open",
      "correlate": [
        "HttpServerError",
        "HttpServerOK"
      ],
      "service": [
        "example.com"
      ],
      "group": "Web",
      "value": "Bad Gateway (501)",
      "text": "The site is down.",
      "tags": [
        "london"
      ],
      "attributes": {
        "company": "ACME Corp"
      },
      "origin": "curl",
      "type": "webAlert"
    }


Response
++++++++

::

    201 CREATED

::

    {
      "status": "ok",
      "id": "f26b3695-0e67-402f-81be-ba966bcb9603",
      "alert": {
        "origin": "curl",
        "text": "The site is down.",
        "lastReceiveTime": "2015-03-01T23:34:30.635Z",
        "receiveTime": "2015-03-01T23:34:28.118Z",
        "trendIndication": "moreSevere",
        "href": "http://api.alerta.io/alert/f26b3695-0e67-402f-81be-ba966bcb9603",
        "rawData": "",
        "previousSeverity": "unknown",
        "event": "HttpServerError",
        "group": "Web",
        "severity": "major",
        "service": [
          "example.com"
        ],
        "id": "f26b3695-0e67-402f-81be-ba966bcb9603",
        "environment": "Production",
        "type": "webAlert",
        "status": "open",
        "repeat": true,
        "tags": [
          "london"
        ],
        "createTime": "2015-03-01T23:34:27.467Z",
        "lastReceiveId": "1637de1f-eac5-48dd-a4dd-8a10e4c89843",
        "resource": "web01",
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
        "history": []
      }
    }

.. _get_alert_id:

Get an alert
~~~~~~~~~~~~

::

  GET /alert/:id

Response
++++++++

::

    {
      "status": "ok",
      "total": 1,
      "alert": {
        "origin": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "text": "",
        "lastReceiveTime": "2015-01-30T23:00:13.985Z",
        "receiveTime": "2015-01-30T23:00:13.985Z",
        "trendIndication": "moreSevere",
        "href": "http://api.alerta.io/alert/8a90ae96-3a9c-422a-8d17-292106266c75",
        "rawData": "",
        "previousSeverity": "unknown",
        "event": "HttpError",
        "group": "Web",
        "severity": "minor",
        "service": [
          "Website"
        ],
        "id": "8a90ae96-3a9c-422a-8d17-292106266c75",
        "environment": "Production",
        "type": "browserAlert",
        "status": "open",
        "repeat": false,
        "tags": [
          "watch:Nick Satterly"
        ],
        "createTime": "2015-01-30T23:00:13.978Z",
        "lastReceiveId": "8a90ae96-3a9c-422a-8d17-292106266c75",
        "resource": "web01",
        "duplicateCount": 0,
        "correlate": [],
        "value": "n/a",
        "timeout": 86400,
        "attributes": {
          "ip": "127.2.52.129"
        },
        "history": [
          {
            "updateTime": "2015-01-30T23:00:13.978Z",
            "severity": "minor",
            "text": "",
            "value": "n/a",
            "event": "HttpError",
            "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
          },
          {
            "status": "closed",
            "text": "status change via console",
            "updateTime": "2015-02-17T14:51:30.609Z",
            "event": "HttpError",
            "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
          },
          {
            "status": "open",
            "text": "status change via console",
            "updateTime": "2015-02-17T14:51:33.169Z",
            "event": "HttpError",
            "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
          }
        ]
      }
    }

Set alert status
~~~~~~~~~~~~~~~~

::

  POST /alert/:id/status

Input
+++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``status``    | string      | **Required** New status from ``open``, ``ack``, ``closed`` |
+---------------+-------------+------------------------------------------------------------+
| ``text``      | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

    {
      "status": "ack",
      "text": "disk needs replacing"
    }

Response
++++++++

::

    200 OK

::

    {
      "status": "ok"
    }

Tag and untag alerts
~~~~~~~~~~~~~~~~~~~~

Tags are a set, not a list, which means that tagging an alert with the same tag does nothing tags can be removed.

::

  POST /alert/:id/tag
  POST /alert/:id/untag

Input
+++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``tags``      | list        |                                                            |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

    {
      "tags": [
        "foo",
        "bar",
        "baz"
      ]
    }

Delete an alert
~~~~~~~~~~~~~~~

::

  DELETE /alert/:id

Response
++++++++

::

    200 OK

::

    {
      "status": "ok"
    }

.. _get_alerts:

Search alerts
~~~~~~~~~~~~~

::

  GET /alerts

Parameters
++++++++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``<attr>``    | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``q``         | mongo query |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``from-date`` | date        |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``to-date``   | date        |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``sort-by``   | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``reverse``   | boolean     |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``group-by``  | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``page``      | integer     |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``limit``     | integer     |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``api-key``   | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+

The ``attr`` parameter is any alert attribute.

Any alert attribute can be queried. To query tags do this, to query attributes key/value do this.

Default is not to use exact match. To use regex ``=~`` and to negate use ``!=``.

Example
+++++++

::

  http://api.alerta.io/alerts?status=open&severity=critical&severity=major&environment=Production&service=Network

Response
++++++++

::


    {
      "status": "ok",
      "total": 2,
      "pageSize": 1,
      "statusCounts": {
        "open": 2
      },
      "alerts": [
        {
          "origin": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
          "text": "",
          "lastReceiveTime": "2015-01-30T23:00:13.985Z",
          "receiveTime": "2015-01-30T23:00:13.985Z",
          "trendIndication": "moreSevere",
          "href": "http://api.alerta.io/alert/8a90ae96-3a9c-422a-8d17-292106266c75",
          "rawData": "",
          "previousSeverity": "unknown",
          "event": "HttpError",
          "group": "Web",
          "severity": "minor",
          "service": [
            "Website"
          ],
          "id": "8a90ae96-3a9c-422a-8d17-292106266c75",
          "environment": "Production",
          "type": "browserAlert",
          "status": "open",
          "repeat": false,
          "tags": [],
          "createTime": "2015-01-30T23:00:13.978Z",
          "lastReceiveId": "8a90ae96-3a9c-422a-8d17-292106266c75",
          "resource": "web01",
          "duplicateCount": 0,
          "correlate": [],
          "value": "n/a",
          "timeout": 86400,
          "attributes": {
            "ip": "127.2.52.129"
          },
          "history": [
            {
              "updateTime": "2015-01-30T23:00:13.978Z",
              "severity": "minor",
              "text": "",
              "value": "n/a",
              "event": "HttpError",
              "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
            },
            {
              "status": "closed",
              "text": "status change via console",
              "updateTime": "2015-02-17T14:51:30.609Z",
              "event": "HttpError",
              "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
            },
            {
              "status": "open",
              "text": "status change via console",
              "updateTime": "2015-02-17T14:51:33.169Z",
              "event": "HttpError",
              "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
            }
          ]
        }
      ],
      "page": 1,
      "more": true,
      "severityCounts": {
        "minor": 2
      },
      "lastTime": "2015-01-30T23:00:13.985Z",
      "pages": 2,
      "autoRefresh": true
    }

.. _get_alerts_history:

Get history of alerts
~~~~~~~~~~~~~~~~~~~~~

::

  GET /alerts/history

Parameters
++++++++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``<attr>``    | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+


Example
+++++++

::

  http://api.alerta.io/alerts/history?resource=router0011

Response
++++++++

::

    {
      "status": "ok",
      "lastTime": "2014-12-15T09:55:31.344Z",
      "history": [
        {
          "origin": "mod_wsgi/ex-std-node439.prod.rhcloud.com",
          "updateTime": "2014-12-15T09:55:31.341Z",
          "tags": [
            "location=London",
            "region=EU"
          ],
          "text": "Router is up.",
          "href": "http://api.alerta.io/alert/53482b80-ca57-43da-ab73-8e0a8456c531",
          "group": "Network",
          "id": "53482b80-ca57-43da-ab73-8e0a8456c531",
          "resource": "router0011",
          "severity": "normal",
          "service": [
            "Shared"
          ],
          "value": "UP",
          "event": "node_up",
          "environment": "Production",
          "attributes": {},
          "type": "exceptionAlert"
        },
        {
          "status": "closed",
          "origin": "mod_wsgi/ex-std-node439.prod.rhcloud.com",
          "updateTime": "2014-12-15T09:55:31.344Z",
          "tags": [
            "location=London",
            "region=EU"
          ],
          "text": "new alert status change",
          "href": "http://api.alerta.io/alert/53482b80-ca57-43da-ab73-8e0a8456c531",
          "group": "Network",
          "id": "53482b80-ca57-43da-ab73-8e0a8456c531",
          "resource": "router0011",
          "service": [
            "Shared"
          ],
          "event": "node_up",
          "environment": "Production",
          "attributes": {},
          "type": "exceptionAlert"
        }
      ]
    }

Get severity and status counts for alerts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /alerts/count

Parameters
++++++++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``<attr>``    | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

  http://api.alerta.io/alerts/count?status=open&status=ack

Response
++++++++

::

    {
      "status": "ok",
      "total": 12,
      "statusCounts": {
        "ack": 2,
        "open": 10
      },
      "severityCounts": {
        "major": 1,
        "warning": 3,
        "critical": 2,
        "minor": 5,
        "normal": 1
      }
    }

Top 10 alerts by resource
~~~~~~~~~~~~~~~~~~~~~~~~~

The top 10 resources are grouped by ``event`` by default but this can be any valid attribute.
::

  GET /alerts/top10

Parameters
++++++++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``group-by``  | string      | Any valid alert attribute. Default: ``event``              |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

  http://api.alerta.io/alerts/top10?group-by=group

Response
++++++++

::

    {
      "status": "ok",
      "total": 10,
      "top10": [
        {
          "count": 7,
          "group": "Misc",
          "duplicateCount": 0,
          "environments": [
            "Development",
            "Production"
          ],
          "services": [
            "sdff",
            "web",
            "Web",
            "test",
            "aaa",
            "Svc"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/f5b7cbc2-ae92-4e0c-acd3-01d4ec466785",
              "resource": "web",
              "id": "f5b7cbc2-ae92-4e0c-acd3-01d4ec466785"
            },
            {
              "href": "http://api.alerta.io/alert/5c92228f-c511-4d5b-9c81-dc98d3fd67e6",
              "resource": "xv",
              "id": "5c92228f-c511-4d5b-9c81-dc98d3fd67e6"
            },
            {
              "href": "http://api.alerta.io/alert/7e18e2ca-40d3-4c0d-8b90-067b67f82eee",
              "resource": "res1",
              "id": "7e18e2ca-40d3-4c0d-8b90-067b67f82eee"
            },
            {
              "href": "http://api.alerta.io/alert/d6f5bcce-6442-4471-a869-b8c017b74b2b",
              "resource": "web01",
              "id": "d6f5bcce-6442-4471-a869-b8c017b74b2b"
            },
            {
              "href": "http://api.alerta.io/alert/710cc471-569b-4558-8f00-714f4f91bfaf",
              "resource": "res1",
              "id": "710cc471-569b-4558-8f00-714f4f91bfaf"
            },
            {
              "href": "http://api.alerta.io/alert/8fbd3de5-4ed4-4a75-b208-87bed86a7bed",
              "resource": "asdf",
              "id": "8fbd3de5-4ed4-4a75-b208-87bed86a7bed"
            },
            {
              "href": "http://api.alerta.io/alert/d71bb399-2241-4c53-8dd7-3c541699c86a",
              "resource": "sdf",
              "id": "d71bb399-2241-4c53-8dd7-3c541699c86a"
            }
          ]
        },
        {
          "count": 5,
          "group": "Web",
          "duplicateCount": 11,
          "environments": [
            "Production"
          ],
          "services": [
            "example.com",
            "API",
            "Website",
            "Mobile"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/f26b3695-0e67-402f-81be-ba966bcb9603",
              "resource": "web01",
              "id": "f26b3695-0e67-402f-81be-ba966bcb9603"
            },
            {
              "href": "http://api.alerta.io/alert/75e28e73-a76b-4850-8fdb-87fe67d05b1c",
              "resource": "web02",
              "id": "75e28e73-a76b-4850-8fdb-87fe67d05b1c"
            },
            {
              "href": "http://api.alerta.io/alert/8a90ae96-3a9c-422a-8d17-292106266c75",
              "resource": "web01",
              "id": "8a90ae96-3a9c-422a-8d17-292106266c75"
            },
            {
              "href": "http://api.alerta.io/alert/28681862-af94-4a02-8024-d7a20dd59696",
              "resource": "web01:www-http",
              "id": "28681862-af94-4a02-8024-d7a20dd59696"
            }
          ]
        },
        {
          "count": 3,
          "group": "OS",
          "duplicateCount": 10,
          "environments": [
            "Production"
          ],
          "services": [
            "Platform",
            "Mobile"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/c0a7bbdb-0ab2-4f5b-aa9a-bd7f770ef77f",
              "resource": "host44",
              "id": "c0a7bbdb-0ab2-4f5b-aa9a-bd7f770ef77f"
            },
            {
              "href": "http://api.alerta.io/alert/44106634-6662-491a-9915-6d5e27b5fab7",
              "resource": "i-9d7303dd:/dev/xvdb",
              "id": "44106634-6662-491a-9915-6d5e27b5fab7"
            }
          ]
        },
        {
          "count": 2,
          "group": "Cisco",
          "duplicateCount": 9,
          "environments": [
            "Production"
          ],
          "services": [
            "Network"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/627fc0e3-38a4-46d7-8064-7a00161c77d6",
              "resource": "C-AJPTYO01-VG01-L-3845",
              "id": "627fc0e3-38a4-46d7-8064-7a00161c77d6"
            },
            {
              "href": "http://api.alerta.io/alert/5af0e69f-620c-49b1-9694-d1c2f3e23fbe",
              "resource": "G-NNYBUF01-WR01-H-7206",
              "id": "5af0e69f-620c-49b1-9694-d1c2f3e23fbe"
            }
          ]
        },
        {
          "count": 1,
          "group": "NetApp",
          "duplicateCount": 5,
          "environments": [
            "Production"
          ],
          "services": [
            "Storage"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/8124c797-9843-45c2-9f3b-a6ab610a335c",
              "resource": "netapp51",
              "id": "8124c797-9843-45c2-9f3b-a6ab610a335c"
            }
          ]
        },
        {
          "count": 1,
          "group": "CloudWatch",
          "duplicateCount": 2,
          "environments": [
            "Production"
          ],
          "services": [
            "496780030265"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/8e3b6042-ac6e-453a-b118-afa52067fc18",
              "resource": "InstanceId:i-0c678beb",
              "id": "8e3b6042-ac6e-453a-b118-afa52067fc18"
            }
          ]
        },
        {
          "count": 1,
          "group": "web",
          "duplicateCount": 0,
          "environments": [
            "Development"
          ],
          "services": [
            "web"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/72e6d62d-1d15-4899-a6a5-f511f2fb7e7f",
              "resource": "wb01",
              "id": "72e6d62d-1d15-4899-a6a5-f511f2fb7e7f"
            }
          ]
        },
        {
          "count": 1,
          "group": "Hardware",
          "duplicateCount": 0,
          "environments": [
            "Production"
          ],
          "services": [
            "Network"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/36b4a748-1067-4fbd-a1b5-45658118bd9b",
              "resource": "host678:eth0",
              "id": "36b4a748-1067-4fbd-a1b5-45658118bd9b"
            }
          ]
        },
        {
          "count": 1,
          "group": "Network",
          "duplicateCount": 0,
          "environments": [
            "Production"
          ],
          "services": [
            "Shared"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/53482b80-ca57-43da-ab73-8e0a8456c531",
              "resource": "router0011",
              "id": "53482b80-ca57-43da-ab73-8e0a8456c531"
            }
          ]
        },
        {
          "count": 1,
          "group": "Oracle",
          "duplicateCount": 0,
          "environments": [
            "Development"
          ],
          "services": [
            "Database"
          ],
          "resources": [
            {
              "href": "http://api.alerta.io/alert/5f49bd9a-e612-4489-a540-e1992c6b98c4",
              "resource": "mydb",
              "id": "5f49bd9a-e612-4489-a540-e1992c6b98c4"
            }
          ]
        }
      ]
    }

.. _environments:

Environments
------------

An environment cannot be created -- it is a dynamically derived resource based on existing alerts.

List of all environments
~~~~~~~~~~~~~~~~~~~~~~~~

List all environments and alert count for each.

::

  GET /environments

Parameters
++++++++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``<attr>``    | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

  http://api.alerta.io/environments

Response
++++++++

::

    {
      "status": "ok",
      "total": 2,
      "environments": [
        {
          "environment": "Development",
          "count": 5
        },
        {
          "environment": "Production",
          "count": 18
        }
      ]
    }

.. _services:

Services
--------

A service cannot be created -- it is a dynamically derived resource based on existing alerts.

List of all services
~~~~~~~~~~~~~~~~~~~~

List all services by environment and count of alerts for each.

::

  GET /services

Parameters
++++++++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``<attr>``    | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

  http://api.alerta.io/services?environment=Production

Response
++++++++

::

    {
      "status": "ok",
      "services": [
        {
          "environment": "Production",
          "count": 1,
          "service": "API"
        },
        {
          "environment": "Production",
          "count": 2,
          "service": "Mobile"
        },
        {
          "environment": "Production",
          "count": 2,
          "service": "Website"
        }
      ],
      "total": 3
    }

.. _heartbeats:

Heartbeats
----------

Send a heartbeat
~~~~~~~~~~~~~~~~

Update a heartbeat or create a new one if it doesn't already exist for the heartbeat ``origin``.

::

  POST /heartbeat

Input
+++++

+---------------+-------------+------------------------------------------------------------+
| Name          | Type        | Description                                                |
+===============+=============+============================================================+
| ``origin``    | string      |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``tags``      | list        |                                                            |
+---------------+-------------+------------------------------------------------------------+
| ``timeout``   | integer     |                                                            |
+---------------+-------------+------------------------------------------------------------+

Example
+++++++

::

    {
        "origin": "foo",
        "tags": [
            "bar"
        ],
        "createTime": "2015-03-02T01:48:42.106Z",
        "timeout": 300,
        "type": "Heartbeat",
        "id": "aa4d7327-0139-49d4-bf68-6deb003c85d5"
    }

Response
++++++++

::

  201 CREATED

::

    {
      "status": "ok",
      "heartbeat": {
        "origin": "foo",
        "tags": [],
        "createTime": "2015-03-02T01:52:12.116Z",
        "href": "http://api.alerta.io/heartbeat/b703f112-b5ab-4ca6-baa6-c317fb875814",
        "timeout": 300,
        "receiveTime": "2015-03-02T01:52:12.116Z",
        "type": "Heartbeat",
        "id": "b703f112-b5ab-4ca6-baa6-c317fb875814"
      },
      "id": "b703f112-b5ab-4ca6-baa6-c317fb875814"
    }

Get a heartbeat
~~~~~~~~~~~~~~~

::

  GET /heartbeat/:id

Response
++++++++

::

    {
      "status": "ok",
      "heartbeat": {
        "origin": "foo",
        "tags": [],
        "createTime": "2015-03-02T01:52:12.116Z",
        "href": "http://api.alerta.io/heartbeat/b703f112-b5ab-4ca6-baa6-c317fb875814",
        "timeout": 300,
        "receiveTime": "2015-03-02T01:52:12.116Z",
        "type": "Heartbeat",
        "id": "b703f112-b5ab-4ca6-baa6-c317fb875814"
      },
      "total": 1
    }

List all heartbeats
~~~~~~~~~~~~~~~~~~~

::

  GET /heartbeats

Response
++++++++

::

    {
      "status": "ok",
      "heartbeats": [
        {
          "origin": "alerta/vagrant-debian-wheezy64",
          "tags": [],
          "createTime": "2015-02-06T22:44:08.719Z",
          "href": "http://api.alerta.io/heartbeat/1f50a075-b5a2-4a94-918b-e1eab401a817",
          "timeout": 86400,
          "receiveTime": "2015-02-06T23:02:19.553Z",
          "type": "Heartbeat",
          "id": "1f50a075-b5a2-4a94-918b-e1eab401a817"
        },
        {
          "origin": "foo",
          "tags": [],
          "createTime": "2015-03-02T01:52:12.116Z",
          "href": "http://api.alerta.io/heartbeat/b703f112-b5ab-4ca6-baa6-c317fb875814",
          "timeout": 300,
          "receiveTime": "2015-03-02T01:52:12.116Z",
          "type": "Heartbeat",
          "id": "b703f112-b5ab-4ca6-baa6-c317fb875814"
        }
      ],
      "total": 2,
      "time": "2015-03-02T01:58:10.357Z"
    }

Delete a heartbeat
~~~~~~~~~~~~~~~~~~

::

  DELETE /heartbeat/:id

Response
++++++++

::

    200 OK

::

    {
      "status": "ok"
    }
