.. _tutorial 10:

Using Docker to deploy Alerta
=============================

In this tutorial, you will learn how to deploy Alerta using
Docker_.

.. _Docker: https://www.docker.com/why-docker

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Run the container`_
  * `Step 2: Customise configuration`_
  * `Step 3: Run using docker-compose`_
  * `Step 4: Install additional plugins or webhooks`_ 
  * `Step 5: Complex setups`_ 
  * `Production deployments`_ 
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


.. note:: If at any point in this tutorial something doesn't work as
  expected remember that you can set ``DEBUG=1`` for more verbose logging
  which you can access using the ``docker logs`` command. And you can
  always run a shell inside the container using
  ``docker exec -ti <container> sh`` command. All important configuration
  files are in the ``/app`` and ``/web`` directories.

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
  $ docker run --name alerta-web \
    -e DATABASE_URL=$DATABASE_URL \
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

Next try the API endpoint. Using ``curl`` the output would look like
the following::

  $ curl http://localhost:8080/api/alerts\?api-key\=5226852b-207c-47a6-9c7c-fce4d849347d
  {
    "alerts": [], 
    "autoRefresh": true, 
    "lastTime": "2020-06-07T12:35:26.085Z", 
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

Generate an alert that you can then view in the Alerta web UI by running::

  $ docker exec -ti 523906cd28e5 \
    alerta send \
    -E Development \
    -S Web \
    -r web01 \
    -e http5xx \
    -s warning \
    -t 'Too many 5xx responses'

.. tip:: Keep a copy of the returned alert id. You will need this in `Step 4`_.

And finally, try browsing to the web UI using http://localhost:8080/

.. _Step 2:

Step 2: Customise configuration
-------------------------------

In `Step 1`_ you launched an Alerta container using the default configuration.

To customise your Alerta server for your environment you can override
the defaults using either environment variables (for common settings) or
by mounting a configuration file into the container.

Configuration via Environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A full list of environment variables supported by the Alerta docker image
can be found in the `README`_ file. They include all of the most
common settings for a standard deployment.

.. _README: https://github.com/alerta/docker-alerta/blob/master/README.md#environment-variables

You already used one environment variable (``DATABASE_URL``) to tell Alerta
where the database could be found and what the database credentials were.

The environment variables ``ADMIN_PASSWORD``, ``ADMIN_KEY``, ``ADMIN_KEY_MAXAGE``,
and ``HEARTBEAT_SEVERITY`` are only supported by the Docker container and are
provided specifically to ease the deployment of Alerta in Docker environments.

Of these, it is really only ``ADMIN_PASSWORD`` that needs to be set otherwise
the default password of "alerta" will be assigned.

It can be useful to also set ``ADMIN_KEY`` to a known value otherwise an random API
key will be generated with ``admin`` privileges. That API key can be assigned
by a configuration management tool and used when integrating with other tools,
for example.

So, to run Alerta with set values for ``ADMIN_PASSWORD`` and ``ADMIN_KEY``, and to
enable ``DEBUG`` run::

  $ docker run --name alerta-web \
    -e DATABASE_URL=$DATABASE_URL \
    -e DEBUG=1 \
    -e ADMIN_PASSWORD=Pa55w0rd \
    -e ADMIN_KEY=docker-api-key \
    --link alerta-db:db -d -p 8080:8080 alerta/alerta-web

.. note:: Use the above command for this tutorial but remember to set your
    ``ADMIN_PASSWORD`` and ``ADMIN_KEY`` to something different when deploying
    to your environment.

The default admin username is "alerta". This can be set using ``ADMIN_USERS`` which
allows you to set one or more admin users to be created at container launch time::

  $ docker run --name alerta-web \
    -e DATABASE_URL=$DATABASE_URL \
    -e ADMIN_USERS=alice,bob,charlotte,dave \
    -e ADMIN_PASSWORD=Pa55w0rd \
    -e ADMIN_KEY=docker-api-key \
    --link alerta-db:db -d -p 8080:8080 alerta/alerta-web

One of the important benefits of the Docker image is that many plugins come
pre-installed so the container starts immediately the database is available.

However, only a few plugins are enabled by default ie. ``remote_ip``,
``reject``, ``heartbeat``, ``blackout``, ``forwarder``. To enable more, or
to disable some of the defaults, use the ``PLUGINS`` environment variable
like so::

  $ docker run --name alerta-web \
    -e DATABASE_URL=$DATABASE_URL \
    -e ADMIN_USERS=alice,bob,charlotte,dave \
    -e ADMIN_PASSWORD=Pa55w0rd \
    -e ADMIN_KEY=docker-api-key \
    -e PLUGINS=reject,heartbeat,blackout,normalise \
    --link alerta-db:db -d -p 8080:8080 alerta/alerta-web

By now, you can see that the number of environment variables listed
on the command line is growing and becoming unmanageable and we
haven't even looked at all the different authentication settings.

Configuration via external ``alertad.conf`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So now we will use a configuration file that we can mount into the
container at run time. The alternative is to continue using
environment variables (if we only need to set configuration that is
supported by environment variables) but instead of using ``docker run``
we use ``docker-compose`` and its YAML configuration file.

