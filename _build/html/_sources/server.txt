Alerta Server
=============

Features
--------

- de-duplication & correlation

Installation
------------

$ pip install alerta-server
$ alertad


Deployment
----------

AWS Cloudformation
OpenShift
Docker
Vagrant
Packer
Heroku
Google App Engine / Google Compute Cloud


Event Correlation
-----------------

A core feature of alerta is out-of-the-box de-duplication and simple event correlation.

This means an alert with the same event and resource attributes at the same severity are considered duplicates. If the severity changes they will be collapsed into one alert and only the most recent is shown.

It is also possible to define sets of alerts that should be considered relateed. That is, if a "node_up" is received after a "node_down" then they can be correlated to only show the most recent node status.
