.. _development:

Development
===========

Python SDK
----------

Alerta is developed in Python so the Python SDK is a core component of the monitoring system.

.. code-block:: python

    >>> from alerta.api import ApiClient
    >>> from alerta.alert import Alert
    >>>
    >>> api = ApiClient(endpoint='http://api.alerta.io', key='tiPMW41QA+cVy05E7fQA/roxAAwHqZq/jznh8MOk')
    >>> alert = Alert(resource='foo', event='bar')
    >>> alert
    Alert(id='6e625266-fb7c-4c11-bf95-27a6a0be432b', environment='', resource='foo', event='bar', severity='normal', status='unknown')
    >>> api.send(alert)
    {u'status': u'ok', u'id': u'5fdb224b-9378-422d-807e-fdf8610416d2'}

    >>> api.get_alert('5fdb224b-9378-422d-807e-fdf8610416d2')['alert']['severity']
    u'normal'
    >>>
    >>> api.get_alerts(resource='foo')['alerts'][0]['id']
    u'5fdb224b-9378-422d-807e-fdf8610416d2'

    >>> from alerta.heartbeat import Heartbeat
    >>> hb = Heartbeat(origin='baz')
    >>> hb
    Heartbeat(id='21d586a6-9bd5-4b18-b0bb-4fb876db4851', origin='baz', create_time=datetime.datetime(2014, 6, 14, 20, 2, 33, 55118), timeout=300)
    >>> api.send(hb)
    {u'status': u'ok', u'id': u'6bf11e97-9664-4fa3-b830-8e6d0d84b4cc'}
    >>>

Installation
~~~~~~~~~~~~

::

    $ pip install alerta


::

    $ git clone git@github.com:alerta/python-alerta.git
    $ cd python-alerta
    $ python setup.py install
