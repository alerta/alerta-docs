API Overview
============

REST API   http://api.alerta.io
resources: alerts, heartbeats, keys, users
alert and heartbeat JSON formats
methods, attributes and responses
JSONP, CORS, Caching “Last-Modified” (wip)


alerts - CRUD, query, services, environments
heartbeats - CRUD
auth - google oauth, github oauth, api keys, specified users

Version
-------


Base URL
--------

Get list of all endpoints...

$ curl https://api.alerta.io

-> Alerts
-> Heartbeats
-> ...

Authentication
--------------

Google OAuth2



API Keys
--------

Create your own key when logged in.


Instance References
----------

"href" attributes.

POST Response
-------------

The body of a resource is returned in the response body so that it can be used immediately. For example, from that you can know the alert id, whether it is a duplicate or not, whether the severity has increased or decreased, etc.

Deleting
--------

DELETE or _method=DELETE


Dates & Times
-------------

All dates and times are in ISO8601 format.

YYYY-MM-DDTHH-mm-ss.fffZ

Camel Case
----------

Standard attributes are camel case. If user-defined attributes are also camel case then auto formating will occur in the alert web UI. eg. "myCamelCaseKey" -> My Camel Case Key

JSONP
-----

callback=

Caching
-------

Not supported.


.. _status_codes:

HTTP Status Codes
-----------------

+------------------+---------------------------------------------------------------------+
| Code             | Description                                                         |
+==================+=====================================================================+
| 200 OK           | No error.                                                           |
+------------------+---------------------------------------------------------------------+
| 201 Created      | Resource created successfully.                                      |
+------------------+---------------------------------------------------------------------+
| 400 Bad Request  | Mandatory parameter or data missing.                                |
+------------------+---------------------------------------------------------------------+
| 401 Unauthorized | Authorization required.                                             |
+------------------+---------------------------------------------------------------------+
| 403 Forbidden    | Pre-receive hook rejected request or authorization failed.          |
+------------------+---------------------------------------------------------------------+
| 404 Not Found    | Resource (such as alert or heartbeat) not found.                    |
+------------------+---------------------------------------------------------------------+
| 500 Server Error | Internal error. Default code used for all unexpected server errors. |
+------------------+---------------------------------------------------------------------+



Embedding
---------

See oEmbed

Explorer
--------

http://explorer.alerta.io


Libraries
---------

Python

python-alerta



