.. _webui heartbeats:

Heartbeats
==========

The heartbeats page shows the health status of all monitored components that
send periodic heartbeat signals to Alerta. Navigate to it from the main menu
under *Status > Heartbeats*.

Heartbeat List
--------------

Each heartbeat is displayed with the following information:

- **Origin** -- the source that sent the heartbeat (typically a hostname or
  service name)
- **Tags** -- any tags associated with the heartbeat
- **Status** -- one of ``ok``, ``slow``, or ``expired``
- **Latency** -- the round-trip time for the last heartbeat
- **Timeout** -- the configured timeout threshold in seconds
- **Last Receive Time** -- when the last heartbeat was received
- **Customer** -- the customer associated with the heartbeat (if applicable)

Heartbeat Status
~~~~~~~~~~~~~~~~

Status is derived from the timeout and latency values:

- **ok** -- the heartbeat was received within the timeout period
- **slow** -- the heartbeat was received but the latency exceeded a threshold
- **expired** -- no heartbeat was received within the timeout period

Filtering and Search
--------------------

Use the status filter buttons to show only heartbeats matching a particular
status (ok, slow, or expired). The search box allows filtering by origin
or tags.

Heartbeat Alerts
----------------

When a heartbeat expires, Alerta can automatically generate an alert to
notify you of the failure. This is controlled by the ``HEARTBEAT_EVENTS``
server configuration. Expired heartbeats typically generate a ``HeartbeatFail``
alert with ``major`` severity.

Deleting Heartbeats
-------------------

Click the delete icon next to a heartbeat to remove it. This is useful for
cleaning up heartbeats from decommissioned hosts or services that are no
longer sending signals.
