.. _tutorial 2:

Alert timeouts, heartbeats and House-keeping
============================================

In this tutorial, you will learn how and why to set timeout
values for alerts, how heartbeats can be used to verify system
health and what house-keeping tasks need to be configured
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
"clear" or "ok" state. Timeouts are set on a per-alert basis.

Heartbeats can be sent from any source or by a proxy on behalf of any
source. They are sent at regular intervals within a specified timeout
period otherwise they are considered to be stale. Stale heartbeats
can be used to generate alerts.

Processing alert and heartbeat timeouts requires a scheduled cron job.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
where we installed and configured a basic Alerta instance or you have
access to a similarly configured Alerta server.

Step 1: Housekeeping
--------------------

To work with alert timeouts we first need to setup a regular housekeeping
job that runs every minute to check for stale alerts and update the
status::

    $ vi /usr/local/bin/housekeepingAlerts.js

::

    // housekeepingAlerts.js

    now = new Date();

    // mark timed out alerts as EXPIRED and update alert history
    db.alerts.aggregate([
        { $project: { event: 1, status: 1, lastReceiveId: 1, timeout: 1, expireTime: { $add: [ "$lastReceiveTime", { $multiply: [ "$timeout", 1000 ]} ]} } },
        { $match: { status: { $ne: 'expired' }, expireTime: { $lt: now }, timeout: { $ne: 0 }}}
    ]).forEach( function(alert) {
        db.alerts.update(
            { _id: alert._id },
            {
                $set: { status: 'expired' },
                $push: {
                    history: {
                        event: alert.event,
                        status: 'expired',
                        text: "alert timeout status change",
                        id: alert.lastReceiveId,
                        updateTime: now
                    }
                }
            }, false, true);
    })

    // delete CLOSED or EXPIRED alerts older than 2 hours
    two_hrs_ago = new Date(new Date() - 2*60*60*1000);
    db.alerts.remove({status: {$in: ['closed', 'expired']}, lastReceiveTime: {$lt: two_hrs_ago}});

    // delete INFORM alerts older than 12 hours
    twelve_hrs_ago = new Date(new Date() - 12*60*60*1000);
    db.alerts.remove({severity: 'informational', lastReceiveTime: {$lt: twelve_hrs_ago}});

.. tip::

    Alerts with a timeout value of zero (0) will never be expired and
    therefore never deleted if using the above script.

Add the `cron` entry to run every minute as alerta (creating a user if it
doesn't already exist)::

    $ echo "* * * * * root /usr/bin/mongo --quiet monitoring /usr/local/bin/housekeepingAlerts.js" >/etc/cron.d/alerta

Step 2: Alert Timeouts
----------------------

The default timeout period for an alert is 86400 seconds, or one day.
This means that one day after the alert is last received it should be
considered to be stale and the status changed to "expired".

.. note::

    The alert "lastReceiveTime" is used to determine alert expiry. This
    is so that alerts that continue to be sent within the timeout period
    will never expire.

In addition to expiring timed-out alerts, the script in step 1 is
also responsible for deleting "closed" or "expired" alerts more than
2 hours old and deleting alerts with severity "informational" that
are more than 12 hours old.

Both of these actions can be changed to suit your environment, either
by adjusting the thresholds for deletion or not deleting at all.

Step 3: Heartbeats
------------------

Heartbeats can be sent to the Alerta API using the command-line tool, for
example::

    $ alerta heartbeat --origin dc1-oem-01 --timeout 60

To generate alerts from stale heartbeats run::

    $ alerta heartbeats --alert

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
