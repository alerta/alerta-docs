.. _webhooks:


Custom Webhooks
===============

Custom webhooks are a simple but effective way of adding support for direct integration
to any system via a webhook without having to modify the core source code.  They are
written in python and are required to implement all methods of a base class.

.. code-block:: python

    def incoming(self, path: str, query_string: ImmutableMultiDict, payload: Any) -> Union[Alert, JSON]:
        """
        Parse webhook path, query string and/or payload in JSON or plain text and
        return an alert or a custom JSON response.
        """
        raise NotImplementedError

They are loaded into memory when the Alerta API starts up and dynamically add an
API endpoint path to the list of available webhooks at :file:`/webhooks/<webhook_name>`
and trigger for that and all subpaths of that URL. eg. :file:`/webhooks/<webhook_name>/<alert_id>`

To set this up follow the instructions for triggering a webhook in the system to be 
integrated with and for the webhook URL append :file:`/webhooks/<webhook_name>` to
to the Alerta API URL but replace ``<webhook_name>`` with the name of the of the system.

Next, write the webhook python code. For more information on how to write the python
code see the `webhook examples`_ in the contrib repo or follow the tutorial.

**Example Custom Webhook URL for Sentry**

:file:`https://alerta.example.com/api/webhooks/sentry`

Code for the webhook can be found in the contrib repo `Sentry webhook`_ directory.

.. _webhook examples: https://github.com/alerta/alerta-contrib/tree/master/webhooks
.. _Sentry webhook: https://github.com/alerta/alerta-contrib/tree/master/webhooks/sentry



