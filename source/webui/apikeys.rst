.. _webui api keys:

API Keys
========

The API Keys page allows you to create and manage API keys used to
authenticate with the Alerta API. Navigate to it from the main menu
under *Configuration > API Keys*.

Creating an API Key
-------------------

Click the **+** button to create a new API key. The following fields are
required:

- **Scopes** -- select one or more scopes to grant to the key. Common
  choices include ``read``, ``write``, and ``admin``. Fine-grained scopes
  such as ``read:alerts``, ``write:alerts``, and ``write:heartbeats`` are
  also available.
- **Expires** -- set an expiry time for the key. Keys can be created with
  a fixed duration or set to never expire.
- **Text** -- a free-text description to identify the purpose of the key.

After creation, the full API key value is displayed once. Copy it immediately
as it cannot be retrieved again.

.. note:: Users can only create keys with scopes that are equal to or less
          than their own permissions. Admin users can create keys with any
          scope.

Listing API Keys
----------------

The API keys table shows all keys you have access to view, with the following
columns:

- **Key** -- a partial view of the key value (last 4 characters)
- **Scopes** -- the scopes assigned to the key
- **Description** -- the text description
- **Expires** -- the expiry date and time
- **Status** -- ``active`` or ``expired``
- **Customer** -- the customer associated with the key (if applicable)

Admin users can see all API keys. Non-admin users only see their own keys.

Revoking API Keys
-----------------

Click the delete icon next to a key to revoke it. Revoked keys are immediately
invalidated and can no longer be used for API authentication.

.. tip:: Use read-only scopes (``read``) for monitoring dashboards and
         integrations that do not need to modify data. Use ``write`` scopes
         only for tools that need to create or update alerts.
