.. _authentication:

Authentication
==============

By default, authentication is not enabled, however there are some features that are :ref:`not available <watched_alerts>` unless users login. To enforce authentication set ``AUTH_REQUIRED`` to ``True``::

    AUTH_REQUIRED = True

.. note:: Ensure that the :envvar:`SECRET_KEY` that is used to encode cookies is a unique, randomly generated sequence of ASCII characters. The following command generates a suitable 32-character random string::

    $ LC_CTYPE=C tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 && echo

Alerta supports two types of authentication for the web UI (:ref:`Basic Auth <basic auth>` and :ref:`OAuth <oauth2>`) as well as :ref:`API keys <api keys>` for direct access to the API.

.. _basic auth:

Basic Authentication
--------------------

HTTP `Basic authentication`_ is a very simple method for enforcing access control.

.. _Basic authentication: https://en.wikipedia.org/wiki/Basic_access_authentication

To use Basic Auth set the ``provider`` configuration setting in the Web UI :file:`config.js` file to ``basic``. There is no configuration required of the Alerta server::

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "/api",
        'provider'    : "basic"
      })
      .constant('colors', {});

.. note:: HTTP Basic auth does not provide any encryption of the username or password so it is strongly advised to only use Basic auth over HTTPS.

.. _oauth2:

OAuth2 Authentication
---------------------

OAuth authentication is provided by Google_ or GitHub_ `OAuth 2.0`_ OpenID_ connect service or Twitter_ `OAuth 1.0a`_ service.

.. note:: If alerta is deployed to a publicly accessible web server it is important to configure the OAuth2 settings correctly to ensure that only authorised users can access and modify your alerts.

.. _Google: https://developers.google.com/accounts/docs/OpenIDConnect
.. _GitHub: https://developer.github.com/v3/oauth/
.. _Twitter: https://dev.twitter.com/web/sign-in/implementing
.. _OAuth 2.0: http://tools.ietf.org/html/draft-ietf-oauth-v2-22
.. _OAuth 1.0a: http://oauth.net/core/1.0a/
.. _OpenID: http://openid.net/connect/

.. _google oauth2:

To use OAuth set the ``provider`` configuration setting in the Web UI :file:`config.js` file to ``google``, ``github`` or ``twitter`` and then follow the steps below to setup the Alert server::

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "/api",
        'provider'    : "google",
        'client_id'   : "INSERT-CLIENT-ID-HERE" // replace with the client id for your OAuth provider
      })
      .constant('colors', {});

Google OAuth2
~~~~~~~~~~~~~

To use Google as the OAuth2 provider for Alerta, login to `Google Developer Console`_ and create a new project for alerta.

.. _Google Developer Console: https://console.developers.google.com

- Project Name: alerta
- Project ID: (automatically assigned)

Go to *APIs and auth -> APIs* and set *Google+ API* to **ON**. Next go to *APIs and auth -> Credentials* and click **Create New Client ID** and choose **Web Application**.

- Authorized Javscript Origins: http://alerta.example.com
- Authorized Redirect URIs: http://alerta.example.com

Click **Create Client ID** and take note of the Client ID and Client Secret. The configuration settins for ``alerta`` server are as follows::

    OAUTH2_CLIENT_ID = '379647311730-sj130ru952o3o7ig8u0ts8np2ojivr8d.apps.googleusercontent.com'
    OAUTH2_CLIENT_SECRET = '8HrqJhbrYn9oDtaJqExample'

.. _allowed_email_domains:

To restrict access to users with particular `Google apps domains`_ use::

    ALLOWED_EMAIL_DOMAINS = ['example.org', 'mycompany.com']

.. _`Google apps domains`: https://www.google.co.uk/intx/en_au/work/apps/business/

.. note:: ``ALLOWED_EMAIL_DOMAINS`` can be an asterisk (``*``) to force login but *not* restrict who can login.

.. _github_oauth2:

GitHub OAuth2
~~~~~~~~~~~~~

To use GitHub as the OAuth2 provider for Alerta, login to GitHub and go to *Settings -> Applications -> Register New Application*.

- Application Name: Alerta
- Homepage URL: http://alerta.io
- Application description (optional): Guardian Alerta monitoring system
- Authorization callback URL: http://alerta.example.com

.. note:: The `Authorization callback URL` is the most important setting and it is nothing more than the URL domain (ie. without any path) where the alerta Web UI is being hosted.

Click Register Application and take note of the Client ID and Client Secret. Then configuration settings for ``alerta`` server are as follows::

    OAUTH2_CLIENT_ID = 'f7b0c15e2b722e0e38f4'
    OAUTH2_CLIENT_SECRET = '7aa9094369b72937910badab0424dc7393x8mpl3'

.. _allowed_github_orgs:

To restrict access to users who are members of particular `GitHub organisations`_ use::

    ALLOWED_GITHUB_ORGS = ['example', 'mycompany']

