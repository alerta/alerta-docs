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

Querying for all CPU alerts using the alerta CLI could then becomes::

    $ alerta query --filter event=~cpu

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
| ``Syslog``         | unix system log messages                   |
+--------------------+--------------------------------------------+
| ``Hardware``       | hardware errors                            |
+--------------------+--------------------------------------------+
| ``Storage``        | NFS, SAN, NAS storage infrastructure       |
+--------------------+--------------------------------------------+
| ``Database``       | database errors, table space utilisation   |
+--------------------+--------------------------------------------+
| ``Security``       | security/authorization messages            |
+--------------------+--------------------------------------------+
| ``Network``        | network devices and infrastructure         |
+--------------------+--------------------------------------------+
| ``Cloud``          | cloud-based services or infrastructure     |
+--------------------+--------------------------------------------+

Querying for all performance-related alerts using the alerta CLI could then become::

    $ alerta query --filter group=Performance

Environments & Services
~~~~~~~~~~~~~~~~~~~~~~~

Choose a set of environments and enforce them. ie. ``PROD``, ``DEV`` or ``Production``, ``Development`` but not both. The same for services eg. ``MobileAPI``, ``Mobile-API`` and ``mobile api`` are all valid but needlessly different and impossible to query for reliably.

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

Enforcing Conventions
---------------------

Once a set of naming conventions are agreed, they can be enforced by using a simple :ref:`pre-receive <pre_receive>` plug-in.

A full working example called `reject`_ can be found in the plug-ins directory of the project code repository and is installed by default. The server configuration settings :envvar:`ORIGIN_BLACKLIST` and :envvar:`ALLOWED_ENVIRONMENTS` can be used to tailor it for your circumstances.

.. _`reject`: https://github.com/guardian/alerta/blob/master/alerta/plugins/reject.py
