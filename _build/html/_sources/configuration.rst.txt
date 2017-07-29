.. _configuration:

Configuration
=============

The following settings **only** apply to the Alerta server. For ``alerta``
CLI configuration options see :ref:`command-line reference <cli>` and for
Web UI configuration options see :ref:`web UI reference <webui>`.

The configuration file uses standard python syntax for setting variables.
The default settings (defined in `settings.py`) **should not** be modified
directly. To change any of these settings create a configuration file that
overrides these default settings. The default location for the server
configuration file is ``/etc/alertad.conf`` however the location itself
can be overridden by using a environment variable :envvar:`ALERTA_SVR_CONF_FILE`.

For example, to set the blackout period default duration to 1 day (ie. 86400
seconds)::

    $ export ALERTA_SVR_CONF_FILE=~/.alertad.conf
    $ echo "BLACKOUT_DURATION = 86400" >$ALERTA_SVR_CONF_FILE

Config File Settings
--------------------

.. _general config:

General Settings
~~~~~~~~~~~~~~~~
.. code:: python

    DEBUG = False
    BASE_URL = ''
    LOGGER_NAME = 'alerta'
    LOG_FILE = None

.. index:: DEBUG, LOGGER_NAME, LOG_FILE

``DEBUG``
    debug mode. Set to ``True`` for increased logging.
``BASE_URL``
    if API served behind a proxy use ``BASE_URL`` to fix relative links
``LOGGER_NAME``
    name of logger used by python ``logging`` module
``LOG_FILE``
    full path to write rotating server log file

.. _api config:

API Settings
~~~~~~~~~~~~
::

    QUERY_LIMIT = 10000
    HISTORY_LIMIT = 100
    API_KEY_EXPIRE_DAYS = 365

.. index:: QUERY_LIMIT, HISTORY_LIMIT, API_KEY_EXPIRE_DAYS

``QUERY_LIMIT``
    maximum number of alerts returned in a single query.
``HISTORY_LIMIT``
    number of history entries returned in alert details.
``API_KEY_EXPIRE_DAYS``
    number of days an API key is valid for.

.. _mongo_config:

MongoDB Settings
~~~~~~~~~~~~~~~~

The document-oriented datastore MongoDB_ is used for persistent data. It
can be set-up as a stand-alone server or in a `replica set`_ for high
availability.

.. _MongoDB: https://www.mongodb.com
.. _replica set: http://docs.mongodb.org/manual/core/replica-set-high-availability/

::

    MONGO_URI = 'mongodb://localhost:27017/monitoring'
    MONGO_DATABASE = 'monitoring'

.. index:: MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_REPLSET, MONGO_USERNAME, MONGO_PASSWORD

``MONGO_URI``
    MongoDB connection URI string.
``MONGO_DATABASE``
    database name can be used to override default database defined in ``MONGO_URI``.

The MongoDB configuration can be overridden in a number of different ways to
ensure that Alerta can be easily deployed in many different environments.

For information about deploying Alerta using a MongoDB replica set refer to
the :ref:`high availability <high availability>` recommendations for a
production deployment.

.. _auth config:

Authentication Settings
~~~~~~~~~~~~~~~~~~~~~~~

If enabled, authentication provides additional benefits beyond just security,
such as auditing, and features like the ability to assign and watch alerts.

::

    SECRET_KEY = 'changeme'
    AUTH_REQUIRED = False

    ADMIN_USERS = []
    CUSTOMER_VIEWS = False

    OAUTH2_CLIENT_ID = None  # Google or GitHub OAuth2 client ID and secret
    OAUTH2_CLIENT_SECRET = None
    ALLOWED_EMAIL_DOMAINS = ['*']

    GITHUB_URL = None
    ALLOWED_GITHUB_ORGS = ['*']

    GITLAB_URL = None
    ALLOWED_GITLAB_GROUPS = ['*']

    KEYCLOAK_URL = None
    KEYCLOAK_REALM = None
    ALLOWED_KEYCLOAK_ROLES = ['*']

    TOKEN_EXPIRE_DAYS = 14

