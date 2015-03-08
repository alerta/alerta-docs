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
- Callback URL: any valid web address

Create your twitter application, switch to *Settings* tab and enable *Allow this application to be used to Sign in with Twitter*.

Select the *Keys and Access Tokens* tab and take note of the Consumer Key (API Key), for the OAuth Client ID, and the Consumer Secret (API Secret), for the OAuth Client Secret. Then update the ``alertad`` configuration settings as follows::

    OAUTH2_CLIENT_ID = '1Hfs7vUYPI1krKNFr2Pdg'  # consumer key
    OAUTH2_CLIENT_SECRET = 'C0PthnGzCYzICnjG2dXaS6GhU4qqHEtcPMy33x8mpl3'  # consumer secret

.. _`Twitter Application Management`: https://dev.twitter.com/apps

To restrict access to particular users use the *circle of trust* approach. That is, add yourself to the list of allowed users, ensure ``AUTH_REQUIRED`` is set to ``True`` and restart ``alertad``. To gain access now, a user will need to be listed in the *Users* page. Note that any authorised user can add anyone else.

.. note:: Twitter does not support OAuth2 for user

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

User Authorisation
------------------

Google and GitHub OAuth2 are used for user authentication, not user authorisation. Authentication proves that you are who you say you are.

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


