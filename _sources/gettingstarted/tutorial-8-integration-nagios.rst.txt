.. _tutorial 8 nagios:

Nagios Integration
==================

In this tutorial, you will learn how to integrate Nagios_ with
Alerta so that Nagios host and service alerts are forwarded to
the Alerta API.

.. _Nagios: https://www.nagios.org/

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Install the integration package`_
  * `Step 2: Configure the event handler`_
  * `Step 3: Define notification commands`_
  * `Step 4: Test the integration`_
  * `Next Steps`_

Overview
--------

The ``nagios-alerta`` integration package provides an event handler
script that forwards Nagios notifications to Alerta. Nagios states
are mapped to Alerta severities as follows:

========== ================
Nagios     Alerta Severity
========== ================
CRITICAL   ``critical``
WARNING    ``warning``
UNKNOWN    ``indeterminate``
OK         ``normal``
DOWN       ``major``
UP         ``normal``
========== ================

Prerequisites
-------------

Before you begin, you should have:

  * A working Nagios installation (Nagios Core 4.x or later)
  * A running Alerta server (see :ref:`tutorial 10`)
  * An Alerta API key with ``write:alerts`` scope
  * Python 3.6+ on the Nagios server

.. _Step 1:

Step 1: Install the integration package
----------------------------------------

Install ``nagios-alerta`` on your Nagios server using pip::

    $ pip install nagios-alerta

Verify the installation by checking that the ``alerta-nagios``
script is available::

    $ which alerta-nagios
    /usr/local/bin/alerta-nagios

.. _Step 2:

Step 2: Configure the event handler
------------------------------------

Create or edit the Alerta configuration file used by the event
handler at ``/etc/nagios/alerta.conf``:

.. code-block:: ini

    [alerta]
    endpoint = http://alerta.example.com:8080/api
    key = your-api-key-here

.. _Step 3:

Step 3: Define notification commands
-------------------------------------

Add the following command definitions to your Nagios configuration
(typically in ``/etc/nagios/objects/commands.cfg``):

.. code-block:: cfg

    define command {
        command_name    notify-host-by-alerta
        command_line    /usr/local/bin/alerta-nagios \
                        --endpoint http://alerta.example.com:8080/api \
                        --key $USER10$ \
                        --environment Production \
                        --service Nagios \
                        --host-state "$HOSTSTATE$" \
                        --resource "$HOSTNAME$" \
                        --event "host_down" \
                        --text "$HOSTOUTPUT$"
    }

    define command {
        command_name    notify-service-by-alerta
        command_line    /usr/local/bin/alerta-nagios \
                        --endpoint http://alerta.example.com:8080/api \
                        --key $USER10$ \
                        --environment Production \
                        --service Nagios \
                        --service-state "$SERVICESTATE$" \
                        --resource "$HOSTNAME$" \
                        --event "$SERVICEDESC$" \
                        --text "$SERVICEOUTPUT$"
    }

Set the API key in ``/etc/nagios/resource.cfg`` to avoid exposing
it in the command definition::

    $USER10$=your-api-key-here

Next, assign these commands to a contact or contact group in your
Nagios configuration:

.. code-block:: cfg

    define contact {
        contact_name                    alerta
        alias                           Alerta
        service_notification_commands   notify-service-by-alerta
        host_notification_commands      notify-host-by-alerta
        service_notification_period     24x7
        host_notification_period        24x7
        service_notification_options    w,u,c,r
        host_notification_options       d,u,r
    }

Reload the Nagios configuration to apply the changes::

    $ sudo systemctl reload nagios

.. _Step 4:

Step 4: Test the integration
----------------------------

Trigger a test notification from the Nagios command line::

    $ /usr/local/bin/alerta-nagios \
        --endpoint http://alerta.example.com:8080/api \
        --key your-api-key-here \
        --environment Development \
        --service Nagios \
        --service-state WARNING \
        --resource web01 \
        --event "HTTP Check" \
        --text "Test alert from Nagios"

Verify the alert appears in the Alerta web UI or query using
the CLI::

    $ alerta query --filter resource=web01

You should see the test alert with severity ``warning``.

Next Steps
----------

  * :ref:`Webhook Integrations <tutorial 8 webhooks>`
  * :ref:`Troubleshooting <tutorial 9>`