.. index:: AUTH_REQUIRED, SECRET_KEY, ADMIN_USERS, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET, ALLOWED_EMAIL_DOMAINS, ALLOWED_GITHUB_ORGS, GITLAB_URL, ALLOWED_GITLAB_GROUPS, KEYCLOAK_URL, KEYCLOAK_REALM, ALLOWED_KEYCLOAK_ROLES

``SECRET_KEY``
    a unique, randomly generated sequence of ASCII characters.
``AUTH_REQUIRED``
    set to ``True`` to force users to authenticate when using web UI or command-line tool
``ADMIN_USERS``
    list of user email addresses or accounts that should be given admin rights.
``CUSTOMER_VIEWS``
    enable alert views partitioned by customer
``OAUTH2_CLIENT_ID``
    client ID required by OAuth2 provider for Google, Github, GitLab or Keycloak.
``OAUTH2_CLIENT_SECRET``
    client secret required by OAuth2 provider for Google, Github, GitLab or Keycloak.
``ALLOWED_EMAIL_DOMAINS``
    list of authorised email domains when using Google as OAuth2 provider.
``GITHUB_URL``
    GitHub Enteprise URL for privately run GitHub server when using GitHub as OAuth2 provider.
``ALLOWED_GITHUB_ORGS``
    list of authorised GitHub organisations a user must belong to when using Github as OAuth2 provider.
``GITLAB_URL``
    GitLab website URL for public or privately run GitLab server when using GitLab as OAuth2 provider.
``ALLOWED_GITLAB_GROUPS``
    list of authorised GitLab groups a user must belong to when using GitLab as OAuth2 provider.
``KEYCLOAK_URL``
    Keycloak website URL when using Keycloak as OAuth2 provider.
``KEYCLOAK_REALM``
    Keycloak realm when using Keycloak as OAuth2 provider.
``ALLOWED_KEYCLOAK_ROLES``
    list of authorised Keycloak roles a user must belong to when using Keycloak as OAuth2 provider.

.. _switch config:

Switch Settings
~~~~~~~~~~~~~~~

Server-side switches used to control and limit access to the API by clients
for reasons related to security, performance or availability.

::

    AUTO_REFRESH_ALLOW = 'ON'
    SENDER_API_ALLOW = 'ON'

.. index:: AUTO_REFRESH_ALLOW, SENDER_API_ALLOW

``AUTO_REFRESH_ALLOW``
    set to 'OFF' to reduce load on API server by forcing clients to manually refresh
``SENDER_API_ALLOW``
    set to 'OFF' to block clients from sending new alerts to API server

.. _CORS config:

CORS Settings
~~~~~~~~~~~~~

::

    CORS_ORIGINS = [
        'http://try.alerta.io',
        'http://explorer.alerta.io',
        'http://localhost'
    ]

.. index:: CORS_ORIGINS

``CORS_ORIGINS``
    list of URL origins that can access the API

.. _severity config:

Severity Settings
~~~~~~~~~~~~~~~~~

The severities and their order are customisable to fit with the environment
in which Alerta is deployed.

::

    SEVERITY_MAP = {
        'security': 0,
        'critical': 1,
        'major': 2,
        'minor': 3,
        'warning': 4,
        'indeterminate': 5,
        'cleared': 5,
        'normal': 5,
        'ok': 5,
        'informational': 6,
        'debug': 7,
        'trace': 8,
        'unknown': 9
    }
    DEFAULT_SEVERITY = 'indeterminate'

.. index:: SEVERITY_MAP, DEFAULT_SEVERITY

``SEVERITY_MAP``
    severity names and levels are fully customisable.
``DEFAULT_SEVERITY``
    the previous severity assigned to new alerts.

.. _blackout config:

Blackout Periods Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

Alerts can be suppressed based on alert attributes for arbitrary durations
known as "blackout periods".

::

    BLACKOUT_DURATION = 3600

.. index:: BLACKOUT_DURATION

``BLACKOUT_DURATION``
    default period for an alert blackout

.. _email config:

Email Settings
~~~~~~~~~~~~~~

If email verification is enabled then emails are sent to users when they
sign up via BasicAuth. They must click on the provided link to verify their
email address before they can login.

