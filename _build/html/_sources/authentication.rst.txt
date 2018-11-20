.. _authentication:

Authentication
==============

By default, authentication is not enabled, however there are some features
that are :ref:`not available <watched_alerts>` unless users login such as
watching alerts.

Alerta supports three authentication mechanisms for the web UI and
``alerta`` command-line tool.

* `Basic Auth`_
* `Basic Auth using LDAP`_
* `GitHub OAuth2`_
* `GitLab OAuth2`_
* `Google OAuth2`_
* `Keycloak OAuth2`_
* `SAML 2.0`_
* `API Keys`_

To enforce authentication set ``AUTH_REQUIRED`` to ``True`` and set the
``SECRET_KEY`` to some random string in the ``alertad.conf`` server
configuration settings file::

    AUTH_REQUIRED = True
    SECRET_KEY = 'UszE5hI_hx5pXKcsCP_2&1DIs&9_Ve*k'

.. note:: Ensure that the :envvar:`SECRET_KEY` that is used to encode
          tokens and API keys is a unique, randomly generated sequence
          of ASCII characters. The following command generates a suitable
          32-character random string on Mac or Linux::

          $ LC_CTYPE=C tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 && echo

.. _basic auth:

Basic Auth
----------

Basic Auth (built-in)
~~~~~~~~~~~~~~~~~~~~~

The most straight-forward authentication strategy to implement of the
three is HTTP `Basic Authentication`_ provided by the Alerta API
because there is no additional configuration required of the Alerta
server to use it other than setting ``AUTH_REQUIRED`` to ``True``.

.. _Basic Authentication: https://en.wikipedia.org/wiki/Basic_access_authentication

.. note:: HTTP Basic Auth does not provide any encryption of the username
          or password so it is strongly advised to only use Basic Auth over
          HTTPS.

.. _basic_auth_ldap:

Basic Auth using LDAP
~~~~~~~~~~~~~~~~~~~~~

LDAP can be used as the Basic Auth provider to authenticate users
if desired. It requires the installation of an additional Python
package called "`python-ldap`_" and can be installed like so::

    $ pip install python-ldap

.. _`python-ldap`: https://pypi.org/project/python-ldap/

.. important:: If the Alerta API is installed in a Python virtual
    environment ensure that the ``python-ldap`` package is installed
    into the same environment otherwise it won't be auto-detected.

The configuration settings for LDAP authentication include the LDAP
server URL and a map of LDAP domains to search filters which means
that multiple LDAP domains can be supported::

    LDAP_URL = 'ldap://localhost:389'  # replace with your LDAP server
    LDAP_DOMAINS = {
        'my-domain.com': 'uid=%s,ou=users,dc=my-domain,dc=com'
    }

A typical user called ``user1``, for the example above, would login
using an email address of ``user1@my-domain.com`` even if that
email address doesn't actually exist.

All users are initially assigned the "user" role by default. 

.. note:: User sign-up, email verfication and password reset through the
    Alerta web UI or CLI is not supported. Self-service user management
    needs to be handled by the LDAP authentication provider.

.. _oauth2:

OAuth2 Authentication
---------------------

OAuth authentication is provided by Google_ `OpenID Connect`_, GitHub_,
GitLab_ `OAuth 2.0`_ or Keycloak_ `OAuth 2.0`_ and configuration is more
involved than the Basic Auth setup.

.. note:: If Alerta is deployed to a publicly accessible web server it
    is important to configure the OAuth2 settings correctly to
    ensure that only authorised users can access and modify your
    alerts.

.. _Google: https://developers.google.com/accounts/docs/OpenIDConnect
.. _GitHub: https://developer.github.com/v3/oauth/
.. _GitLab: https://docs.gitlab.com/ce/integration/oauth_provider.html
.. _Keycloak: https://www.keycloak.org/documentation.html
.. _OAuth 2.0: http://tools.ietf.org/html/draft-ietf-oauth-v2-22
.. _OpenID Connect: http://openid.net/connect/

Ensure ``AUTH_REQUIRED`` and ``SECRET_KEY`` are set and that the
``AUTH_PROVIDER`` setting is

Then follow the steps below for the chosen OAuth provider to create an
OAuth client ID and client secret. The client ID and client secret
will need to be added to the ``alertad.conf`` file for the Alerta server.

.. _google oauth2:

Google OAuth2
~~~~~~~~~~~~~

