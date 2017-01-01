.. _api:

API Reference
=============

.. contents:: Resource Types
   :local:
   :depth: 2

.. _alerts:

Alerts
------

.. _post_alert:

Create an alert
~~~~~~~~~~~~~~~

Creates a new alert, or updates an existing alert if the ``environment``-
``resource``-``event`` combination already exists.

::

    POST /alert

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``resource``    | string   | **Required** resource under alarm            |
+-----------------+----------+----------------------------------------------+
| ``event``       | string   | **Required** event name                      |
+-----------------+----------+----------------------------------------------+
| ``environment`` | string   | environment, used to namespace the resource  |
+-----------------+----------+----------------------------------------------+
| ``severity``    | string   | see :ref:`severity_table` table              |
+-----------------+----------+----------------------------------------------+
| ``correlate``   | list     | list of related event names                  |
+-----------------+----------+----------------------------------------------+
| ``status``      | string   | see :ref:`status_table` table                |
+-----------------+----------+----------------------------------------------+
| ``service``     | list     | list of effected services                    |
+-----------------+----------+----------------------------------------------+
| ``group``       | string   | used to group events of similar type         |
+-----------------+----------+----------------------------------------------+
| ``value``       | string   | event value                                  |
+-----------------+----------+----------------------------------------------+
| ``text``        | string   | freeform text description                    |
+-----------------+----------+----------------------------------------------+
| ``tags``        | set      | set of tags                                  |
+-----------------+----------+----------------------------------------------+
| ``attributes``  | dict     | dictionary of key-value pairs                |
+-----------------+----------+----------------------------------------------+
| ``origin``      | string   | monitoring component that generated the alert|
+-----------------+----------+----------------------------------------------+
| ``type``        | string   | event type                                   |
+-----------------+----------+----------------------------------------------+
| ``createTime``  | datetime | time alert was generated at the origin       |
+-----------------+----------+----------------------------------------------+
| ``timeout``     | integer  | seconds before alert is considered stale     |
+-----------------+----------+----------------------------------------------+
| ``rawData``     | string   | unprocessed raw data                         |
+-----------------+----------+----------------------------------------------+

.. note:: Only ``resource`` and ``event`` are mandatory. The ``status`` can be
          dynamically assigned by the Alerta API based on the ``severity``.

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "attributes": {
            "region": "EU"
          },
          "correlate": [
            "HttpServerError",
            "HttpServerOK"
          ],
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "origin": "curl",
          "resource": "web01",
          "service": [
            "example.com"
          ],
          "severity": "major",
          "tags": [
            "dc1"
          ],
          "text": "Site is down.",
          "type": "exceptionAlert",
          "value": "Bad Gateway (501)"
        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    {
      "alert": {
        "attributes": {
          "ip": "127.0.0.1",
          "region": "EU"
        },
        "correlate": [
          "HttpServerError",
          "HttpServerOK"
        ],
        "createTime": "2017-01-01T11:31:57.716Z",
        "customer": null,
        "duplicateCount": 0,
        "environment": "Production",
        "event": "HttpServerError",
        "group": "Web",
        "history": [],
        "href": "http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe",
        "id": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
        "lastReceiveId": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
        "lastReceiveTime": "2017-01-01T11:31:57.718Z",
        "origin": "curl",
        "previousSeverity": "indeterminate",
        "rawData": "",
        "receiveTime": "2017-01-01T11:31:57.718Z",
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
      },
      "id": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
      "status": "ok"
    }

.. _get_alert_id:

Retrieve an alert
~~~~~~~~~~~~~~~~~

Retrieves an alert with the given alert ID.

