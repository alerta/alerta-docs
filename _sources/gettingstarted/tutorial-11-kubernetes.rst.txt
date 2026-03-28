.. _tutorial 11:

Kubernetes Deployment
=====================

In this tutorial, you will learn how to deploy Alerta to a
Kubernetes_ cluster using the official Docker image.

.. _Kubernetes: https://kubernetes.io/

**Contents**

  * Overview_
  * Prerequisites_
  * `Step 1: Create a namespace`_
  * `Step 2: Deploy PostgreSQL`_
  * `Step 3: Create ConfigMap and Secret`_
  * `Step 4: Deploy the Alerta API`_
  * `Step 5: Create an Ingress`_
  * `Step 6: Verify the deployment`_
  * `Next Steps`_

Overview
--------

The `Alerta Docker image`_ contains the API server, web UI,
housekeeping, plugins, and webhooks. Deploying to Kubernetes
involves creating a database backend, configuring the application
via ConfigMaps and Secrets, and exposing it through a Service
and Ingress.

.. _Alerta Docker image: https://hub.docker.com/r/alerta/alerta-web/

Prerequisites
-------------

Before you begin, you should have:

  * A Kubernetes cluster (Minikube_, kind_, or a managed cluster)
  * ``kubectl`` configured to access the cluster
  * Familiarity with the Docker deployment (see :ref:`tutorial 10`)

.. _Minikube: https://minikube.sigs.k8s.io/
.. _kind: https://kind.sigs.k8s.io/

.. _Step 1:

Step 1: Create a namespace
--------------------------

Create a dedicated namespace for the Alerta deployment::

    $ kubectl create namespace alerta

Set it as the default for subsequent commands::

    $ kubectl config set-context --current --namespace=alerta

.. _Step 2:

Step 2: Deploy PostgreSQL
-------------------------

Deploy a simple PostgreSQL instance using a StatefulSet. Create
a file called ``postgres.yaml``:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: postgres-secret
      namespace: alerta
    type: Opaque
    stringData:
      POSTGRES_USER: alerta
      POSTGRES_PASSWORD: ch4ng3m3
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: postgres
      namespace: alerta
    spec:
      selector:
        app: postgres
      ports:
        - port: 5432
      clusterIP: None
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: postgres
      namespace: alerta
    spec:
      serviceName: postgres
      replicas: 1
      selector:
        matchLabels:
          app: postgres
      template:
        metadata:
          labels:
            app: postgres
        spec:
          containers:
            - name: postgres
              image: postgres:16
              envFrom:
                - secretRef:
                    name: postgres-secret
              ports:
                - containerPort: 5432
              volumeMounts:
                - name: pgdata
                  mountPath: /var/lib/postgresql/data
      volumeClaimTemplates:
        - metadata:
            name: pgdata
          spec:
            accessModes: ["ReadWriteOnce"]
            resources:
              requests:
                storage: 5Gi

Apply it::

    $ kubectl apply -f postgres.yaml

.. note:: For production, consider using a PostgreSQL operator such
   as CloudNativePG_ or a managed database service.

.. _CloudNativePG: https://cloudnative-pg.io/

.. _Step 3:

Step 3: Create ConfigMap and Secret
------------------------------------

Store the Alerta configuration in a ConfigMap and sensitive
values in a Secret:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: alerta-secret
      namespace: alerta
    type: Opaque
    stringData:
      DATABASE_URL: "postgres://alerta:ch4ng3m3@postgres:5432/alerta"
      ADMIN_PASSWORD: "Pa55w0rd"
      ADMIN_KEY: "k8s-admin-api-key"
    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: alerta-config
      namespace: alerta
    data:
      AUTH_REQUIRED: "True"
      ADMIN_USERS: "admin@example.com"
      PLUGINS: "reject,heartbeat,blackout"

Save as ``alerta-config.yaml`` and apply::

    $ kubectl apply -f alerta-config.yaml

.. _Step 4:

Step 4: Deploy the Alerta API
------------------------------

Create a Deployment and Service for the Alerta server. Save
the following as ``alerta-deployment.yaml``:

.. code-block:: yaml

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: alerta
      namespace: alerta
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: alerta
      template:
        metadata:
          labels:
            app: alerta
        spec:
          containers:
            - name: alerta
              image: alerta/alerta-web:latest
              ports:
                - containerPort: 8080
              envFrom:
                - secretRef:
                    name: alerta-secret
                - configMapRef:
                    name: alerta-config
              readinessProbe:
                httpGet:
                  path: /api/management/gtg
                  port: 8080
                initialDelaySeconds: 10
                periodSeconds: 10
              livenessProbe:
                httpGet:
                  path: /_
                  port: 8080
                initialDelaySeconds: 15
                periodSeconds: 20
              resources:
                requests:
                  cpu: 100m
                  memory: 256Mi
                limits:
                  cpu: 500m
                  memory: 512Mi
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: alerta
      namespace: alerta
    spec:
      selector:
        app: alerta
      ports:
        - port: 8080
          targetPort: 8080

Apply it::

    $ kubectl apply -f alerta-deployment.yaml

.. _Step 5:

Step 5: Create an Ingress
--------------------------

Expose Alerta externally using an Ingress resource. This example
assumes an nginx ingress controller is installed:

.. code-block:: yaml

    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: alerta-ingress
      namespace: alerta
      annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
    spec:
      ingressClassName: nginx
      rules:
        - host: alerta.example.com
          http:
            paths:
              - path: /
                pathType: Prefix
                backend:
                  service:
                    name: alerta
                    port:
                      number: 8080

Save as ``alerta-ingress.yaml`` and apply::

    $ kubectl apply -f alerta-ingress.yaml

.. _Step 6:

Step 6: Verify the deployment
------------------------------

Check that all pods are running::

    $ kubectl get pods -n alerta
    NAME                      READY   STATUS    RESTARTS   AGE
    alerta-6d8f9b7c4d-abc12   1/1     Running   0          2m
    alerta-6d8f9b7c4d-def34   1/1     Running   0          2m
    postgres-0                1/1     Running   0          5m

Test the health check endpoint::

    $ kubectl port-forward svc/alerta 8080:8080 -n alerta &
    $ curl http://localhost:8080/api/management/healthcheck
    {"status": "ok"}

Send a test alert::

    $ curl -X POST http://localhost:8080/api/alert \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Key k8s-admin-api-key' \
      -d '{
        "resource": "k8s-test",
        "event": "DeploymentTest",
        "environment": "Development",
        "service": ["Kubernetes"],
        "severity": "informational",
        "text": "Alerta is running on Kubernetes"
      }'

Browse to the web UI at http://localhost:8080 (via port-forward)
or at your Ingress hostname to confirm everything is working.

Next Steps
----------

  * Configure TLS on the Ingress for production use
  * Set up Horizontal Pod Autoscaling for the Alerta Deployment
  * :ref:`Troubleshooting <tutorial 9>`
