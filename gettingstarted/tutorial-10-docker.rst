.. _tutorial 10:

Using Docker to deploy Alerta
=============================

In this tutorial, you will learn how to deploy Alerta using
Docker.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Run the container`_
  * `Step 2: Customise configuration`_
  * `Step 3: Run using docker-compose`_
  * `Step 4: Install additional plugins or webhooks`_ 
  * `Step 5: Complex setups`_ 
  * `Step 6: Production deployments (Bonus)`_ 
  * `Debugging and Troubleshooting`_ 


Overview
--------

The `"official" Docker image`_ for Alerta has been download more
than `2 million times`_ and contains everything needed
to deploy Alerta in most scenarios, such as:

  * Alerta API
  * Alerta Web UI
  * housekeeping
  * built-in and contributed plugins
  * built-in webhooks
  * all auth providers "ready-to-go"

.. _`"official" Docker image`: https://hub.docker.com/r/alerta/alerta-web/
.. _`2 million times`: https://hub.docker.com/v2/repositories/alerta/alerta-web/

More complex deployments can either use it as a base image and
extend it with additional plugins, webhooks or alternatively,
the Dockerfile_ can be used as a starting point to build your
own base image.

.. _Dockerfile: https://github.com/alerta/docker-alerta/blob/master/Dockerfile

Prerequisites
-------------

To follow this tutorial you will need access to a Docker
environment where you can build Docker images and run containers.
The fastest way to get going is to use `Docker Desktop`_.

.. _Docker Desktop: https://www.docker.com/products/docker-desktop

Follow the instructions on the Docker website and then return
to this tutorial and continue with `Step 1`_.

To get bonus points, `install Minikube`_, the "single-node Kubernetes
cluster in a virtual machine on your personal computer" which you
will need to complete `Step 6`_ where you mimic deploying to production.

.. _install Minikube: https://kubernetes.io/docs/tasks/tools/install-minikube/

.. _Step 1:

Step 1: Run the container
-------------------------

We will first start a Postgres database container which is
required by Alerta::

  $ export POSTGRES_USER=alerta
  $ export POSTGRES_PASSWORD=al3rt8

  $ docker run --name alerta-db \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -d postgres

Next, we start the Alerta docker container::

  $ export DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@db:5432/alerta
  $ docker run --name alerta-web -e DATABASE_URL=$DATABASE_URL \
    --link alerta-db:db -d -p 8080:8080 alerta/alerta-web

Now get the container id of the Alerta server and tail the logs::

  $ docker ps
  CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
  523906cd28e5        alerta/alerta-web   "docker-entrypoint.s…"   21 seconds ago       Up 21 seconds       0.0.0.0:8080->8080/tcp   alerta-web
  ddd2a1333b38        postgres            "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp                 alerta-db

  $ docker logs -f 523906cd28e5  # note that your container id will be different

If it is running you should see log entries for the API server similar to the
following::

  2020-06-06 19:21:12,507 DEBG 'nginx' stdout output:
  ip=\- [\06/Jun/2020:19:21:12 +0000] "\GET /api/config HTTP/1.1" \200 \873 "\-" "\python-requests/2.21.0"
  /web | /api/config | > GET /api/config HTTP/1.1

Next try the API endpoint. Using the `http`_ tool the output would look like
the following::

  $ http http://localhost:8080/api/alerts
  HTTP/1.1 200 OK
  Access-Control-Allow-Origin: http://localhost
  Connection: keep-alive
  Content-Length: 203
  Content-Type: application/json
  Date: Sat, 06 Jun 2020 19:19:45 GMT
  Server: nginx/1.14.2
  Vary: Origin
  X-Request-ID: aff1e858-7547-4c26-bff1-f884da47ea12

  {
      "alerts": [],
      "autoRefresh": true,
      "lastTime": "2020-06-06T19:19:45.318Z",
      "message": "not found",
      "more": false,
      "page": 1,
      "pageSize": 1000,
      "pages": 0,
      "severityCounts": {},
      "status": "ok",
      "statusCounts": {},
      "total": 0
  }

.. _http: https://httpie.org/docs#installation

And finally, try browsing to the web UI using http://localhost:8080/

Step 2: Customise configuration
-------------------------------

configuration
- using env vars
- using external config file

Step 3: Run using docker-compose
--------------------------------

- docker-compose up

Step 4: Install additional plugins or webhooks
----------------------------------------------

extending base image
- installing plugins
- installing webhooks


Step 5: Complex setups
----------------------

- behind proxy
- ssl termination
- sub path
build your own
- custom web ui subpath

.. _step 6:

Step 6: Production deployments (Bonus)
--------------------------------------

Despite `what Docker say`_, it is not advisable to use ``docker-compose``
for production deployments. Instead you should consider container
runtime platforms such as Kubernetes_, `AWS Elastic Container Service`_,
or `Google Cloud GKE`_.

.. _what Docker say: https://docs.docker.com/compose/production/
.. _Kubernetes: https://kubernetes.io/
.. _AWS Elastic Container Service: https://aws.amazon.com/ecs/
.. _Google Cloud GKE: https://cloud.google.com/kubernetes-engine/

For the purpose of this tutorial, you can run Alerta in Kubernetes
using a tool called ``mini-kube``.



Debugging and Troubleshooting
-----------------------------

tbc