.. _`GitHub organisations`: https://github.com/blog/674-introducing-organizations

.. note:: ``ALLOWED_GITHUB_ORGS`` can be an asterisk (``*``) to force login but *not* restrict who can login.

.. important:: To revoke access of your instance of alerta to your GitHub user info at any time go to *Settings -> Applications -> Authorized* applications, find alerta in the list of applications and click the **Revoke** button.

Twitter OAuth
~~~~~~~~~~~~~

To use Twitter as the OAuth provider for Alerta, login to `Twitter Application Management`_ and create a new App.

- Name: Alerta for *Organisation*
- Description: Alerta monitoring system
- Website: http://alerta.io
- Callback URL: http://alerta.example.com

Create your twitter application, switch to *Settings* tab and enable *Allow this application to be used to Sign in with Twitter*.

Select the *Keys and Access Tokens* tab and take note of the Consumer Key (API Key), for the OAuth Client ID, and the Consumer Secret (API Secret), for the OAuth Client Secret. Then update the ``alertad`` configuration settings as follows::

    OAUTH2_CLIENT_ID = '1Hfs7vUYPI1krKNFr2Pdg'  # consumer key
    OAUTH2_CLIENT_SECRET = 'C0PthnGzCYzICnjG2dXaS6GhU4qqHEtcPMy33x8mpl3'  # consumer secret

.. _`Twitter Application Management`: https://dev.twitter.com/apps

To restrict access to particular users use the *circle of trust* approach. That is, add yourself to the list of allowed users, ensure ``AUTH_REQUIRED`` is set to ``True`` and restart ``alertad``. To gain access now, a user will need to be manually added to the *Users* page. Note that any existing user can add and remove users for the list of authorised users.

.. note:: Twitter does not support OAuth2 for user logins.




.. _cross_origin:

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

.. _api keys:

API Keys
--------

If authentication is enforced, then an API key is needed to access the alerta API programatically or to use the :ref:`alerta CLI <cli>`. Keys can be easily generated from the Alerta web UI and can be `read-write` or `read-only`. They are valid for 1 year but this period is configurable using ``API_KEY_EXPIRE_DAYS`` in the :ref:`server configuration <api config>`.

See the :ref:`example CLI config <cli config>` for how to set the API key for the command-line tool.

To use an API key in an API query you must set the correct HTTP ``Authorization`` header::

    curl 'http://api.alerta.io/alerts' -H 'Authorization: Key demo-key' -H 'Accept: application/json'

or use the ``api-key`` GET parameter::

    curl 'http://api.alerta.io/alerts?api-key=demo-key' -H 'Accept: application/json'

.. note:: Using the HTTP ``Authorization`` header is preferred so that API keys are not inadvertently captured in log files and accidentally exposed.

.. _users:

User Authorisation
------------------

Google and GitHub OAuth2 are used for user authentication, not user authorisation. Authentication proves that you are who you say you are. Authorization says that you are allowed to access what you have requested.

To control who has access to Alerta you can restrict access to users with a :ref:`certain email domain name <allowed_email_domains>` by setting ``ALLOWED_EMAIL_DOMAINS`` or who belong to a :ref:`particular GitHub organisation <allowed_github_orgs>` by setting ``ALLOWED_GITHUB_ORGS``.

For those situations where it is not possible to group users in this way it is possible to selectively allow access on a per-user basis. How this is done depends on whether you are using Google or GitHub as OAuth2 provider for user login.

Per-User Authorisation using Google
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumes that the user wanting access to Alerta either does not have an email address in the configured Google app email domains::

    ALLOWED_EMAIL_DOMAINS = ['onlyus.com']

Or that the list of allowed email domains is empty::

    ALLOWED_EMAIL_DOMAINS = ['']

Manaully add the user email address by selecting *Configuration -> Users* from the alerta console.

Name: a name to associate with the address, does not need to match registered name
Login: email address of the user wanting access eg. ``let.me.in@gmail.com``

This user will now be able to login to alerta using ``let.me.in@gmail.com`` account eventhough ``gmail.com`` is not listed in the ``ALLOWED_EMAIL_DOMAINS`` setting.

Per-User Authorisation using GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumes that the user wanting access to Alerta is either not a member of the configured GitHub orgs::

    ALLOWED_GITHUB_ORGS = ['onlyus']

Or that the list of allowed GitHub organisations is empty::

    ALLOWED_GITHUB_ORGS = ['']

Manaully add the user GitHub username by selecting *Configuration -> Users* from the alerta console.

Name: a name to associate with the address, does not need to match registered name
Login: GitHub username of user wanting access eg. ``letmein``

This user will now be able to login to alerta using ``letmein`` GitHub account eventhough they are not members of the organisations listed in the ``ALLOWED_GITHUB_ORGS`` setting.