::

    GET /alert/:id

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "alert": {
        "attributes": {
          "ip": "127.0.0.1",
          "region": "EU"
        },
        "correlate": [
          "HttpServerError",
          "HttpServerOK"
        ],
        "createTime": "2017-01-01T11:31:57.716Z",
        "customer": null,
        "duplicateCount": 0,
        "environment": "Production",
        "event": "HttpServerError",
        "group": "Web",
        "history": [
          {
            "event": "HttpServerError",
            "id": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
            "severity": "major",
            "text": "Site is down.",
            "type": "severity",
            "updateTime": "2017-01-01T11:31:57.716Z",
            "value": "Bad Gateway (501)"
          },
          {
            "event": "HttpServerError",
            "id": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
            "status": "open",
            "text": "new alert status change",
            "type": "status",
            "updateTime": "2017-01-01T11:31:57.718Z"
          }
        ],
        "href": "http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe",
        "id": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
        "lastReceiveId": "1711c57e-5c6a-4c39-881b-9d8d174feafe",
        "lastReceiveTime": "2017-01-01T11:31:57.718Z",
        "origin": "curl",
        "previousSeverity": "indeterminate",
        "rawData": "",
        "receiveTime": "2017-01-01T11:31:57.718Z",
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
      },
      "status": "ok",
      "total": 1
    }

Set alert status
~~~~~~~~~~~~~~~~

Sets the status of an alert, and logs the status change to the alert history.

::

    POST /alert/:id/status

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``status``      | string   | **Required** New status from ``open``,       |
|                 |          | ``assign``, ``ack``, ``closed``, ``expired`` |
+-----------------+----------+----------------------------------------------+
| ``text``        | string   | reason for status change                     |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe/status \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "status": "ack",
          "text": "disk needs replacing."
        }'

Tag and untag alerts
~~~~~~~~~~~~~~~~~~~~

Adds or removes tag values from the set of tags for an alert.

::

    POST /alert/:id/tag
    POST /alert/:id/untag

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``tags``        | set      | tags to add or remove                        |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe/tag \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "tags": [
            "linux",
            "linux2.6",
            "dell"
          ]
        }'

Update alert attributes
~~~~~~~~~~~~~~~~~~~~~~~

Adds, deletes or modifies alert attributes. To delete an attribute assign
"null" to the attribute.

::

    PUT /alert/:id/attributes

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``attributes``  | dict     | dictionary of key-value attributes           |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPUT http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe/attributes \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "attributes": {
            "incidentKey": "1234abcd",
            "ip": "10.1.1.1",
            "region": null
          }
        }'


Delete an alert
~~~~~~~~~~~~~~~

Permanently deletes an alert. It cannot be undone.

::

    DELETE /alert/:id

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XDELETE http://localhost:8080/alert/1711c57e-5c6a-4c39-881b-9d8d174feafe \
    -H 'Authorization: Key demo-key'

.. _get_alerts:

Search alerts
~~~~~~~~~~~~~

Searches for alerts using alert attributes or a mongo-type query parameter to
filter results.

::

    GET /alerts

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``<attr>``      | string   | any attribute. eg. ``status=open``           |
+-----------------+----------+----------------------------------------------+
| ``q``           | json     | mongo query see `Mongo Query Operators`_     |
+-----------------+----------+----------------------------------------------+
| ``fields``      | list     | show or hide alert attributes                |
+-----------------+----------+----------------------------------------------+
| ``from-date``   | date     |                                              |
+-----------------+----------+----------------------------------------------+
| ``to-date``     | date     |                                              |
+-----------------+----------+----------------------------------------------+
| ``sort-by``     | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``reverse``     | boolean  |                                              |
+-----------------+----------+----------------------------------------------+
| ``group-by``    | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``page``        | integer  |                                              |
+-----------------+----------+----------------------------------------------+
| ``limit``       | integer  |                                              |
+-----------------+----------+----------------------------------------------+

.. _Mongo Query Operators: http://docs.mongodb.org/manual/reference/operator/query/

The ``attr`` parameter is any alert attribute.

Any alert attribute can be queried. To query tags do this, to query attributes key/value do this.

Default is not to use exact match. To use regex ``=~`` and to negate use ``!=``.

