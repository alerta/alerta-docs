Alerta CLI
==========

``alerta`` is the unified command-line tool for the alerta monitoring system. It can be used to
send and query alerts, tag alerts and change alert status, delete alerts,
dump alert history or see the raw alert data.

``alerta`` can also be used to send heartbeats to the alerta server.

Installation
------------

To install the ``alerta`` client the tool can be installed using pip::

    $ pip install alerta

Or, by cloning the git repository::

    $ git clone https://github.com/alerta/python-alerta.git
    $ cd python-alerta
    $ python setup.py install


Configuration
-------------

Options can be set in a configuration file, as environment variables or
on the command line. Profiles can be used to easily switch between different
configuration settings.

+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| Option      | Config File | Environment Variable              | Optional Argument               | Default                   |
+=============+=============+===================================+=================================+===========================+
| file        |     n/a     | :envvar:`ALERTA_CONF_FILE`        |     n/a                         | :file:`~/.alerta.conf`    |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| profile     |  profile    | :envvar:`ALERTA_DEFAULT_PROFILE`  | ``--profile PROFILE``           | None                      |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| endpoint    |  endpoint   | :envvar:`ALERTA_ENDPOINT`         | ``--endpoint-url URL``          | ``http://localhost:8080`` |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| key         |  key        | :envvar:`ALERTA_API_KEY`          | n/a                             | None                      |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| timezone    |  timezone   | n/a                               | n/a                             | Europe/London             |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| output      |  output     | n/a                               | ``--output OUTPUT``, ``--json`` | text                      |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| color       |  color      | :envvar:`CLICOLOR`                | ``--color``, ``--no-color``     | color on                  |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| debug       |  debug      | :envvar:`DEBUG`                   | ``--debug``                     | no debug                  |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+

.. note:: The ``profile`` option can only be set in the ``[DEFAULT]`` section.


**Example**

Configuration file :file:`~/.alerta.conf`::

    [DEFAULT]
    timezone = Australia/Sydney
    output = json

    [profile production]
    endpoint = https://api.alerta.io
    key = demo-key

    [profile development]
    endpoint = http://localhost:8080
    debug = yes

Set environment variables::

    $ export ALERTA_CONF_FILE=~/.alerta.conf
    $ export ALERTA_DEFAULT_PROFILE=production

Use production configuration settings by default::

    $ alerta query

Switch to development configuration settings when required::

    $ alerta --profile development query

Precedence
----------

Command-line configuration options have precedence over environment variables, which have precedence over the configuration file. Within the configuration file profile-specific sections have precedence over the ``[DEFAULT]`` section.


Commands
--------

 Some stuff about sub-commands.

:command:`send`
^^^^^^^^^^^^^^^

Send alert to server

The only mandatory options are ``resource`` and ``event``. All the others will
be set to sensible defaults.

+------------------+-----------------------+
| Attribute        | Default               |
+==================+=======================+
| environment      | empty string          |
+------------------+-----------------------+
| severity         | ``normal``            |
+------------------+-----------------------+
| status           | ``unknown``           |
+------------------+-----------------------+
| group            | ``Misc``              |
+------------------+-----------------------+
| correlate        | empty list            |
+------------------+-----------------------+
| value            | ``n/a``               |
+------------------+-----------------------+
| text             | empty list            |
+------------------+-----------------------+
| tags             | empty list            |
+------------------+-----------------------+
| attributes       | empty hash map        |
+------------------+-----------------------+
| origin           | program/host          |
+------------------+-----------------------+
| type             | ``exceptionAlert``    |
+------------------+-----------------------+
| timeout          | 86400 (1 day)         |
+------------------+-----------------------+
| raw data         | empty string          |
+------------------+-----------------------+

**Examples**

To send a minor alert followed by a normal::

    alert send --resource web01 --event HttpError --group Web --severity minor

    alert send --resource web01 --event HttpOK --group Web --severity normal


:command:`query`
^^^^^^^^^^^^^^^^

    query               List alerts based on query filter

:command:`watch`
^^^^^^^^^^^^^^^^

    watch               Watch alerts based on query filter

:command:`raw`
^^^^^^^^^^^^^^

    raw                 Show alert raw data

:command:`history`
^^^^^^^^^^^^^^^^^^

    history             Show alert history

:command:`tag`
^^^^^^^^^^^^^^

    tag                 Tag alerts

:command:`ack`
^^^^^^^^^^^^^^

    ack                 Acknowledge alerts

:command:`unack`
^^^^^^^^^^^^^^^^

    unack               Unacknowledge alerts

:command:`close`
^^^^^^^^^^^^^^^^

    close               Close alerts

:command:`delete`
^^^^^^^^^^^^^^^^^

    delete              Delete alerts

:command:`heartbeat`
^^^^^^^^^^^^^^^^^^^^

    heartbeat           Send heartbeat to server

:command:`config`
^^^^^^^^^^^^^^^^^

    config              Show config

:command:`help`
^^^^^^^^^^^^^^^

    help                Show help

:command:`version`
^^^^^^^^^^^^^^^^^^

    version             Show alerta version info

Bugs
----

Log any issues on `GitHub`_ or submit a `pull request`_.

.. _`github`: https://github.com/alerta/python-alerta/issues
.. _`pull request`: https://github.com/alerta/python-alerta/pulls
