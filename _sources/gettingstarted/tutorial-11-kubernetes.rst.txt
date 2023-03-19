.. _tutorial 11:

Using Docker to deploy Alerta
=============================

In this tutorial, you will learn how to deploy Alerta using
Kubernetes_.

.. _Kubernetes:

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Run the container`_
  * `Step 2: Customise configuration`_
  * `Step 3: Run using docker-compose`_
  * `Step 4: Install additional plugins or webhooks`_ 
  * `Step 5: Complex setups`_ 
  * `Step 6: Production deployments (Bonus)`_ 
  * `Debugging and Troubleshooting`_ 

Overview
--------

The `"official" Docker image`_ for Alerta has been download more
than `2 million times`_ and contains everything needed
to deploy Alerta in most scenarios, such as:

  * Alerta API
  * Alerta Web UI
  * housekeeping
  * built-in and contributed plugins
  * built-in webhooks
  * all auth providers "ready-to-go"

.. _`"official" Docker image`: https://hub.docker.com/r/alerta/alerta-web/
.. _`2 million times`: https://hub.docker.com/v2/repositories/alerta/alerta-web/

More complex deployments can either use it as a base image and
extend it with additional plugins, webhooks or alternatively,
the Dockerfile_ can be used as a starting point to build your
own base image.

.. _Dockerfile: https://github.com/alerta/docker-alerta/blob/master/Dockerfile

Prerequisites
-------------

To follow this tutorial you will need to `install Minikube`_, the "single-node Kubernetes
cluster in a virtual machine on your personal computer" which you
will need to complete `Step 6`_ where you mimic deploying to production.

.. _install Minikube: https://kubernetes.io/docs/tasks/tools/install-minikube/


