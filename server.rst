.. _server:

Server
======

The ``alertad`` server receives alerts from multiple sources, :ref:`correlates <correlation>` and :ref:`de-duplicates  <deduplication>` them, and makes the alerts available via a JSON API.

Alerts can be intercepted as they are received to modify, enhance or reject them using :ref:`pre-receive hooks <pre_receive>`. Alerts can also be used to trigger actions in other systems after the alert has been processed using :ref:`post-receive hooks <post_receive>`.

There are several integrations with popular monitoring tools available and webhooks can be used to trivially integrate with Pingdom and AWS Cloudwatch.


Alert Database
--------------

The document-oriented datastore MongoDB_ is used as the backend for Alerta to store alerts, heartbeats, API keys and the :ref:`user exception list <user_exception_list>`. It can be used as a stand-alone server or in a replicaset for high availability.

.. _MongoDB: https://www.mongodb.com

MongoDB Settings
~~~~~~~~~~~~~~~~

::

    # MongoDB
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DATABASE = 'monitoring'

    MONGO_USERNAME = 'alerta'
    MONGO_PASSWORD = None

MongoDB Replica Set Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

:file:/etc/mongod.conf

::

    replSetName=alerta
::

    > rs.initiate()
    > rs.add("mongodb1.example.net")
    > rs.add("mongodb1.example.net")


.. _MongoDB_Replica: http://docs.mongodb.org/manual/tutorial/deploy-replica-set/

::

    MONGO_REPLSET = None  # 'alerta'


.. _event_processing:

Event Processing
----------------

.. _deduplication:

De-duplication
~~~~~~~~~~~~~~

.. _correlation:

Simple Correlation
~~~~~~~~~~~~~~~~~~

.. _plugins:

Plug-ins
--------

.. _pre_receive:

Pre-Receive Hooks
~~~~~~~~~~~~~~~~~

.. _post_receive:

Post Receive Hooks
~~~~~~~~~~~~~~~~~~

Query


Settings
--------

::

    #
    # ***** ALERTA SERVER DEFAULT SETTINGS -- DO NOT MODIFY THIS FILE *****
    #
    # To override these settings use /etc/alertad.conf or the contents of the
    # configuration file set by the environment variable ALERTA_SVR_CONF_FILE.

    DEBUG = False

    SECRET_KEY = r'0Afk\(,8$cr(Y8:MA""knd>[@$U[G.eQL6DjAmVs'

    QUERY_LIMIT = 10000  # maximum number of alerts returned by a single query
    HISTORY_LIMIT = 100  #


    AUTH_REQUIRED = False
    OAUTH2_CLIENT_ID = 'INSERT-OAUTH2-CLIENT-ID-HERE'  # Google or GitHub OAuth2 client ID and secret
    OAUTH2_CLIENT_SECRET = 'INSERT-OAUTH2-CLIENT-SECRET-HERE'
    ALLOWED_EMAIL_DOMAINS = ['gmail.com']
    ALLOWED_GITHUB_ORGS = ['guardian']
    API_KEY_EXPIRE_DAYS = 365  # 1 year

    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization', 'Access-Control-Allow-Origin']
    CORS_ORIGINS = [
        'http://try.alerta.io',
        'http://explorer.alerta.io',
        'chrome-extension://jplkjnjaegjgacpfafdopnpnhmobhlaf',
        'http://localhost'
    ]
    CORS_SUPPORTS_CREDENTIALS = AUTH_REQUIRED

    # Plug-ins
    PLUGINS = ['reject', 'amqp']
    # PLUGINS = ['amqp', 'enhance', 'logstash', 'normalise', 'reject', 'sns']

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


Dynamic Settings
----------------
switch.auto_refresh_allow


Production
----------

don't run in foreground
Web server


example configs
nginx -> https://github.com/alerta/docker-alerta/blob/master/nginx.conf

CORS if not same origin

Configure WSGI App
------------------

http://flask.pocoo.org/docs/0.10/deploying/#deployment

Configure Authentication
------------------------

- login
- add any special users
- create API keys

Configure a Plug-in
-------------------


Configure an Integration
------------------------


Deployment
----------

Heroku

OpenShift

AWS

Docker

Packer