To use Google as the OAuth2 provider for Alerta, login to
`Google Developer Console`_ and create a new project for alerta.

.. _Google Developer Console: https://console.developers.google.com

- Project Name: alerta
- Project ID: (automatically assigned)

Go to *APIs and auth -> APIs* and set *Google+ API* to **ON**. Next
go to *APIs and auth -> Credentials* and click **Create New Client ID**
and choose **Web Application**.

- Authorized Javscript Origins: http://alerta.example.com
- Authorized Redirect URIs: http://alerta.example.com

Click **Create Client ID** and take note of the Client ID and Client
Secret. The configuration settings for ``alerta`` server are as follows::

    AUTH_PROVIDER = 'google'
    OAUTH2_CLIENT_ID = '379647311730-sj130ru952o3o7ig8u0ts8np2ojivr8d.apps.googleusercontent.com'
    OAUTH2_CLIENT_SECRET = '8HrqJhbrYn9oDtaJqExample'

.. _allowed_email_domains:

To restrict access to users with particular `Google apps domains`_ use::

    ALLOWED_EMAIL_DOMAINS = ['example.org', 'mycompany.com']

.. _`Google apps domains`: https://www.google.co.uk/intx/en_au/work/apps/business/

.. note:: ``ALLOWED_EMAIL_DOMAINS`` can be an asterisk (``*``) to force
          login but *not* restrict who can login.

.. _github_oauth2:

GitHub OAuth2
~~~~~~~~~~~~~

To use GitHub as the OAuth2 provider for Alerta, login to GitHub and go
to *Settings -> Applications -> Register New Application*.

- Application Name: Alerta
- Homepage URL: http://alerta.io
- Application description (optional): Guardian Alerta monitoring system
- Authorization callback URL: http://alerta.example.com

.. note:: The `Authorization callback URL` is the most important setting
          and it is nothing more than the URL domain (ie. without any path)
          where the alerta Web UI is being hosted.

Click Register Application and take note of the Client ID and Client
Secret. Then configuration settings for ``alerta`` server are as follows::

    AUTH_PROVIDER = 'github'
    OAUTH2_CLIENT_ID = 'f7b0c15e2b722e0e38f4'
    OAUTH2_CLIENT_SECRET = '7aa9094369b72937910badab0424dc7393x8mpl3'

.. _allowed_github_orgs:

To restrict access to users who are members of particular
`GitHub organisations`_ use::

    ALLOWED_GITHUB_ORGS = ['example', 'mycompany']

.. _`GitHub organisations`: https://github.com/blog/674-introducing-organizations

.. note:: ``ALLOWED_GITHUB_ORGS`` can be an asterisk (``*``) to force login
          but *not* restrict who can login.

.. important:: To revoke access of your instance of alerta to your GitHub
               user info at any time go to
               *Settings -> Applications -> Authorized* applications, find
               alerta in the list of applications and click the **Revoke**
               button.

GitLab OAuth2
~~~~~~~~~~~~~

To use GitLab as the OAuth2 provider for Alerta, login to GitLab and go
to *Profile Settings -> Applications -> New Application*.

- Name: Alerta
- Callback URL: http://alerta.example.com
- Scopes: ``openid``

.. image:: _static/images/gitlab-oauth2-screen-shot-3.png

.. note:: The `Callback URL` is the most important setting and it
          is nothing more than the URL domain (ie. without any path)
          where the alerta Web UI is being hosted.

Click *Submit* and take note of the Application ID and Secret. Then
configuration settings for ``alerta`` server are as follows (replacing
the values shown below with the values generated by GitLab)::

    AUTH_PROVIDER = 'gitlab'
    GITLAB_URL = 'https://gitlab.com'  # or your own GitLab server
    OAUTH2_CLIENT_ID = 'd31e9caa131f72901b16d22289c824f423bd5cbf187a11245f402e8b2707d591'
    OAUTH2_CLIENT_SECRET = '42f1de369ec706996cadda234986779eeb65c0201a6f286b9751b1f845d62c8a'

.. _allowed_gitlab_groups:

To restrict access to users who are members of particular `GitLab groups`_ use::

    ALLOWED_GITLAB_GROUPS = ['group1', 'group2']

.. _`GitLab groups`: https://docs.gitlab.com/ee/user/group/index.html

.. note:: ``ALLOWED_GITLAB_GROUPS`` can be an asterisk (``*``) to force
          login but *not* restrict who can login.

