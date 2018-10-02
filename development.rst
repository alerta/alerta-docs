.. _development:

Development
===========

Python SDK
----------

Alerta is developed in Python so the Python SDK is a core component of the monitoring system.

Installation
~~~~~~~~~~~~

Install using pip:

::

    $ pip install alerta

Install master branch directly from GitHub:

::

    $ pip install git+https://github.com/alerta/python-alerta-client.git@master

Examples
~~~~~~~~

Initialise the alerta API client:

.. code-block:: python

    >>> from alertaclient.api import Client
    >>> client = Client(endpoint='https://alerta-api.herokuapps.com', key='demo-key')

Send an alert:

.. code-block:: python

    >>> client.send_alert(resource='foo', event='bar')
    ...
    alertaclient.exceptions.UnknownError: [POLICY] Alert environment does not match one of Production, Development

Send an alert again, this time including the required ``environment`` and ``service``:

.. code-block:: python

    >>> client.send_alert(resource='foo', event='bar', environment='Development', service=['Web'])
    ('fd3ecad4-6558-4ec7-96cc-aff6cdf1fabc', Alert(id='fd3ecad4-6558-4ec7-96cc-aff6cdf1fabc', environment='Development', resource='foo', event='bar', severity='normal', status='closed', customer=None), None)

Query for the alert just sent, by alert ID:

.. code-block:: python

    >>> client.get_alert('fd3ecad4-6558-4ec7-96cc-aff6cdf1fabc')
    Alert(id='fd3ecad4-6558-4ec7-96cc-aff6cdf1fabc', environment='Development', resource='foo', event='bar', severity='normal', status='closed', customer=None)

Search for alerts by attributes:

.. code-block:: python

    >>> client.get_alerts([('resource','foo'),('environment','Development')])
    [Alert(id='fd3ecad4-6558-4ec7-96cc-aff6cdf1fabc', environment='Development', resource='foo', event='bar', severity='normal', status='closed', customer=None)]

Send a heartbeat:

.. code-block:: python

    >>> client.heartbeat(origin='baz')
    Heartbeat(id='98c220e6-5148-4b19-8ae8-e1c078b7d68c', origin='baz', create_time=datetime.datetime(2018, 9, 6, 8, 48, 48, 817000), timeout=86400, customer=None)

For more details, visit the `Alerta Python SDK page`_.

.. _Alerta Python SDK page: https://github.com/alerta/python-alerta-client

Ruby SDK
--------

The Ruby SDK is a work-in-progress. For more details, visit the `Alerta Ruby SDK page`_.

.. _Alerta Ruby SDK page: https://github.com/alerta/alerta-ruby

Haskell SDK
-----------

This SDK supplies bindings to the Alerta REST API so that it can be
used from Haskell.

For more details, visit the `Haskell Package page`_.

.. _Haskell Package page: https://hackage.haskell.org/package/alerta

Gource Visualization
--------------------

View the development of Alerta over the years as an animated tree `Gource visualization <https://www.youtube.com/watch?v=BO3z2AHpXBU>`_.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/BO3z2AHpXBU" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>