**If customer views enabled then the customer for that user will be applied as a filter.**

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/alerts?group=Web \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "alerts": [
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "US"
          },
          "correlate": [
            "HttpServerError",
            "HttpServerOK"
          ],
          "createTime": "2017-01-01T12:01:21.048Z",
          "customer": null,
          "duplicateCount": 0,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "history": [
            {
              "event": "HttpServerError",
              "id": "0099bae5-9683-48a1-a49d-f566fe143770",
              "severity": "critical",
              "text": "Site is down.",
              "type": "severity",
              "updateTime": "2017-01-01T12:01:21.048Z",
              "value": "Internal Server Error (500)"
            },
            {
              "event": "HttpServerError",
              "id": "0099bae5-9683-48a1-a49d-f566fe143770",
              "status": "open",
              "text": "new alert status change",
              "type": "status",
              "updateTime": "2017-01-01T12:01:21.050Z"
            }
          ],
          "href": "http://localhost:8080/alert/0099bae5-9683-48a1-a49d-f566fe143770",
          "id": "0099bae5-9683-48a1-a49d-f566fe143770",
          "lastReceiveId": "0099bae5-9683-48a1-a49d-f566fe143770",
          "lastReceiveTime": "2017-01-01T12:01:21.050Z",
          "origin": "curl",
          "previousSeverity": "indeterminate",
          "rawData": "",
          "receiveTime": "2017-01-01T12:01:21.050Z",
          "repeat": false,
          "resource": "web02",
          "service": [
            "example.com"
          ],
          "severity": "critical",
          "status": "open",
          "tags": [
            "dc2"
          ],
          "text": "Site is down.",
          "timeout": 86400,
          "trendIndication": "moreSevere",
          "type": "exceptionAlert",
          "value": "Internal Server Error (500)"
        },
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "EU"
          },
          "correlate": [
            "HttpServerError",
            "HttpServerOK"
          ],
          "createTime": "2017-01-01T12:00:01.662Z",
          "customer": null,
          "duplicateCount": 0,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "history": [
            {
              "event": "HttpServerError",
              "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
              "severity": "major",
              "text": "Site is down.",
              "type": "severity",
              "updateTime": "2017-01-01T12:00:01.662Z",
              "value": "Bad Gateway (501)"
            },
            {
              "event": "HttpServerError",
              "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
              "status": "open",
              "text": "new alert status change",
              "type": "status",
              "updateTime": "2017-01-01T12:00:01.664Z"
            }
          ],
          "href": "http://localhost:8080/alert/e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "lastReceiveId": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "lastReceiveTime": "2017-01-01T12:00:01.664Z",
          "origin": "curl",
          "previousSeverity": "indeterminate",
          "rawData": "",
          "receiveTime": "2017-01-01T12:00:01.664Z",
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
      ],
      "autoRefresh": true,
      "lastTime": "2017-01-01T12:01:21.050Z",
      "more": false,
      "page": 1,
      "pageSize": 10000,
      "pages": 1,
      "severityCounts": {
        "critical": 1,
        "major": 1
      },
      "status": "ok",
      "statusCounts": {
        "open": 2
      },
      "total": 2
    }

.. _get_alerts_history:

List all alert history
~~~~~~~~~~~~~~~~~~~~~~

Returns a list of alert severity and status changes.

::

    GET /alerts/history

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``<attr>``      | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/alerts/history?service=example.com \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "history": [
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "EU"
          },
          "customer": null,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "href": "http://localhost:8080/alert/e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "origin": "curl",
          "resource": "web01",
          "service": [
            "example.com"
          ],
          "severity": "major",
          "tags": [
            "dc1"
          ],
          "text": "Site is down.",
          "type": "severity",
          "updateTime": "2017-01-01T12:00:01.662Z",
          "value": "Bad Gateway (501)"
        },
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "EU"
          },
          "customer": null,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "href": "http://localhost:8080/alert/e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "origin": "curl",
          "resource": "web01",
          "service": [
            "example.com"
          ],
          "status": "open",
          "tags": [
            "dc1"
          ],
          "text": "new alert status change",
          "type": "status",
          "updateTime": "2017-01-01T12:00:01.664Z"
        },
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "US"
          },
          "customer": null,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "href": "http://localhost:8080/alert/0099bae5-9683-48a1-a49d-f566fe143770",
          "id": "0099bae5-9683-48a1-a49d-f566fe143770",
          "origin": "curl",
          "resource": "web02",
          "service": [
            "example.com"
          ],
          "severity": "critical",
          "tags": [
            "dc2"
          ],
          "text": "Site is down.",
          "type": "severity",
          "updateTime": "2017-01-01T12:01:21.048Z",
          "value": "Internal Server Error (500)"
        },
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "US"
          },
          "customer": null,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "href": "http://localhost:8080/alert/0099bae5-9683-48a1-a49d-f566fe143770",
          "id": "0099bae5-9683-48a1-a49d-f566fe143770",
          "origin": "curl",
          "resource": "web02",
          "service": [
            "example.com"
          ],
          "status": "open",
          "tags": [
            "dc2"
          ],
          "text": "new alert status change",
          "type": "status",
          "updateTime": "2017-01-01T12:01:21.050Z"
        },
        {
          "attributes": {
            "ip": "127.0.0.1",
            "region": "EU"
          },
          "customer": null,
          "environment": "Production",
          "event": "HttpServerError",
          "group": "Web",
          "href": "http://localhost:8080/alert/e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
          "origin": "curl",
          "resource": "web01",
          "service": [
            "example.com"
          ],
          "status": "ack",
          "tags": [
            "dc1"
          ],
          "text": "disk needs replacing.",
          "type": "status",
          "updateTime": "2017-01-01T12:07:27.455Z"
        }
      ],
      "lastTime": "2017-01-01T12:07:27.455Z",
      "status": "ok"
    }