.. important:: To revoke access of your instance of alerta to your
               GitLab user info at any time go to
               *Profile Settings -> Applications -> Authorized appliations*,
               find alerta in the list of applications and click the **Revoke**
               button.

Keycloak OAuth2
~~~~~~~~~~~~~~~

To use Keycloak as the OAuth2 provider for Alerta, login to Keycloak admin interface, select the realm and go
to *Clients -> Create*.

- Client ID: alerta-ui
- Client protocol: openid-connect
- Root URL: http://alerta.example.org

After the client is created, edit it and change the following properties:

- Access Type: confindential

Add the following mapper under the *Mappers* tab::

    Name: role memberships
    Mapper type: User Realm Role
    Token Claim Name: roles
    Claim JSON type: String
    Add to userinfo: ON

Now go to *Installation* and generate it by selecting 'Keycloak OIDC JSON'. You should get something like this::

   {
     "realm": "master",
     "auth-server-url": "https://keycloak.example.org/auth",
     "ssl-required": "external",
     "resource": "alerta-ui",
     "credentials": {
       "secret": "418bbf31-aef-33d1-a471-322a60276879"
     },
     "use-resource-role-mappings": true
   }

Take note of the realm, resource and secret. Then configuration settings for ``alerta`` server are as follows (replacing
the values shown below with the values generated by Keycloak)::

    AUTH_PROVIDER = 'keycloak'
    KEYCLOAK_URL = 'https://keycloak.example.org'
    KEYCLOAK_REALM = 'master'
    OAUTH2_CLIENT_ID = 'alerta-ui'
    OAUTH2_CLIENT_SECRET = '418bbf31-aef-33d1-a471-322a60276879'

.. _allowed_keycloak_roles:

To restrict access to users who are associated with a particular `Keycloak role`_ use::

    ALLOWED_KEYCLOAK_ROLES = ['role1', 'role2']

.. _`Keycloak role`: https://keycloak.gitbooks.io/documentation/server_admin/topics/roles.html

.. note:: ``ALLOWED_KEYCLOAK_ROLES`` can be an asterisk (``*``) to force
          login but *not* restrict who can login.

.. _cross_origin:

Cross-Origin
~~~~~~~~~~~~

If the Alerta API is not being served from the same domain as the Alerta
Web UI then the ``CORS_ORIGINS`` setting needs to be updated to prevent
`modern browsers <http://enable-cors.org/client.html>`_ from blocking
the cross-origin requests.

::

    CORS_ORIGINS = [
        'http://try.alerta.io',
        'http://explorer.alerta.io',
        'chrome-extension://jplkjnjaegjgacpfafdopnpnhmobhlaf',
        'http://localhost'
    ]

.. _saml2:

SAML 2.0 Authentication
-----------------------

OAuth authentication is provided by Google_ `OpenID Connect`_, GitHub_,
GitLab_ `OAuth 2.0`_ or Keycloak_ `OAuth 2.0`_ and configuration is more involved than the Basic
Auth setup.

SAML 2.0
--------
Generate private/public key pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    openssl req -utf8 -new -x509 -days 3652 -nodes -out "alerta.cert" -keyout "alerta.key"

.. note::

    This key pair is not related to HTTPS.

Configure pysaml2
~~~~~~~~~~~~~~~~~
Bare-minimum config example::

    AUTH_PROVIDER = 'saml2'
    SAML2_CONFIG = {
        'metadata': {
            'local': ['/path/to/federationmetadata.xml']
        },
        'key_file': '/path/to/alerta.key',
        'cert_file': '/path/to/alerta.cert'
    }

..

``metadata``
    IdP metadata (refer to `saml2 documentation <https://pysaml2.readthedocs.io/en/latest/howto/config.html#metadata>`_ for possible ways of specifying it)
``key_file``, ``cert_file``
    path to aforementioned keys

Refer to pysaml2 documentation and source code if you need additional options:

- https://pysaml2.readthedocs.io/en/latest/howto/config.html
- https://github.com/rohe/pysaml2/blob/master/src/saml2/config.py

Note: entityid and service provider endpoints are configured by default based on your BASE_URL value which is mandatory if you use SAML (see :ref:`general config`)

ALLOWED_SAML2_GROUPS
~~~~~~~~~~~~~~~~~~~~

To restrict access to users who are members of particular group use::

    ALLOWED_SAML2_GROUPS = ['alerta_ro', 'alerta_rw']

