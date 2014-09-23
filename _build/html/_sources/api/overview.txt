Overview
========

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


Embedding
---------

widgets

Explorer
--------

http://explorer.alerta.io


Libraries
---------

Python

python-alerta

Ruby

ruby-gem-alerta


