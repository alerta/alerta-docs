.. _webui config:

Configuration
-------------

To configure the Alerta web UI modify "in place" the default ``config.json`` file
that is supplied with the web application. It uses simple JSON syntax.

.. deprecated:: 6.0
    The Alerta web UI previously used an `AngularJS configuration block`_
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


**config.js Javascript Configuration**

.. deprecated:: 5.0
    Use :envvar:`DATABASE_URL` and :envvar:`DATABASE_NAME` instead.

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
Full list of API server settings that can be used to configure clients can be found
at :ref:`webui settings`.

.. raw:: html
    <style> .red { background-color: red } </style>

Severity Colors
---------------

.. |blu| image:: https://via.placeholder.com/16x16/0000ff/0000ff
.. |red| image:: https://via.placeholder.com/16x16/ff0000/ff0000
.. |org| image:: https://via.placeholder.com/16x16/ffa500/ffa500
.. |ylw| image:: https://via.placeholder.com/16x16/ffff00/ffff00
.. |dbl| image:: https://via.placeholder.com/16x16/1e90ff/1e90ff
.. |lbl| image:: https://via.placeholder.com/16x16/add8e6/add8e6
.. |grn| image:: https://via.placeholder.com/16x16/00cc00/00cc00
.. |prp| image:: https://via.placeholder.com/16x16/9d006d/9d006d
.. |vlt| image:: https://via.placeholder.com/16x16/7554bf/7554bf
.. |slv| image:: https://via.placeholder.com/16x16/c0c0c0/c0c0c0

+-------------------+---------------+---------------------------------+
| Severity          | Severity Code | Colour                          |
+===================+===============+=================================+
| ``security``      | 0             | |blu| ``#0000FF``  (Blue)       |
+-------------------+---------------+---------------------------------+
| ``critical``      | 1             | |red| ``#FF0000``  (Red)        |
+-------------------+---------------+---------------------------------+
| ``major``         | 2             | |org| ``#FFA500``  (Orange)     |
+-------------------+---------------+---------------------------------+
| ``minor``         | 3             | |ylw| ``#FFFF00``  (Yellow)     |
+-------------------+---------------+---------------------------------+
| ``warning``       | 4             | |dbl| ``#1E90FF``  (DodgerBlue) |
+-------------------+---------------+---------------------------------+
| ``indeterminate`` | 5             | |lbl| ``#00CC00`` (LightBlue)   |
+-------------------+---------------+---------------------------------+
| ``cleared``       | 5             | |grn| ``#00CC00`` (Green*)      |
+-------------------+---------------+---------------------------------+
| ``normal``        | 5             | |grn| ``#00CC00`` (Green*)      |
+-------------------+---------------+---------------------------------+
| ``ok``            | 5             | |grn| ``#00CC00`` (Green*)      |
+-------------------+---------------+---------------------------------+
| ``informational`` | 6             | |grn| ``#00CC00`` (Green*)      |
+-------------------+---------------+---------------------------------+
| ``debug``         | 7             | |prp| ``#9D006D`` (Purple*)     |
+-------------------+---------------+---------------------------------+
| ``trace``         | 8             | |vlt| ``#7554BF`` (Violet*)     |
+-------------------+---------------+---------------------------------+
| ``unknown``       | 9             | |slv| ``#C0C0C0`` (Silver)      |
+-------------------+---------------+---------------------------------+
