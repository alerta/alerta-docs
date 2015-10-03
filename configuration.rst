Configuration
=============

The following settings **only** apply to the Alerta server. For ``alerta`` CLI configuration options see :ref:`command-line reference <cli>`.

The default settings **should not** be modified directly. To change any of these settings create a configuration file that overrides these default settings. The default location for the server configuration file is ``/etc/alertad.conf`` however the location itself can be overridden by using a environment variable :envvar:`ALERTA_SVR_CONF_FILE`.

For example, to set the blackout period default duration to 1 day (ie. 86400 seconds)::

    $ export ALERTA_SVR_CONF_FILE=~/.alertad.conf
    $ echo "BLACKOUT_DURATION = 86400" >$ALERTA_SVR_CONF_FILE

File Settings
-------------

.. _general config:

General Settings
~~~~~~~~~~~~~~~~
::

    DEBUG = False

    SECRET_KEY = r'0Afk\(,8$cr(Y8:MA""knd>[@$U[G.eQL6DjAmVs'

.. _api config:

API Settings
~~~~~~~~~~~~
::

    QUERY_LIMIT = 10000  # maximum number of alerts returned by a single query
    HISTORY_LIMIT = 100  #
    API_KEY_EXPIRE_DAYS = 365  # 1 year

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

The MongoDB configuration can be overridden in a number of different ways to ensure that Alerta can be easily deployed in many different environments.

For information about deploying Alerta using a MongoDB replica set see the examples in :ref:`production deployment <deploy replicaset>`.

.. _auth config:

Authentication Settings
~~~~~~~~~~~~~~~~~~~~~~~

::

    AUTH_REQUIRED = False
    OAUTH2_CLIENT_ID = 'INSERT-OAUTH2-CLIENT-ID-HERE'  # Google or GitHub OAuth2 client ID and secret
    OAUTH2_CLIENT_SECRET = 'INSERT-OAUTH2-CLIENT-SECRET-HERE'
    ALLOWED_EMAIL_DOMAINS = ['gmail.com']
    ALLOWED_GITHUB_ORGS = ['guardian']

.. _CORS config:

CORS Settings
~~~~~~~~~~~~~

::

    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization', 'Access-Control-Allow-Origin']
    CORS_ORIGINS = [
        'http://try.alerta.io',
        'http://explorer.alerta.io',
        'chrome-extension://jplkjnjaegjgacpfafdopnpnhmobhlaf',
        'http://localhost'
    ]
    CORS_SUPPORTS_CREDENTIALS = AUTH_REQUIRED


.. _blackout config:

Blackout Periods Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    BLACKOUT_DURATION = 3600  # default period = 1 hour

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

Environment Variables
---------------------

Some configuration settings are special because they can be overridden by environment variables. This is to make deployment to different platforms and managed environments easier. eg. RedHat OpenShift, Heroku, Packer, Docker, and AWS or to make use of managed MongoDB services. Note that not all would need to be used to deploy to each different environment.

.. note:: Environment variables are read after configuration files so they will always override any other setting.

General Settings
~~~~~~~~~~~~~~~~
::

    SECRET_KEY
    OAUTH2_CLIENT_ID
    OAUTH2_CLIENT_SECRET
    ALLOWED_EMAIL_DOMAINS
    ALLOWED_GITHUB_ORGS
    CORS_ORIGINS

MongoDB Settings
~~~~~~~~~~~~~~~~
::

    MONGO_URI
    MONGOHQ_URL
    MONGOLAB_URI
    MONGO_PORT

Dynamic Settings
----------------

Using the management switchboard dynamic settings can be switched on and off without restarting the Alerta server daemon.

http://api.alerta.io/management/switchboard

switch.auto_refresh_allow


