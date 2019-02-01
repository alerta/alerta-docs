.. _configuration:

Configuration
=============

The following settings are configured on the Alerta server. For ``alerta``
CLI configuration options see :ref:`command-line reference <cli>` and for
Web UI configuration options see :ref:`web UI reference <webui>`.

The configuration file uses standard python syntax for setting variables.
The default settings (defined in :file:`settings.py`) **should not** be modified
directly.

To change any of these settings create a configuration file that overrides
these default settings. The default location for the server configuration
file is ``/etc/alertad.conf`` however the location itself can be overridden
by using a environment variable :envvar:`ALERTA_SVR_CONF_FILE`.

For example, to set the blackout period default duration to 1 day (ie. 86400
seconds)::

    $ export ALERTA_SVR_CONF_FILE=~/.alertad.conf
    $ echo "BLACKOUT_DURATION = 86400" >$ALERTA_SVR_CONF_FILE

Config File Settings
--------------------

.. _general config:

General Settings
~~~~~~~~~~~~~~~~

**Example**

.. code:: python

    DEBUG = True
    SECRET_KEY = 'changeme'
    BASE_URL = '/api'
    USE_PROXYFIX = False
    LOG_HANDLERS = ['console', 'file']
    LOG_FILE = '/var/log/alertad.log'
    LOG_MAX_BYTES = 5*1024*1024  # 5 MB
    LOG_BACKUP_COUNT = 2
    LOG_FORMAT = 'verbose'

.. index:: DEBUG, SECRET_KEY, BASE_URL, USE_PROXYFIX
.. index:: LOG_CONFIG_FILE, LOG_HANDLERS, LOG_FILE, LOG_MAX_BYTES, LOG_BACKUP_COUNT, LOG_FORMAT, LOG_METHODS

``DEBUG``
    debug mode for increased logging (default is ``False``)
``SECRET_KEY``
    a unique, randomly generated sequence of ASCII characters.
``BASE_URL``
    if API served on a path or behind a proxy use it to fix relative links (no default)
``USE_PROXYFIX``
    if API served behind SSL terminating proxy (default is ``False``)
``LOG_CONFIG_FILE``
    full path to logging configuration file in dictConfig format (no default)
``LOG_HANDLERS``
    list of log handlers eg. 'console', 'file', 'wsgi' (default is 'console')
``LOG_FILE``
    full path to write rotating server log file (no default)
``LOG_MAX_BYTES``
    maximum size of log file before rollover (default is 10 MB)
``LOG_BACKUP_COUNT``
    number of rollover files before older files are deleted (default is 2)
``LOG_FORMAT``
    log file formatter name eg. 'default', 'simple', 'verbose', 'json'
``LOG_METHODS``
    only log listed HTTP methods eg. 'GET', 'POST', 'PUT', 'DELETE' (default is all HTTP methods)

.. _api config:

API Settings
~~~~~~~~~~~~

**Example**

.. code:: python

    ALARM_MODEL='ALERTA'
    DEFAULT_FIELD = 'text'
    DEFAULT_PAGE_SIZE = 1000
    HISTORY_LIMIT = 100
    HISTORY_ON_VALUE_CHANGE = False  # do not log if only value changes

.. index:: ALARM_MODEL, DEFAULT_FIELD, DEFAULT_PAGE_SIZE, HISTORY_LIMIT, HISTORY_ON_VALUE_CHANGE

``ALARM_MODEL``
    set to ``ISA_18_2`` to use experimental alarm model (default is ``ALERTA``)
``DEFAULT_FIELD``
    search default field when no field given when using lucene query syntax (default is ``text``)
``DEFAULT_PAGE_SIZE``
    maximum number of alerts returned in a single query (default 1000)
``HISTORY_LIMIT``
    number of history entries for each alert before old entries are deleted (default 100)
``HISTORY_ON_VALUE_CHANGE``
    create history entry for duplicate alerts if value changes (default ``True``)

.. _database_config:

Database Settings
~~~~~~~~~~~~~~~~~

