.. _webui reports:

Reports
=======

The reports page provides aggregate views of alert activity to help identify
problem areas and recurring issues. Navigate to it from the main menu under
*Status > Reports*.

Available Reports
-----------------

Three report types are available:

Top 10 Count
~~~~~~~~~~~~~

Shows the top 10 alerts by total occurrence count. This highlights the
noisiest alert sources -- resources and events that generate the most
duplicate alerts.

Top 10 Flapping
~~~~~~~~~~~~~~~

Shows the top 10 alerts that change severity most frequently. Flapping
alerts indicate unstable conditions where a resource repeatedly transitions
between ok and problem states.

Top 10 Standing
~~~~~~~~~~~~~~~

Shows the top 10 longest-standing alerts -- those that have been in an
open state for the longest duration without being resolved or acknowledged.

Filtering
---------

Each report can be filtered by:

- **Environment** -- restrict the report to a specific environment
- **Service** -- restrict the report to one or more services

Group By
--------

Reports can be grouped by different alert attributes (e.g. resource, event,
service, group) to change the aggregation level. This allows you to see,
for example, the top 10 noisiest resources versus the top 10 noisiest
event types.
