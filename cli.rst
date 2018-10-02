.. _cli:

Alerta CLI
==========

``alerta`` is the unified command-line tool, terminal GUI and Python SDK
for the alerta monitoring system.

It can be used to send and query alerts, tag alerts and change alert status,
delete alerts, dump alert history or see the raw alert data. It can also be
used to send heartbeats to the alerta server, and generate alerts based on
missing or slow heartbeats.

.. image:: _static/images/alerta-top-80x25.png


Installation
------------

The ``alerta`` client tool can be installed using pip::

    $ pip install alerta

Or, by cloning the git repository::

    $ git clone https://github.com/alerta/python-alerta-client.git
    $ cd python-alerta-client
    $ pip install .


.. _cli config:

Configuration
-------------

Options can be set in a configuration file, as environment variables or
on the command line. Profiles can be used to easily switch between different
configuration settings.

+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| Option      | Config File | Environment Variable              | Optional Argument               | Default                   |
+=============+=============+===================================+=================================+===========================+
| file        |     n/a     | :envvar:`ALERTA_CONF_FILE`        | ``--config-file FILE``          | :file:`~/.alerta.conf`    |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| profile     |  profile    | :envvar:`ALERTA_DEFAULT_PROFILE`  | ``--profile PROFILE``           | None                      |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| endpoint    |  endpoint   | :envvar:`ALERTA_ENDPOINT`         | ``--endpoint-url URL``          | ``http://localhost:8080`` |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| key         |  key        | :envvar:`ALERTA_API_KEY`          | n/a                             | None                      |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| provider    |  provider   | :envvar:`ALERTA_API_KEY`          | n/a                             | basic                     |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| client id   |  client_id  | n/a                               | n/a                             | None                      |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| GitHub URL  |  github_url | n/a                               | n/a                             | ``https://github.com``    |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| GitLab URL  |  gitlab_url | n/a                               | n/a                             | ``https://gitlab.com``    |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| timezone    |  timezone   | n/a                               | n/a                             | Europe/London             |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| timeout     |  timeout    | n/a                               | n/a                             | 5s TCP connection timeout |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| ssl verify  |  sslverify  | :envvar:`REQUESTS_CA_BUNDLE`      | n/a                             | verify SSL certificates   |
+-------------+-------------+-----------------------------------+---------------------------------+---------------------------+
| output      |  output     | n/a                               | ``--output FORMAT``, ``--json`` | text                      |
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

    [profile development]
    endpoint = https://localhost:8443
    key = demo-key
    sslverify = off
    timeout = 10.0
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
the configuration file, profile-specific sections have precedence over
the ``[DEFAULT]`` section.

Authentication
--------------

If the Alerta API enforces authentication, then the ``alerta`` command-line
tool can be configured to present an API key or Bearer token to the API when
accessing secured endpoints.

**API Keys**

API keys can be generated in the web UI, or by an authenticated user using
the ``alerta`` CLI, and should be added to the configuration file as the "key"
setting as shown in the following example::

    [profile production]
    endpoint = https://api.alerta.io
    key = LMvzLsfJyGpSuLmaB9kp-8gCl4I3YZkV4i7IGb6S

**Bearer Tokens**

Alternatively, a user can "login" to the API and retrieve a Bearer token if
the Alerta API is configured to use either ``basic``, ``github``, ``gitlab``
or ``google`` as the authentication provider. An OAuth Client ID is required
if not using ``basic`` and settings should be added to the configuration
file as shown in the example below::

    [profile cloud]
    endpoint = https://alerta-api.herokuapp.com
    provider = google
    client_id = 736147134702-glkb1pesv716j1utg4llg7c3rr7nnhli.apps.googleusercontent.com

Commands
--------

The ``alerta`` tool is invoked by specifying a command using the
following format::

    $ alerta [OPTIONS] COMMAND [ARGS]...

The following group of commands are related to creating, querying and managing
alerts.

.. _cli_send:

:command:`send`
~~~~~~~~~~~~~~~

Send an alert.

::

    $ alerta send [OPTIONS]

    Options:
    -r, --resource RESOURCE        Resource under alarm
    -e, --event EVENT              Event name
    -E, --environment ENVIRONMENT  Environment eg. Production, Development
    -s, --severity SEVERITY        Severity eg. critical, major, minor, warning
    -C, --correlate EVENT          List of related events eg. node_up, node_down
    -S, --service SERVICE          List of affected services eg. app name, Web,
                                    Network, Storage, Database, Security
    -g, --group GROUP              Group event by type eg. OS, Performance
    -v, --value VALUE              Event value
    -t, --text DESCRIPTION         Description of alert
    -T, --tag TAG                  List of tags eg. London, os:linux, AWS/EC2
    -A, --attributes KEY=VALUE     List of attributes eg. priority=high
    -O, --origin ORIGIN            Origin of alert in form app/host
    --type EVENT_TYPE              Event type eg. exceptionAlert,
                                    performanceAlert, nagiosAlert
    --timeout SECONDS              Seconds before an open alert will be expired
    --raw-data STRING              Raw data of orignal alert eg. SNMP trap PDU.
                                    '@' to read from file, '-' to read from stdin
    --customer STRING              Customer
    -h, --help                     Show this message and exit.

