.. _quick_start:

Quickstart
==========

This is a quick-start guide that will get you running Alerta in under 5 minutes.

Install MongoDB
---------------

For Debian/Ubuntu, run::

    $ sudo apt-get install -y mongodb-org
    $ sudo mongod -f /etc/mongod.conf &

If ``apt-get`` can't locate the "mongodb-org" metapackage package then
follow `these steps`_ to add MongoDB package repository to apt sources
list.

.. _these steps: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

For other operating systems, see the installation_ steps on the MongoDB web site.

.. _installation: https://docs.mongodb.com/upcoming/installation/

Install the Alerta Server
-------------------------

To install the alerta server::

    $ pip3 install alerta-server
    $ alertad run --port 8080

You should see something like::

    * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)

Install the Web Console
-----------------------

To install the web console::

    $ wget https://github.com/alerta/alerta-webui/releases/latest/download/alerta-webui.tar.gz
    $ tar zxvf alerta-webui.tar.gz
    $ cd dist
    $ python3 -m http.server 8000

    >> browse to http://localhost:8000

Install the Alerta CLI
----------------------

To install the ``alerta`` command-line tool::

    $ pip3 install alerta

Send some alerts
----------------

To send an alert to the server::

    $ alerta send -r web01 -e NodeDown -E Production -S Website -s major -t "Web server is down." -v ERROR

The alert should appear almost immediately in the console. If it doesn't it's
either a CORS issues or a bug_.

.. _bug: https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Falerta%2Falerta-docs%2Fissues%2Fnew

What's next?
------------

Take the :ref:`step-by-step tutorials <tutorials>` or dive straight into a :ref:`deployment <deployment>`.
