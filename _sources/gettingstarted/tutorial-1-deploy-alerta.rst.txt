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

The server is based on the most recent stable Ubuntu cloud image, `Ubuntu 18.04
LTS (Bionic Beaver)`_. The Alerta server will be installed to run as a `uWsgi`_
application proxied behind an `nginx`_ web server. The web console will
be served from the same nginx server and configured to support Basic Auth
logins.

Customisation will involve defining a new alert severity called
"fatal" that will be blue in colour, and allowing an additional alert
environment called "Code" in addition to "Production" and "Development".

.. _`Ubuntu 18.04 LTS (Bionic Beaver)`: https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes
.. _uWsgi: https://uwsgi-docs.readthedocs.io
.. _nginx: https://www.nginx.com

Prerequisites
-------------

Before you begin, ensure you are familiar with the Ubuntu/Debian operating
system, that you have "super user" privileges (ie. a ``root`` user login)
and remote ``ssh`` access to the server you are deploying to.

Step 1: Install Packages
------------------------

To install MongoDB 4.0 run the following commands::

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
    $ echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org

Start the MongoDB server, check it is running and set it to start on reboot::

    $ sudo systemctl start mongod
    $ sudo systemctl status mongod
    $ sudo systemctl enable mongod

To run Alerta we need to ensure all Python 3 dependencies are installed::

    $ sudo apt-get install -y python3 python3-setuptools python3-pip python3-dev python3-venv
    $ sudo apt-get install -y nginx uwsgi-plugin-python3

To install the Alerta server and ``alerta`` command-line tool into a
Python 3 virtual environment run::

    $ cd /opt
    $ python3 -m venv alerta
    $ alerta/bin/pip install --upgrade pip wheel alerta-server alerta uwsgi

To install the web console run::

    $ wget https://github.com/alerta/alerta-webui/releases/latest/download/alerta-webui.tar.gz
    $ tar zxvf alerta-webui.tar.gz
    $ cp dist /var/www/html

Step 2: Configuration
---------------------

Create a wsgi python file, uWsgi configuration file and ``systemd`` script::

    $ sudo vi /var/www/wsgi.py

::

    from alerta import create_app
    app = create_app()

The uwsgi server mounts the Alerta API on ``/api``, logs to syslog and
uses a unix socket to communicate with the nginx web server::

    $ sudo vi /etc/uwsgi.ini

::

    [uwsgi]
    chdir = /var/www
    mount = /api=wsgi.py
    callable = app
    manage-script-name = true
    env = BASE_URL=/api

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
    ExecStart=/opt/alerta/bin/uwsgi --ini /etc/uwsgi.ini

    [Install]
    WantedBy=multi-user.target

Start the uwsgi server, check the current status and enable it to start
on reboot::

    $ sudo service start uwsgi
    $ sudo service status uwsgi
    $ sudo service enable uwsgi

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

Modify the existing web console ``config.json`` configuration file to
set the ``endpoint`` to ``/api``::

    $ sudo vi /var/www/html/config.json

::

    {"endpoint": "/api"}

At this point you should be able to view the web console on port 80 in
your web browser.

Step 3: Customisation
---------------------

Firstly, generate a random string::

    $ cat /dev/urandom | tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= | head -c 32 && echo

Assign the random string to the ``SECRET_KEY`` sever setting::

    $ vi /etc/alertad.conf

::

    SECRET_KEY='<INSERT_RANDOM_STRING>'

Add a new severity level called "Fatal" as the highest possible
severity and remove some unwanted severity levels::

    $ vi /etc/alertad.conf

::

    SEVERITY_MAP = {
        'fatal': 0,
        'critical': 1,
        'warning': 4,
        'indeterminate': 5,
        'ok': 5,
        'unknown': 9
    }

The default "normal" severity is ``normal`` however it is no longer
a valid severity following the changes made above so you must explicity
set the default severity to ``ok`` by adding::

    DEFAULT_NORMAL_SEVERITY = 'ok'

And change the color map to reflect the new severities::

    COLOR_MAP = {
        'severity': {
            'fatal': 'blue',
            'critical': 'red',
            'warning': '#1E90FF',
            'indeterminate': 'lightblue',
            'ok': '#00CC00',
            'unknown': 'silver'
        }
    }

.. reject

Configure the default "reject" plugin to allow the additional
alert environment called "Code" and not just "Production"
or "Development"::

    $ vi /etc/alertad.conf

::

    PLUGINS=['reject']
    ALLOWED_ENVIRONMENTS=['Production', 'Development', 'Code']

Make sure you restart uwsgi so that the Alerta API picks up the
new severity and plugin configurations::

    $ sudo service uwsgi restart

To use the command-line tool to submit a test alert you first need
to create a configuration file that defines what API endpoint to
use::

    $ vi $HOME/.alerta.conf

::

    [DEFAULT]
    endpoint = http://localhost/api

Send a test "fatal" alert and confirm it has been received by viewing
it in the web console::

    $ /opt/alerta/bin/alerta send --resource net01 --event down --severity fatal \
    --environment Code --service Network --text 'net01 is down.'

Note that the above can be shortened by using argument flags instead of the
full argument names::

    $ /opt/alerta/bin/alerta send -r net01 -e down -s fatal -E Code -S Network -t 'net01 is down.'

To view the alerts in a terminal run::

    $  /opt/alerta/bin/alerta query

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * :ref:`Use alert timeouts to expire stale alerts <tutorial 2>`
  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
