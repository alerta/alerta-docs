.. _tutorial 8 zabbix:

Integration with Zabbix
=======================

In this tutorial, you will learn how to configure Zabbix_ to
forward alerts to Alerta using the ``zabbix-alerta`` integration
package.

.. _Zabbix: https://www.zabbix.com/

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Install zabbix-alerta`_
  * `Step 2: Configure the alert script`_
  * `Step 3: Create a Zabbix media type`_
  * `Step 4: Create an action`_
  * `Step 5: Test the integration`_
  * `Next Steps`_

Overview
--------

The ``zabbix-alerta`` package provides an alert script that Zabbix
calls when a trigger fires. Zabbix severities are mapped to Alerta
severities as follows:

==================== ================
Zabbix Severity      Alerta Severity
==================== ================
Disaster             ``critical``
High                 ``major``
Average              ``minor``
Warning              ``warning``
Information          ``informational``
Not classified       ``indeterminate``
OK (resolved)        ``normal``
==================== ================

Prerequisites
-------------

Before you begin, you should have:

  * Zabbix Server 4.0 or later
  * A running Alerta server (see :ref:`tutorial 10`)
  * An Alerta API key with ``write:alerts`` scope
  * Python 3.6+ on the Zabbix server

.. _Step 1:

Step 1: Install zabbix-alerta
-----------------------------

Install the integration package on your Zabbix server::

    $ pip install zabbix-alerta

Find the Zabbix ``AlertScriptsPath`` by checking the Zabbix server
configuration::

    $ grep AlertScriptsPath /etc/zabbix/zabbix_server.conf
    AlertScriptsPath=/usr/lib/zabbix/alertscripts

Create a symlink so Zabbix can find the script::

    $ ln -s $(which zabbix-alerta) /usr/lib/zabbix/alertscripts/

.. _Step 2:

Step 2: Configure the alert script
-----------------------------------

Create a configuration file at ``/etc/alerta/zabbix-alerta.conf``:

.. code-block:: ini

    [alerta]
    endpoint = http://alerta.example.com:8080/api
    key = your-api-key-here
    environment = Production

Test the script from the command line to verify connectivity::

    $ zabbix-alerta --endpoint http://alerta.example.com:8080/api \
        --key your-api-key-here \
        --environment Development \
        --severity warning \
        --resource zabbix-test \
        --event "Test Trigger" \
        --text "Testing zabbix-alerta integration"

.. _Step 3:

Step 3: Create a Zabbix media type
-----------------------------------

In the Zabbix web UI, navigate to **Administration > Media types**
and create a new media type:

  * **Name:** Alerta
  * **Type:** Script
  * **Script name:** zabbix-alerta
  * **Script parameters:**

    #. ``{ALERT.SENDTO}``
    #. ``{ALERT.SUBJECT}``
    #. ``{ALERT.MESSAGE}``

Then assign the ``Alerta`` media type to a Zabbix user under
**Administration > Users**. Set the **Send to** field to the
Alerta API endpoint URL.

.. _Step 4:

Step 4: Create an action
-------------------------

Navigate to **Configuration > Actions** and create a new trigger
action:

  * **Name:** Send to Alerta
  * **Conditions:** Select the trigger severities you want to forward
  * **Operations:** Add an operation that sends a message to
    the user configured in Step 3

For the **Default message**, use the following template so the
integration script can parse trigger details:

.. code-block:: text

    resource={HOST.NAME}
    event={TRIGGER.NAME}
    environment=Production
    severity={TRIGGER.SEVERITY}
    status={TRIGGER.STATUS}
    value={TRIGGER.VALUE}
    text={ITEM.LASTVALUE}
    tags=zabbix,{TRIGGER.TAGS}

Set the **Recovery message** similarly, but with ``status=OK``.

.. _Step 5:

Step 5: Test the integration
-----------------------------

Create a simple test trigger in Zabbix on a monitored host, or
use the Zabbix ``zabbix_sender`` utility to push a test value
that triggers an existing threshold::

    $ zabbix_sender -z zabbix-server -s "test-host" -k test.key -o 100

Check the Alerta web UI or CLI to verify the alert was received::

    $ alerta query --filter resource=test-host

Once confirmed, you can disable or remove the test trigger.

Next Steps
----------

  * :ref:`Webhook Integrations <tutorial 8 webhooks>`
  * :ref:`Troubleshooting <tutorial 9>`
