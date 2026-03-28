.. _tutorial 9:

Troubleshooting
===============

This guide covers common problems you may encounter when running
Alerta and how to diagnose them.

**Contents**

  * Overview_
  * `Step 1: Enable debug logging`_
  * `Step 2: Check server health`_
  * `Step 3: Common web UI errors`_
  * `Step 4: Authentication failures`_
  * `Step 5: Database connection errors`_
  * `Step 6: Plugin errors`_
  * `Step 7: Common CLI errors`_
  * `Next Steps`_

Overview
--------

When something goes wrong, start by enabling debug logging,
then check the management endpoints for server health. Most
issues fall into a few common categories: CORS misconfiguration,
authentication problems, database connectivity, or plugin errors.

.. _Step 1:

Step 1: Enable debug logging
-----------------------------

Set the following in your ``alertad.conf`` to enable verbose
debug output:

.. code-block:: python

    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    LOG_FORMAT = 'verbose'

If running in Docker, set the ``DEBUG`` environment variable::

    $ docker run -e DEBUG=1 alerta/alerta-web

The verbose log format includes timestamps, module names, and
line numbers which are essential for diagnosing issues. Check
the logs for lines containing ``ERROR`` or ``WARNING``::

    $ grep -E 'ERROR|WARNING' /var/log/alerta/alertad.log

For Docker deployments::

    $ docker logs alerta-web 2>&1 | grep -E 'ERROR|WARNING'

.. _Step 2:

Step 2: Check server health
----------------------------

Alerta provides management endpoints for monitoring server health.

**Health check** -- returns ``OK`` if the server is running and
the database is reachable::

    $ curl http://localhost:8080/api/management/healthcheck
    {
      "status": "ok"
    }

**Good to go** -- a lightweight check suitable for load balancers::

    $ curl http://localhost:8080/api/management/gtg
    OK

**Properties** -- shows server configuration, version, and database
info (requires admin API key)::

    $ curl http://localhost:8080/api/management/properties \
      -H 'Authorization: Key your-admin-api-key'

**Heartbeats** -- check that expected heartbeats are being received.
Stale heartbeats often indicate a broken integration::

    $ alerta heartbeats

.. _Step 3:

Step 3: Common web UI errors
------------------------------

**CORS errors**

If the browser console shows ``Access-Control-Allow-Origin`` errors,
the web UI cannot reach the API due to cross-origin restrictions.
Set ``CORS_ORIGINS`` in ``alertad.conf`` to allow the web UI origin:

.. code-block:: python

    CORS_ORIGINS = [
        'http://localhost:8080',
        'https://alerta.example.com'
    ]

For Docker deployments, set the ``CORS_ORIGINS`` environment variable.

**Blank page or missing alerts**

Check the browser developer console (F12) for JavaScript errors.
Ensure the ``API_URL`` in the web UI configuration points to the
correct Alerta API endpoint. For Docker, this is set via the
``BASE_URL`` environment variable.

.. _Step 4:

Step 4: Authentication failures
-------------------------------

**"401 Unauthorized" errors**

  * Verify the API key is valid and has not expired::

        $ alerta key --list

  * Check that ``AUTH_REQUIRED`` is set consistently -- if the server
    requires authentication, all clients must provide credentials
  * Ensure API keys have the correct scopes (``read``, ``write:alerts``,
    ``admin``) for the operations being attempted

**OAuth / SSO login failures**

  * Verify ``OAUTH2_CLIENT_ID`` and ``OAUTH2_CLIENT_SECRET`` are correct
  * Check that the redirect URI matches exactly what is configured in
    the OAuth provider
  * Enable debug logging to see the full OAuth exchange

.. _Step 5:

Step 5: Database connection errors
-----------------------------------

**"could not connect to server" or timeout errors**

  * Verify the ``DATABASE_URL`` is correct and the database is reachable
    from the Alerta server::

        $ psql "$DATABASE_URL" -c "SELECT 1"

  * For Docker, ensure the database container is running and on the
    same network::

        $ docker network inspect <network_name>

  * Check for connection pool exhaustion in the logs -- this may
    indicate too many concurrent connections

.. _Step 6:

Step 6: Plugin errors
---------------------

Plugins that raise exceptions will cause alerts to be rejected.
Debug logging will show the full traceback.

**Common plugin issues:**

  * A plugin listed in ``PLUGINS`` is not installed -- the server will
    fail to start. Check installed packages::

        $ pip list | grep alerta

  * A plugin raises an exception during ``pre_receive`` -- the alert
    will be rejected with a 403 error
  * A ``post_receive`` plugin failure is logged but does not reject
    the alert

To temporarily disable a problematic plugin, remove it from the
``PLUGINS`` list and restart the server.

.. _Step 7:

Step 7: Common CLI errors
--------------------------

**"connection refused" or timeout**

  * Check that the ``ALERTA_ENDPOINT`` environment variable or
    ``--endpoint`` flag points to the correct URL::

        $ alerta --endpoint http://localhost:8080/api query

**"not found" when alerts exist**

  * The default query filters by open and acknowledged status.
    Use ``--status`` to query other statuses::

        $ alerta query --status closed

**"environment not allowed"**

  * The alert environment must be in the server ``ALLOWED_ENVIRONMENTS``
    list. Check the current setting via the management properties
    endpoint.

Next Steps
----------

  * :ref:`Using Docker to deploy Alerta <tutorial 10>`
  * :ref:`Kubernetes Deployment <tutorial 11>`
