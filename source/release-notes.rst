
Releases
========

Roadmap
+++++++

* Improve documentation esp. tutorials and web UI guides
* Custom alert filters and dashboard views
* Use OpenAPI (Swagger_) to generate client libraries

.. _Swagger: https://swagger.io/specification/

.. _releases:

Release History
+++++++++++++++

.. _release_9_1:

Release 9.1.0 (28-03-2026)
--------------------------

* CAS (Central Authentication Service) authentication provider
* Pagination support for environments endpoint
* Alert counters for rejected, rate-limited and blackout alerts
* SQL injection prevention in Postgres query parser
* Self-update endpoint restricted to allowlisted fields
* Allow LDAP users with no email set to log in
* Python 3.12 support

.. _release_9_0:

Release 9.0.0 (17-03-2023)
--------------------------

* Major version bump with breaking changes
* Bulk API tag, untag and attributes endpoints
* Proxy authentication support (``AUTH_PROXY``)
* Forwarder, heartbeat, remote_ip, escalate, timeout and acked_by added as built-in plugins
* ``StrEnum`` dependency for enums
* Replaced ``pkg_resources`` with ``importlib.metadata``
* Support custom backends defined as entry points
* Show or hide API server version info
* Add ``CLIPBOARD_TEMPLATE`` setting
* Security fix for auth bypass via registration when ``AUTH_PROVIDER != basic``
* Do not expose exception errors to end users
* End support for Python 3.6 and Python 3.7

.. _release_8_7:

Release 8.7.0 (06-12-2021)
--------------------------

* Support all OpenID Connect ``client_secret_*`` token endpoint auth methods
* Use GitHub teams for role lookup
* Optionally print warnings if database create fails
* Prometheus metrics uptime stat
* Dependency updates for security (cryptography, PyJWT, pyparsing)

.. _release_8_6:

Release 8.6.0 (20-05-2021)
--------------------------

* Escalate severity custom action plugin
* Support for user-defined API keys
* Support read-only users
* Add alert origin to blackout options
* Support custom auth scopes
* Support custom top10 report sizes
* Log dismissing notes to alert history
* Add default blackout duration to config endpoint

.. _release_8_4:

Release 8.4.0 (27-02-2021)
--------------------------

* Timeout policy plugin to enforce ack and shelve timeouts
* Support for custom error responses in plugins and webhooks
* Add pagination support to collection responses
* Syslog logging output format
* Add colors for Ack and Shelved statuses
* Add allowed environments to config endpoint
* Add ``X-Request-ID`` as CORS header
* Performance improvement: do not query for ``rawData`` or ``history`` if not required

.. _release_8_1:

Release 8.1.0 (05-11-2020)
--------------------------

* Refactor LDAP auth to simplify configuration
* Configurable default user and guest roles
* Do not allow LDAP login with empty password
* Hide fields with large data from default alerts response (eg. ``rawData`` and alert history)
* Switch from Travis CI to GitHub Actions for CI testing

.. _release_8_0:

Release 8.0.0 (22-06-2020)
--------------------------

* Major version bump
* End support for Python 3.5
* Fix sort-by severity and status, and reverse sort
* Update Grafana webhook for rule tags

.. _release_7_0:

Release 7.0.0 (14-04-2019)
--------------------------

* Web UI `version 7`_ complete redesign based on `Vue.js`_ and `Vuetify`_
* Supports any OpenID Connect compliant auth provider
* Add user groups for Basic Auth role and customer assignment
* Edit users, groups, customers, blackouts, permissions and API keys
* Added user preferences eg. custom shelve time, date/time formats and dark mode
* Add operator notes to alerts and supplementary notes to alert actions
* Multi-select alerts and actions on hover
* Minimum MongoDB version is now 3.2

.. _version 7: https://github.com/alerta/alerta-webui
.. _Google material design: https://www.google.com/design/spec/material-design/introduction.html
.. _Vue.js: https://vuejs.org/
.. _Vuetify: https://vuetifyjs.com

.. _release_6_8:

Release 6.8.0 (2-3-2019)
------------------------

* Prevent invalid actions for a given alert status
* Lock down Python package versions for deterministic builds
* And sundry fixes

.. _release_6_7:

Release 6.7.0 (17-1-2019)
-------------------------

* Sundry fixes

.. _release_6_6:

Release 6.6.0 (1-1-2019)
------------------------

