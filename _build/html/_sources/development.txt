.. _development:

Development
===========

Python SDK
----------

Alerta is developed in Python so the Python SDK is a core component of the monitoring system.

Initialise the alerta API client:

.. code-block:: python

    >>> from alertaclient.api import ApiClient
    >>> api = ApiClient(endpoint='http://api.alerta.io', key='tiPMW41QA+cVy05E7fQA/roxAAwHqZq/jznh8MOk')

As of 4.8.5, you can specify ssl verify False (defaults to True) for testing:

.. code-block:: python

    >>> api = ApiClient(endpoint='http://api.alerta.io', key='tiPMW41QA+cVy05E7fQA/roxAAwHqZq/jznh8MOk', ssl_verify=False)

Send an alert:

.. code-block:: python

    >>> from alertaclient.alert import Alert
    >>> alert = Alert(resource='foo', event='bar')
    >>> alert
    Alert(id='6e625266-fb7c-4c11-bf95-27a6a0be432b', environment='', resource='foo', event='bar', severity='normal', status='unknown')
    >>> api.send(alert)
    {u'status': u'ok', u'id': u'5fdb224b-9378-422d-807e-fdf8610416d2'}

Query for the alert just sent:

.. code-block:: python

    >>> api.get_alert('5fdb224b-9378-422d-807e-fdf8610416d2')['alert']['severity']
    u'normal'
    >>> api.get_alerts(resource='foo')['alerts'][0]['id']
    u'5fdb224b-9378-422d-807e-fdf8610416d2'

Send a heartbeat:

.. code-block:: python

    >>> from alerta.heartbeat import Heartbeat
    >>> hb = Heartbeat(origin='baz')
    >>> hb
    Heartbeat(id='21d586a6-9bd5-4b18-b0bb-4fb876db4851', origin='baz', create_time=datetime.datetime(2014, 6, 14, 20, 2, 33, 55118), timeout=300)
    >>> api.send(hb)
    {u'status': u'ok', u'id': u'6bf11e97-9664-4fa3-b830-8e6d0d84b4cc'}

Installation
~~~~~~~~~~~~

Install using pip:

::

    $ pip install alerta

Install from GitHub:

::

    $ git clone git@github.com:alerta/python-alerta-client.git
    $ cd python-alerta
    $ python setup.py install

For more details, visit the `Alerta Python SDK page`_.

.. _Alerta Python SDK page: https://github.com/alerta/python-alerta-client
