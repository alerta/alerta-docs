Configuration
=============

The following settings **only** apply to the Alerta server. For ``alerta`` CLI configuration options see :ref:`command-line reference <cli>` and for Web UI configuration options see :ref:`web UI reference <webui>`.

The default settings **should not** be modified directly. To change any of these settings create a configuration file that overrides these default settings. The default location for the server configuration file is ``/etc/alertad.conf`` however the location itself can be overridden by using a environment variable :envvar:`ALERTA_SVR_CONF_FILE`.

For example, to set the blackout period default duration to 1 day (ie. 86400 seconds)::

    $ export ALERTA_SVR_CONF_FILE=~/.alertad.conf
    $ echo "BLACKOUT_DURATION = 86400" >$ALERTA_SVR_CONF_FILE

Config File Settings
--------------------

.. _general config:

General Settings
~~~~~~~~~~~~~~~~
.. code:: python

    DEBUG = False
    SECRET_KEY = r'0Afk\(,8$cr(Y8:MA""knd>[@$U[G.eQL6DjAmVs'

.. index:: DEBUG, SECRET_KEY

``DEBUG``
    debug mode. Set to ``True`` for increased logging.
``SECRET_KEY``
    a unique, randomly generated sequence of ASCII characters.

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

The document-oriented datastore MongoDB_ is used for persistent data. It can be set-up as a stand-alone server or in a `replica set`_ for high availability.

.. _MongoDB: https://www.mongodb.com
.. _replica set: http://docs.mongodb.org/manual/core/replica-set-high-availability/

::

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DATABASE = 'monitoring'
    MONGO_REPLSET = None  # 'alerta'

    MONGO_USERNAME = 'alerta'
    MONGO_PASSWORD = None

.. index:: MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_REPLSET, MONGO_USERNAME, MONGO_PASSWORD

``MONGO_HOST``
    hostname of the database.
``MONGO_PORT``
    TCP port the database is listening on.
``MONGO_DATABASE``
    database name.
``MONGO_REPLSET``
    replica set name.
``MONGO_USERNAME``
    username.
``MONGO_PASSWORD``
    password.

The MongoDB configuration can be overridden in a number of different ways to ensure that Alerta can be easily deployed in many different environments.

For information about deploying Alerta using a MongoDB replica set refer to the :ref:`high availability <high availability>` recommendations for a production deployment.

.. _auth config:

Authentication Settings
~~~~~~~~~~~~~~~~~~~~~~~

::

    AUTH_REQUIRED = False
    OAUTH2_CLIENT_ID = 'INSERT-OAUTH2-CLIENT-ID-HERE'  # Google, GitHub, GitLab or Twitter OAuth2 client ID and secret
    OAUTH2_CLIENT_SECRET = 'INSERT-OAUTH2-CLIENT-SECRET-HERE'
    ALLOWED_EMAIL_DOMAINS = ['gmail.com']
    ALLOWED_GITHUB_ORGS = ['guardian']
    ALLOWED_GITLAB_GROUPS = ['acmecorp']

.. index:: AUTH_REQUIRED, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET, ALLOWED_EMAIL_DOMAINS, ALLOWED_GITHUB_ORGS, GITLAB_URL, ALLOWED_GITLAB_GROUPS

``AUTH_REQUIRED``
    set to ``True`` to force users to authenticate when using web UI or command-line tool
``OAUTH2_CLIENT_ID``
    client ID required by OAuth2 provider for Google, Github, GitLab or Twitter.
``OAUTH2_CLIENT_SECRET``
    client secret required by OAuth2 provider for Google, Github, GitLab or Twitter.
``ALLOWED_EMAIL_DOMAINS``
    list of authorised email domains when using Google as OAuth2 provider.
``ALLOWED_GITHUB_ORGS``
    list of authorised GitHub organisations a user must belong to when using Github as OAuth2 provider.
``GITLAB_URL``
    GitLab website URL for public or privately run GitLab server when using GitLab as OAuth2 provider.
``ALLOWED_GITLAB_GROUPS``
    list of authorised GitLab groups a user must belong to when using GitLab as OAuth2 provider.

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

.. _blackout config:

Blackout Periods Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    BLACKOUT_DURATION = 3600

.. index:: BLACKOUT_DURATION

``BLACKOUT_DURATION``
    default period for an alert blackout

.. _plugin config:

Plug-in Settings
~~~~~~~~~~~~~~~~

::

    # Plug-ins
    PLUGINS = ['reject']
    # PLUGINS = ['amqp', 'enhance', 'logstash', 'normalise', 'reject', 'sns']

    ORIGIN_BLACKLIST = ['foo/bar$', '.*/qux']  # reject all foo alerts from bar, and everything from qux
    ALLOWED_ENVIRONMENTS = ['Production', 'Development']  # reject alerts without allowed environments

    # AMQP Credentials
    AMQP_URL = 'mongodb://localhost:27017/kombu'        # MongoDB
    # AMQP_URL = 'amqp://guest:guest@localhost:5672//'  # RabbitMQ
    # AMQP_URL = 'redis://localhost:6379/'              # Redis

    # AWS Credentials
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_REGION = 'eu-west-1'

    # Inbound
    AMQP_QUEUE = 'alerts'
    AWS_SQS_QUEUE = 'alerts'

    # Outbound
    AMQP_TOPIC = 'notify'
    AWS_SNS_TOPIC = 'notify'

    # Logstash
    LOGSTASH_HOST = 'localhost'
    LOGSTASH_PORT = 6379

``PLUGINS``
    list of enabled plugins
``ORIGIN_BLACKLIST``
    ``reject`` plugin list of alert origins blacklisted from submitting alerts. useful for rouge alert sources.
``ALLOWED_ENVIRONMENTS``
    ``reject`` plugin list of allowed environments. useful for enforcing discrete set of environments.

Environment Variables
---------------------

Some configuration settings are special because they can be overridden by environment variables. This is to make deployment to different platforms and managed environments easier. eg. RedHat OpenShift, Heroku, Packer, Docker, and AWS or to make use of managed MongoDB services. Note that not all would need to be used to deploy to each different environment.

.. note:: Environment variables are read after configuration files so they will always override any other setting.

General Settings
~~~~~~~~~~~~~~~~

:envvar:`SECRET_KEY`
    see above
:envvar:`OAUTH2_CLIENT_ID`
    see above
:envvar:`OAUTH2_CLIENT_SECRET`
    see above
:envvar:`ALLOWED_EMAIL_DOMAINS`
    see above
:envvar:`ALLOWED_GITHUB_ORGS`
    see above
:envvar:`GITLAB_URL`
    see above
:envvar:`ALLOWED_GITLAB_GROUPS`
    see above
:envvar:`CORS_ORIGINS`
    see above

MongoDB Settings
~~~~~~~~~~~~~~~~

:envvar:`MONGO_URI`
    override all of the MongoDB config file settings using the standard `connection string format`_
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

Using the :ref:`management switchboard <metrics>` on the API some dynamic settings can be switched on and off without restarting the Alerta server daemon.

Currently, there is only one setting that can be toggled in this way and it is the Auto-refresh allow switch.

Auto-Refresh Allow
~~~~~~~~~~~~~~~~~~

The Alerta Web UI will automatically referesh the list of alerts in the alert console every 5 seconds.

If for whatever reason, the Alerta API is experiencing heavy load the ``auto_refresh_allow`` switch can be turned off and the Web UI will respect that and switch to manual refresh mode. The Alerta web UI will start auto-refereshing again if the ``auto_refresh_allow`` switch is turned back on.
