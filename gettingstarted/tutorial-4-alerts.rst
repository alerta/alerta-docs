.. _tutorial 4:

Alerts explored in-depth
========================

In this tutorial you will learn about alert de-duplication and
simple correlation techniques as well as alert tags and custom
attributes, environments and services.

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: De-duplication`_
  * `Step 2: Simple Correlation`_
  * `Step 3: Tags and Custom attributes`_
  * `Step 4: Environments and Services`_
  * `Next Steps`_

Overview
--------

Alert de-duplication and simple correlation available with Alerta
 to take advantage of the state-based
browser and reduce alert console noise.

Prerequisites
-------------

It is assumed that you have completed :ref:`Tutorial 1 <tutorial 1>`
or you have access to an Alerta server that you can send alerts to
using the ``alerta`` command-line tool.

It would also help to have access to the Alerta web console as
it can be very satisfying to see the alerts update in the console
in realtime rather than having to continually run ``alerta query``
to see the results.

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

Not that this is the default behaviour. No special configuration or alert
format is required. As long as the alert resource and event are the same
then alerts will be de-duplicated.

This even works with different severities. Try the above again but with
a different severity this time:

.. code-block:: console

  $ alerta send -r user01 -e loginError -s major -E Production -S Security \
  -t 'user01 login failed.'
  c94750b0-ef16-4f80-94fd-9de0fe789e68 (indeterminate -> major)

  $ alerta send -r user01 -e loginError -s critical -E Production -S Security \
  -t 'user01 login failed.'
  c94750b0-ef16-4f80-94fd-9de0fe789e68 (major -> critical)

This is not strictly a duplicate, because the severity has changed, but
the principle is that as long as the event and resource are the same
then the alert will only be displayed once.

Step 2: Simple Correlation
--------------------------

Alerta has support for simple correlation which means that it can
be configured to replace one alert with another related alert.

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
above can be used to produce a similar results as this simple
correlation.

To demonstrate **correlation by deduplication** replace the different
login event names with "loginStatus" and move the actual event name
to "value".

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

Step 3: Tags and Custom attributes
----------------------------------

TBC

Step 4: Environments and Services
---------------------------------

TBC

Next Steps
----------

After you deploy your Alerta server, you might want to try some of
the following tutorials:

  * :ref:`Use alert timeouts to expire stale alerts <tutorial 2>`
  * Configure a plugin to notify a Slack Channel
  * Send alerts to the Alerta API using the command-line tool
  * Create filtered alert views for different customers
