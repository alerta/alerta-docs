.. _releases:

Release History
===============

Release 4.5 (9-9-2015)
----------------------

* Added ability to blackout alerts for defined periods

Release 4.4 (11-6-2015)
-----------------------

* MongoDB version 3 support

Release 4.3 (12-5-2015)
-----------------------

* Support Basic Auth for user logins

Release 4.2 (13-3-2015)
-----------------------

* API keys can be `read-only` as well as `read-write`

Release 4.1 (25-2-2015)
-----------------------

* Twitter OAuth login
* API response pagination

Release 4.0 (15-1-2015)
-----------------------

* Change web browser authentication to use JWT tokens
* Add support for Google and GitHub OAuth/OpenID Connect

Release 3.3 (16-12-2014)
------------------------

* Add Amazon AWS Cloudwatch web hook integration

Release 3.2 (11-10-2014)
------------------------

* Major refactor and simplification of server architecture
* Add server-side plug-ins with ``pre_receive()`` and ``post_receive()`` hooks

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

* Major refactoring into python modules
* Replace CGI scripts with Flask microframework
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