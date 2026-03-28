.. _tutorial 6:

Authentication Setup
====================

In this tutorial you will learn how to enable authentication, create
users, generate API keys, and control access to the Alerta API.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Enable Authentication`_
  * `Step 2: Set a Secret Key`_
  * `Step 3: Create an Admin User`_
  * `Step 4: Log In and Obtain a Token`_
  * `Step 5: Generate an API Key`_
  * `Step 6: Restrict Email Domains`_
  * `Step 7: Email Verification`_
  * `Next Steps`_

Overview
--------

By default, Alerta runs without authentication -- any client can read
and write alerts. Enabling authentication adds user signup, login
tokens, API keys, and role-based access control. This tutorial covers
Basic Auth (username/password). For OAuth, LDAP, SAML, or OpenID
Connect, see the :ref:`authentication <authentication>` reference.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
or you have access to an Alerta server that you can configure.

Step 1: Enable Authentication
-----------------------------

Set ``AUTH_REQUIRED`` to ``True`` in ``alertad.conf``::

    AUTH_REQUIRED = True

After restarting the server, all API requests without a valid token or
API key will receive a ``401 Unauthorized`` response:

.. code-block:: console

  $ curl http://localhost:8080/api/alerts
  {"message": "Authorization required ...", "status": "error"}

Step 2: Set a Secret Key
-------------------------

The ``SECRET_KEY`` is used to sign JWT tokens. Change it from the
default before enabling authentication::

    SECRET_KEY = 'R4nd0m-$3cret-k3y-ch4nge-m3!'

.. warning::

  Use a long, random string. If the secret key is compromised,
  attackers can forge valid authentication tokens.

Step 3: Create an Admin User
-----------------------------

Define one or more admin users in ``alertad.conf`` by email address::

    ADMIN_USERS = ['admin@example.com']

Then sign up using the API. The first matching email in ``ADMIN_USERS``
is granted the ``admin`` role automatically:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/auth/signup -H 'Content-Type: application/json' -d '{
      "name": "Admin",
      "email": "admin@example.com",
      "password": "Adm1n-Pa55w0rd",
      "text": "Primary administrator"
    }'

.. note::

  Signup is enabled by default (``SIGNUP_ENABLED = True``). Set it
  to ``False`` after creating initial accounts if you want to prevent
  self-service registration.

Step 4: Log In and Obtain a Token
---------------------------------

Exchange credentials for a JWT bearer token:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/auth/login -H 'Content-Type: application/json' -d '{
      "username": "admin@example.com",
      "password": "Adm1n-Pa55w0rd"
    }'
  {"token": "eyJhbGciOiJIUzI1NiIs..."}

Use the token in subsequent requests via the ``Authorization`` header:

.. code-block:: console

  $ curl http://localhost:8080/api/alerts -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIs...'

Tokens expire after ``TOKEN_EXPIRE_DAYS`` (default 14 days).

Step 5: Generate an API Key
----------------------------

API keys are better suited for the CLI tool and long-lived
integrations. Create one through the API:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/key \
    -H 'Authorization: Bearer <token>' \
    -H 'Content-Type: application/json' -d '{
      "scopes": ["read", "write"],
      "text": "CLI access key"
    }'

Configure the ``alerta`` CLI to use the key:

.. code-block:: console

  $ alerta --endpoint-url http://localhost:8080/api --api-key <api-key> query

Or set environment variables:

.. code-block:: console

  $ export ALERTA_ENDPOINT=http://localhost:8080/api
  $ export ALERTA_API_KEY=<api-key>
  $ alerta query

API keys expire after ``API_KEY_EXPIRE_DAYS`` (default 365 days).

Step 6: Restrict Email Domains
------------------------------

Limit who can sign up by specifying allowed email domains. The
default allows all domains::

    ALLOWED_EMAIL_DOMAINS = ['example.com', 'ops.example.com']

Users with email addresses outside these domains will be rejected
at signup.

Step 7: Email Verification
--------------------------

Require new users to verify their email address before they can
use the API. Enable email verification and configure SMTP::

    EMAIL_VERIFICATION = True
    SMTP_HOST = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_STARTTLS = True
    SMTP_USERNAME = 'alerts@example.com'
    SMTP_PASSWORD = 'smtp-password'
    MAIL_FROM = 'alerts@example.com'

Unverified users will receive a ``403 Forbidden`` response until
they click the verification link sent to their email.

Next Steps
----------

Now that you have authentication configured, you might want to try
some of the following tutorials:

  * :ref:`Partition alerts using customer views <tutorial 7>`
  * :ref:`Suppressing alerts using blackouts <tutorial 5>`
  * For OAuth, LDAP, SAML, and OpenID Connect see :ref:`authentication`
