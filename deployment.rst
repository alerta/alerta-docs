.. _deployment:

Deployment
==========

WSGI Server
-----------

There are many ways to deploy Alerta. It can be run as ``alertad`` during development or testing but when run in a production environment, it should `always be deployed`_ as a WSGI application. See the list of `real world`_ examples below.

.. _always be deployed: http://flask.pocoo.org/docs/0.10/deploying/#deployment
.. _WSGI: http://www.fullstackpython.com/wsgi-servers.html

.. _one: https://github.com/alerta/vagrant-try-alerta/blob/master/scripts/alerta.sh
.. _two: https://github.com/alerta/openshift-api-alerta/blob/master/wsgi.py
.. _three: https://github.com/alerta/alerta-cfn/blob/master/Alerta_Single_Instance.template
.. _four: https://github.com/alerta/docker-alerta/blob/master/supervisord.conf

.. _reverse proxy:

Reverse Proxy Web UI
--------------------

serve web UI from same domain as API, if possible to avoid potential CORS errors

(example apache and nginx and gunicorn configs)

.. _static website:

Static Website
--------------

The Alerta web UI is just a directory of static assets that can be served from any location. An easy way to serve the web UI is from an `Amazon S3 bucket`_. Ensure that the domain is listed in the ``CORS_ORIGINS`` server configuration setting though.

.. _Amazon S3 bucket: http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html

.. _auth_ssl:

Authentication & SSL
--------------------

choose an auth provider

decide whether to use HTTPS or not

if multiple web servers ensure same SECRET_KEY is used

.. _replicaset:

MongoDB Replica Set
-------------------

multiple instances backed by mongo replica set

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

.. _real world:

Real World Examples
-------------------

There are several examples of how to run Alerta as a WSGI app on a Debian vagrant host, on an AWS EC2 instance, on RedHat Openshift and Docker.

* Vagrant_
* Heroku_
* OpenShift_
* `AWS EC2`_
* Docker_
* Packer_

.. _Vagrant: https://github.com/alerta/vagrant-try-alerta
.. _Heroku: https://github.com/guardian/alerta#deploy-to-the-cloud
.. _Openshift: https://github.com/alerta/openshift-api-alerta
.. _AWS EC2: https://github.com/alerta/alerta-cloudformation
.. _Docker: https://github.com/alerta/docker-alerta
.. _Packer: https://github.com/alerta/packer-templates
