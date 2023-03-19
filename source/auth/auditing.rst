.. _audit log:

Audit Log
=========

An audit trail can be enabled to keep track of changes to Alerta.

Every audit event will have an audit ``id``, ``@timestamp``, ``event``,
``category``, ``message``, ``user``, ``resource``, ``request`` and
``extra`` elements. The ``extra`` element may include relevant data
depending on the type of event.

**Example Audit Event**

.. code:: json

    {
      "id": "c87210da-3cfb-4cbd-b8ec-4fe9ed39aeef",
      "@timestamp": "2018-11-10T21:36:23.946Z",
      "event": "apikey-deleted",
      "category": "admin",
      "message": "",
      "user": {
        "id": "satterly",
        "customers": [],
        "scopes": [
          "admin",
          "read",
          "write"
        ]
      },
      "resource": {
        "id": "dc0b5a62-015b-4ba3-965e-012ca2e4db9b",
        "type": "apikey"
      },
      "request": {
        "endpoint": "api.delete_key",
        "method": "DELETE",
        "url": "http://localhost:8080/key/dc0b5a62-015b-4ba3-965e-012ca2e4db9b",
        "args": {},
        "data": "",
        "ipAddress": "127.0.0.1"
      },
      "extra": {}
    }

Audit events can be logged locally to the standard application log
(which could also help with general debugging) or forwarded to a
HTTP endpoint using a POST.

**Example Loggly configuration**

The following example configuration can be used to log all ``admin``,
``write`` and ``auth`` requests to the Flask application log file and
forward the events to the Loggly_ "logging-as-a-service" endpoint,
replacing ``TOKEN`` in the Loggly URL with your customer token.

.. _Loggly: https://www.loggly.com/docs/http-endpoint/

.. code:: python

    AUDIT_TRAIL = ['admin', 'write', 'auth']
    AUDIT_LOG = True  # log to Flask application logger
    AUDIT_URL='http://logs-01.loggly.com/inputs/TOKEN/tag/http/'

.. image:: ../_static/images/loggly-screen-shot-2.png
