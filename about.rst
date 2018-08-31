.. _about:

About
=====

Alerta started at `The Guardian`_ out of necessity as a replacement for a legacy
monitoring tool but only after exhaustively evaluating all credible alternatives
first.

Initially all we wanted was to be able to create alert thresholds against the
hundreds of thousands of `Ganglia metrics`_ collected for the website and view the
alerts in a web console ie. a Ganglia "alerter". Not having a proper name for
this `metrics and monitoring system`_ the working name of "an alerter" stuck and
a simple homophone was chosen to aid future Google searches.

In the end, the thresholding of metrics proved very difficult to scale so we
eventually split the project in two and metric thresholding was given to Riemann
(see `riemann-config`_) and the alert correlation, de-duplication and visualisation
became the "Alerta" project.

Over the years the project has evolved to meet the constantly changing needs of
the `Guardian developer teams`_ as they moved to a more agile, dynamic, "`swimlaned`_"
architecture which has meant, for the operations team, a shift from static,
self-hosted infrastructureto an internal OpenStack cloud to then finally an external
cloud service.

In that time certain key features of Alerta have been deprecated as requirements
changed (eg. the message bus, Ganglia, Riemann) and others added (eg. OAuth2 login,
CloudWatch, Pingdom, PagerDuty integration). In the process it has been slimmed
down to fewer core components making it easier to understand, deploy and manage.

As such, Alerta is now quite different to the somewhat "over engineered" initial
solution but the core concepts of being a flexible, easy-to-use tool remain and
it is now a "cloud-ready" solution adapted to the challenges of a fast changing
environment.

.. _`The Guardian`: http://www.theguardian.com/
.. _Ganglia metrics: https://github.com/ganglia/monitor-core/wiki
.. _`metrics and monitoring system`: https://www.theguardian.com/info/developer-blog/2012/oct/04/winning-the-metrics-battle
.. _Guardian developer teams: https://developers.theguardian.com/
.. _`swimlaned`: http://akfpartners.com/growth-blog/fault-isolative-architectures-or-swimlaning
.. _`riemann-config`: https://github.com/guardian/riemann-config
