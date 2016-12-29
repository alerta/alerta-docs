.. _cli:

Alerta CLI
==========

``alerta`` is the unified command-line tool for the alerta monitoring
system. It can be used to send and query alerts, tag alerts and change
alert status, delete alerts, dump alert history or see the raw alert data.

``alerta`` can also be used to send heartbeats to the alerta server.

Installation
------------

The ``alerta`` client tool can be installed using pip::

    $ pip install alerta

Or, by cloning the git repository::

    $ git clone https://github.com/alerta/python-alerta.git
    $ cd python-alerta
    $ python setup.py install


.. _cli config:

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
| ssl verify  |  sslverify  | :envvar:`REQUESTS_CA_BUNDLE`      | n/a                             | verify SSL certificates   |
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
    key = LMvzLsfJyGpSuLmaB9kp-8gCl4I3YZkV4i7IGb6S

    [profile development]
    endpoint = https://localhost:8443
    key = demo-key
    sslverify = off
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

Command-line configuration options have precedence over environment
variables, which have precedence over the configuration file. Within
the configuration file profile-specific sections have precedence over
the ``[DEFAULT]`` section.

Commands
--------

The ``alerta`` tool is invoked by specifying a command using the
following format::

    $ alerta [OPTIONS] COMMAND [FILTERS]

.. _cli_send:

:command:`send`
~~~~~~~~~~~~~~~

Send an alert to the server::

    $ alerta [OPTIONS] send [-r RESOURCE] [-e EVENT] [-E ENVIRONMENT]
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
      --status STATUS       status should not normally be defined as it is server-
                            assigned eg. "open", "closed"
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

The only mandatory options are ``resource`` and ``event``. All the others will
be set to sensible defaults.

+------------------+-----------------------+
| Attribute        | Default               |
+==================+=======================+
| environment      | empty string          |
+------------------+-----------------------+
| severity         | ``normal``            |
+------------------+-----------------------+
| correlate        | empty list            |
+------------------+-----------------------+
| status           | ``unknown``           |
+------------------+-----------------------+
| service          | empty list            |
+------------------+-----------------------+
| group            | ``Misc``              |
+------------------+-----------------------+
| value            | ``n/a``               |
+------------------+-----------------------+
| text             | empty string          |
+------------------+-----------------------+
| tags             | empty list            |
+------------------+-----------------------+
| attributes       | empty dictionary      |
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

To send a ``minor`` alert followed by a ``normal`` alert that correlates::

    $ alerta send --resource web01 --event HttpError --correlate HttpOK --group Web --severity minor
    $ alerta send --resource web01 --event HttpOK --correlate HttpError --group Web --severity normal

To send an alert with custom attribute called ``customer``::

    $ alerta send -r web01 -e HttpError -g Web -s major --attributes customer="Tyrell Corp"


To query for major and minor open alerts for the Production environment of the Mobile API service::

    $ alerta query --filters severity=major severity=minor status=open environment=Production service="Mobile API"

To query for all alerts with "disk" in the alert text::

    $ alerta query --filters text=~disk


:command:`query`
~~~~~~~~~~~~~~~~

Search for alerts::

    $ alerta [OPTIONS] query [--details] [--ids IDs] [--filters FILTERS]

    optional arguments:
      -h, --help            show this help message and exit
      --details             Show alert details
      -i IDs [IDs ...], --ids IDs [IDs ...]
                            List of alert IDs (can use short 8-char id).
      --filters FILTERS [FILTERS ...]
                            KEY=VALUE eg. serverity=warning resource=web


:command:`watch`
~~~~~~~~~~~~~~~~

