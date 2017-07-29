
Releases
========

Roadmap
+++++++

* Custom alert filters and dashboard views
* Web UI redesign using `Google material design`_

.. _Google material design: https://www.google.com/design/spec/material-design/introduction.html

.. _releases:

Release History
+++++++++++++++

Release 4.9 (16-03-2017)
------------------------

* LDAP authentication via Keycloak_ support
* `MongoDB SSL`_ connection support

.. _Keycloak: https://www.keycloak.org/
.. _MongoDB SSL: http://api.mongodb.com/python/current/examples/tls.html

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

Release 4.6 (26-11-2015)
------------------------

* Customer views for multitenancy_ support
* Authorisation using *Admin* and *User* roles

.. _multitenancy: https://en.wikipedia.org/wiki/Multitenancy

Release 4.5 (9-9-2015)
----------------------

* Added ability to blackout alerts for defined periods
* Use GitLab for OAuth2 login
* Python 3 support (both ``alerta`` client and WSGI server)

Release 4.4 (11-6-2015)
-----------------------

* MongoDB version 3 support

Release 4.3 (12-5-2015)
-----------------------

* Support Basic Auth for user logins

Release 4.2 (13-3-2015)
-----------------------

* PagerDuty webhook integration
* API keys can be `read-only` as well as `read-write`

Release 4.1 (25-2-2015)
-----------------------

* Twitter OAuth login
* API response pagination

Release 4.0 (15-1-2015)
-----------------------

* Change web browser authentication to use JWT tokens
* Improve Google OAuth login and add GitHub OAuth

Release 3.3 (16-12-2014)
------------------------

* Add Amazon AWS CloudWatch, Pingdom web hook integration
* Slack and HipChat plugins

Release 3.2 (11-10-2014)
------------------------

* Major refactor and simplification of server architecture
* Add Google OAuth user logins
* API keys for controlling programatic access
* Add support for server-side custom plugins eg. Logstash, AWS SNS, AMQP
* Deprecated RabbitMQ as a dependency

Release 3.1 (9-5-2014)
----------------------

* Extend API to support new dashboard
* Stability and performance enhancements

Release 3.0 (25-3-2014)
-----------------------

* Deploy server and dashboard as Python WSGI apps
* Add AWS Cloudwatch, PagerDuty and Solarwinds integrations
* Pinger module for host availablity checks
* Start development of `version 3`_ console based on AngularJS

Release 2.0 (11-3-2013)
-----------------------

* Major refactoring into python modules and classes
* API rewrite based on Flask microframework
* Dashboard_ rewritten using Flask server-side templates
* Integrations for AWS SNS, Syslog, Dynect and URL monitoring

Release 1.0 (27-3-2012)
-----------------------

* CGI script receives alerts and pushes to ActiveMQ message bus
* Background daemon reads message bus, processes and stores to MongoDB
* HTML/JavaScript console displays alerts on web dashboard
* Integrations for AWS EC2, Ganglia, IRC, Kibana, Email and SNMP

.. _`#68`: https://github.com/guardian/alerta/issues/68
.. _version 3: https://github.com/alerta/angular-alerta-webui
.. _Dashboard: https://github.com/alerta/alerta-dashboard
.. _first commit: https://github.com/guardian/alerta/commit/a4473ecd39d992deb00c66f454b3a76147dfb38b
