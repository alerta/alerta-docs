Alerta monitoring system
========================

The alerta monitoring system is a tool used to consolidate and de-duplicate
alerts from multiple sources for quick 'at-a-glance' visualisation. With
just one system you can monitor alerts from many other monitoring tools
on a single screen.

.. image:: _static/images/alerta-screen-shot-3.png

Alerta combines a JSON API :ref:`server <server>` for receiving, processing and
rendering alerts with a simple, yet effective :ref:`webui` and :ref:`command-line
tool <cli>`. There are numerous :ref:`integrations <integrations>` with popular_
monitoring_ tools_ and it is easy to add your own using the :ref:`API <api>`
directly, the :ref:`Python SDK <development>` or the same command-line tool to
:ref:`send alerts <cli_send>`. Access to the API and command-line tool can be
restricted using :ref:`API keys <api_keys>` and to the web console using
:ref:`Basic Auth <basic auth>` or :ref:`OAuth2 <oauth2>` providers Google,
GitHub and GitLab.

.. _popular: https://www.pingdom.com
.. _monitoring: https://www.nagios.com
.. _tools: https://www.pagerduty.com

:ref:`Get started <quick_start>` today!

Demo Sites
----------

There are two public web consoles available for demonstration and testing:

- https://try.alerta.io (Google OAuth)
- https://alerta.herokuapp.com (BasicAuth)

The web consoles are powered by a single public API which can be used
as a sandbox for integration testing:

- https://alerta-api.herokuapp.com

The "API Explorer" can be used to query for and send alerts to the
public API server:

- https://explorer.alerta.io

The ``alerta`` command-line tool can also be used to generate alerts.
The required API key is ``demo-key``.

.. toctree::
   :maxdepth: 2
   :hidden:

   quick-start
   design
   server
   webui
   cli
   integrations
   configuration
   authentication
   authorization
   deployment
   plugins
   webhooks
   customer-views
   federated
   conventions
   development
   Tutorials <tutorials>
   resources

.. toctree::
  :glob:
  :maxdepth: 2
  :hidden:

  api/reference
  api/query-syntax
  api/alert
  api/heartbeat

Contribute
----------

* Core project: https://github.com/alerta/alerta
* Web UI: https://github.com/alerta/alerta-webui
* Python SDK: https://github.com/alerta/python-alerta-client
* Contributions and integrations: https://github.com/alerta/alerta-contrib
* Docker container: https://github.com/alerta/docker-alerta

Support
-------

* Slack: https://slack.alerta.dev
* :ref:`Frequently Asked Questions <faq>`
* Issue Tracker: https://github.com/alerta/alerta/issues

.. toctree::
   :maxdepth: 1
   :hidden:

   faq

License
-------

This project is licensed under the Apache license, Version 2.0 .

.. toctree::
   :maxdepth: 2
   :hidden:

   release-notes
   about

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
