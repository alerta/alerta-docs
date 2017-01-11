.. _tutorial 4:

Alerts explored in-depth
========================

In this tutorial you will learn about alert de-duplication and
simple correlation techniques as well as alert tags and custom
attributes, environments and services and more.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: De-duplication`_
  * `Step 2: Simple Correlation`_
  * `Step 3: Automatic status changes`_
  * `Step 4: Tags and Custom attributes`_
  * `Step 5: Environments and Services`_
  * `Step 6: Groups, types and origins`_
  * `Step 7: Saving raw data`_
  * `Next Steps`_

Overview
--------

Though only event and resource are the only mandatory
attributes the standard alert format is extensive with more
than :ref:`two dozen fields <alert format>`.

This tutorial will explain what the different attributes are
and what they are for. And once you understand what the different
attributes are for you will be able to chose more useful values to
assign to them to get the most out of Alerta.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
or you have access to an Alerta server that you can send alerts to
using the ``alerta`` command-line tool.

It would also help to have access to the Alerta web console as
it can be very satisfying to see the alerts update in the console
in realtime rather than having to continually run the ``alerta query``
command to see the results.

Step 1: De-duplication
----------------------

Alert de-duplication is used to reduce the number of alerts in the
console by only displaying the duplicate alerts once but updating
key alert attributes and incrementing a duplicate counter.

To demonstrate de-duplication, run the following command to generate
the same alert, multiple times:

.. code-block:: console

  $ alerta send -r user01 -e loginError -s major -E Production -S Security \
  -t 'user01 login failed.'
  57eb528a-84bf-4080-b54a-37e2888207f3 (indeterminate -> major)

  $ alerta send -r user01 -e loginError -s major -E Production -S Security \
  -t 'user01 login failed.'
  57eb528a-84bf-4080-b54a-37e2888207f3 (1 duplicates)

Note that this is the default behaviour. No special configuration or alert
format is required. As long as the alert resource and event are the same
then alerts will be de-duplicated.

Step 2: Simple Correlation
--------------------------

Alerta has support for simple correlation which means that it can
be configured to update one alert with another related alert.

To demonstrate **simple correlation**, run the following commands to
generate alerts that replace each other and only show the most
recent:

.. code-block:: console

  $ alerta send -r user01 -e loginError -s major -E Production -S Security \
  -t 'user01 login failed.' -C loginError -C loginWarn -C loginOk
  572cb438-5d09-4cdc-babd-410020e3bc15 (indeterminate -> major)

  $ alerta send -r user01 -e loginWarn -s warning -E Production -S Security \
  -t 'user01 password reset.' -C loginError -C loginWarn -C loginOk
  572cb438-5d09-4cdc-babd-410020e3bc15 (major -> warning)

  $ alerta send -r user01 -e loginOk -s normal -E Production -S Security \
  -t 'user01 login success.' -C loginError -C loginWarn -C loginOk
  572cb438-5d09-4cdc-babd-410020e3bc15 (warning -> normal)

The most important part of the above commands were the
``-C loginError -C loginWarn -C loginOk`` arguments. The "-C"
option is short for "--correlate" and informs the Alerta server
that alerts with these events should be correlated together.

Interestingly the de-duplication logic demonstrated in :ref:`Step 1 <>`
above can be used to produce similar results as this simple
correlation.

To demonstrate **correlation by de-duplication** replace the different
login event names with the more generic "loginStatus" and move the
actual event name to "value".

.. code-block:: console

  $ alerta send -r user01 -e loginStatus -v loginError -s major -E Production \
  -S Security -t 'user01 login failed.'
  1acab7c8-e08e-4fef-98ad-3b07ba238120 (indeterminate -> major)

  $ alerta send -r user01 -e loginStatus -v loginWarn -s warning -E Production \
  -S Security -t 'user01 password reset.'
  1acab7c8-e08e-4fef-98ad-3b07ba238120 (major -> warning)

  $ alerta send -r user01 -e loginStatus -v loginOk -s normal -E Production \
  -S Security -t 'user01 login success.'
  1acab7c8-e08e-4fef-98ad-3b07ba238120 (warning -> normal)

This method gives you the benefits of correlation without the overhead
of having to define all the correlated event names in advance.

Step 3: Automatic status changes
--------------------------------

In the examples above you sent alerts with different severities
and they caused the same alert to transition from severity to
severity.

What you might not have noticed is that the alert status also
changed. For example, when a new alert is received the status
was automatically set to ``open``. And when the alert severity
was changed to ``normal`` the status automatically changed to
``closed``.

.. code-block:: console

  $ alerta send -r user01 -e loginStatus -v loginError -s major -E Production \
  -S Security -t 'user01 login failed.'
  12c4d5f4-1be9-436d-a90a-1adc1a473815 (indeterminate -> major)
  => open

  $ alerta send -r user01 -e loginStatus -v loginOk -s normal -E Production \
  -S Security -t 'user01 login success.'
  12c4d5f4-1be9-436d-a90a-1adc1a473815 (major -> normal)
  => closed

In addition to ``open`` and ``closed`` you can set the status
of alerts to ``ack`` or ``assign`` based on your alert handling
procedures.

An important feature of Alerta is that it will automatically
``re-open`` an alert that was ``acked`` if the severity for the
new alert is higher than that already received.

.. code-block:: console

  $ alerta send -r user01 -e loginStatus -v loginError -s major -E Production \
  -S Security -t 'user01 login failed.'
  9df79583-397b-4d6b-8c6e-3f446bd0c7b3 (indeterminate -> major)
  => open

  $ alerta ack --id 9df79583
  => ack

  $ alerta send -r user01 -e loginStatus -v loginError -s critical -E Production \
  -S Security -t 'user01 login failed.'
  9df79583-397b-4d6b-8c6e-3f446bd0c7b3 (major -> critical)
  => open

Alerts are also ``re-opened`` if they are ``closed`` or ``expired``
when any severity except ``normal`` is received for that alert.

.. code-block:: console

  $ alerta send -r user01 -e loginStatus -v loginError -s major -E Production \
  -S Security -t 'user01 login failed.'
  9564d012-1d37-45c2-94c6-ba5e26af8389 (indeterminate -> major)
  => open

  $ alerta send -r user01 -e loginStatus -v loginOk -s normal -E Production \
  -S Security -t 'user01 login success.'
  9564d012-1d37-45c2-94c6-ba5e26af8389 (major -> normal)
  => closed

  $ alerta send -r user01 -e loginStatus -v loginError -s major -E Production \
  -S Security -t 'user01 login failed.'
  9564d012-1d37-45c2-94c6-ba5e26af8389 (normal -> major)
  => open

Step 4: Tags and Custom attributes
----------------------------------

TBC

Step 5: Environments and Services
---------------------------------

TBC

Step 6: Groups, types and origins
---------------------------------

TBC

Step 7: Saving raw data
-----------------------

TBC

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * :ref:`Use alert timeouts to expire stale alerts <tutorial 2>`
  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
