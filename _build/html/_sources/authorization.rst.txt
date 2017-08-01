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
| ``admin:alerts``       | Grants read, write and delete access to alerts.              |
+------------------------+--------------------------------------------------------------+
| ``read:blackouts``     | Grants read-only access to blackouts.                        |
+------------------------+--------------------------------------------------------------+
| ``write:blackouts``    | Grants read/write access to blackouts.                       |
+------------------------+--------------------------------------------------------------+
| ``read:heartbeats``    | Read-only access to heartbeats.                              |
+------------------------+--------------------------------------------------------------+
| ``write:heartbeats``   | Grants read/write access to heartbeats.                      |
+------------------------+--------------------------------------------------------------+
| ``admin:heartbeats``   | Grants read, write and delete access to heartbeats.          |
+------------------------+--------------------------------------------------------------+
| ``admin:users``        | Fully manage users.                                          |
+------------------------+--------------------------------------------------------------+
| ``admin:customers``    | Fully manage customers.                                      |
+------------------------+--------------------------------------------------------------+
| ``read:keys``          | List and view API keys.                                      |
+------------------------+--------------------------------------------------------------+
| ``write:keys``         | Create, list and view API keys.                              |
+------------------------+--------------------------------------------------------------+
| ``admin:keys``         | Fully manage API keys.                                       |
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
