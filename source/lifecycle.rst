.. _lifecycle:

Alert Lifecycle
===============

Alerta uses a state machine to manage alert status transitions. The status
of an alert changes automatically based on incoming severity changes or
explicitly via operator actions.

Statuses
--------

+-----------------+----------------------------------------------------------+
| Status          | Description                                              |
+=================+==========================================================+
| ``open``        | Alert is new or has been re-opened                       |
+-----------------+----------------------------------------------------------+
| ``assign``      | Alert has been assigned (placeholder, no transitions)    |
+-----------------+----------------------------------------------------------+
| ``ack``         | Alert has been acknowledged by an operator               |
+-----------------+----------------------------------------------------------+
| ``shelved``     | Alert has been shelved (temporarily hidden)              |
+-----------------+----------------------------------------------------------+
| ``blackout``    | Alert was received during a blackout period              |
+-----------------+----------------------------------------------------------+
| ``closed``      | Alert has been closed (normal severity or by operator)   |
+-----------------+----------------------------------------------------------+
| ``expired``     | Alert was not updated within its timeout period          |
+-----------------+----------------------------------------------------------+

Actions
-------

+------------------+---------------------------------------------------------+
| Action           | Description                                             |
+==================+=========================================================+
| ``open``         | Re-open a closed, ack'd or expired alert                |
+------------------+---------------------------------------------------------+
| ``ack``          | Acknowledge an open alert                               |
+------------------+---------------------------------------------------------+
| ``unack``        | Un-acknowledge, returns to previous status               |
+------------------+---------------------------------------------------------+
| ``shelve``       | Shelve an open or ack'd alert                           |
+------------------+---------------------------------------------------------+
| ``unshelve``     | Un-shelve, returns to previous status                   |
+------------------+---------------------------------------------------------+
| ``close``        | Close an alert (sets severity to normal)                |
+------------------+---------------------------------------------------------+
| ``expired``      | System action when alert times out                      |
+------------------+---------------------------------------------------------+
| ``timeout``      | System action on ack/shelve timeout                     |
+------------------+---------------------------------------------------------+

State Transition Table
----------------------

The table below shows the resulting status for each combination of current
status and trigger (operator action or severity change). Empty cells mean
the transition is not valid or the status remains unchanged.

**Operator Actions**

+------------------+------------+------------+------------+------------+------------+
| Current Status   | ``open``   | ``ack``    | ``unack``  | ``shelve`` | ``close``  |
+==================+============+============+============+============+============+
| ``open``         | *invalid*  | ``ack``    | *invalid*  | ``shelved``| ``closed`` |
+------------------+------------+------------+------------+------------+------------+
| ``ack``          | ``open``   | *invalid*  | *previous* | ``shelved``| ``closed`` |
+------------------+------------+------------+------------+------------+------------+
| ``shelved``      | ``open``   | *invalid*  | *invalid*  | *invalid*  | ``closed`` |
+------------------+------------+------------+------------+------------+------------+
| ``blackout``     |            |            |            |            | ``closed`` |
+------------------+------------+------------+------------+------------+------------+
| ``closed``       | ``open``   | *invalid*  |            | *invalid*  | *invalid*  |
+------------------+------------+------------+------------+------------+------------+
| ``expired``      | ``open``   | *invalid*  |            |            |            |
+------------------+------------+------------+------------+------------+------------+

.. note::
    ``unack`` returns to the status the alert had before it was acknowledged.
    ``unshelve`` returns to the status the alert had before it was shelved.

**Severity Changes** (automatic, no operator action)

+------------------+---------------------+-------------------+--------------------+
| Current Status   | More severe         | Less severe       | Normal severity    |
+==================+=====================+===================+====================+
| ``open``         | ``open``            | ``open``          | ``closed``         |
+------------------+---------------------+-------------------+--------------------+
| ``ack``          | ``open`` |dagger|   | ``ack``           | ``closed``         |
+------------------+---------------------+-------------------+--------------------+
| ``shelved``      | ``shelved``         | ``shelved``       | ``closed``         |
+------------------+---------------------+-------------------+--------------------+
| ``blackout``     | *previous*          | *previous*        | ``closed``         |
+------------------+---------------------+-------------------+--------------------+
| ``closed``       | ``open`` |ddagger|  | ``closed``        | ``closed``         |
+------------------+---------------------+-------------------+--------------------+
| ``expired``      | ``open``            | ``open``          | ``closed``         |
+------------------+---------------------+-------------------+--------------------+

.. |dagger| unicode:: U+2020
.. |ddagger| unicode:: U+2021

|dagger| An ack'd alert is re-opened only if the severity genuinely increases
(ie. the previous severity was not the default ``indeterminate``).

|ddagger| A closed alert re-opens to ``shelved`` if it was previously shelved
before being closed.

**System Actions**

+------------------+-----------------------------------------------------+
| Action           | Result                                              |
+==================+=====================================================+
| ``expired``      | Any status -> ``expired``                           |
+------------------+-----------------------------------------------------+
| ``timeout``      | If previously ``ack`` -> ``ack``, otherwise ``open``|
+------------------+-----------------------------------------------------+

**Blackout Transitions**

When a blackout period ends, the alert returns to the status it had before
the blackout began. If the alert was created during a blackout (no previous
status), it transitions based on the current severity.

**Custom Actions**

Unrecognised actions (ie. custom actions defined by plugins via the
``take_action`` hook) do not trigger any state transition. The severity
and status are returned unchanged.

**Plugin Overrides**

If a ``pre_receive()`` plugin sets a non-default status on the alert, the
state machine respects that status and skips the normal transition logic.
The only exception is normal-severity alerts, which are always auto-closed
regardless of the plugin-set status.
