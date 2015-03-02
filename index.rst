Alerta monitoring system
========================

The alerta monitoring system is a tool used to consolidate and de-duplicate alerts from multiple sources for quick 'at-a-glance' visualisation. With just one system you can monitor alerts from many other monitoring tools on a single screen.

Alerta combines a JSON API :ref:`server` for receiving, manipulating and rendering alerts with a simple, yet effective :ref:`webui` and :ref:`command-line tool <cli>`. There are numerous :ref:`integrations <integrations>` with popular monitoring tools and it is easy to add your own using the :ref:`API <api>` directly, the :ref:`Python SDK <development>` or the same command-line tool to :ref:`send alerts <cli_send>`. Access to the API and command-line tool can be restricted using :ref:`API keys <api_keys>` and to the web console using Google or GitHub :ref:`OAuth2 <oauth2>`.

:ref:`Get started <getting_started>` today!

Demo Sites
----------

There are two demonstration and testing sites -- one for Google OAuth and one for GitHub OAuth:

-  http://try.alerta.io (Google OAuth)
-  http://alerta.herokuapp.com (GitHub OAuth)

And two API servers, configured to support Google and GitHub OAuth2:

-  http://api.alerta.io
-  http://alerta-api.herokuapp.com

The API Explorer website can be used to query for, and send alerts to, the http://api.alerta.io API server. The command-line tool ``alerta`` can also be used to generate alerts. The required API key is ``demo-key``.

- http://explorer.alerta.io


.. toctree::
   :hidden:

   getting-started
   server
   webui
   cli
   integrations
   authentication
   development
   faq

.. toctree::
  :glob:
  :titlesonly:
  :hidden:

  api/overview
  api/reference
  api/format

Contribute
----------

- Core project: http://github.com/guardian/alerta
- Integrations, etc: http://github.com/alerta

Support
-------

- Issue Tracker: http://github.com/guardian/alerta/issues

License
-------

This project is licensed under the Apache license.

.. toctree::
   :hidden:

   release-notes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
