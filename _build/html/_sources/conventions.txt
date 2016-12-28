.. _conventions:

Conventions
===========

Always favour convention over configuration. And any configuration
should have sensible defaults.

Naming Conventions
------------------

Resources
~~~~~~~~~

The key alert attribute name of ``resource`` was specifically chosen
so as not to be host centric. A resource *can* be a hostname, but it
might also be an EC2 instance ID, a Docker container ID or some other
type of non-host unique identifier.

Environments & Services
~~~~~~~~~~~~~~~~~~~~~~~

The environment attribute is used to namespace_ the alert resource.
This allows you to have two resources with the same name (eg. ``web01``)
but that are differentiated by their environments (eg. ``Production``
and ``Development``).

.. _namespace: https://en.wikipedia.org/wiki/Namespace

Choose a set of environments and enforce them. ie. ``PROD``, ``DEV``
or ``Production``, ``Development`` but not both. The same for services
eg. ``MobileAPI``, ``Mobile-API`` and ``mobile api`` are all valid
but needlessly different and impossible to query for consistently
or generate aggregate metrics for.

Note that the service attribute is a **list** because it is common for
infrastructure (ie. some resource) to be used by more than one
service. That is, if a component failure occurs that problem could
cause an outage in multiple services.

Event Names
~~~~~~~~~~~

It can be useful to define a convention when it comes to naming
events. Possible options are:

* Camel case - ``DiskUtilHigh``
* Hierarchy - ``NW:INTERFACE:DOWN``
* SNMP - ``cpuAlarmHigh``

Querying for all Disk utilisation alerts using the ``alerta`` CLI
is then relatively straight-forward::

    $ alerta query --filter event=~DiskUtil

Event Groups
~~~~~~~~~~~~

Another consideration is to ensure you make use of the event group
which gives you the ability to group related alerts.

Some suggested event groups with possible events are listed below.

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

Querying for all performance-related alerts using the ``alerta`` CLI
could then become::

    $ alerta query --filter group=Performance

Severity Levels
---------------

Agree on a subset of severity levels and be consistent with what
they mean. For example, if severity levels are used consistently
then integrating with a paging or email system becomes easier.

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

Once a set of naming conventions are agreed, they can be enforced by
using a simple :ref:`pre-receive <prereceive>` plugin.

A full working example called `reject`_ can be found in the plug-ins
directory of the project code repository and is installed by default.
The server configuration settings :envvar:`ORIGIN_BLACKLIST` and
:envvar:`ALLOWED_ENVIRONMENTS` can be used to tailor it for your
circumstances.

.. _`reject`: https://github.com/guardian/alerta/blob/master/alerta/plugins/reject.py