We look at using ``docker-compose`` next, however, for now let's see
how we can set :ref:`any configuration setting <configuration>` using
an external ``alertad.conf`` file.

Create a file called ``alertad.conf`` in your current working directory
and we will include all of the environment variable settings from above
and a few more, so you can see how they compare:

.. code-block:: python

  DEBUG=True
  DATABASE_URL='postgres://alerta:al3rt8@db:5432/alerta'
  AUTH_REQUIRED=True
  ADMIN_USERS=['alice','bob','charlotte','dave']
  ADMIN_PASSWORD='Pa55w0rd'
  ADMIN_KEY='docker-api-key'
  PLUGINS=['reject','heartbeat','blackout','normalise']

The most important difference to note is that the configuration file
must be valid Python, so strings must be quoted, comma-separated variables
become Python lists, ``1`` becomes ``True`` etc.

Then to mount this file into the docker container at run time use::

  $ docker run --name alerta-web \
    -v $PWD/alertad.conf:/app/alertad.conf \
    --link alerta-db:db -d -p 8080:8080 alerta/alerta-web

.. note:: You may first need to stop your previous Alerta container.

You should see that if you log out of the web UI you will be forced
to login if you want to continue. This proves that the ``AUTH_REQUIRED``
setting was read from the supplied configuration file. Excellent!

However, things are starting to get a little more complex now as we
have an additional file to manage as well as remembering the exact
command to launch Postgres and the Alerta API. And stopping and starting
the containers at the right time and in the right order becomes tricky
if we add more dependencies to your monitoring stack, like Prometheus
and Alertmanager, for example.

This is where container orchestration comes into play. And the first
step towards Docker container configuration and deployment is to
use the ``docker-compose`` tool which we will look at now.

.. _Step 3:

Step 3: Run using docker-compose
--------------------------------

The ``docker-compose`` tool can be used to launch an entire Docker
container stack with one command, namely ``docker-compose up``.

Create a new file called ``docker-compose.yaml`` in your current
working directory and include the following:

.. code-block:: yaml

  version: '3'
  services:
    api:
      image: alerta/alerta-web
      ports:
        - 8080:8080
      environment:
        - DEBUG=1
        - DATABASE_URL=postgres://alerta:8l3rt8@db:5432/alerta
        - AUTH_REQUIRED=True
        - ADMIN_USERS=alice,bob,charlotte,dave
        - ADMIN_PASSWORD=Pa55w0rd
        - ADMIN_KEY=docker-api-key
        - PLUGINS=reject,heartbeat,blackout,normalise
      networks:
        - net
      depends_on:
        - db
      restart: always
    db:
      image: postgres
      volumes:
        - ./pg-data:/var/lib/postgresql/data
      environment:
        POSTGRES_DB: alerta
        POSTGRES_USER: alerta
        POSTGRES_PASSWORD: 8l3rt8
      networks:
        - net
      restart: always
  networks:
    net: {}

Now launch both Alerta and Postgres at the same time using::

  $ docker-compose up

And verify by browsing to http://localhost:8080 as before.

You can replace ``environment:`` with ``volumes:`` if you want or need
to mount a configuration file into the container, like so:

.. code-block:: yaml

  version: '3'
  services:
    web:
      image: alerta/alerta-web
      ports:
        - 8080:8080
      volumes:
        - ./alertad.conf:/app/alertad.conf
      networks:
        - net
      depends_on:
        - db
      restart: always
    db:
      image: postgres
      volumes:
        - ./pg-data:/var/lib/postgresql/data
      environment:
        POSTGRES_DB: alerta
        POSTGRES_USER: alerta
        POSTGRES_PASSWORD: 8l3rt8
      networks:
        - net
      restart: always
  networks:
    net: {}

