.. _tutorial 7:

Partition Alerts using Customer Views
=====================================

In this tutorial you will learn how to partition alerts by customer
so that different teams or tenants only see their own alerts.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Enable Customer Views`_
  * `Step 2: Configure Admin Users`_
  * `Step 3: Create Customer Lookups`_
  * `Step 4: Send Alerts as Different Customers`_
  * `Step 5: Verify Alert Isolation`_
  * `Next Steps`_

Overview
--------

Customer views allow a single Alerta deployment to serve multiple
teams or tenants. When enabled, alerts are tagged with a customer
name based on the authenticated user, and non-admin users can only
view alerts belonging to their own customer. Administrators retain
access to all alerts.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 6 <tutorial 6>`
and have a working Alerta server with authentication enabled. You
will need an admin user and the ability to create additional user
accounts.

Step 1: Enable Customer Views
------------------------------

Set ``CUSTOMER_VIEWS`` to ``True`` in ``alertad.conf``::

    CUSTOMER_VIEWS = True

Restart the server for the change to take effect.

Step 2: Configure Admin Users
------------------------------

Admin users can see all alerts regardless of customer. Ensure your
admin email is listed in ``alertad.conf``::

    ADMIN_USERS = ['admin@example.com']

Step 3: Create Customer Lookups
-------------------------------

Customer lookups map users to customer names. The mapping is based
on the user's login domain, email prefix, Keycloak role, GitHub org,
or a specific match. Create lookups using the API as an admin:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/customer \
    -H 'Authorization: Bearer <admin-token>' \
    -H 'Content-Type: application/json' -d '{
      "customer": "Company A",
      "match": "companya.com"
    }'

  $ curl -XPOST http://localhost:8080/api/customer \
    -H 'Authorization: Bearer <admin-token>' \
    -H 'Content-Type: application/json' -d '{
      "customer": "Company B",
      "match": "companyb.com"
    }'

The ``match`` field is compared against the authenticated user's
email domain. Any user with an ``@companya.com`` email will be
assigned to "Company A".

Verify the lookups:

.. code-block:: console

  $ curl http://localhost:8080/api/customers \
    -H 'Authorization: Bearer <admin-token>'

Step 4: Send Alerts as Different Customers
------------------------------------------

Create a user account for each customer and generate API keys:

.. code-block:: console

  $ curl -XPOST http://localhost:8080/api/auth/signup -H 'Content-Type: application/json' -d '{
      "name": "User A",
      "email": "ops@companya.com",
      "password": "Pa55w0rd-A"
    }'

  $ curl -XPOST http://localhost:8080/api/auth/signup -H 'Content-Type: application/json' -d '{
      "name": "User B",
      "email": "ops@companyb.com",
      "password": "Pa55w0rd-B"
    }'

Log in as each user and send alerts:

.. code-block:: console

  $ # As Company A
  $ curl -XPOST http://localhost:8080/api/alert \
    -H 'Authorization: Bearer <token-A>' \
    -H 'Content-Type: application/json' -d '{
      "resource": "web01",
      "event": "HttpError",
      "environment": "Production",
      "service": ["Web"],
      "severity": "major",
      "text": "Company A: HTTP 500 errors."
    }'

  $ # As Company B
  $ curl -XPOST http://localhost:8080/api/alert \
    -H 'Authorization: Bearer <token-B>' \
    -H 'Content-Type: application/json' -d '{
      "resource": "db01",
      "event": "DbError",
      "environment": "Production",
      "service": ["Database"],
      "severity": "critical",
      "text": "Company B: database connection refused."
    }'

Alerts are automatically tagged with the customer name derived from
the authenticated user -- no ``customer`` field needs to be set
explicitly.

Step 5: Verify Alert Isolation
------------------------------

Query alerts as each user to confirm isolation:

.. code-block:: console

  $ # Company A only sees their own alert
  $ curl -s http://localhost:8080/api/alerts \
    -H 'Authorization: Bearer <token-A>' | python -m json.tool
  # Returns only "Company A: HTTP 500 errors."

  $ # Company B only sees their own alert
  $ curl -s http://localhost:8080/api/alerts \
    -H 'Authorization: Bearer <token-B>' | python -m json.tool
  # Returns only "Company B: database connection refused."

  $ # Admin sees all alerts
  $ curl -s http://localhost:8080/api/alerts \
    -H 'Authorization: Bearer <admin-token>' | python -m json.tool
  # Returns both alerts

Blackout periods also respect customer views -- a blackout created
by a non-admin user will only apply to alerts for that user's
customer.

Next Steps
----------

Now that you understand customer views, you might want to try
some of the following tutorials:

  * :ref:`Customising alerts <tutorial 4 customisation>`
  * :ref:`Suppressing alerts using blackouts <tutorial 5>`
