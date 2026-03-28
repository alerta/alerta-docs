.. _webui permissions:

Permissions
===========

The permissions page manages the mapping between user roles (or group names)
and the scopes they are granted. Navigate to it from the main menu under
*Configuration > Permissions*.

How Permissions Work
--------------------

Alerta uses a role-based access control model. Each user has one or more
roles (e.g. ``admin``, ``ops``, ``devops``). Permissions define which
scopes each role is granted. When a user makes an API request, their
roles are looked up and the corresponding scopes determine what actions
are allowed.

The available scopes follow the pattern ``action:resource`` and include:

- ``read``, ``write``, ``admin`` -- broad scopes
- ``read:alerts``, ``write:alerts``, ``delete:alerts``, ``admin:alerts``
- ``read:blackouts``, ``write:blackouts``, ``admin:blackouts``
- ``read:heartbeats``, ``write:heartbeats``, ``admin:heartbeats``
- ``write:users``, ``admin:users``
- ``read:keys``, ``write:keys``, ``admin:keys``
- ``read:perms``, ``admin:perms``
- ``read:groups``, ``admin:groups``

Creating a Permission
---------------------

Click the **+** button to create a new role-to-scope mapping:

- **Match** -- the role or group name to match (e.g. ``ops``, ``devops``,
  ``network-team``). This is compared against the user's roles and group
  memberships.
- **Scopes** -- select one or more scopes to grant to users matching this
  role.

.. note:: The ``admin`` role has all scopes by default and does not need
          an explicit permission mapping.

Listing Permissions
-------------------

The permissions table shows all configured role-to-scope mappings with the
match string and assigned scopes. Use this view to audit which roles have
access to which resources.

Deleting Permissions
--------------------

Click the delete icon next to a permission to remove the mapping. Users
with that role will lose the associated scopes on their next API request.

.. tip:: Start with minimal scopes and add more as needed. For example,
         give a monitoring dashboard role only ``read:alerts`` and
         ``read:heartbeats`` scopes.