There is a choice of either Postgres or MongoDB as the backend database.

The database is defined using the standard database connection URL formats. Many
database configuration options are supported as connection URL parameters.

**Postgres Example**

.. code:: python

    DATABASE_URL = 'postgresql://other@localhost/otherdb?connect_timeout=10&application_name=myapp'
    DATABASE_NAME = 'monitoring'

See `Postgres connection strings`_ for more information.

.. _Postgres connection strings: https://www.postgresql.org/docs/9.6/static/libpq-connect.html

**MongoDB Example**

.. code:: python

    DATABASE_URL = 'mongodb://db1.example.net,db2.example.net:2500/?replicaSet=test&connectTimeoutMS=300000'
    DATABASE_NAME = 'monitoring'
    DATABASE_RAISE_ON_ERROR = False  # creating tables & indexes manually

See `MongoDB connection strings`_ for more information.

.. _MongoDB connection strings: https://docs.mongodb.org/v3.0/reference/connection-string/#standard-connection-string-format

.. index:: DATABASE_URL, DATABASE_NAME, DATABASE_RAISE_ON_ERROR

``DATABASE_URL``
    database connection string (default is ``mongodb://localhost:27017/monitoring``)
``DATABASE_NAME``
    database name can be used to override database in connection string (no default)
``DATABASE_RAISE_ON_ERROR``
    terminate startup if database configuration fails (default is ``True``)

.. _bulk_api_config:

Bulk API Settings
~~~~~~~~~~~~~~~~~

The bulk API requires a Celery backend and can be used to off-load
long-running tasks. (experimental)

**Example Redis Task Queue**

.. code:: python

    BULK_QUERY_LIMIT = 10000
    CELERY_BROKER_URL='redis://localhost:6379/0'
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'

.. index:: BULK_QUERY_LIMIT, CELERY_BROKER_URL, CELERY_RESULT_BACKEND

``BULK_QUERY_LIMIT``
    limit the number of tasks in a single bulk query (default is ``100000``)
``CELERY_BROKER_URL``
    URL of Celery-supported broker (no default)
``CELERY_RESULT_BACKEND``
    URL of Celery-supported result backend (no default)

.. _auth config:

Authentication Settings
~~~~~~~~~~~~~~~~~~~~~~~

If enabled, authentication provides additional benefits beyond just security,
such as auditing, and features like the ability to assign and watch alerts.

**Example**

.. code:: python

    AUTH_REQUIRED = True
    AUTH_PROVIDER = 'basic'
    ADMIN_USERS = ['admin@alerta.io', 'devops@example.com']
    USER_DEFAULT_SCOPES = ['read', 'write:alerts']
    CUSTOMER_VIEWS = True
    SIGNUP_ENABLED = False
    ALLOWED_EMAIL_DOMAINS = ['alerta.io', 'example.com']
    TOKEN_EXPIRE_DAYS = 4*365  # 4 years

    LDAP_URL = 'ldap://openldap'
    LDAP_DOMAINS = {
        'my-domain.com': 'cn=%s,dc=my-domain,dc=com'
    }

.. index:: AUTH_REQUIRED, AUTH_PROVIDER, ADMIN_USERS, USER_DEFAULT_SCOPES, CUSTOMER_VIEWS, BASIC_AUTH_REALM, SIGNUP_ENABLED
.. index:: OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET, ALLOWED_EMAIL_DOMAINS, GITHUB_URL, ALLOWED_GITHUB_ORGS, GITLAB_URL, ALLOWED_GITLAB_GROUPS, LDAP_URL, LDAP_DOMAINS
.. index:: PINGFEDERATE_URL, PINGFEDERATE_PUBKEY_LOCATION, PINGFEDERATE_TOKEN_ALGORITHM, PINGFEDERATE_OPENID_PAYLOAD_USERNAME, PINGFEDERATE_OPENID_PAYLOAD_EMAIL, PINGFEDERATE_OPENID_PAYLOAD_GROUP
.. index:: KEYCLOAK_URL, KEYCLOAK_REALM, ALLOWED_KEYCLOAK_ROLES, SAML2_CONFIG, ALLOWED_SAML2_GROUPS, SAML2_USER_NAME_FORMAT, TOKEN_EXPIRE_DAYS, API_KEY_EXPIRE_DAYS

``AUTH_REQUIRED``
    users must authenticate when using web UI or command-line tool (default ``False``)
``AUTH_PROVIDER``
    valid authentication providers are ``basic``, ``github``, ``gitlab``, ``google``, ``keycloak``, ``pingfederate``, ``saml2`` (default is ``basic``)
``ADMIN_USERS``
    email addresses or logins that have ``admin`` role
``USER_DEFAULT_SCOPES``
    default permissions assigned to logged in users (default is ``['read', 'write']``)
``CUSTOMER_VIEWS``
    alert views partitioned by customer (default is ``False``)
``BASIC_AUTH_REALM``
    BasicAuth authentication realm (default is ``Alerta``)
``SIGNUP_ENABLED``
    prevent sign-up of new users via the web UI (default is ``True``)
``OAUTH2_CLIENT_ID``
    client ID required by OAuth2 providers (no default)
``OAUTH2_CLIENT_SECRET``
    client secret required by OAuth2 providers (no default)
``ALLOWED_EMAIL_DOMAINS``
    authorised email domains when using email as login (default is ``*``)
``GITHUB_URL``
    API URL for privately run GitHub Enterprise server when using GitHub as OAuth2 provider (no default)
``ALLOWED_GITHUB_ORGS``
    authorised GitHub organisations a user must belong to when using Github as OAuth2 provider (default is ``*``)
``GITLAB_URL``
    API URL for public or privately run GitLab server when using GitLab as OAuth2 provider (default is ``https://gitlab.com``)
``ALLOWED_GITLAB_GROUPS``
    authorised GitLab groups a user must belong to when using GitLab as OAuth2 provider (default is ``*``)
``LDAP_URL``
    URL of the LDAP server (no default)
``LDAP_DOMAINS``
    dictionary of LDAP domains and LDAP search filters (no default)
``PINGFEDERATE_URL``
    PingFederate OpenID access token URL (no default)
``PINGFEDERATE_PUBKEY_LOCATION``
    PingFederate public key location (no default)
``PINGFEDERATE_TOKEN_ALGORITHM``
    PingFederate JWT token algorithm (no default)
``PINGFEDERATE_OPENID_PAYLOAD_USERNAME``
    PingFederate JWT user attribute name (no default)
``PINGFEDERATE_OPENID_PAYLOAD_EMAIL``
    PingFederate JWT email attribute name (no default)
``PINGFEDERATE_OPENID_PAYLOAD_GROUP``
    PingFederate JWT group attribute name  (no default)
``KEYCLOAK_URL``
    Keycloak website URL when using Keycloak as OAuth2 provider (no default)
``KEYCLOAK_REALM``
    Keycloak realm when using Keycloak as OAuth2 provider (no default)
``ALLOWED_KEYCLOAK_ROLES``
    list of authorised Keycloak roles a user must belong to when using
    Keycloak as OAuth2 provider (default is ``*``)
``SAML2_CONFIG``
    ``pysaml2`` configuration ``dict``. See :ref:`saml2` (no default)
``ALLOWED_SAML2_GROUPS``
    list of authorised groups a user must belong to. See :ref:`saml2` for
    details (default is ``*``)
``SAML2_USER_NAME_FORMAT``
    Python format string which will be rendered to user's name using SAML
    attributes. See :ref:`saml2` (default is ``'{givenName} {surname}'``)
``TOKEN_EXPIRE_DAYS``
    number of days a bearer token is valid (default is ``14``)
``API_KEY_EXPIRE_DAYS``
    number of days an API key is valid (default is ``365``)

.. _Audit Log config:

Audit Log Settings
~~~~~~~~~~~~~~~~~~

Audit events can be logged locally to the standard application log (which
could also help with general debugging) or forwarded to a HTTP endpoint
using a POST.

**Example**

.. code:: python

    AUDIT_TRAIL = ['admin', 'write', 'auth']
    AUDIT_LOG = True  # log to Flask application logger
    AUDIT_URL = 'https://listener.logz.io:8071/?token=TOKEN'

.. index:: AUDIT_TRAIL, AUDIT_LOG, AUDIT_URL

``AUDIT_TRAIL``
    audit trail for ``admin``, ``write`` or ``auth`` changes. (default is ``['admin']``)
``AUDIT_LOG``
    enable audit logging to configured application log file (default is ``False``)
``AUDIT_URL``
    forward audit logs to HTTP POST URL (no default)

.. _CORS config:

CORS Settings
~~~~~~~~~~~~~

**Example**

.. code:: python

    CORS_ORIGINS = [
        'http://localhost',
        'http://localhost:8000',
        r'https?://\w*\.?local\.alerta\.io:?\d*/?.*'  # => http(s)://*.local.alerta.io:<port>
    ]

.. index:: CORS_ORIGINS

``CORS_ORIGINS``
    URL origins that can access the API for Cross-Origin Resource Sharing (CORS)

.. _severity config:

Severity Settings
~~~~~~~~~~~~~~~~~

The severities and their order are customisable to fit with the environment
in which Alerta is deployed.

**Example**

.. code:: python

    SEVERITY_MAP = {
        'critical': 1,
        'warning': 4,
        'indeterminate': 5,
        'ok': 5,
        'unknown': 9
    }
    DEFAULT_NORMAL_SEVERITY = 'ok'  # 'normal', 'ok', 'cleared'
    DEFAULT_PREVIOUS_SEVERITY = 'indeterminate'

    COLOR_MAP = {
        'severity': {
            'critical': 'red',
            'warning': '#1E90FF',
            'indeterminate': 'lightblue',
            'ok': '#00CC00',
            'unknown': 'silver'
        },
        'text': 'black',
        'highlight': 'skyblue '
    }

.. index:: SEVERITY_MAP, DEFAULT_NORMAL_SEVERITY, DEFAULT_PREVIOUS_SEVERITY, COLOR_MAP

``SEVERITY_MAP``
    dictionary of severity names and levels
``DEFAULT_NORMAL_SEVERITY``
    severity to be assigned to new alerts (default is ``normal``)
``DEFAULT_PREVIOUS_SEVERITY``
    previous severity to be assigned to new alerts (default is ``indeterminate``)
``COLOR_MAP``
    dictionary of severity colors, text and highlight color

.. _timeout config:

Timeout Settings
~~~~~~~~~~~~~~~~

Alert timeouts are important for housekeeping and heartbeat timeouts
are important for generating alerts from stale heartbeats.

**Example**

.. code:: python

    ALERT_TIMEOUT = 43200  # 12 hours
    HEARTBEAT_TIMEOUT = 7200  # 2 hours

.. index:: ALERT_TIMEOUT, HEARTBEAT_TIMEOUT

``ALERT_TIMEOUT``
    default timeout period in seconds for alerts (default is ``86400``)
``HEARTBEAT_TIMEOUT``
    default timeout period in seconds for heartbeats (default is ``86400``)

.. _email config:

Email Settings
~~~~~~~~~~~~~~

If email verification is enabled then emails are sent to users when they
sign up via BasicAuth. They must click on the provided link to verify their
email address before they can login.

**Example**

.. code:: python

    EMAIL_VERIFICATION = True
    SMTP_HOST = 'smtp.example.com'
    MAIL_FROM = 'noreply@alerta.io'

.. index:: EMAIL_VERIFICATION, SMTP_HOST, SMTP_PORT, MAIL_LOCALHOST, SMTP_STARTTLS, SMTP_USE_SSL, SSL_KEY_FILE, SSL_CERT_FILE, MAIL_FROM, SMTP_USERNAME, SMTP_PASSWORD

``EMAIL_VERIFICATION``
    enforce email verification of new users (default is ``False``)
``SMTP_HOST``
    SMTP host of mail server (default is ``smtp.gmail.com``)
``SMTP_PORT``
    SMTP port of mail server (default is ``587``)
``MAIL_LOCALHOST``
    mail server to use in HELO/EHLO command (default is ``localhost``)
``SMTP_STARTTLS``
    SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands
    that follow will be encrypted (default is ``False``)
``SMTP_USE_SSL``
    used for situations where SSL is required from the beginning of the
    connection and using ``SMTP_STARTTLS`` is not appropriate (default is ``False``)
``SSL_KEY_FILE``
    a PEM formatted private key file for the SSL connection(no default)
``SSL_CERT_FILE``
    a PEM formatted certificate chain file for the SSL connection (no default)
``MAIL_FROM``
    valid email address from which emails are sent (no default)
``SMTP_USERNAME``
    application-specific username, if different to MAIL_FROM user (no default)
``SMTP_PASSWORD``
    application-specific password for ``MAIL_FROM`` or ``SMTP_USERNAME`` (no default)

.. _webui config:

Web UI Settings
~~~~~~~~~~~~~~~

The following settings are specific to the web UI and are not used by the server.

**Example**

.. code:: python

    SITE_LOGO_URL = 'http://pigment.github.io/fake-logos/logos/vector/color/fast-banana.svg'
    DATE_FORMAT_SHORT_TIME = 'HH:mm'
    DATE_FORMAT_MEDIUM_DATE = 'EEE d MMM HH:mm'
    DATE_FORMAT_LONG_DATE = 'd/M/yyyy h:mm:ss.sss a'
    DEFAULT_AUDIO_FILE = '/audio/Bike Horn.mp3'
    COLUMNS = ['severity', 'status', 'lastReceiveTime', 'duplicateCount',
            'customer', 'environment', 'service', 'resource', 'event', 'value', 'text']
    SORT_LIST_BY = 'lastReceiveTime'
    ACTIONS = ['createIssue', 'updateIssue']
    GOOGLE_TRACKING_ID = 'UA-44644195-5'
    AUTO_REFRESH_INTERVAL = 30000  # 30s

.. index:: SITE_LOGO_URL, DATE_FORMAT_SHORT_TIME, DATE_FORMAT_MEDIUM_DATE, DATE_FORMAT_LONG_DATE
.. index:: DEFAULT_AUDIO_FILE, COLUMNS, SORT_LIST_BY, ACTIONS, GOOGLE_TRACKING_ID, AUTO_REFRESH_INTERVAL

``SITE_LOGO_URL``
    URL of company logo to replace "alerta" in navigation bar (no default)
``DATE_FORMAT_SHORT_TIME``
    format used for time in columns eg. ``09:24`` (default is ``HH:mm``)
``DATE_FORMAT_MEDIUM_DATE``
    format used for dates in columns eg. ``Tue 9 Oct 09:24`` (default is ``EEE d MMM HH:mm``) 
``DATE_FORMAT_LONG_DATE``
    format used for date and time in detail views eg. ``9/10/2018 9:24:03.036 AM`` (default is ``d/M/yyyy h:mm:ss.sss a``) 
``DEFAULT_AUDIO_FILE``
    make sound when new alert arrives. must exist on client at relative path eg. ``/audio/Bike Horn.mp3`` (no default)
``COLUMNS``
  user defined columns and column order for alert list view (default is standard web console column order)
``SORT_LIST_BY``
    to sort by newest use ``lastReceiveTime`` or oldest use ``-createTime``. minus means reverse (default is ``lastReceiveTime``)
``ACTIONS``
    adds buttons to web console for operators to trigger custom actions against alert (no default)
``GOOGLE_TRACKING_ID``
    used by the web UI to send tracking data to Google Analytics (no default)
``AUTO_REFRESH_INTERVAL``
    interval in milliseconds at which the web UI refreshes alert list (default is ``5000``)

.. _plugin config:

Plugin Settings
~~~~~~~~~~~~~~~~

Plugins are used to extend the behaviour of the Alerta server without
having to modify the core application. The only plugins that are installed
and enabled by default are the ``reject`` and ``blackout`` plugins. Other
plugins are available in the `contrib repo`_.

.. _contrib repo: https://github.com/alerta/alerta-contrib/tree/master/plugins

**Example**

.. code:: python

    PLUGINS = ['reject', 'blackout', 'slack']
    PLUGINS_RAISE_ON_ERROR = False  # keep processing other plugins if exception

.. index:: PLUGINS, PLUGINS_RAISE_ON_ERROR

``PLUGINS``
    list of enabled plugins (default ``['reject', 'blackout']``)
``PLUGINS_RAISE_ON_ERROR``
    stop processing plugins if there is an exception (default is ``True``)

**Reject Plugin Settings**

Alerts can be rejected based on the ``origin`` or ``environment`` alert attributes. 

**Example**

.. code:: python

    ORIGIN_BLACKLIST = ['foo/bar$', '.*/qux']  # reject all foo alerts from bar, and everything from qux
    ALLOWED_ENVIRONMENTS = ['Production', 'Development', 'Testing']

.. index:: ORIGIN_BLACKLIST, ALLOWED_ENVIRONMENTS

``ORIGIN_BLACKLIST``
    list of alert origins blacklisted from submitting alerts. useful for rouge alert sources (no default)
``ALLOWED_ENVIRONMENTS``
    list of allowed environments. useful for enforcing discrete set of environments (default is ``['Production', 'Development']``)

.. note:: To disable the ``reject`` plugin simply remove it from the
    list of enabled plugins in the ``PLUGINS`` configuration setting
    to override the default.

**Blackout Plugin Settings**

Alerts can be suppressed based on alert attributes for arbitrary durations
known as "blackout periods". An alert received during a blackout period is
rejected, by default.

**Example**

.. code:: python

    BLACKOUT_DURATION = 7200  # 2 hours
    NOTIFICATION_BLACKOUT = True
    BLACKOUT_ACCEPT = ['normal', 'ok', 'cleared']

.. index:: BLACKOUT_DURATION, NOTIFICATION_BLACKOUT, BLACKOUT_ACCEPT

``BLACKOUT_DURATION``
    default period for an alert blackout (default is ``3600``)
``NOTIFICATION_BLACKOUT``
    instead of rejecting alerts received during blackout periods, set ``status``
    of alert to ``blackout`` and do not forward to plugins (default is ``False``)
``BLACKOUT_ACCEPT``
    used with ``NOTIFICATION_BLACKOUT`` if alerts with ``status`` of ``blackout``
    should still be closed by "ok" alerts (no default)

Environment Variables
---------------------

Some configuration settings are special because they can be overridden by
environment variables. This is to make deployment to different platforms
and managed environments such as Heroku, Kubernetes and AWS easier, or to
make use of managed Postgres or MongoDB services.

.. note:: Environment variables are read after configuration files so they
    will always override any other setting.

General Settings
~~~~~~~~~~~~~~~~

:envvar:`DEBUG`
    :ref:`see above <general config>`
:envvar:`BASE_URL`
    :ref:`see above <general config>`
:envvar:`USE_PROXYFIX`
    :ref:`see above <general config>`
:envvar:`SECRET_KEY`
    :ref:`see above <general config>`
:envvar:`AUTH_REQUIRED`
    :ref:`see above <auth config>`
:envvar:`AUTH_PROVIDER`
    :ref:`see above <auth config>`
:envvar:`ADMIN_USERS`
    :ref:`see above <auth config>`
:envvar:`CUSTOMER_VIEWS`
    :ref:`see above <auth config>`
:envvar:`OAUTH2_CLIENT_ID`
    :ref:`see above <auth config>`
:envvar:`OAUTH2_CLIENT_SECRET`
    :ref:`see above <auth config>`
:envvar:`ALLOWED_EMAIL_DOMAINS`
    :ref:`see above <auth config>`
:envvar:`GITHUB_URL`
    :ref:`see above <auth config>`
:envvar:`ALLOWED_GITHUB_ORGS`
    :ref:`see above <auth config>`
:envvar:`GITLAB_URL`
    :ref:`see above <auth config>`
:envvar:`ALLOWED_GITLAB_GROUPS`
    :ref:`see above <auth config>`
:envvar:`KEYCLOAK_URL`
    :ref:`see above <auth config>`
:envvar:`KEYCLOAK_REALM`
    :ref:`see above <auth config>`
:envvar:`ALLOWED_KEYCLOAK_ROLES`
    :ref:`see above <auth config>`
:envvar:`PINGFEDERATE_OPENID_ACCESS_TOKEN_URL`
    :ref:`see above <auth config>`
:envvar:`PINGFEDERATE_OPENID_PAYLOAD_USERNAME`
    :ref:`see above <auth config>`
:envvar:`PINGFEDERATE_OPENID_PAYLOAD_EMAIL`
    :ref:`see above <auth config>`
:envvar:`PINGFEDERATE_OPENID_PAYLOAD_GROUP`
    :ref:`see above <auth config>`
:envvar:`PINGFEDERATE_PUBKEY_LOCATION`
    :ref:`see above <auth config>`
:envvar:`PINGFEDERATE_TOKEN_ALGORITHM`
    :ref:`see above <auth config>`
:envvar:`CORS_ORIGINS`
    :ref:`see above <cors config>`
:envvar:`MAIL_FROM`
    :ref:`see above <email config>`
:envvar:`SMTP_PASSWORD`
    :ref:`see above <email config>`
:envvar:`GOOGLE_TRACKING_ID`
    :ref:`see above <webui config>`
:envvar:`PLUGINS`
    :ref:`see above <plugin config>`

Database Settings
~~~~~~~~~~~~~~~~~

:envvar:`DATABASE_URL`
    used by both :ref:`Postgres <Postgres connection strings>` and
    :ref:`MongoDB <MongoDB connection strings>` for database connection strings
:envvar:`DATABASE_NAME`
    database name can be used to override default database defined in ``DATABASE_URL``

MongoDB Settings
~~~~~~~~~~~~~~~~

.. deprecated:: 5.0
    Use :envvar:`DATABASE_URL` and :envvar:`DATABASE_NAME` instead.

:envvar:`MONGO_URI`
    used to override ``MONGO_URI`` config variable using the standard connection string format
:envvar:`MONGODB_URI`
    alternative name for ``MONGO_URI`` environment variable which is used by some managed services
:envvar:`MONGOHQ_URL`
    automatically set when using `Heroku MongoHQ`_ managed service
:envvar:`MONGOLAB_URI`
    automatically set when using `Heroku MongoLab`_ managed service
:envvar:`MONGO_PORT`
    automatically set when deploying `Alerta to a Docker`_ linked mongo container

.. _Heroku MongoHQ: https://devcenter.heroku.com/articles/mongohq
.. _Heroku MongoLab: https://devcenter.heroku.com/articles/mongolab
.. _Alerta to a Docker: https://github.com/alerta/docker-alerta

Dynamic Settings
----------------

Using the :ref:`management switchboard <metrics>` on the API some dynamic
settings can be switched on and off without restarting the Alerta server
daemon.

Currently, there is only one setting that can be toggled in this way and
it is the Auto-refresh allow switch.

Auto-Refresh Allow
~~~~~~~~~~~~~~~~~~

The Alerta Web UI will automatically referesh the list of alerts in the alert
console every 5 seconds.

If for whatever reason, the Alerta API is experiencing heavy load the
``auto_refresh_allow`` switch can be turned off and the Web UI will respect
that and switch to manual refresh mode. The Alerta web UI will start
auto-refereshing again if the ``auto_refresh_allow`` switch is turned back on.