Get severity and status counts for alerts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a count of alerts grouped by severity and status.

::

    GET /alerts/count

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``<attr>``      | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/alerts/count?environment=Production \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "severityCounts": {
        "critical": 1,
        "major": 1
      },
      "status": "ok",
      "statusCounts": {
        "ack": 1,
        "open": 1
      },
      "total": 2
    }

Top 10 alerts by resource
~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of the top 10 resources grouped by an alert attribute. By
default it is grouped by ``event`` but this can be any valid attribute.

::

    GET /alerts/top10/count
    GET /alerts/top10/flapping

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``<attr>``      | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``q``           | dict     | mongo query see `Mongo Query Operators`_     |
+-----------------+----------+----------------------------------------------+
| ``group-by``    | string   | any valid alert attribute. Default:``event`` |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/alerts/top10?group-by=group \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "status": "ok",
      "top10": [
        {
          "count": 2,
          "duplicateCount": 0,
          "environments": [
            "Production"
          ],
          "group": "Web",
          "resources": [
            {
              "href": "http://localhost:8080/alert/0099bae5-9683-48a1-a49d-f566fe143770",
              "id": "0099bae5-9683-48a1-a49d-f566fe143770",
              "resource": "web02"
            },
            {
              "href": "http://localhost:8080/alert/e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
              "id": "e9fb05a0-b65c-4faa-8868-6f06a74a2b5b",
              "resource": "web01"
            }
          ],
          "services": [
            "example.com"
          ]
        }
      ],
      "total": 1
    }

.. _environments:

Environments
------------

An environment cannot be created -- it is a dynamically derived resource based
on existing alerts.

List all environments
~~~~~~~~~~~~~~~~~~~~~

Returns a list of environments and an alert count for each.

::

    GET /environments

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``<attr>``      | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/environments \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "environments": [
        {
          "count": 2,
          "environment": "Production"
        }
      ],
      "status": "ok",
      "total": 1
    }

.. _services:

Services
--------

A service cannot be created -- it is a dynamically derived resource based on existing alerts.

List all services
~~~~~~~~~~~~~~~~~

Returns a list of services grouped by environment and an alert count for each.

::

    GET /services

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``<attr>``      | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/services?environment=Production \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "services": [
        {
          "count": 2,
          "environment": "Production",
          "service": "example.com"
        }
      ],
      "status": "ok",
      "total": 1
    }

.. _blackouts:

Blackout Periods
----------------

Create a blackout
~~~~~~~~~~~~~~~~~

Create a new blackout period for alert suppression.

::

    POST /blackout

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``environment`` | string   | **Required**                                 |
+-----------------+----------+----------------------------------------------+
| ``resource``    | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``service``     | list     |                                              |
+-----------------+----------+----------------------------------------------+
| ``event``       | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``group``       | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``tags``        | list     |                                              |
+-----------------+----------+----------------------------------------------+
| ``startTime``   | datetime | start time of blackout. Default: now         |
+-----------------+----------+----------------------------------------------+
| ``endTime``     | datetime | end time. Default: now +                     |
|                 |          | ``BLACKOUT_DURATION``                        |
+-----------------+----------+----------------------------------------------+
| ``duration``    | integer  | seconds. Default: ``BLACKOUT_DURATION``      |
|                 |          | Only used if ``endTime`` not defined         |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/blackout \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "environment": "Production",
          "service": "example.com",
          "group": "Web"
        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    {
      "blackout": {
        "duration": 3600,
        "endTime": "2017-01-01T15:35:53.695Z",
        "environment": "Production",
        "id": "77059317-bf66-44ef-a63d-b2e2aa8c0612",
        "priority": 3,
        "service": "example.com",
        "startTime": "2017-01-01T14:35:53.695Z"
      },
      "id": "77059317-bf66-44ef-a63d-b2e2aa8c0612",
      "status": "ok"
    }

