# Title Heading 1

The Alerta API receives alerts from multiple sources, correlates, de-duplicates or suppresses them, and makes the alerts available via a RESTful JSON API.

## Subsection Heading 2

Alerta comes out-of-the-box with key features designed to reduce the burden of alert management. When an event is received it it is processed in the following way:

1. all plugin pre-receive hooks are run in listed order, an alert is immediately rejected if any plugins return a `RejectException` or `RateLimit` exception
2. alert is checked against any active blackout periods, alert suppressed if any match
3. alert is checked if duplicate, if so duplicate count is increased and repeat set to True

Each of the above actions are explained in more detail in the following sections.

## Plugins

[Plugins](https://en.wikipedia.org/wiki/Plug-in_(computing)) are small python scripts.