* Remove dependency on deprecated Google+ API (#788)

.. _release_6_5:

Release 6.5.0 (23-11-2018)
--------------------------

* Add missing single resource endpoints (#763)

.. _release_6_4:

Release 6.4.0 (14-11-2018)
--------------------------

* Add audit trail for "admin", "write" and "auth" requests
* Fix bi-directional prometheus integration (#740)

.. _release_6_3:

Release 6.3.0 (21-10-2018)
--------------------------

* Enhance query to use :ref:`Lucene query syntax <query_string_syntax>`
* Add "proxy fix" server config option if using SSL terminating proxy

.. _release_6_2:

Release 6.2.0 (13-10-2018)
--------------------------

* Make web UI alert list columns user-configurable
* Add "take action" method to plugins for triggering external actions
* Allow admins to sign-up new users even when sign-up is disabled
* Add filtering and auto-refresh to Watch List and Top10 web pages
* Show all possible menu options when authentication not enabled
* Use scopes instead of type aliases when defining API key permissions

.. _release_6_1:

Release 6.1.0 (11-10-2018)
--------------------------

* Added bulk API endpoints for background processing (experimental)
* Added alternative alarm model based on ISA 18.2 / IEC 62682 (experimental)
* Allow users to replace "alerta" web navbar logo with company logo
* Sort by "Create Time" for better integration with Prometheus
* Lots more Python 3 type annotations (and some resulting bug fixes)
*  Remove redundant duplicate messages from API logging
* Run tests against Python 3.7 & MongoDB 4.0 for forward compatibility checking
* Add date/time formats and audio back to web UI config and tweak severity colors
* Add support for X-API-Key authentication header (for OpenAPI support)

.. _release_6_0:

Release 6.0.0 (18-09-2018)
--------------------------

* First release to support Python 3 only
* Add static type checking to build pipeline and start type annotations
* Add audit info for blackouts including user and reason
* Support every combination of alert attribute for blackouts
* Config API endpoint for dynamically updating client configuration
* Improved email confirmation and user reset of forgotten passwords

.. _release_5_2:

Release 5.2.0 (25-04-2018)
--------------------------

* First release to support Python 3.6+ only
* Final release to support Python 2.7
* LDAP authentication support for BasicAuth logins
* Change "status" endpoints to "action" endpoints
* Allow admin to override customer assigned to an alert

.. _release_5_1:

Release 5.1.0 (08-04-2018)
--------------------------

* alarm shelving for temporarily removing alerts from the main alert list
* new blackout status that don't trigger plugins to keep track of suppressed alerts
* add history entry for de-duplicated alerts with a value change
* multiple customers for auth providers that allow membership of more than one group
* Python 3 support only (no breaking changes for Python 2, yet)

.. _release_5_0:

Release 5.0.0 (07-10-2017)
--------------------------

* Support for PostgreSQL (including Amazon RDS and Google Cloud SQL)
* API responses are Gzipped to make everything faster
* Development command line has changed from `alertad` to `alertad run`
* Major code refactor with flatter structure (beware imports! see next)
* WSGI import has changed from `from alerta.app import app` to simply `from alerta import app`
* Plugins import has changed from `from alerta.app import app` to `from alerta.plugins import app`
* Blackout is now a plugin so it can be disabled and replaced with a custom blackout handler
* Switched to using wheels for distribution via PyPI See http://pythonwheels.com/
* Alerta API now supports multiple roles for BasicAuth (though not supported in the web UI yet)
* Alert format: `value` is now always cast to a string.
* Added `/management/housekeeping` URL to replace `housekeepingAlerts.js` cron job script
* `DATABASE_URL` connection URI setting replaces every other MongoDB setting with a non-mongo specific variable

.. _release_4_10:

Release 4.10 (27-07-2017)
-------------------------

* Scope-based permissions model based on RBAC_
* SAML2_ authentication user logins
* Prometheus webhook updated to support version 4
* Plugin result chaining for tags and attributes

.. _RBAC: http://csrc.nist.gov/groups/SNS/rbac/
.. _SAML2: https://tools.ietf.org/html/rfc7522

.. _release_4_9:

Release 4.9 (16-03-2017)
------------------------

* LDAP authentication via Keycloak_ support
* `MongoDB SSL`_ connection support
* Pingdom webhook changed to use new "State change" webhook

.. _Keycloak: https://www.keycloak.org/
.. _MongoDB SSL: http://api.mongodb.com/python/current/examples/tls.html

.. _release_4_8:

Release 4.8 (05-09-2016)
------------------------

* Use GitHub Enterprise for OAuth2 login
* Riemann_ webhook integration
* Telegram_ webhook and `related plugin`_ for bi-directional integration
* Grafana_ webhook integration
* Switch to MongoDB URI connection string format
* Added simple *good-to-go* health check
* Added "flap detection" utility method for use in plugins
* Fix oEmbed API endpoint
* Default severity changed from "unknown" to "indeterminate"
* Add routing rules for plugins

.. _Riemann: http://riemann.io/
.. _Telegram: https://telegram.org/
.. _related plugin: https://github.com/alerta/alerta-contrib/tree/master/plugins/telegram
.. _Grafana: http://grafana.org/

.. _release_4_7:

Release 4.7 (24-01-2016)
------------------------

* Prometheus_ webhook integration
* `Google Stackdriver`_ webhook integration
* Configurable severities
* Blackout periods by customer
* Status change hook for plugins
* Require authentication on webhooks if auth enabled
* Limit alert history in MongoDB
* Send email confirmation for Basic Auth sign-ups
* Removed support for Twitter OAuth1

.. _Prometheus: http://prometheus.io/docs/alerting/alertmanager/
.. _Google Stackdriver: https://cloud.google.com/stackdriver/

.. _release_4_6:

Release 4.6 (26-11-2015)
------------------------

* Customer views for multitenancy_ support
* Authorisation using *Admin* and *User* roles

.. _multitenancy: https://en.wikipedia.org/wiki/Multitenancy

.. _release_4_5:

Release 4.5 (9-9-2015)
----------------------

* Added ability to blackout alerts for defined periods
* Use GitLab for OAuth2 login
* Python 3 support (both ``alerta`` client and WSGI server)

.. _release_4_4:

Release 4.4 (11-6-2015)
-----------------------

* MongoDB version 3 support

.. _release_4_3:

Release 4.3 (12-5-2015)
-----------------------

* Support Basic Auth for user logins

.. _release_4_2:

Release 4.2 (13-3-2015)
-----------------------

* PagerDuty webhook integration
* API keys can be `read-only` as well as `read-write`

.. _release_4_1:

Release 4.1 (25-2-2015)
-----------------------

* Twitter OAuth login
* API response pagination

.. _release_4_0:

Release 4.0 (15-1-2015)
-----------------------

* Change web browser authentication to use JWT tokens
* Improve Google OAuth login and add GitHub OAuth

.. _release_3_3:

Release 3.3 (16-12-2014)
------------------------

* Add Amazon AWS CloudWatch, Pingdom web hook integration
* Slack and HipChat plugins

.. _release_3_2:

Release 3.2 (11-10-2014)
------------------------

* Major refactor and simplification of server architecture
* Add Google OAuth user logins
* API keys for controlling programatic access
* Add support for server-side custom plugins eg. Logstash, AWS SNS, AMQP
* Deprecated RabbitMQ as a dependency

.. _release_3_1:

Release 3.1 (9-5-2014)
----------------------

* Extend API to support new dashboard
* Stability and performance enhancements

.. _release_3_0:

Release 3.0 (25-3-2014)
-----------------------

* Deploy server and dashboard as Python WSGI apps
* Add AWS Cloudwatch, PagerDuty and Solarwinds integrations
* Pinger module for host availablity checks
* Start development of `version 3`_ console based on AngularJS

.. _release_2_0:

Release 2.0 (11-3-2013)
-----------------------

* Major refactoring into python modules and classes
* API rewrite based on Flask microframework
* Dashboard_ rewritten using Flask server-side templates
* Integrations for AWS SNS, Syslog, Dynect and URL monitoring

.. _release_1_0:

Release 1.0 (27-3-2012)
-----------------------

* CGI script receives alerts and pushes to ActiveMQ message bus
* Background daemon reads message bus, processes and stores to MongoDB
* HTML/JavaScript console displays alerts on web dashboard
* Integrations for AWS EC2, Ganglia, IRC, Kibana, Email and SNMP

.. _`#68`: https://github.com/alerta/alerta/issues/68
.. _version 3: https://github.com/alerta/angular-alerta-webui
.. _Dashboard: https://github.com/alerta/alerta-dashboard
.. _first commit: https://github.com/alerta/alerta/commit/a4473ecd39d992deb00c66f454b3a76147dfb38b
