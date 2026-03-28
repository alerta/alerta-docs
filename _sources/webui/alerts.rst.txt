.. _webui alerts:

Alerts View
===========

The alerts view is the main screen of the Alerta web console. It displays a
summary list of all alerts, colour-coded by severity, with tools for filtering,
searching, and taking action on individual or multiple alerts.

Alert Summary List
------------------

The alert list displays one row per alert with columns that are configurable
via the ``COLUMNS`` server setting. The default columns include severity,
status, last receive time, duplicate count, customer, environment, service,
resource, event, value, and text.

Each row is colour-coded by severity (see :ref:`webui config` for the colour
table). The status is shown as a text label -- ``open``, ``ack``, ``shelved``,
``closed``, ``blackout``, or ``expired``.

Columns can be sorted in ascending or descending order by clicking the column
header.

Environment Tabs
~~~~~~~~~~~~~~~~

Tabs across the top of the alert list allow filtering by environment (e.g.
``Production``, ``Development``). The ``ALL`` tab shows alerts from every
environment. The available tabs are driven by the environments present in
current alerts.

Alert Detail View
~~~~~~~~~~~~~~~~~

Click on an alert row to open the detail view. This shows the full set of
alert attributes, custom attributes, tags, history (status changes and severity
changes with timestamps), and any notes attached to the alert.

From the detail view you can add notes, view raw JSON data, and see the full
alert history timeline.

Alert Actions
~~~~~~~~~~~~~

The following actions are available from the alert detail view or via the
toolbar when alerts are selected:

- **Open** -- reopen a closed or acknowledged alert
- **Ack** -- acknowledge an alert (sets status to ``ack``)
- **Shelve** -- temporarily suppress an alert for a configurable timeout
- **Close** -- close an alert (sets status to ``closed``)
- **Watch** -- add the alert to your personal watch list
- **Delete** -- permanently remove the alert (requires ``delete:alerts`` scope)

Multi-select is supported -- use the checkboxes on the left of each row to
select multiple alerts, then apply an action to all of them at once.

Alert Status Indicators (ASI)
-----------------------------

The ASI panels appear above the alert list and show aggregate counts based
on configurable queries. Three panel types are available: the default panels
show counts by severity, and custom panels can be configured to show counts
for arbitrary alert queries.

Clicking an ASI panel filters the alert list to show only matching alerts.

Search Box
----------

The search box supports a query DSL for filtering alerts. Examples::

    resource:web01
    severity:critical
    service:Web AND status:open
    group:Network
    tags:linux

Use the ``Watched only`` toggle to restrict the view to alerts you are
watching. The ``Full screen`` button hides the navigation bar, and the
``Force refresh`` button reloads the alert list immediately.

Filter Side Bar
---------------

The filter side bar on the left provides faceted filtering by:

- **Status** -- open, ack, shelved, closed, etc.
- **Service** -- filter by one or more service names
- **Group** -- filter by alert group
- **Date/Time** -- filter by time range (last hour, last day, etc.)
- **Customer** -- filter by customer (when customer views are enabled)

More Options
------------

- **Display density** -- toggle between comfortable and compact row spacing
- **Download as CSV** -- export the current alert list to a CSV file