List all blackouts
~~~~~~~~~~~~~~~~~~

Returns a list of blackout periods, including expired blackouts.

::

    GET /blackouts

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/blackouts \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "blackouts": [
        {
          "duration": 3600,
          "endTime": "2017-01-01T15:37:42.746Z",
          "environment": "Production",
          "id": "864fb326-3743-456f-a94b-86c304b436d4",
          "priority": 3,
          "remaining": 3561,
          "service": "example.com",
          "startTime": "2017-01-01T14:37:42.746Z",
          "status": "active"
        },
        {
          "duration": 3600,
          "endTime": "2017-01-01T15:38:16.639Z",
          "environment": "Development",
          "group": "Performance",
          "id": "7b599c38-cd05-453a-8fa9-fc29cf5edfd4",
          "priority": 5,
          "remaining": 3594,
          "startTime": "2017-01-01T14:38:16.639Z",
          "status": "active"
        }
      ],
      "status": "ok",
      "time": "2017-01-01T14:38:21.676Z",
      "total": 2
    }

Delete a blackout
~~~~~~~~~~~~~~~~~

Permanently deletes a blackout period. It cannot be undone.

::

    DELETE /blackout/:id

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XDELETE http://localhost:8080/blackout/77059317-bf66-44ef-a63d-b2e2aa8c0612 \
    -H 'Authorization: Key demo-key'

.. _heartbeats:

Heartbeats
----------

Send a heartbeat
~~~~~~~~~~~~~~~~

Creates a new heartbeat, or updates an existing heartbeat if a heartbeat
from the ``origin`` already exists.

::

    POST /heartbeat

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``origin``      | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``tags``        | list     |                                              |
+-----------------+----------+----------------------------------------------+
| ``timeout``     | integer  | Seconds.                                     |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/heartbeat \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{
          "origin": "cluster05",
          "timeout": 120,
          "tags": ["db05", "dc2"]
        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

  {
    "heartbeat": {
      "createTime": "2017-01-01T16:07:31.409Z",
      "customer": null,
      "href": "http://localhost:8080/heartbeat/221207f4-1f4b-4dc3-b754-5e67bc6241d1",
      "id": "221207f4-1f4b-4dc3-b754-5e67bc6241d1",
      "origin": "cluster05",
      "receiveTime": "2017-01-01T16:07:31.409Z",
      "tags": [
        "db05",
        "dc2"
      ],
      "timeout": 120,
      "type": "Heartbeat"
    },
    "id": "221207f4-1f4b-4dc3-b754-5e67bc6241d1",
    "status": "ok"
  }

Get a heartbeat
~~~~~~~~~~~~~~~

Retrieves a heartbeat based on the heartbeat ID.

::

    GET /heartbeat/:id

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/heartbeat/221207f4-1f4b-4dc3-b754-5e67bc6241d1 \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "heartbeat": {
        "createTime": "2017-01-01T16:07:31.409Z",
        "customer": null,
        "href": "http://localhost:8080/hearbeat/221207f4-1f4b-4dc3-b754-5e67bc6241d1",
        "id": "221207f4-1f4b-4dc3-b754-5e67bc6241d1",
        "origin": "cluster05",
        "receiveTime": "2017-01-01T16:07:31.409Z",
        "tags": [
          "db05",
          "dc2"
        ],
        "timeout": 120,
        "type": "Heartbeat"
      },
      "status": "ok",
      "total": 1
    }

List all heartbeats
~~~~~~~~~~~~~~~~~~~

Returns a list of all heartbeats.