.. _Step 4:

Step 4: Install additional plugins or webhooks
----------------------------------------------

Docker containers should be treated as `"immutable"`_ infrastructure which means
that once deployed they should not be modified. So if you need to use a custom
plugin or webhook not already pre-installed then you will need to install it
during image build time, not after the container as been deployed.

.. _`"immutable"`: https://www.oreilly.com/radar/an-introduction-to-immutable-infrastructure/

To do this you can extend the base image by creating a ``Dockerfile`` and
using the ``FROM`` instruction. For example, to install the `MS Teams webhook`_
create a ``Dockerfile`` as below:

.. _`MS Teams webhook`: https://github.com/alerta/alerta-contrib/tree/master/webhooks/msteams

.. code-block:: yaml

  FROM alerta/alerta-web

  RUN /venv/bin/pip install \
      git+https://github.com/alerta/alerta-contrib.git#subdirectory=webhooks/msteams

You can either build the Docker image using the ``docker build`` command or
add a reference to your ``docker-compose.yaml`` file and use ``docker-compose build``.
Modify the ``docker-compose.yaml`` as follows adding the ``build`` line and changing
the ``image`` line slightly to remove the "alerta/" organisation reference like so:

.. code-block:: yaml

  version: '3'
  services:
    web:
      build: .
      image: alerta-web
      ports:
        - 8080:8080
      volumes:
        - ./alertad.conf:/app/alertad.conf
      networks:
        - net
      depends_on:
        - db
      restart: always
    db:
      image: postgres
      volumes:
        - ./pg-data:/var/lib/postgresql/data
      environment:
        POSTGRES_DB: alerta
        POSTGRES_USER: alerta
        POSTGRES_PASSWORD: 8l3rt8
      networks:
        - net
      restart: always
  networks:
    net: {}

Now build the new image and run it using::

  $ docker-compose up --build

Once again you should be able to browse to http://localhost:8080 and log
in to the web console.

To verify that the MS Teams webhook is now available, use curl to send a
HTTP POST request to the webhook URL (replace ``alert_id`` with your alert
id from `Step 1`_)::

  $ curl -XPOST http://localhost:8080/api/webhooks/msteams \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: docker-api-key' \
  -d '{"action":"ack","alert_id":"da9b3d24-3ee3-4cdc-8a58-a6533c9e9af9"}'
  {
    "message": "status changed", 
    "status": "ok"
  }

.. _Step 5:

Step 5: Complex setups
----------------------

Alerta, just like any web service, can be deployed in numerous different
ways to suit your environment. Most commonly, it will be deployed behind
a reverse proxy (which would be responsible for SSL termination) and perhaps
on a sub-path such as ``/alerta`` (eg. https://monitoring.example.com/alerta/ui)

It is beyond the scope of this introductory tutorial to step you through
every possible scenario however, below is a list of example ``docker-compose``
deployments that illustrate some of these scenarios:

  * `Apache reverse proxy`_
  * `Envoy proxy`_
  * `nginx reverse proxy`_
  * `Traefik proxy`_

.. _Apache reverse proxy:  https://github.com/alerta/docker-alerta/tree/master/examples/apache
.. _Envoy proxy: https://github.com/alerta/docker-alerta/tree/master/examples/envoy
.. _nginx reverse proxy: https://github.com/alerta/docker-alerta/tree/master/examples/nginx
.. _Traefik proxy: https://github.com/alerta/docker-alerta/tree/master/examples/traefik

Production deployments
----------------------

Despite `what Docker say`_, it is not advisable to use ``docker-compose``
for production deployments. Instead you should consider container
runtime platforms such as Kubernetes_, `AWS Elastic Container Service`_,
or `Google Cloud GKE`_.

.. _what Docker say: https://docs.docker.com/compose/production/
.. _Kubernetes: https://kubernetes.io/
.. _AWS Elastic Container Service: https://aws.amazon.com/ecs/
.. _Google Cloud GKE: https://cloud.google.com/kubernetes-engine/

Next Steps
----------

In a future tutorial, you will learn how to deploy Alerta with Kubernetes
using a tool called ``mini-kube``. So stay tuned!
