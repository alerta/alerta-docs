.. alerta documentation master file, created by
   sphinx-quickstart on Sat Apr  5 19:46:54 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Alerta monitoring system
========================

Alerta accepts alerts from any monitoring system, correlates and de-duplicates them, and then presents them via an API. A web console and a command-line tool are used for visualisation and operational tasks.

There is a standard alert format that all systems need to support

Alert format::

    {
        "status": "unknown",
        "origin": "alert/macbookpro-2.local",
        "resource": "http://example.com",
        "severity": "critical",
        "correlate": [
            "SiteOK",
            "SiteDown"
        ],
        "tags": [
            "EU0167g"
        ],
        "text": "Site is down.",
        "createTime": "2014-04-05T20:50:19.511Z",
        "value": "0/8 available",
        "event": "SiteDown",
        "environment": "production",
        "service": [
            "Web"
        ],
        "rawData": "HTTP/1.1 500 Server Error",
        "timeout": 86400,
        "attributes": {
            "priority": "high"
        },
        "group": "Network",
        "type": "exceptionAlert",
        "id": "9c3c165a-aabb-4c20-8602-dd5ae9548a60"
    }


Server
------

.. toctree::
   :maxdepth: 2

   server
   integrations
   release-notes

Web UI
------

.. toctree::
   :maxdepth: 2

   webui

Client
------

.. toctree::
   :maxdepth: 2

   client

API
---

.. toctree::
   :maxdepth: 1

   api/overview
   api/resources
   api/format
   api/alerts
   api/heartbeats
   api/users
   api/keys
   api/webhooks

Contribute
----------

- Issue Tracker: github.com/guardian/alerta/issues
- Source Code: github.com/guardian/alerta and github.com/alerta

Support
-------

If you have any issues, please let us know.
We have a mailing list located at: alerta-users@google-groups.com
Visit the forum at: https://groups.google.com/d/forum/alerta-users

License
-------

This project is licensed under the Apache license.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