::

    EMAIL_VERIFICATION = False
    SMTP_HOST = 'smtp.gmail.com'
    SMTP_PORT = 587
    MAIL_FROM = 'your@gmail.com'
    SMTP_PASSWORD = ''

.. index:: EMAIL_VERIFICATION, SMTP_HOST, SMTP_PORT, MAIL_FROM, SMTP_PASSWORD

``EMAIL_VERIFICATION``
    set to ``True`` to enable email verification of new users.
``SMTP_HOST``
    SMTP host of mail server.
``SMTP_PORT``
    SMTP port of mail server.
``MAIL_FROM``
    valid email address from which verification emails are sent.
``SMTP_PASSWORD``
    password for ``MAIL_FROM`` email account, Gmail uses application-specific passwords

.. _plugin config:

Plugin Settings
~~~~~~~~~~~~~~~~

Plugins are used to extend the behaviour of the Alerta server without
having to modify the core application. The only plugin that is installed
and enabled by default is the ``reject`` plugin. Other plugins are available
in the `contrib repo`_.

.. _contrib repo: https://github.com/alerta/alerta-contrib/tree/master/plugins

::

    # Plugins
    PLUGINS = ['reject']

    ORIGIN_BLACKLIST = ['foo/bar$', '.*/qux']  # reject all foo alerts from bar, and everything from qux
    ALLOWED_ENVIRONMENTS = ['Production', 'Development']  # reject alerts without allowed environments

``PLUGINS``
    list of enabled plugins
``ORIGIN_BLACKLIST``
    ``reject`` plugin list of alert origins blacklisted from submitting alerts. useful for rouge alert sources.
``ALLOWED_ENVIRONMENTS``
    ``reject`` plugin list of allowed environments. useful for enforcing discrete set of environments.

.. note:: To completely disable the ``reject`` plugin simply remove it
    from the list of enabled plugins in the ``PLUGINS`` configuration
    setting to override the default.

Environment Variables
---------------------

Some configuration settings are special because they can be overridden by
environment variables. This is to make deployment to different platforms
and managed environments easier. eg. RedHat OpenShift, Heroku, Packer, Docker,
and AWS or to make use of managed MongoDB services. Note that not all would
need to be used to deploy to each different environment.

.. note:: Environment variables are read after configuration files so they
    will always override any other setting.

General Settings
~~~~~~~~~~~~~~~~

:envvar:`DEBUG`
    see above
:envvar:`BASE_URL`
    see above
:envvar:`SECRET_KEY`
    see above
:envvar:`AUTH_REQUIRED`
    see above
:envvar:`ADMIN_USERS`
    see above
:envvar:`CUSTOMER_VIEWS`
    see above
:envvar:`OAUTH2_CLIENT_ID`
    see above
:envvar:`OAUTH2_CLIENT_SECRET`
    see above
:envvar:`ALLOWED_EMAIL_DOMAINS`
    see above
:envvar:`GITHUB_URL`
  see above
:envvar:`ALLOWED_GITHUB_ORGS`
    see above
:envvar:`GITLAB_URL`
    see above
:envvar:`ALLOWED_GITLAB_GROUPS`
    see above
:envvar:`CORS_ORIGINS`
    see above
:envvar:`MAIL_FROM`
    see above
:envvar:`SMTP_PASSWORD`
    see above
:envvar:`PLUGINS`
    see above

MongoDB Settings
~~~~~~~~~~~~~~~~

:envvar:`MONGO_URI`
    used to override ``MONGO_URI`` config variable using the standard `connection string format`_
:envvar:`MONGODB_URI`
    alternative name for ``MONGO_URI`` environment variable which is used by some managed services
:envvar:`MONGOHQ_URL`
    automatically set when using `Heroku MongoHQ`_ managed service
:envvar:`MONGOLAB_URI`
    automatically set when using `Heroku MongoLab`_ managed service
:envvar:`MONGO_PORT`
    automatically set when deploying `Alerta to a Docker`_ linked mongo container

.. _connection string format: https://docs.mongodb.org/v3.0/reference/connection-string/#standard-connection-string-format
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
