
alert: command-line tool
========================

`alert` is the unified command-line tool for alerta.


Configuration Options
---------------------

Command-line options have precedence over environment variables, which have
precedence over the configuration file. Within the configuration file
profile-specific sections have precedence over the `DEFAULT` section.

+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| Variable    | Config File | Environment Variable              | Option                      | Default                   |
+=============+=============+===================================+=============================+===========================+
| config_file |     n/a     | :envvar:`ALERTA_CONF_FILE`        |     n/a                     | :file:`~/.alerta.conf`    |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| profile     |     n/a     | :envvar:`ALERTA_DEFAULT_PROFILE`  | ``--profile``               | None                      |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| endpoint    |  endpoint   | :envvar:`ALERTA_DEFAULT_ENDPOINT` | ``--endpoint-url``          | ``http://localhost:8080`` |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| timezone    |  timezone   | n/a                               | n/a                         | Europe/London             |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| output      |  output     | n/a                               | ``--output``, ``--json``    | text                      |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| color       |  color      | :envvar:`CLICOLOR`                | ``--color``, ``--no-color`` | color on                  |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+
| debug       |  debug      | n/a                               | ``--debug``                 | no debug                  |
+-------------+-------------+-----------------------------------+-----------------------------+---------------------------+

Examples
++++++++

Configuration file :file:`~/.alerta/config`::

    [DEFAULT]
    timezone = Australia/Sydney
    output = json

    [profile production]
    endpoint = http://alerta.prod.com:8080

    [profile development]
    endpoint = http://alerta.dev.com:8080
    debug = yes

Set environment variables::

    $ export ALERTA_CONF_FILE=~/.alerta/config
    $ export ALERTA_DEFAULT_PROFILE=production

Use production configuration settings by default::

    $ alert query

Switch to development configuration settings when required::

    $ alert --profile development query


:command:`send`
---------------

Send alert to server

The only mandatory options are ``resource`` and ``event``. All the others will
be set to sensible defaults.

Examples
++++++++

To send a minor alert followed by a normal::

    alert send --resource web01 --event HttpError --group Web --severity minor

    alert send --resource web01 --event HttpOK --group Web --severity normal


:command:`query`
----------------

    query               List alerts based on query filter

:command:`watch`
----------------

    watch               Watch alerts based on query filter

:command:`raw`
--------------

    raw                 Show alert raw data

:command:`history`
------------------

    history             Show alert history

:command:`tag`
--------------

    tag                 Tag alerts

:command:`ack`
--------------

    ack                 Acknowledge alerts

:command:`unack`
----------------

    unack               Unacknowledge alerts

:command:`close`
----------------

    close               Close alerts

:command:`delete`
-----------------

    delete              Delete alerts

:command:`heartbeat`
--------------------

    heartbeat           Send heartbeat to server

:command:`config`
-----------------

    config              Show config

:command:`help`
---------------

    help                Show help

:command:`version`
------------------

    version             Show alerta version info
