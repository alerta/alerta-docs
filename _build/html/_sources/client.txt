
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


:command:`send`
---------------

Send alert to server

The only mandatory options are ``resource`` and ``event``. All the others will
be set to sensible defaults.


::

    usage: alert [OPTIONS] send [-h] [-r RESOURCE] [-e EVENT] [-E ENVIRONMENT]
                                [-s SEVERITY] [-C CORRELATE] [--status STATUS]
                                [-S SERVICE] [-g GROUP] [-v VALUE] [-t TEXT]
                                [-T TAG] [-A ATTRIBUTES] [-O ORIGIN]
                                [--type EVENT_TYPE] [--timeout TIMEOUT]
                                [--raw-data RAW_DATA]

    optional arguments:
      -h, --help            show this help message and exit
      -r RESOURCE, --resource RESOURCE
                            resource under alarm
      -e EVENT, --event EVENT
                            event
      -E ENVIRONMENT, --environment ENVIRONMENT
                            environment eg. "production", "development", "testing"
      -s SEVERITY, --severity SEVERITY
                            severity
      -C CORRELATE, --correlate CORRELATE
                            correlate
      --status STATUS       status should not normally be defined eg. "open",
                            "closed"
      -S SERVICE, --service SERVICE
                            service affected eg. the application name, "Web",
                            "Network", "Storage", "Database", "Security"
      -g GROUP, --group GROUP
                            group
      -v VALUE, --value VALUE
                            value
      -t TEXT, --text TEXT  Freeform alert text eg. "Host not responding to ping."
      -T TAG, --tag TAG     List of tags eg. "London", "os:linux", "AWS/EC2".
      -A ATTRIBUTES, --attribute ATTRIBUTES
                            List of Key=Value attribute pairs eg. "priority=high",
                            "moreInfo=..."
      -O ORIGIN, --origin ORIGIN
                            Origin of alert. Usually in form of "app/host"
      --type EVENT_TYPE     event type eg. "exceptionAlert", "serviceAlert"
      --timeout TIMEOUT     Timeout in seconds before an "open" alert will be
                            automatically "expired" or "deleted"
      --raw-data RAW_DATA   raw data

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