::

  GET /heartbeats

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/heartbeats \
    -H 'Authorization: Key demo-key'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    {
      "heartbeats": [
        {
          "createTime": "2017-01-01T16:07:31.409Z",
          "customer": null,
          "href": "http://localhost:8080/heartbeat/221207f4-1f4b-4dc3-b754-5e67bc6241d1",
          "id": "221207f4-1f4b-4dc3-b754-5e67bc6241d1",
          "origin": "cluster05",
          "receiveTime": "2017-01-01T16:07:31.409Z",
          "tags": [
            "db05",
            "dc2"
          ],
          "timeout": 120,
          "type": "Heartbeat"
        },
        {
          "createTime": "2017-01-01T16:18:42.839Z",
          "customer": null,
          "href": "http://localhost:8080/heartbeat/55881e1e-ec53-4637-8f4d-05b252d385d5",
          "id": "55881e1e-ec53-4637-8f4d-05b252d385d5",
          "origin": "device03",
          "receiveTime": "2017-01-01T16:18:42.839Z",
          "tags": [
            "v2.2",
            "dc1"
          ],
          "timeout": 900,
          "type": "Heartbeat"
        }
      ],
      "status": "ok",
      "time": "2017-01-01T16:19:51.896Z",
      "total": 2
    }

Delete a heartbeat
~~~~~~~~~~~~~~~~~~

Permanently deletes a heartbeat. It cannot be undone.

::

    DELETE /heartbeat/:id

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XDELETE http://localhost:8080/heartbeat/221207f4-1f4b-4dc3-b754-5e67bc6241d1 \
    -H 'Authorization: Key demo-key'

.. _api_keys:

API Keys
--------

Create an API key
~~~~~~~~~~~~~~~~~

Creates a new API key.

::

    POST /key

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``user``        | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``text``        | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{

        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    ???

List all API keys
~~~~~~~~~~~~~~~~~

Returns a list of API keys.

::

    GET /keys

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    ???

List all API keys for a user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of all API keys for a user.

::

    GET /keys/:user

Parameters
++++++++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``user``        | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{

        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    ???

Delete an API key
~~~~~~~~~~~~~~~~~

Permanently deletes an API key. It cannot be undone.

::

    DELETE /key/:key

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json'

.. _users:

Users
-----

Create a user
~~~~~~~~~~~~~

Creates a new user.

::

    POST /user

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``name``        | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``login``       | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``provider``    | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``text``        | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{

        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    ???

Update a user
~~~~~~~~~~~~~

Updates the specified user by setting the values of the parameters passed.
Any parameters not provided will be left unchanged.

::

    PUT /user/:user

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``name``        | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``login``       | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``provider``    | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``text``        | string   |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{

        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    ???

List all users
~~~~~~~~~~~~~~

Returns a list of users.

::

    GET /users

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/users \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    ???

Delete a user
~~~~~~~~~~~~~

Permanently deletes a user. It cannot be undone.

::

    DELETE /user/:user

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XDELETE http://localhost:8080/user/bar \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json'

.. _customers:

Customers
---------

Create a customer
~~~~~~~~~~~~~~~~~

Creates a new customer lookup. Used to match user logins to customers.

::

    POST /customer

Input
+++++

+-----------------+----------+----------------------------------------------+
| Name            | Type     | Description                                  |
+=================+==========+==============================================+
| ``customer``    | string   |                                              |
+-----------------+----------+----------------------------------------------+
| ``match``       | regex    |                                              |
+-----------------+----------+----------------------------------------------+

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XPOST http://localhost:8080/alert \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json' \
    -d '{

        }'

Example Response
++++++++++++++++

::

    201 CREATED

.. code-block:: json

    ???

List all customers
~~~~~~~~~~~~~~~~~~

Returns a list of customers.

::

    GET /customers

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl http://localhost:8080/customers \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json'

Example Response
++++++++++++++++

::

    200 OK

.. code-block:: json

    ???

Delete a customer
~~~~~~~~~~~~~~~~~

Permanently delete a customer. It cannot be undone.

::

    DELETE /customer/:customer

Example Request
+++++++++++++++

.. code-block:: bash

    $ curl -XDELETE http://localhost:8080/customer/foo \
    -H 'Authorization: Key demo-key' \
    -H 'Content-type: application/json'
