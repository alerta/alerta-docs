.. _quick_start:

Quickstart
==========

This is a quick-start guide that will get you running Alerta in under 5 minutes  .

Install MongoDB
---------------

For Debian/Ubuntu, run::

    $ sudo apt-get install -y mongodb-org
    $ mongod

For other operating systems, see the installation_ steps on the MongoDB web site.

.. _installation: http://docs.mongodb.org/manual/installation/

Install the Alerta Server
-------------------------

To install the alerta server::

    $ pip install alerta-server
    $ alertad

You should see something like::

    Starting alerta version 4.1.2 ...

Install the Web Console
-----------------------

To install the web console::

    $ wget -O alerta-web.tgz https://github.com/alerta/angular-alerta-webui/tarball/master
    $ tar zxvf alerta-web.tgz
    $ cd alerta-angular-alerta-webui-*/app
    $ python -m SimpleHTTPServer 8000

    >> browse to http://localhost:8000

Send some alerts
----------------

To send an alert to the server::

    $ alerta send -r web01 -e NodeDown -E Production -S Website -s major -t "Web server is down." -v ERROR

The alert should appear almost immediately in the console. If it doesn't it's either a :ref:`CORS issues <cross_origin>` or a bug_.

.. _bug: https://github.com/alerta/alerta-docs/issues/new