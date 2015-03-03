.. _server:

Server
======

Correlation
-----------

De-duplication
~~~~~~~~~~~~~~

Simple Correlation
~~~~~~~~~~~~~~~~~~

Plug-ins
--------

pre-receive, post-receive hooks

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

    # MongoDB
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DATABASE = 'monitoring'
    MONGO_REPLSET = None  # 'alerta'

    MONGO_USERNAME = 'alerta'
    MONGO_PASSWORD = None

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
