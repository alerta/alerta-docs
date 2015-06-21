.. _about:

About
=====

Alerta started out of necessity as a replacement for a legacy monitoring tool but only after exhaustively evaluating all credible alternatives first.

Initially all we wanted was to be able to create alert thresholds for our significant Ganglia install base [#]_ and view the alerts in a web console -- ie. a Ganglia "alerter". Not having a proper name for the project the working name of "an alerter" stuck and a simple homophone was chosen to aid future Google searches.

In the end, the thresholding of metrics proved very difficult to scale so we eventually split the project in two and metric thresholding was given to Riemann (see riemann-config) and the alert correlation, de-duplication and visualisation became "alerta".

Over the years the project has evovled to meet the needs of the Guardian development teams as they moved to a more agile, dynamic, "`swimlaned`_" architecture which has meant, for the operations team, a shift from static, self-hosted infrastructure to an internal OpenStack cloud to finally an external cloud service.

In that time certain key features of alerta have been deprecated as requirements changed (eg. the message bus, Ganglia, Riemann) and others added (eg. OAuth2 login, CloudWatch, Pingdom, PagerDuty integration). In the process it has been slimmed down with fewer components making it easier to understand, deploy and manage.

As such, alerta is now quite different to the somewhat "over engineered" initial solution but the core concepts of being a flexible, easy-to-use tool remain and it is now a "cloud-ready" solution adapted to challenges of a fast changing environment.

.. _`swimlaned`: http://akfpartners.com/techblog/2008/05/30/fault-isolative-architectures-or-%E2%80%9Cswimlaning%E2%80%9D/

.. _[#] A monitoring tool should not need to collect it's own metrics, you should alert from what you already collect with metric tools.
