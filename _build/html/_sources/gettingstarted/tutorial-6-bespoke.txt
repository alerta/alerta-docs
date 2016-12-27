.. _tutorial 6:

Bespoke Monitoring
==================


Overview
--------

Monitoring real-world environments using requires very specific work
integrate with monitoring tools.

  * ``alerta`` command-line tool
  * Alerta API
  * Alerta client Python SDK

  - with and without Auth

  - correlation & de-duplication

  resend emails after x https://github.com/alerta/alerta-contrib/issues/64


Custom Severities

  Add a custom severity called ``Fatal`` which will be the new highest severity::

    $ vi /etc/alertad.conf
    SEVERITY_MAP = {
      'fatal': 0,
      'critical': 1,
      ...
    }


    fatal = black

    $ vi config.js