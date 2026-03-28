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
      "endpoint": "https://api.alerta.dev", 
      "github_url": null, 
      "gitlab_url": "https://gitlab.com", 
      "keycloak_realm": null, 
      "keycloak_url": null, 
      "cas_server": null,
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

Severity Colors
---------------

.. raw:: html

    <table class="docutils align-default">
    <thead><tr><th>Severity</th><th>Code</th><th>Colour</th></tr></thead>
    <tbody>
    <tr><td><code>security</code></td><td>0</td><td><span style="display:inline-block;width:14px;height:14px;background:#0000FF;border:1px solid #ccc;vertical-align:middle"></span> <code>#0000FF</code> Blue</td></tr>
    <tr><td><code>critical</code></td><td>1</td><td><span style="display:inline-block;width:14px;height:14px;background:#FF0000;border:1px solid #ccc;vertical-align:middle"></span> <code>#FF0000</code> Red</td></tr>
    <tr><td><code>major</code></td><td>2</td><td><span style="display:inline-block;width:14px;height:14px;background:#FFA500;border:1px solid #ccc;vertical-align:middle"></span> <code>#FFA500</code> Orange</td></tr>
    <tr><td><code>minor</code></td><td>3</td><td><span style="display:inline-block;width:14px;height:14px;background:#FFFF00;border:1px solid #ccc;vertical-align:middle"></span> <code>#FFFF00</code> Yellow</td></tr>
    <tr><td><code>warning</code></td><td>4</td><td><span style="display:inline-block;width:14px;height:14px;background:#1E90FF;border:1px solid #ccc;vertical-align:middle"></span> <code>#1E90FF</code> DodgerBlue</td></tr>
    <tr><td><code>indeterminate</code></td><td>5</td><td><span style="display:inline-block;width:14px;height:14px;background:#ADD8E6;border:1px solid #ccc;vertical-align:middle"></span> <code>#ADD8E6</code> LightBlue</td></tr>
    <tr><td><code>cleared</code></td><td>5</td><td><span style="display:inline-block;width:14px;height:14px;background:#00CC00;border:1px solid #ccc;vertical-align:middle"></span> <code>#00CC00</code> Green</td></tr>
    <tr><td><code>normal</code></td><td>5</td><td><span style="display:inline-block;width:14px;height:14px;background:#00CC00;border:1px solid #ccc;vertical-align:middle"></span> <code>#00CC00</code> Green</td></tr>
    <tr><td><code>ok</code></td><td>5</td><td><span style="display:inline-block;width:14px;height:14px;background:#00CC00;border:1px solid #ccc;vertical-align:middle"></span> <code>#00CC00</code> Green</td></tr>
    <tr><td><code>informational</code></td><td>6</td><td><span style="display:inline-block;width:14px;height:14px;background:#00CC00;border:1px solid #ccc;vertical-align:middle"></span> <code>#00CC00</code> Green</td></tr>
    <tr><td><code>debug</code></td><td>7</td><td><span style="display:inline-block;width:14px;height:14px;background:#9D006D;border:1px solid #ccc;vertical-align:middle"></span> <code>#9D006D</code> Purple</td></tr>
    <tr><td><code>trace</code></td><td>8</td><td><span style="display:inline-block;width:14px;height:14px;background:#7554BF;border:1px solid #ccc;vertical-align:middle"></span> <code>#7554BF</code> Violet</td></tr>
    <tr><td><code>unknown</code></td><td>9</td><td><span style="display:inline-block;width:14px;height:14px;background:#C0C0C0;border:1px solid #ccc;vertical-align:middle"></span> <code>#C0C0C0</code> Silver</td></tr>
    </tbody>
    </table>

.. note:: The ``indeterminate`` color was incorrectly shown as green in
    previous versions of this documentation. It is ``#ADD8E6`` (LightBlue)
    in the source code.
