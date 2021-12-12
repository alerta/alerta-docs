
Releases
========

Roadmap
+++++++

* Improve documentation esp. tutorials and web UI guides
* Custom alert filters and dashboard views
* Use OpenAPI (Swagger_) to generate client libraries
* Use Celery tasks for bulk API requests (productionalize)

.. _Swagger: https://swagger.io/specification/

.. _releases:

Release History
+++++++++++++++

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
* Switched to using wheels for distribution via PyPI See https://pythonwheels.com/
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

.. _RBAC: https://csrc.nist.gov/projects/role-based-access-control
.. _SAML2: https://datatracker.ietf.org/doc/html/rfc7522

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
.. _Grafana: https://grafana.com/

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

.. _Prometheus: https://prometheus.io/docs/alerting/latest/alertmanager/
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
