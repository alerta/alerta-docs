.. _authentication:

Authentication
==============

By default, authentication is not enabled, however there are some features that are :ref:`not available <watched_alerts>` unless users login. To enforce authentication set ``AUTH_REQUIRED`` to ``True``::

    AUTH_REQUIRED = True

.. note:: Ensure that the :envvar:`SECRET_KEY` that is used to encode cookies is a unique, randomly generated sequence of ASCII characters. The following command generates a suitable 32-character random string::

    $ LC_CTYPE=C tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 && echo

.. _oauth2:

OAuth2 Authentication
---------------------

User authentication for the web console is provided by Google_ or GitHub_ `OAuth 2.0`_ OpenID_ connect service.

.. note:: If alerta is deployed to a publicly accessible web server it is important to configure the OAuth2 settings correctly to ensure that only authorised users can access and modify your alerts.

.. _Google: https://developers.google.com/accounts/docs/OpenIDConnect
.. _GitHub: https://developer.github.com/v3/oauth/
.. _`OAuth 2.0`: http://tools.ietf.org/html/draft-ietf-oauth-v2-22
.. _OpenID: http://openid.net/connect/


Configuration
-------------

.. _google_oauth2:

Google OAuth2
~~~~~~~~~~~~~

To use Google as the OAuth2 provider for ``alerta``, login to `Google Developer Console`_ and create a new project for alerta.

.. _Google Developer Console: https://console.developers.google.com

- Project Name: alerta
- Project ID: (automatically assigned)

Go to *APIs and auth -> APIs* and set *Google+ API* to **ON**. Next go to *APIs and auth -> Credentials* and click **Create New Client ID** and choose **Web Application**.

- Authorized Javscript Origins: http://alerta.example.com
- Authorized Redirect URIs: http://alerta.example.com

Click **Create Client ID** and take note of the Client ID and Client Secret. The configuration settins for ``alerta`` server are as follows:

::

    OAUTH2_CLIENT_ID = '379647311730-sj130ru952o3o7ig8u0ts8np2ojivr8d.apps.googleusercontent.com'
    OAUTH2_CLIENT_SECRET = '8HrqJhbrYn9oDtaJqExample'
    ALLOWED_EMAIL_DOMAINS = ['example.com']

.. note:: ``ALLOWED_EMAIL_DOMAINS`` can be an asterisk (``*``) to force login but *not* restrict who can login.

.. _github_oauth2:

GitHub OAuth2
~~~~~~~~~~~~~

To use GitHub as the OAuth2 provider for ``alerta``, login to GitHub and go to *Settings -> Applications -> Register New Application*.

- Application Name: Alerta
- Homepage URL: http://alerta.io
- Application description (optional): Guardian Alerta monitoring system
- Authorization callback URL: http://alerta.example.com

.. note:: The `Authorization callback URL` is the most important setting and it is nothing more than the URL domain (ie. without any path) where the alerta Web UI is being hosted.

Click Register Application and take note of the Client ID and Client Secret. Then configuration settings for ``alerta`` server are as follows:

::

    OAUTH2_CLIENT_ID = 'f7b0c15e2b722e0e38f4'
    OAUTH2_CLIENT_SECRET = '7aa9094369b72937910badab0424dc7393x8mpl3'
    ALLOWED_GITHUB_ORGS = ['example']

.. note:: ``ALLOWED_GITHUB_ORGS`` can be an asterisk (``*``) to force login but *not* restrict who can login.

.. important:: To revoke access of your instance of alerta to your GitHub user info at any time go to *Settings -> Applications -> Authorized* applications, find alerta in the list of applications and click the **Revoke** button.

Cross-Origin
~~~~~~~~~~~~

If the Alerta API is not being served from the same domain as the Alerta Web UI then the ``CORS_ORIGINS`` setting needs to be updated to prevent `modern browsers <http://enable-cors.org/client.html>`_ from blocking the cross-origin requests.

::

    CORS_ORIGINS = [
        'http://try.alerta.io',
        'http://explorer.alerta.io',
        'chrome-extension://jplkjnjaegjgacpfafdopnpnhmobhlaf',
        'http://localhost'
    ]

.. _api_keys:

API Keys
--------

If authentication is enforced, then an API key is needed to access the alerta API.

::

    API_KEY_EXPIRE_DAYS = 365  # 1 year

.. _users:

Users
-----

POST, OPTIONS  /user  create_user
POST, OPTIONS, DELETE  /user/<user>  delete_user
HEAD, OPTIONS, GET  /users  get_users

