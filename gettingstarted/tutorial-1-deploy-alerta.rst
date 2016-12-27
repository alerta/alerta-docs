.. _tutorial 1:

Deploying an Alerta Server
==========================

Let's get started by installing the Alerta server, the web console
and doing some basic configuration and customisation.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Install Packages`_
  * `Step 2: Configuration`_
  * `Step 3: Customisation`_
  * `Next Steps`_

Overview
--------

The server is based on the most recent stable Ubuntu cloud image, `Ubuntu 16.04
LTS (Xenial)`_. The Alerta server will be installed to run as a `uWsgi`_
application proxied behind an `nginx`_ web server. The web console will
be served from the same nginx server and configured to support Basic Auth
logins.

Customisation will involve defining a new alert severity called
"Fatal" that will be black in colour, and allowing an additional alert
environment called "Code" in addition to "Production" and "Development".

.. _`Ubuntu 16.04 LTS (Xenial)`: https://wiki.ubuntu.com/XenialXerus/ReleaseNotes
.. _uWsgi: https://uwsgi-docs.readthedocs.io
.. _nginx: https://www.nginx.com

Prerequisites
-------------

Before you begin, ensure you are familiar with the Ubuntu/Debian operating
system, that you have "super user" privileges (ie. a ``root`` user login)
and remote ``ssh`` access to the server you are deploying to.

Step 1: Install Packages
------------------------

To install MongoDB 3.2 run the following commands::

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    $ echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    $ sudo apt-get update -y && sudo apt-get upgrade -y
    $ sudo apt-get install -y mongodb-org

Configure MongoDB to run via ``systemd`` and start at boot::

    $ sudo vi /etc/systemd/system/mongodb.service

::

    [Unit]
    Description=High-performance, schema-free document-oriented database
    After=network.target

    [Service]
    User=mongodb
    ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf

    [Install]
    WantedBy=multi-user.target

Start the MongoDB server, check it is running and set it to start on reboot::

    $ sudo systemctl start mongodb
    $ sudo systemctl status mongodb
    $ sudo systemctl enable mongodb

To install the Alerta server and ``alerta`` command-line tool::

    $ sudo apt-get install -y python-pip python-dev nginx
    $ sudo pip install alerta-server alerta uwsgi

To install the web console run::

    $ cd /var/www/html
    $ wget -q -O - https://github.com/alerta/angular-alerta-webui/tarball/master | sudo tar zxf -
    $ sudo mv alerta*/app/* .

Step 2: Configuration
---------------------

Create a wsgi python file, uWsgi configuration file and ``systemd`` script::

    $ sudo vi /var/www/wsgi.py

::

    from alerta.app import app

The uwsgi server mounts the Alerta API on ``/api``, logs to syslog and
uses a unix socket to communicate with the nginx web server::

    $ sudo vi /etc/uwsgi.ini

::

    [uwsgi]
    chdir = /var/www
    mount = /api=wsgi.py
    callable = app
    manage-script-name = true

    master = true
    processes = 5
    logger = syslog:alertad

    socket = /tmp/uwsgi.sock
    chmod-socket = 664
    uid = www-data
    gid = www-data
    vacuum = true

    die-on-term = true

Create a ``systemd`` configuration file for the uwsgi server::

    $ sudo vi /etc/systemd/system/uwsgi.service

::

    [Unit]
    Description=uWSGI service

    [Service]
    ExecStart=/usr/local/bin/uwsgi --ini /etc/uwsgi.ini

    [Install]
    WantedBy=multi-user.target

Start the uwsgi server, check the current status and enable it to start
on reboot::

    $ sudo systemctl start uwsgi
    $ sudo systemctl status uwsgi
    $ sudo systemctl enable uwsgi

::

Configure nginx to serve Alerta as a uWsgi application on ``/api`` and
the web console as static assets.

.. tip::

    Mounting the Alerta API on ``/api`` and serving the web console static
    assets from the same domain avoids any problems with CORS or HTTPS
    mixed content errors.

::

    $ sudo vi /etc/nginx/sites-enabled/default

::

    server {
            listen 80 default_server;
            listen [::]:80 default_server;

            location /api { try_files $uri @api; }
            location @api {
                include uwsgi_params;
                uwsgi_pass unix:/tmp/uwsgi.sock;
                proxy_set_header Host $host:$server_port;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }

            location / {
                    root /var/www/html;
            }

    }

Restart nginx so that it picks up the new configuration::

    $ sudo service nginx restart

Modify the existing web console ``config.js`` configuration file to
set the ``endpoint`` to ``/api`` and chose ``basic`` as the Authentication
Provider::

    $ sudo vi /var/www/html/config.js

::

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "/api",
        'provider'    : "",
        'colors'      : {},
        'severity'    : {},
        'audio'       : {}
      });

At this point you should be able to view the web console on port 80 in
your web browser.

Step 3: Customisation
---------------------

Firstly, generate a random string::

    $ cat /dev/urandom | tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= | head -c 32 && echo

Assign the random string to the `SECRET_KEY` sever setting::

    $ vi /etc/alertad.conf

    SECRET_KEY='<INSERT_RANDOM_STRING>'

Add a new severity level called "Fatal" as the highest possible
severity and remove some unwanted severity levels::

    $ vi /etc/alertad.conf

    SEVERITY_MAP = {
        'fatal': 0,
        'critical': 1,
        'warning': 4,
        'indeterminate': 5,
        'ok': 5,
        'unknown': 9
    }

Configure the default "reject" plugin to allow the additional
alert environment called "Code" and not just "Production"
or "Development"::

    $ vi /etc/alertad.conf

    PLUGINS=['reject']
    ALLOWED_ENVIRONMENTS=['Production', 'Development', 'Code']

Make sure you restart uwsgi so that the Alerta API picks up the
new severity and plugin configurations::

    $ sudo service uwsgi restart

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
