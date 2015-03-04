.. _conventions:

Conventions
===========

Always favour convention over configuration. And any configuration should have sensible defaults.

Naming Conventions
------------------

Event Names
~~~~~~~~~~~

It can be useful to define a convention when it comes to naming events. Possible options are:

* Camel case - ``DiskUtilHigh``
* Hierarchy - ``NW:INTERFACE:DOWN``
* SNMP - ``cpuAlarmHigh``

Querying for all disk alerts then becomes ``event=~disk``.

Event Groups
~~~~~~~~~~~~

Another consideration is to ensure you make use of the event group which gives you the ability to group related alerts like so:

+--------------------+--------------------------------------------+
| Event Groups       | Events (examples)                          |
+====================+============================================+
| ``Service``        | failures with entire services              |
+--------------------+--------------------------------------------+
| ``Application``    | errors from application logs               |
+--------------------+--------------------------------------------+
| ``OS``             | disk space, time sync failing              |
+--------------------+--------------------------------------------+
| ``Performance``    | system load, swap utilisation high         |
+--------------------+--------------------------------------------+
| ``Configuration``  | config mgmt tool alerts eg. Puppet or Chef |
+--------------------+--------------------------------------------+
| ``Web``            | web server errors                          |
+--------------------+--------------------------------------------+
| ``Syslog``         |                                            |
+--------------------+--------------------------------------------+
| ``Hardware``       |                                            |
+--------------------+--------------------------------------------+
| ``Storage``        |                                            |
+--------------------+--------------------------------------------+
| ``Database``       |                                            |
+--------------------+--------------------------------------------+
| ``Security``       |                                            |
+--------------------+--------------------------------------------+
| ``Network``        |                                            |
+--------------------+--------------------------------------------+
| ``Cloud``          | cloud-based services or infrastructure     |
+--------------------+--------------------------------------------+

Environments & Services
~~~~~~~~~~~~~~~~~~~~~~~

Choose a set of environments and enforce them. ie. ``PROD``, ``DEV`` or ``Production``, ``Developement`` but not both. The same for services eg. ``MobileAPI``, ``Mobile-API`` and ``mobile api`` are all valid but needlessly different and difficult to impossible to trigger on reliably.

Severity Levels
---------------

Agree on a subset of severity levels and be consistent with what they mean. For example, if severity levels are used consistently then integrating with a paging or email system becomes easier.

+--------------+----------------------------------+--------------------------------+
| Severity     | Service Level                    | Notification                   |
+==============+==================================+================================+
| ``critical`` | service unavailable              | immediate page out             |
+--------------+----------------------------------+--------------------------------+
| ``major``    | service impaired still available | page during business hours     |
+--------------+----------------------------------+--------------------------------+
| ``minor``    | component failure                | email only                     |
+--------------+----------------------------------+--------------------------------+
| ``warning``  | everything else                  | consolidate into daily email   |
+--------------+----------------------------------+--------------------------------+

