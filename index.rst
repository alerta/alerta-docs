.. alerta documentation master file, created by
   sphinx-quickstart on Sat Apr  5 19:46:54 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Alerta : Monitoring Tool
========================

Alerta accepts alerts from any monitoring system, correlates and deduplicates them, and then presents them via a web console.

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

Contents:

.. toctree::
   :maxdepth: 2

   alert
   api
   api/alerts
   api/heartbeats
   api/webhooks
   client
   correlation

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

