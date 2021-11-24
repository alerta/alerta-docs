.. _tutorial 5:

Suppressing Alerts using Blackouts
==================================

In this tutorial you will learn about suppressing alerts during
scheduled downtime using blackout periods.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Blackout by Environment`_
  * `Step 2: Blackout by Service or Group`_
  * `Step 3: Blackout by Event and/or Resource`_
  * `Step 4: Blackout by Tag`_
  * `Step 5: Accept alerts during Blackout Periods`_
  * `Step 6: Ending Blackout Periods`_
  * `Next Steps`_

Overview
--------

Being able to suppress or mute alerts during scheduled downtime to
put them into "maintenance mode" is important because false alerts can
cause "alert fatigue" and operators can become complacent.

This tutorial will explain how to suppress alerts by defining blackout
periods that match on different alert attributes. 

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
or you have access to an Alerta server that you can send alerts to
using the ``alerta`` command-line tool.

Preferably you have also completed :ref:`Tutorial 3 <tutorial 3>` which
explains how to enable/disable plugins and how they work. For this tutorial
the "blackout" plugin must be enabled. To enable a built-in plugin simply
add it to the list of ``PLUGINS`` in the server configuration file.

It would also help to have access to the Alerta web console as
it can be very helpful to see the alerts update in the console
in real time rather than having to continually run the ``alerta query``
command to see the results.

Step 1: Blackout by Environment
-------------------------------

Alert suppression works by matching alert attributes against any
active blackout periods. At a minimum, a blackout period must define
an alert ``environment`` to suppress.

To demonstrate how to suppress all alerts for the ``Production``
environment run the following commands:

.. code-block:: console

  $ alerta send -r host05:/dev/disk1 -e FsInodeUtil -s major -E Production -S System \
  -g OS -t '/dev/disk1 inode utilisation high.'
  ed8dd6b3-37a5-4687-8a98-99d318eb6c37 (indeterminate -> major)

  $ alerta blackout --environment Production
  26997703-6705-457a-b603-0c151762129c

  $ alerta send -r host05:/dev/disk1 -e FsInodeUtil -s major -E Production -S System \
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

Step 2: Blackout by Service or Group
------------------------------------

Blanket alert suppression can be acheived by defining a blackout period
based on ``service`` or ``group``:

.. code-block:: console

  $ alerta blackout -E Development -S Network --duration 86400
  51ca8a3b-39fd-4315-a748-9150c63632aa

  $ alerta blackout -E Development -g Performance
  06beb220-26ac-4c8a-9e23-bd05911a13b2

  $ alerta blackouts
  ID       CUSTOMER         ENVIRONMENT      SERVICE          RESOURCE         EVENT            GROUP            TAGS                     STATUS   START               DURATION
  51ca8a3b *                Development      Network          *                *                *                *                        active   2017/08/01 21:02:14 86400s
  06beb220 *                Development      *                *                *                Performance      *                        active   2017/08/01 21:03:36 3600s

Step 3: Blackout by Event and/or Resource
-----------------------------------------

It is possible to suppress alerts from a particular ``resource`` or for
a specific ``event`` (or even more specifically for a particular ``resource``-
``event`` combination).

::

  $ alerta blackout -E Development --resource stl-cr-01 --event linkDown
  3c31b062-e3f5-418a-93be-0b70ee593d58

  $ alerta blackouts
  ID       CUSTOMER         ENVIRONMENT      SERVICE          RESOURCE         EVENT            GROUP            TAGS                     STATUS   START               DURATION
  3c31b062 *                Development      *                stl-cr-01        linkDown         *                *                        active   2017/08/01 21:18:59 3600s

Step 4: Blackout by Tag
-----------------------

When generic blackouts based on ``service`` or ``group``, or specific
blackouts based on ``resource`` or ``event`` don't meet the requirements
it is possible to define a blackout rule based on ``tags`` for maximum
flexibility.

.. code-block:: console

  $ alerta blackout --environment Production --tag blackout
  f4fc4ba5-a36f-4508-bd01-5550124ce26f

  $ alerta send -r host05:/dev/disk1 -e FsInodeUtil -s major -E Production -S System \
  -g OS -t '/dev/disk1 inode utilisation high.' --tag blackout
  488ea442-73b6-4b28-bd3e-dd0ae281d094 (Suppressed alert during blackout period)

.. tip::

  Add the "blackout" ``tag`` dynamically using a pre-receive hook to make
  alert suppression dynamic based on some lookup table, which could be managed
  externally to Alerta.

Step 5: Accept alerts during Blackout Periods
---------------------------------------------

To avoid situations where a blackout rule prevents a ``normal`` or
``ok`` alert from auto-closing an existing alert it is possible to allow
"clearing" alerts that would have otherwise been suppressed.

Set the ``BLACKOUT_ACCEPT`` server configuration variable to the list of
allowable severities::

    BLACKOUT_ACCEPT=['normal', 'ok', 'cleared']

Step 6: Ending Blackout Periods
-------------------------------

Delete blackout periods using the web UI. There is no support for deleting a
current, active blackout period using the ``alerta`` command-line tool. It is
possible to "purge" expired blackout periods::

  $ alerta blackouts --purge
  ID       CUSTOMER         ENVIRONMENT      SERVICE          RESOURCE         EVENT            GROUP            TAGS                     STATUS   START               DURATION
  f4fc4ba5 *                Production       *                *                *                *                blackout                 deleted  2017/08/01 17:35:38 3600s    

Next Steps
----------

Now that you understand alert blackouts, you might want to try some of
the following tutorials:

  * :ref:`Authentication and authorization <tutorial 6>`
  * :ref:`Blackout alerts by customer <tutorial 7>`