The only mandatory options are ``resource`` and ``event``. All the others will
be set to sensible defaults.

.. attention:: If the ``reject`` plugin is enabled (which it is by
    default) then alerts must have an ``environment`` attribute that
    is one of either ``Production`` or ``Development`` and it must
    define a ``service`` attribute. For more information on configuring
    or disabling this plugin see :ref:`plugin config`.

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

Query for alerts based on search filter criteria.

::

    $ alerta query [OPTIONS]

    Options:
    -i, --ids UUID       List of alert IDs (can use short 8-char id)
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    --tabular            Tabular output
    --compact            Compact output
    --details            Compact output with details
    -h, --help           Show this message and exit.

:command:`watch`
~~~~~~~~~~~~~~~~

Watch for new alerts.

::

    $ alerta watch [OPTIONS]  

    Options:
    -i, --ids UUID          List of alert IDs (can use short 8-char id)
    -f, --filter FILTER     KEY=VALUE eg. serverity=warning resource=web
    --details               Compact output with details
    -n, --interval SECONDS  Refresh interval
    -h, --help              Show this message and exit.

:command:`top`
~~~~~~~~~~~~~~

Display alerts like unix "top" command.

::

    $ alerta top [OPTIONS]

    Options:
    -h, --help  Show this message and exit.

:command:`raw`
~~~~~~~~~~~~~~

Show raw data for alerts.

::

    $ alerta raw [OPTIONS]

    Options:
    -i, --ids UUID       List of alert IDs (can use short 8-char id)
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -h, --help           Show this message and exit.

:command:`history`
~~~~~~~~~~~~~~~~~~

Show status and severity changes for alerts.

::

    $ alerta history [OPTIONS]

    Options:
    -i, --ids UUID       List of alert IDs (can use short 8-char id)
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -h, --help           Show this message and exit.

:command:`tag`
~~~~~~~~~~~~~~

Add tags to alerts.

::

    $ alerta tag [OPTIONS]

    Options:
    -i, --ids UUID       List of alert IDs (can use short 8-char id)
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -T, --tag TEXT       List of tags  [required]
    -h, --help           Show this message and exit.

:command:`untag`
~~~~~~~~~~~~~~~~

Remove tags from alerts.

::

    $ alerta untag [OPTIONS]

    Options:
    -i, --ids UUID       List of alert IDs (can use short 8-char id)
    -f, --filter FILTER  KEY=VALUE eg. serverity=warning resource=web
    -T, --tag TEXT       List of tags  [required]
    -h, --help           Show this message and exit.ntag alerts ie. remove an assigned tag from alert tag list::

:command:`update`
~~~~~~~~~~~~~~~~~

Update alert attributes.

::

    $ alerta update [OPTIONS]

    Options:
    -i, --ids UUID              List of alert IDs (can use short 8-char id)
    -f, --filter FILTER         KEY=VALUE eg. serverity=warning resource=web
    -A, --attributes KEY=VALUE  List of attributes eg. priority=high  [required]
    -h, --help                  Show this message and exit.

:command:`ack`
~~~~~~~~~~~~~~

Acknowlege alerts ie. change alert ``status`` to ``ack``::

:command:`unack`
~~~~~~~~~~~~~~~~

Unacknowledge alerts ie. change alert ``status`` to ``open``::

:command:`close`
~~~~~~~~~~~~~~~~

Close alerts ie. change alert ``status`` to ``closed``::


:command:`delete`
~~~~~~~~~~~~~~~~~

Delete alerts from server::

:command:`blackout`
~~~~~~~~~~~~~~~~~~~

Blackout alerts based on attributes::

:command:`blackouts`
~~~~~~~~~~~~~~~~~~~~

List all blackout periods::


:command:`heartbeat`
~~~~~~~~~~~~~~~~~~~~

Send a heartbeat to the server::

:command:`heartbeats`
~~~~~~~~~~~~~~~~~~~~~

List all heartbeats::

:command:`user`
~~~~~~~~~~~~~~~

Manage user details (Basic Auth only)::

:command:`users`
~~~~~~~~~~~~~~~~

List all users::


:command:`key`
~~~~~~~~~~~~~~

Create API key::


:command:`keys`
~~~~~~~~~~~~~~~

List all API keys::

:command:`revoke`
~~~~~~~~~~~~~~~~~

Revoke API key::


.. _cli_status:

:command:`status`
~~~~~~~~~~~~~~~~~

Show status and metrics::


:command:`uptime`
~~~~~~~~~~~~~~~~~

Show server uptime::


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
