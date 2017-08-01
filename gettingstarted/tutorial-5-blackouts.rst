.. _tutorial 5:

Suppressing Alerts using Blackouts
==================================

In this tutorial you will learn about suppressing alerts during
scheduled downtime using blackout periods.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Blackout Periods by Environment`_
  * `Step 2: Blackout Periods by Resource`_
  * `Step 3: Blackout Periods by Service`_
  * `Step 4: Blackout Periods by Event`_
  * `Step 5: Blackout Periods by Group`_
  * `Step 6: Blackout Periods by Resource-Event`_
  * `Step 7: Blackout Periods by Tag`_
  * `Step 8: Accept alerts during Blackout Periods`_
  * `Next Steps`_

Overview
--------

Being able to suppress alerts during scheduled downtime is important
because false alerts can cause "alert fatigue" and operators can become
complacent.

This tutorial will explain how to suppress alerts by defining blackout
periods that match on different alert attributes. 

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
or you have access to an Alerta server that you can send alerts to
using the ``alerta`` command-line tool.

It would also help to have access to the Alerta web console as
it can be very helpful to see the alerts update in the console
in realtime rather than having to continually run the ``alerta query``
command to see the results.

Step 1: Blackout Periods by Environment
---------------------------------------

Alert suppression works by matching alert attributes against any
active blackout periods. At a minimum, a blackout period must define
an alert ``environment`` to suppress.

To demonstrate how to suppress all alerts for the ``Production``
environment run the following commands:

.. code-block:: console

  $ alerta send -r /dev/disk1 -e FsInodeUtil -s major -E Production -S System \
  -g OS -t '/dev/disk1 inode utilisation high.'
  a85295da-1f0b-4716-a269-7af300ae9fa3 (indeterminate -> major)

  $ alerta blackout -E Production
  26997703-6705-457a-b603-0c151762129c

  $ alerta send -r /dev/disk1 -e FsInodeUtil -s major -E Production -S System \
  -g OS -t '/dev/disk1 inode utilisation high.'
  217ebb7e-b51a-4f15-b8b6-852c5e965894 (Suppressed alert during blackout period)

Instead of responding with "(1 duplicates)" which might have been expected
the response was instead to indicate that the alert matched a blackout
period and would be suppressed.

To confirm that the blackout period is active run:

.. code-block:: console

  $ alerta blackouts
  ID       CUSTOMER         ENVIRONMENT      SERVICE          RESOURCE         EVENT            GROUP            TAGS                     STATUS   START               DURATION
  26997703 *                Production       *                *                *                *                *                        active   2017/08/01 08:27:03 3600s

Note that the short "blackout id" (ie. ``26997703``)  shown in the output
above matches the id returned from the ``alerta`` command.

Step 2: Blackout Periods by Resource
------------------------------------

Step 3: Blackout Periods by Service
------------------------------------

Step 4: Blackout Periods by Event
------------------------------------

Step 5: Blackout Periods by Group
---------------------------------

Step 6: Blackout Periods by Resource-Event
------------------------------------------

Step 7: Blackout Periods by Tag
-------------------------------

Step 8: Accept alerts during Blackout Periods
---------------------------------------------

 app.config.get('BLACKOUT_ACCEPT', []):


 compare blackouts with using a plugin for rejecting

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * :ref:`Use alert timeouts to expire stale alerts <tutorial 2>`
  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
