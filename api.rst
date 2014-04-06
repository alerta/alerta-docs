REST API v3 Resources
=====================

Alerts
------
Alerts are received and processed before being added to database.

| Resource | Description |
| -------- | -------- |
| [GET /api/alerts?:query](/docs/api/get/alerts) | Returns all alerts or all alerts that meet the query filter. |
| [POST /api/alert](/docs/api/post/alert) | foo |
| [GET /api/alert/:id](/docs/api/get/alert) | foo |
| [POST /api/alert/:id/tag](/docs/api/post/alert/tag) | foo |
| [POST /api/alert/:id/status](/docs/api/post/alert/status) | foo |
| [DELETE /api/alert/:id](/docs/api/delete/alert) | foo |

Heartbeats
----------

Heartbeats are sent from something at regular intervals to ensure that it is operating.

| Resource | Description |
| -------- | -------- |
| [GET /api/heartbeats](/docs/api/get/heartbeats) | foo |
| [POST /api/heartbeat](/docs/api/post/heartbeat) | foo |
| [DELETE /api/heartbeat/:id](/docs/api/delete/heartbeat) | foo |

Web Hooks
---------