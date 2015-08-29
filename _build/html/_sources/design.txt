.. _design:

Design Principles
=================

The following principles guided the design and development of the Alerta monitoring system.

Resource under alarm
---------------------

A :ref:`resource <alert_attributes>` is any entity that it makes sense for you to receive alerts for. You shouldn't be forced to accept a certain "world view" when using a monitoring tool or to repurpose a "host" field for a service or application, or a even a URL. Host-centric monitoring tools belong in the 90's.

Many severity levels
--------------------

You are free to use as many or as few as you like eg. if you plan to only integrate with Nagios then only use ``critical``, ``warning`` and ``ok``. If you are integrating with a fault management system for a telco you might want to use the six `ISO perceived severity levels`_ or alternatively, if you are pushing application alerts you might want to consider using the ``debug`` severity level.

.. _`ISO perceived severity levels`: http://www.itu.int/rec/T-REC-X.733/en

Robust alert reception
----------------------

In accordance with the `robustness principle`_ which is to "be liberal in what you accept from others", alerta will accept any alert as long as it meets the alert format specification. ie. no field needs to be defined in advance for it to be accepted, however the benefits of following a standard :ref:`convention <conventions>` for such attributes as ``environment``, ``service``, ``event`` and ``resource`` (as internally defined by and useful to you) are many.

.. _`robustness principle`: http://en.wikipedia.org/wiki/Robustness_principle

Self-clearing alerts
--------------------

All alerts should have a corresponding ``cleared`` or ``normal`` state so that non-normal alerts can be automatically cleared down by the system. Where an alert cannot send a corresponding clear an alert should specify a ``timeout`` (or have a default assigned) after which it will be deleted.

Alerts are cheap
----------------

Alerts should be resent at regular intervals if they are still active which means that if all data is lost after a certain amount of time (eg. 2 hours?) you are back to where you were. This will be generally true, however, for some alert sources this isn't possible eg. SNMP traps, log errors. Alerts in a normal state can be resent at a longer interval.

Tags and custom attributes
--------------------------

Dynamic 'scale up'/'scale down' environments are the defacto standard now; naming individual servers is lame. Use service discovery and dynamically generated metadata to tag alerts and dynamically assign custom attributes.