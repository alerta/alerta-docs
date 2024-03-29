## About

Alerta started at [The Guardian](https://www.theguardian.com/media/2011/jan/28/wikileaks-julian-assange-alan-rusbridger)
out of necessity as a replacement for a [legacy monitoring tool](https://www.quest.com/foglight/)
but only after exhaustively evaluating [all](https://www.solarwinds.com/)
[credible](https://www.nagios.org/) [alternatives](https://www.zabbix.com/)
first.

Initially all we wanted was to be able to create alert thresholds against the
hundreds of thousands of [Ganglia metrics](https://github.com/ganglia/monitor-core/wiki)
collected for the website and view the alerts in a web console ie. a Ganglia
"alerter". Not having a proper name for this
[metrics and monitoring system](https://www.theguardian.com/info/developer-blog/2012/oct/04/winning-the-metrics-battle)
the working name of "an alerter" stuck and a simple homophone was chosen
to aid future Google searches.

In the end, the thresholding of metrics proved very difficult to scale so we
eventually split the project in two and metric thresholding was given to Riemann
(see [riemann-config](https://github.com/guardian/riemann-config)) and the
alert correlation, de-duplication and visualisation became the "Alerta" project.

Over the years the project has evolved to meet the constantly changing needs of
the [Guardian developer teams](https://www.theguardian.com/info/2021/oct/29/running-a-post-decade-innovation-retrospective)
as they moved to a more agile, dynamic, "[swimlaned](http://akfpartners.com/growth-blog/fault-isolative-architectures-or-swimlaning)"
architecture which has meant, for the operations team, a shift from static,
self-hosted infrastructure to an internal OpenStack cloud to then finally an external
cloud service.

In that time certain key features of Alerta have been deprecated as requirements
changed (eg. the message bus, Ganglia, Riemann) and others added (eg. OAuth2 login,
CloudWatch, Pingdom, PagerDuty integration). In the process it has been slimmed
down to fewer core components making it easier to understand, deploy and manage.

As a result, Alerta is now quite different to the somewhat "over engineered" initial
solution but the core concepts of being a flexible, easy-to-use tool remain and
it is now a "cloud-ready" solution adapted to the challenges of a fast changing
environment.
