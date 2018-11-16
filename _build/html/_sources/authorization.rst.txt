.. _authorization:

Authorization
=============

Authorization is used to limit access to Alerta API resources. The
authorization model is based on `Role Based Access Control`_ (RBAC)
which assigns permissions to functional roles and then users are
assigned to one or more of those roles.

.. _`Role Based Access Control`: http://csrc.nist.gov/groups/SNS/rbac/faq.html

This "role-based access" allows for fine-grained control over exactly
what resources are accessible to which users and exactly what type of
access is allowed -- in a way that is scalable.

For example, to create a new alert the sender will need to be assigned to
a role with ``write:alerts`` permissions. If the sender is not a member of
a role with those permisssions then the request will be rejected with a
``403 Forbidden`` response code.

.. note::

    All access is through roles. Permissions can not be assigned directly
    to users. The only exception to this is the ``ADMIN_USERS`` setting
    which overrides all other roles a user might belong to.

Configuration
-------------

There are two ways to configure role-based access; default and custom
configuration.

Default Authorization
+++++++++++++++++++++

If :ref:`authentication <authentication>` is enabled then the default authorization
is used which defines two roles:

* ``user`` role - everyone is a "user" unless listed in the ``ADMIN_USERS`` setting
* ``admin`` role - only admins can delete alerts and heartbeats, create users etc.

Custom Authorization
++++++++++++++++++++

To use custom authorization simply define one or more permission scope lookups.

As an "admin" user go to *Configuration -> Permissions* and add a new role
with the required scopes. See below for list of valid scopes.

Scopes and Permissions
----------------------

Use these scopes to request access to API resources.

+------------------------+--------------------------------------------------------------+
| Scope                  | Permissions                                                  |
+========================+==============================================================+
| ``read``               | Grants read-only access to all scopes.                       |
+------------------------+--------------------------------------------------------------+
| ``write``              | Grants read/write access to all scopes.                      |
+------------------------+--------------------------------------------------------------+
| ``admin``              | Grants admin, read, write and delete access to all scopes.   |
+------------------------+--------------------------------------------------------------+
| ``read:alerts``        | Read-only access to alerts.                                  |
+------------------------+--------------------------------------------------------------+
| ``write:alerts``       | Grants read/write access to alerts.                          |
+------------------------+--------------------------------------------------------------+
| ``admin:alerts``       | Grants read/write to alerts for any customer.                |
+------------------------+--------------------------------------------------------------+
| ``read:blackouts``     | Grants read-only access to blackouts.                        |
+------------------------+--------------------------------------------------------------+
| ``write:blackouts``    | Grants read/write access to blackouts.                       |
+------------------------+--------------------------------------------------------------+
| ``admin:blackouts``    | Grants read/write access to blackouts for any customer.      |
+------------------------+--------------------------------------------------------------+
| ``read:heartbeats``    | Read-only access to heartbeats.                              |
+------------------------+--------------------------------------------------------------+
| ``write:heartbeats``   | Grants read/write access to heartbeats.                      |
+------------------------+--------------------------------------------------------------+
| ``admin:heartbeats``   | Grants read/write access to heartbeats for any customer.     |
+------------------------+--------------------------------------------------------------+
| ``write:users``        | Grant write access to users.                                 |
+------------------------+--------------------------------------------------------------+
| ``admin:users``        | Fully manage users.                                          |
+------------------------+--------------------------------------------------------------+
| ``read:perms``         | Grants read-only access to permissions and scopes.           |
+------------------------+--------------------------------------------------------------+
| ``admin:perms``        | Grants read, write and delete access to permissions.         |
+------------------------+--------------------------------------------------------------+
| ``read:customers``     | Grants read-only access to customers.                        |
+------------------------+--------------------------------------------------------------+
| ``admin:customers``    | Fully manage customers.                                      |
+------------------------+--------------------------------------------------------------+
| ``read:keys``          | List and view API keys.                                      |
+------------------------+--------------------------------------------------------------+
| ``write:keys``         | Create, list and view API keys.                              |
+------------------------+--------------------------------------------------------------+
| ``admin:keys``         | Fully manage API keys for any customer.                                       |
+------------------------+--------------------------------------------------------------+
| ``write:webhooks``     | Grants write access to webhooks.                             |
+------------------------+--------------------------------------------------------------+
| ``read:oembed``        | Grants read-only to oembed endpoints.                        |
+------------------------+--------------------------------------------------------------+
| ``read:management``    | Grants read-only access to management endpoints.             |
+------------------------+--------------------------------------------------------------+
| ``admin:management``   | Fully manage management endpoints.                           |
+------------------------+--------------------------------------------------------------+
| ``read:userinfo``      | Grants read-only access to userinfo.                         |
+------------------------+--------------------------------------------------------------+

.. note::

    ``write`` implicitly includes ``read``, and ``admin`` implicitly
    includes ``read`` and ``write``.

Audit Log
---------

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

.. image:: _static/images/loggly-screen-shot-2.png
