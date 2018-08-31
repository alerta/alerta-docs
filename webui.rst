.. _webui:

Alerta Web UI
=============

The Alerta web UI console takes full advantage of the :ref:`state-based Alerta API <state based browser>`
to ensure that the most important events at any given time are brought to the
attention of operators.

Configuration
-------------

To configure the Alerta web UI modify "in place" the default ``config.json`` file
that is supplied with the web application. It uses simple JSON syntax.

.. note:: The Alerta web UI before version 6.0 used an `AngularJS configuration block`_
          for configuration settings which has now been deprecated.

.. _AngularJS configuration block: https://docs.angularjs.org/guide/module#configuration-blocks

The three main areas for configuration are:

  * defining the Alerta API endpoint
  * enforcing a use authentication strategy
  * selecting colors for severity, highlighting, text and sound

The default web UI :file:`config.json` configuration file is included below.
It assumes that the Alerta API is running on the same host (but different
port) that the web UI static html files are being served from (line 2):

.. code-block:: json
    :linenos:

    {
      "endpoint": "http://localhost:8080"
    }


Configuration from API Server
-----------------------------

Starting from version 6.0, client configuration is supplied by the API server.
This includes configuration for the web UI and the command-line tool.

Configuration settings are made on the API server and when the web UI console
is bootstrapping it reads the endpoint setting and downloads the rest of
the configuration.

The remote configuration from the API server is merged with the local
configuration settings to provide the final configuration used by
clients.

**Example**

The following API server settings generate the JSON client configuration
shown below that.

.. code-block:: python
    :linenos:

    AUTH_PROVIDER = 'google'
    AUTH_REQUIRED = True
    CUSTOMER_VIEWS = True
    GOOGLE_TRACKING_ID = 'UA-44644195-5'
    OAUTH2_CLIENT_ID = '736147134702-glkb1pesv716j1utg4llg7c3rr7nnhli.apps.googleusercontent.com'
    OAUTH2_CLIENT_SECRET = 'secret'

.. code-block:: json
    :linenos:

    {
      "audio": {}, 
      "auth_required": true, 
      "client_id": "736147134702-glkb1pesv716j1utg4llg7c3rr7nnhli.apps.googleusercontent.com", 
      "colors": {}, 
      "customer_views": true, 
      "dates": {
        "longDate": "EEEE, MMMM d, yyyy h:mm:ss.sss a (Z)", 
        "mediumDate": "medium", 
        "shortTime": "shortTime"
      }, 
      "endpoint": "https://alerta-api.herokuapp.com", 
      "github_url": null, 
      "gitlab_url": "https://gitlab.com", 
      "keycloak_realm": null, 
      "keycloak_url": null, 
      "pingfederate_url": null, 
      "provider": "google", 
      "refresh_interval": 5000, 
      "severity": {
        "cleared": 5, 
        "critical": 1, 
        "debug": 7, 
        "indeterminate": 5, 
        "informational": 6, 
        "major": 2, 
        "minor": 3, 
        "normal": 5, 
        "ok": 5, 
        "security": 0, 
        "trace": 8, 
        "unknown": 9, 
        "warning": 4
      }, 
      "signup_enabled": true, 
      "tracking_id": "UA-44644195-5"
    }


.. note:: For completeness, the ``OAUTH2_CLIENT_ID`` and ``OAUTH2_CLIENT_SECRET``
          configuration settings are included in the example above however it
          should be noted that only the client id is sent to the client (line 4)
          as sending the client secret is not necessary and would compromise security.

Client Settings
~~~~~~~~~~~~~~~
Full list of API server settings that can be used to configure clients.

``AUTH_REQUIRED``

``CUSTOMER_VIEWS``

``AUTH_PROVIDER``

``SIGNUP_ENABLED``

``OAUTH2_CLIENT_ID``

``GITHUB_URL``

``GITLAB_URL``

``KEYCLOAK_URL``

``KEYCLOAK_REALM``

``PINGFEDERATE_URL``

``COLOR_MAP``

``SEVERITY_MAP``

``GOOGLE_TRACKING_ID``

``AUTO_REFRESH_INTERVAL``

.. note:: It is not currently possible to configure dates or audio.