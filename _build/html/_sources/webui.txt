.. _webui:

Alerta Web UI
=============

The Alerta web UI console takes full advantage of the :ref:`state-based Alerta API <state based browser>` to ensure that the most important events at any given time are brought to the attention of operators.

Configuration
-------------

The three main areas for configuration are:

  * defining the Alerta API endpoint
  * enforcing a security strategy
  * selecting colors for severity, highlighting and text

The default web UI :file:`config.js` configuration file is included below. It assumes that the Alerta API is running on the same host (but different port) that the web UI static html files are being served from (line 5), that :ref:`basic auth` will be used (line 6) and so no client id needs to be defined (line 7). Note also that default colours for alert severity, highlighting for multi-select and text are used (line 9):

.. code-block:: javascript
    :linenos:

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "http://"+window.location.hostname+":8080",
        'provider'    : "basic",
        'client_id'   : ""
      })
      .constant('colors', {}); // use default colors

**Example**

An example web UI :file:`config.js` configuration file that assumes that the Alerta API is running on the same host *and port*, but on a different path called ``/api`` (line 5), that :ref:`Google OAuth2 <google oauth2>` is used for authentication (line 6, which requires a valid Google client ID, line 7), and defines different colors for severity levels, highlighting and text (lines 9-26):

.. code-block:: javascript
    :linenos:

    'use strict';

    angular.module('config', [])
      .constant('config', {
        'endpoint'    : "/api",
        'provider'    : "google",
        'client_id'   : "379647311730-sj130ru952o3o7ig8u0ts8np2example.apps.googleusercontent.com"
      })
      .constant('colors', {
        'severity': {
          'critical'     : '#D8122A',
          'major'        : '#EA680F',
          'minor'        : '#FFBE1E',
          'warning'      : '#BA2222',
          'indeterminate': '#A6ACA8',
          'cleared'      : '#00AA5A',
          'normal'       : '#00AA5A',
          'ok'           : '#00AA5A',
          'informational': '#00A1BC',
          'debug'        : '#9D006D',
          'security'     : '#333333',
          'unknown'      : '#A6ACA8'
        },
        'text': 'white',
        'highlight': 'lightgray'
      });


Customer Views
--------------

Managing Alerts
---------------

The browser supports viewing the most recent alerts, a list of the top 10 "worst offenders", and a list of watched alerts.

View Recent Alerts
~~~~~~~~~~~~~~~~~~

Filter by env, svc
Search by any text
Sort by any attribute

showing x out of x (click for another 20 or less)

Multi-select by cmd-click
Action Buttons - open, watch, unwatch, ack, close, delete


.. image:: _static/images/alerta-multi-select-2.png

Alert Details by click
Raw Data
JSON format
Alert History

Top 10
~~~~~~

One of the most important things that can be done to improve the usefulness of an alert console is to reduce the number of alerts to only those that matter.

The top 10 report helps identify alert sources that are the "worst offenders" by grouping by ``event`` name and then sorting by ``count`` and ``duplicateCount``. This report should help operators take corrective action to ensure that the root cause is fixed and reduce the burden of alert management.

In future, this report will support grouping alerts by ``origin``, ``resource``, and event ``group`` and filtering by date range.

.. _watched alerts:

Watching Alerts
~~~~~~~~~~~~~~~

Only logged-in users can watch alerts.


Users
-----

Managing users ...

API Keys
--------

Managing API Keys ...

Blackout Periods
----------------

Managing blackout periods ...


Authentication
--------------

Login
User Profile
Logout

Metrics & Heartbeats
--------------------

Server version and stats


Chrome Extension
----------------