.. note::

    Ensure that pysaml2 authn response identity object contains ``groups``
    attribute. You can do this by writing proper attribute map which will
    convert your IdP-specific attribute name to ``groups``.

Example::

    MAP = {
        ...
        'fro': {
            ...
            'http://schemas.xmlsoap.org/claims/group': 'groups',
            ...
        },
        'to': {
            ...
            'groups': 'http://schemas.xmlsoap.org/claims/group',
            ...
        }
    }

..

See `pysaml2 attribute-map-dir documentation <https://pysaml2.readthedocs.io/en/latest/howto/config.html#attribute-map-dir>`_. ``attribute-map-dir`` can be specified in the ``SAML2_CONFIG``, see `Configure pysaml2`_

SAML2_USER_NAME_FORMAT
~~~~~~~~~~~~~~~~~~~~~~
This is a python string template which is used to generate user's name based on attributes (make sure that `attribute-map-dir <https://pysaml2.readthedocs.io/en/latest/howto/config.html#attribute-map-dir>`_ is properly configured in case default does not fit).
Default is ``'{givenName} {surname}'``.

.. _cross_origin_saml2:

Cross-Origin
~~~~~~~~~~~~
You also need to add your IdP origin to CORS headers::

    CORS_ORIGINS = [
        ...
        'https://sso.example.com',
        ...
    ]

..

Add trusted Service Provider to your Identity Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Your metadata url is: ``{BASE_URL}/auth/saml/metadata.xml``, pass it to your IdP administrator.

.. _api keys:

API Keys
--------

If authentication is enforced, then an API key is needed to access
the alerta API programatically. An API key can also be to used by the
:ref:`alerta CLI <cli>` for when the CLI is used in scripts. See the
:ref:`example CLI config <cli config>` for how to set the API key for
the command-line tool.

Keys can be easily generated from the Alerta web UI and can have any scopes
associated with them. They are valid for 1 year by default but this period
is configurable using ``API_KEY_EXPIRE_DAYS`` in the
:ref:`server configuration <api config>`.

To use an API key in an API query you must put the key in either an
HTTP header or a query parameter.

.. important::

    Using an HTTP header is the preferred method so that API keys are
    not exposed even when using HTTPS or inadvertently captured in log
    files. 

**Example using HTTP header**

Use either the ``Authorization`` header with authorization type of ``Key``::

    $ curl 'http://api.alerta.io/alerts' -H 'Authorization: Key demo-key' -H 'Accept: application/json'

or the custom header ``X-API-Key``::

    $ curl 'http://api.alerta.io/alerts' -H 'X-API-Key: demo-key' -H 'Accept: application/json'

**Example using query paramter**

Use the ``api-key`` URL parameter::

    $ curl 'http://api.alerta.io/alerts?api-key=demo-key' -H 'Accept: application/json'

.. _user auth:

User Authorisation
------------------

Google, GitHub, GitLab and Keycloak OAuth are used for user authentication,
not user authorisation. Authentication proves that you are who you say you
are. Authorization says that you are allowed to access what you have
requested.

To control who has access to Alerta you can restrict access to users
with a :ref:`certain email domain name <allowed_email_domains>` by
setting ``ALLOWED_EMAIL_DOMAINS`` when using Google OAuth2, or who
belong to a :ref:`particular GitHub organisation <allowed_github_orgs>`
by setting ``ALLOWED_GITHUB_ORGS`` when using GitHub OAuth, or who
belong to a :ref:`particular GitLab group <allowed_gitlab_groups>`
by setting ``ALLOWED_GITLAB_GROUPS`` when using GitLab OAuth2.
belong to a :ref:`particular Keycloak role <allowed_keycloak_roles>`
by setting ``ALLOWED_KEYCLOAK_ROLES`` when using Keycloak OAuth2

For those situations where it is not possible to group users in this
way it is possible to selectively allow access on a per-user basis. How
this is done depends on whether you are using Google, GitHub, GitLab
or Keycloak as OAuth2 provider for user login.

.. _user roles:

User Roles
----------

Only allowing certain groups to login is very course. Fine-grained
access control can be acheived by using user roles and permissions.

RBAC is an authorisation model where users acquire permissions
through roles. Default roles are "admin" and "user". You create
roles  relevant to your business functions and assign permissions
as appropriate. For example, custom roles can be created for jobs
like "engineer", "devops", "sysadmin", "dba" or access types like
"read-only" and "read-write".

For more information, see :ref:`Role-Based Access Control <authorization>`.