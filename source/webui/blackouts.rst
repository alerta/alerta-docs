.. _webui blackouts:

Blackouts
=========

Blackout periods suppress alert notifications and actions for matching alerts
during a defined time window. This is useful for planned maintenance windows
or known-noisy periods. Navigate to the blackouts page from the main menu
under *Configuration > Blackouts*.

Creating a Blackout
-------------------

Click the **+** button to create a new blackout. The following fields are
available:

- **Environment** (required) -- the environment to apply the blackout to
- **Resource** -- match a specific resource
- **Service** -- match one or more services
- **Event** -- match a specific event name
- **Group** -- match an alert group
- **Tags** -- match alerts with specific tags
- **Start time** -- when the blackout begins (defaults to now)
- **Duration** -- how long the blackout lasts, or set an explicit end time

The more fields you specify, the narrower the blackout scope. A blackout
with only an environment set will suppress all alerts in that environment.

.. note:: Alerts that match an active blackout are set to ``blackout`` status
          and will not trigger any notification plugins. When the blackout
          expires, suppressed alerts revert to their previous status.

Listing Blackouts
-----------------

The blackout list shows all blackouts with the following information:

- **Environment** and matching criteria (resource, service, event, etc.)
- **Start** and **End** times
- **Status** -- ``pending`` (not yet started), ``active`` (currently in
  effect), or ``expired`` (past the end time)
- **Duration** -- the total blackout duration

Active blackouts are highlighted to make them easy to identify.

Editing and Deleting
--------------------

Click on a blackout to edit its details, including the matching criteria and
time window. Click the delete icon to remove a blackout. Deleting an active
blackout immediately stops suppression of matching alerts.
