.. _deployment:

Deployment
==========

WSGI Server
-----------

There are many ways to deploy Alerta. It can be run as ``alertad``
during development or testing but when run in a production environment,
it should `always be deployed`_ as a WSGI application. See the list
of `real world`_ examples below for different ways to run Alerta as
a WSGI application.

.. _always be deployed: http://flask.pocoo.org/docs/0.10/deploying/
.. _WSGI: http://www.fullstackpython.com/wsgi-servers.html

.. _reverse proxy:

Web Proxy
---------

Running the Alerta API behind a web proxy can greatly simplify the
Web UI setup which means you can completely `avoid`_ the potential
for any cross-origin issues.

.. _avoid: http://oskarhane.com/avoid-cors-with-nginx-proxy_pass/

Also, if you run the API on an HTTPS/SSL endpoint then it can
reduce the possibility of `mixed content`_ errors when a web
application hosted on a HTTP endpoint tries to access resources
on an HTTPS endpoint.

.. _mixed content: https://developer.mozilla.org/en-US/docs/Security/MixedContent/How_to_fix_website_with_mixed_content

**Example API configuration (extract)**

This example nginx server is configured to serve the web UI from
the root ``/`` path and reverse-proxy API requests to ``/api`` to
the WSGI application running on port 8080::

    server {

            listen 80 default_server deferred;

            access_log /dev/stdout main;

            location /api/ {
                    proxy_pass http://backend/;
                    proxy_set_header Host $host:$server_port;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }

            location / {
                    root /app;
            }
    }

    upstream backend {
            server localhost:8080 fail_timeout=0;
    }

The web UI configuration file :file:`config.js` for this setup would
simply be ``/api`` for the ``endpoint`` value, as follows::

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "/api",
        'provider'    : "basic"
      });

.. _static website:

Static Website
--------------

The Alerta web UI is just a directory of static assets that can be
served from any location. An easy and cheap way to serve the web UI
is from an `Amazon S3 bucket`_ as a static website.

.. note:: Serving the Alerta web UI from a static web hosting site
          **will not work** unless that domain is listed in the
          ``CORS_ORIGINS`` Alerta API server configuration settings.

.. _Amazon S3 bucket: http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html

.. _auth_ssl:

Authentication & SSL
--------------------

Alerta supports several authentication mechanisms for both the API
and the web UI and some key features of the web UI, like
:ref:`watching alerts <watched alerts>`, are only available if
authentication is enabled.

The API can be secured using :ref:`API keys` and the web UI can
be secured using :ref:`Basic Auth <basic auth>` or an :ref:`OAuth <oauth2>`
provider from either Google or Github.

If you plan to make the web UI accessible from a public URL it is
strongly advised to :ref:`enforce authentication <Authentication>`
and use HTTPS/SSL connections to the Alerta API to protect private
alert data.

.. _auth_cv:

Authorisation & Customer Views
------------------------------

To restrict access to certain features use :ref:`roles <user roles>`
and :ref:`customer views <customer views>`.

.. _scalability:

Scalability
-----------

Alerta can scale horizontally, in the same way any other web
application scales horizontally -- a load balancer handles the
HTTP requests and distributes those requests between all available
application servers.

.. _scale horizontally: https://blog.openshift.com/best-practices-for-horizontal-application-scaling/

.. note:: If using multiple API servers ensure the same ``SECRET_KEY``
          is used across all servers otherwise there will be problems
          with web UI user logins.

.. _high availability:

High Availability
-----------------

To achieve high system availability the Alerta API should be
deployed to scale out :ref:`horizontally <scalability>` and
the MongoDB database should be deployed as a `replica set`_.

.. _replica set: http://docs.mongodb.org/manual/tutorial/deploy-replica-set/#overview

.. _housekeeping:

House Keeping
-------------

There are some jobs that should be run periodically to keep the
Alerta console clutter free. To timeout *expired* alerts and
delete old *closed* alerts run a contributed MongoDB script_
called :file:`housekeepingAlerts.js` at regular intervals
via ``cron``.

.. _script: https://github.com/alerta/alerta/blob/master/contrib/mongo/housekeepingAlerts.js

.. _stale heartbeats:

:ref:`Heartbeats <heartbeats>` can be sent from any source to
ensure that a system is 'alive'. To generate alerts for stale
heartbeats the ``alerta`` command-line tool can be used::

    $ alerta heartbeats --alert

Again, this should be run at regular intervals via ``cron`` or
some other scheduler.

.. _metrics:

Management & Metrics
--------------------

Use the management endpoint :file:`/management/status` to keep
track of realtime statistics on the performance of the Alerta API
like alert counts and average processing time. For convenience,
these statistics can be viewed in the *About* page of the Alerta
web UI or using the ``alerta`` command-line tool
:ref:`status <cli_status>` command.

Web UI Analytics
----------------

Google analytics can be used to track usage of the Alerta web UI
console. Just create a new tracking code with the `Google analytics`_
console and add it to the ``config.js`` web console configuration
file::

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "/api",
        'provider'    : "basic",
        'tracking_id' : "UA-NNNNNN-N"  // Google Analytics tracking ID
      });

.. _Google analytics: https://analytics.google.com/analytics/web/

.. _real world:

Real World Examples
-------------------

Below are several different examples of how to run Alerta in production
from a Debian `vagrant box`_, an `AWS EC2 instance`_,
`RedHat Openshift PaaS`_ to a `Docker container`_.

.. _vagrant box: https://docs.vagrantup.com/v2/boxes.html
.. _AWS EC2 instance: https://aws.amazon.com/ec2/
.. _RedHat OpenShift PaaS: https://www.openshift.com/products
.. _Docker container: https://www.docker.com/whatisdocker

* Vagrant_ - deploy Alerta stand-alone or with Nagios, Zabbix, Riemann, Sensu or Kibana
* Heroku_ - deploy the Alerta API and the `web ui to Heroku`_ PaaS
* OpenShift_ - deploy the Alerta API to OpenShift Paas
* `AWS EC2`_ - deploy Alerta to EC2 using AWS Cloudformation
* Docker_ - deploy Alerta to a docker container
* Packer_ - deploy Alerta to EC2 using Amazon AMIs
* `Flask deploy`_ - deploy Alerta as a generic Flask app
* `Ansible`_ - deploy Alerta using ansible on Centos 7

.. _Vagrant: https://github.com/alerta/vagrant-try-alerta
.. _Heroku: https://github.com/alerta/alerta#deploy-to-the-cloud
.. _web UI to Heroku: https://github.com/alerta/angular-alerta-webui#deploy-to-the-cloud
.. _Openshift: https://github.com/alerta/openshift-api-alerta
.. _AWS EC2: https://github.com/alerta/alerta-cloudformation
.. _Docker: https://github.com/alerta/docker-alerta
.. _Packer: https://github.com/alerta/packer-templates
.. _Flask deploy: http://flask.pocoo.org/docs/0.10/quickstart/#deploying-to-a-web-server
.. _Ansible: https://github.com/ramshankarjaiswal/ansible/tree/master/roles/alerta