Watch for new alerts::

    $ alerta [OPTIONS] watch [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      --details          Show alert details
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`top`
~~~~~~~~~~~~~~

Show top offenders and stats::

    $ alerta top --help
    usage: alerta [OPTIONS] top [-h]

    optional arguments:
      -h, --help  show this help message and exit

See :ref:`top` for more information.

:command:`raw`
~~~~~~~~~~~~~~

Show raw data for alerts::

    $ alerta [OPTIONS] raw [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`history`
~~~~~~~~~~~~~~~~~~

Show alert history::

    $ alerta [OPTIONS] history [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`tag`
~~~~~~~~~~~~~~

Tag alerts::

    $ alerta [OPTIONS] tag -T TAG [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -T TAG, --tag TAG  List of tags eg. "London", "os:linux", "AWS/EC2".
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`untag`
~~~~~~~~~~~~~~~~

Untag alerts ie. remove an assigned tag from alert tag list::

    $ alerta [OPTIONS] untag -T TAG [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -T TAG, --tag TAG  List of tags eg. "London", "os:linux", "AWS/EC2".
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`ack`
~~~~~~~~~~~~~~

Acknowlege alerts ie. change alert ``status`` to ``ack``::

    $ alerta [OPTIONS] ack [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`unack`
~~~~~~~~~~~~~~~~

Unacknowledge alerts ie. change alert ``status`` to ``open``::

    $ alerta [OPTIONS] unack [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`close`
~~~~~~~~~~~~~~~~

Close alerts ie. change alert ``status`` to ``closed``::

    $ alerta [OPTIONS] close [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`delete`
~~~~~~~~~~~~~~~~~

Delete alerts from server::

    $ alerta [OPTIONS] delete [--id ID] [--filters FILTERS]

    optional arguments:
      -h, --help         show this help message and exit
      -i ID, --id ID     List of alert IDs (can use short 8-char id).
      --filters FILTERS  KEY=VALUE eg. id=5108bc20

:command:`blackout`
~~~~~~~~~~~~~~~~~~~

Blackout alerts based on attributes::

    $ alerta blackout --help
    usage: alerta [OPTIONS] blackout [-r RESOURCE] [-e EVENT] [-E ENVIRONMENT]
                                [-S SERVICE] [-g GROUP] [-T TAG]

    optional arguments:
      -h, --help            show this help message and exit
      -r RESOURCE, --resource RESOURCE
                            resource under alarm
      -e EVENT, --event EVENT
                            event
      -E ENVIRONMENT, --environment ENVIRONMENT
                            environment eg. "production", "development", "testing"
      -S SERVICE, --service SERVICE
                            service affected eg. the application name, "Web",
                            "Network", "Storage", "Database", "Security"
      -g GROUP, --group GROUP
                            group
      -T TAG, --tag TAG     List of tags eg. "London", "os:linux", "AWS/EC2".
      --start START         Start of blackout period
      --duration DURATION   Duration of blackout period (default: 1 hour)

:command:`blackouts`
~~~~~~~~~~~~~~~~~~~~

List all blackout periods::

    $ alerta blackouts --help
    usage: alerta [OPTIONS] blackouts [-h]

    optional arguments:
      -h, --help  show this help message and exit
      --purge     Delete all expired blackout periods

:command:`heartbeat`
~~~~~~~~~~~~~~~~~~~~

Send a heartbeat to the server::

    $ alerta [OPTIONS] heartbeat [-T TAG] [-O ORIGIN] [--timeout TIMEOUT]

    optional arguments:
      -h, --help            show this help message and exit
      -T TAG, --tag TAG     List of tags eg. "London", "os:linux", "AWS/EC2".
      -O ORIGIN, --origin ORIGIN
                            Origin of heartbeat. Usually in form of "app/host"
      --timeout TIMEOUT     Timeout in seconds before a heartbeat will be
                            considered stale

:command:`heartbeats`
~~~~~~~~~~~~~~~~~~~~~

List all heartbeats::

    $ alerta heartbeats --help
    usage: alerta [OPTIONS] heartbeats [-h]

    optional arguments:
      -h, --help  show this help message and exit
      --alert     Send alerts on stale or slow heartbeats

:command:`user`
~~~~~~~~~~~~~~~

Manage user details (Basic Auth only)::

    $ alerta user --help
    usage: alerta [OPTIONS] user --user-name USER [--password PASSWORD]

    optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user-name USER
                            User name
      -p PASSWORD, --password PASSWORD
                            New password

:command:`users`
~~~~~~~~~~~~~~~~

List all users::

    $ alerta users --help
    usage: alerta [OPTIONS] users [-h]

    optional arguments:
      -h, --help  show this help message and exit

:command:`key`
~~~~~~~~~~~~~~

Create API key::

    $ alerta key --help
    usage: alerta [OPTIONS] key [-u USER] [--readonly] [--customer CUSTOMER|--no-customer] [-t TEXT]

    optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user-name USER
                            User name
      -O, --readonly        read only API key
      --customer CUSTOMER   customer view
      --no-customer         do not associate with customer
      -t TEXT, --text TEXT  text

:command:`keys`
~~~~~~~~~~~~~~~

List all API keys::

    $ alerta keys --help
    usage: alerta [OPTIONS] keys [-h]

    optional arguments:
      -h, --help  show this help message and exit

:command:`revoke`
~~~~~~~~~~~~~~~~~

Revoke API key::

    $ alerta revoke --help
    usage: alerta [OPTIONS] revoke [--api-key KEY]

    optional arguments:
      -h, --help            show this help message and exit
      -K API_KEY, --api-key API_KEY
                            API key to be revoked.

.. _cli_status:

:command:`status`
~~~~~~~~~~~~~~~~~

Show status and metrics::

    $ alerta status --help
    usage: alerta [OPTIONS] status [-h]

    optional arguments:
      -h, --help  show this help message and exit

:command:`uptime`
~~~~~~~~~~~~~~~~~

Show server uptime::

    $ alerta uptime --help
    usage: alerta [OPTIONS] uptime [-h]

    optional arguments:
      -h, --help  show this help message and exit

:command:`version`
~~~~~~~~~~~~~~~~~~

Show version information for ``alerta`` and dependencies.

:command:`help`
~~~~~~~~~~~~~~~

Show all ``OPTIONS``, ``COMMANDS`` and some example ``FILTERS``.

Bugs
----

Log any issues on `GitHub`_ or submit a `pull request`_.

.. _`github`: https://github.com/alerta/python-alerta/issues
.. _`pull request`: https://github.com/alerta/python-alerta/pulls
