.. _tutorial 2:

Alert timeouts, heartbeats and Housekeeping
============================================

In this tutorial, you will learn how and why to set timeout
values for alerts, how heartbeats can be used to verify system
health and what housekeeping tasks need to be configured
to support both of these features.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Housekeeping`_
  * `Step 2: Alert timeouts`_
  * `Step 3: Heartbeats`_
  * `Next Steps`_

Overview
--------

Alert timeout values can be used to automatically "expire" alerts
that are no longer active. Timeouts can be used for any type of
alert but are most useful for alerts which do not have a corresponding
"clear" or "ok" state, such as syslog messages. Timeouts are set on
a per-alert basis.

Heartbeats can be sent from any source or by a proxy on behalf of any
source. They are sent at regular intervals within a specified timeout
period otherwise they are considered to be stale. Stale heartbeats
can be used to generate alerts or availability reports.

Processing alert and heartbeat timeouts requires a scheduled cron job.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
where you installed and configured a basic Alerta instance or you have
access to a similarly configured Alerta server.

Step 1: Housekeeping
--------------------

To work with alert timeouts you first need to setup a regular housekeeping
job that runs every minute to expire and delete alerts. The alerta
command-line client supports this::

    $ alerta housekeeping

Add the `cron` entry to run every minute as root (the root user is used
to keep the tutorial simple however there is nothing about what the
script does that actually requires root access)::

    $ echo "* * * * * root /usr/bin/alerta housekeeping" >/etc/cron.d/alerta

.. tip::

    Your path to the alerta command-line tool may be different. Check
    the path with ``$ which alerta``

Step 2: Alert Timeouts
----------------------

The default timeout period for an alert is 86400 seconds, or one day.
This means that one day after the alert is last received it should be
considered to be stale and the status changed to "expired".

.. note::

    The alert ``lastReceiveTime`` is used to determine alert expiry. This
    is so that alerts that continue to be sent within the timeout period
    will never expire.

In addition to expiring timed-out alerts, the script in step 1 is
also responsible for deleting "closed" or "expired" alerts more than
2 hours old and deleting alerts with severity "informational" that
are more than 12 hours old.

Both of these actions can be changed to suit your environment, either
by adjusting the thresholds for deletion or not deleting at all.

Send a test alert with a short timeout period and verify that once the
timeout period has been exceeded the status is changed to "expired"::

    $ alerta send -r user01 -e fail -s major -E Code -S Security \
    -t 'user01 login failed.' --timeout 20

Step 3: Heartbeats
------------------

Heartbeats can be sent to the Alerta API using the command-line tool, for
example::

    $ alerta heartbeat --origin dc1-oem-01 --timeout 60

To generate alerts from stale heartbeats run::

    $ alerta heartbeats --alert

To set the ``environment`` or ``group`` for a heartbeat alert use tags.

    $ alerta heartbeat -O dc1-oem-02 -T environment:Development -T group:Network

Add the above command as a cron job so that alerts are generated whenever
a heartbeat is stale or slow::

    $ echo "* * * * * root /usr/local/bin/alerta heartbeats --alert" >>/etc/cron.d/alerta

Next Steps
----------

After you setup your housekeeping jobs, you might want to try some of
the following tutorials:

* Configure a plugin to notify a Slack Channel
* Send alerts to the Alerta API using the command-line tool
* Create filtered alert views for different customers
