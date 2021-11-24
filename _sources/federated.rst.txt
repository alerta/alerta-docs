.. _federated:

Federated Alerta
================

Alerta servers can forward alerts, actions and deletes to
other Alerta servers or downstream systems using the ``forwarder``
built-in plugin.

In this way, Alerta servers can be organised in a hierarchy of
sub-ordinate servers forwarding to servers above them to create a hierarchy of Alerta servers.

Also individual Alerta servers can be kept in sync with others 
each other to create a "active-active" architectures where any
server can be used as the "primary" and if a failure occurs any
other server can take over.

Alerta can be configured to send some or all of the following:

  * received alerts
  * all alert actions or just specific actions. eg. ``ack``, ``shelve``, ``open``, ``close``
  * custom alert actions eg. ``createIssue`` or ``ringBell``
  * alert deletions

.. note:: Forwarding heartbeats is not currently possible but may
    be supported in a future release.

.. _forwarding_configuration

Configuration
-------------

``BASE_URL``

Set the ``BASE_URL`` to the public endpoint that will be used by 
the web UI, alert generating systems, and forwarding Alerta servers


``PLUGINS``

Simply add the ``fowarder`` plugin to this list of configured plugins
to enable and load it when the API starts.

``FWD_DESTINATIONS``

Forwarder destinations have three parts:

  * remote ``BASE_URL``
  * authentication credentials
  * forwarding filter

Example

.. code-block:: python

    FWD_DESTINATIONS = [
        ('http://localhost:9000', {'username': 'user', 'password': 'pa55w0rd', 'timeout': 10}, ['alerts', 'actions']),  # BasicAuth
        # ('https://httpbin.org/anything', dict(username='foo', password='bar', ssl_verify=False), ['*']),
        ('http://localhost:9001', {
            'key': 'e3b8afc0-db18-4c51-865d-b95322742c5e',
            'secret': 'MDhjZGMyYTRkY2YyNjk1MTEyMWFlNmM3Y2UxZDU1ZjIK'
        }, ['actions']),  # Hawk HMAC
        ('http://localhost:9002', {'key': 'demo-key'}, ['delete']),  # API key
        ('http://localhost:9003', {'token': 'bearer-token'}, ['*']),  # Bearer token
    ]


.. _forwarding_loops

Forwarding Loops
----------------

The configured remote ``BASE_URL`` must match the ``BASE_URL`` as set at
the remote server otherwise forwarding loops are possible (see next).

There is no problem with Alerta servers forwarding alerts and actions
to each other. This is the basis of an "active-active" failover
configuration.

However, if misconfigured, servers can endlessly forward to each other
and back again which would eventually lead to resource exhaustion and
failure.

The solution is to borrow the concept of a "forwarding loop" header
from mail servers. If the ``X-Alerta-Loop`` header contains the Alerta
server name (ie ``BASE_URL``) of the receiving server then the receiving
server should not process the request.

And if an alert or action is to be forwarded to a remote Alerta server
that is already in the "forwarding loop" header then that server should
be skipped.

https://qmail.mivzakim.net/qmail-manual-html/misc/RFCLOOPS.html

.. _forwarding_auth

Authentication
--------------

Alerta supports multiple authentication methods for the remote
systems when forwarding:

  * HMAC
  * API Key 
  * BasicAuth
  * Bearer token

The recommended authentication method for Alerta-to-Alerta forwarding is
HMAC because it is the most secure, it does not require a user to be
associated with the credentials and the credentials do not expire.

The other authentication methods are available for use when forwarding to
non-Alerta systems.

To generate HMAC key and secret, it is useful to use a UUID for the key
and base64 encoded string for the secret so that they are visibly different.

On macOs, run::

    $ uuidgen | tr '[:upper:]' '[:lower:]'         <= create HMAC "key"
    58e7c66f-b990-4610-9496-60eb3c63339b

    $ date | md5 | base64                        <= create HMAC "secret"
    MzVlMzQ5NWYzYWE2YTgxYTUyYmIyNDY0ZWE2ZWJlYTMK

.. _forwarding_filters

Forwarding Filters
------------------

The types of entites to be forwarded are configurable:

  * ``*`` - everything ie. alerts, all actions (incl. custom), deletes
  * ``alerts`` - alerts
  * ``actions`` - all actions
  * individual actions - eg. ``ack``
  * custom actions eg. ``createIssue``
  * ``delete``

Examples

.. code-block:: python

    ['*']
    ['alerts', 'ack', 'unack', 'close', 'delete']
    ['alerts', 'delete']

.. _non_alerta_forwarding

Non-Alerta Forwarding
---------------------

It is possible to make use of Alerta forwarding to forward alerts to
non-Alerta systems. However, any forwarding destination will need to 
implement the following endpoints:

  * ``POST`` ``/alert`` - alert receiver
  * ``PUT`` ``/alert/{alertId}/action`` - action alerts
  * ``DELETE`` ``/alert/{alertId}`` - delete alerts

Responses should have HTTP ``200 OK`` status code on success.
HTTP response bodies are not parsed so they will not effect the result.
However, it is good practise to add meaningful messages to the
payloads which will be useful when debugging.

Troubleshooting
---------------

  * Enable detailed logging with ``DEBUG=True``.
  * Use a dummy endpoint such as ``https://httpbin.org/anything``

Future Enhancements
-------------------

  * heartbeat forwarding
  * circuit-breaker retry logic
  * configurable endpoints
