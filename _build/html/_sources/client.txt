
alert: command-line tool
========================

`alert` is the unified command-line tool for alerta.


Configuration Options
---------------------

Command-line options have precedence over environment variables, which have
precedence over the configuration file. Within the configuration file
profile-specific sections have precedence over the `DEFAULT` section.

+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| Variable    | Config File | Environment Variable        | Option                      | Default                   |
+=============+=============+=============================+=============================+===========================+
| config_file |     n/a     | ``ALERTA_CONF_FILE``        |     n/a                     | ``~/.alerta.conf``        |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| profile     |     n/a     | ``ALERTA_DEFAULT_PROFILE``  | ``--profile``               | None                      |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| endpoint    |  endpoint   | ``ALERTA_DEFAULT_ENDPOINT`` | ``--endpoint-url``          | ``http://localhost:8080`` |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| timezone    |  timezone   | n/a                         | n/a                         | Europe/London             |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| output      |  output     | n/a                         | ``--output``, ``--json``    | text                      |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| color       |  color      | ``CLICOLOR``                | ``--color``, ``--no-color`` | color on                  |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+
| debug       |  debug      | n/a                         | ``--debug``                 | no debug                  |
+-------------+-------------+-----------------------------+-----------------------------+---------------------------+


send
----

    send                Send alert to server

query
-----
    query               List alerts based on query filter

watch
-----
    watch               Watch alerts based on query filter

raw
---
    raw                 Show alert raw data

history
-------
    history             Show alert history

tag
---
    tag                 Tag alerts

ack
---
    ack                 Acknowledge alerts

unack
-----
    unack               Unacknowledge alerts

close
-----
    close               Close alerts

delete
------
    delete              Delete alerts

heartbeat
---------
    heartbeat           Send heartbeat to server

config
------
    config              Show config

help
----
    help                Show help

version
-------
    version             Show alerta version info
