

Deployment
----------

run as WSGI app, not a background process

only ever run `alertad` like you are now during development. Alerta is designed to run as a WSGI application behind Apache or nginx and that's the only way I've ever run it in production environments.

There are quite a few examples of how to run it as a WSGI app behind a web server (or using gunicorn) [here](https://github.com/alerta/vagrant-try-alerta/blob/master/scripts/alerta.sh), [here](https://github.com/alerta/alerta-cfn/blob/master/Alerta_Single_Instance.template), [here](https://github.com/alerta/openshift-api-alerta/blob/master/wsgi.py), and [here](https://github.com/alerta/docker-alerta/blob/master/supervisord.conf)

.. _reverse proxy:

serve web UI from same domain as API, if possible to avoid potential CORS errors

(example apache and nginx and gunicorn configs)

choose an auth provider

decide whether to use HTTPS or not

if multiple web servers ensure same SECRET_KEY is used

multiple instances backed by mongo replica set


choose plugins, enable/disable core, install contrib and enable

::

    DEBUG = False
    SECRET_KEY = ...

Configure WSGI App
~~~~~~~~~~~~~~~~~~

http://flask.pocoo.org/docs/0.10/deploying/#deployment


don't run in foreground
Web server


example configs
nginx -> https://github.com/alerta/docker-alerta/blob/master/nginx.conf

CORS if not same origin

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




Vagrant

Heroku

OpenShift

AWS

Docker

Packer
