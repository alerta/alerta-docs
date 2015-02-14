
Release History
===============

4.0.5 (30-1-2015)
-----------------

4.0.4 ()

4.0.3 ()

4.0.2 ()

4.0.1 ()


4.0.0 (15-1-2015)
-----------------

3.3.7 ()

3.3.2 (17-12-2014)
------------------

Improvements
++++++++++++

* Add Pingdom web hook integration

Bugfixes
++++++++

* Update Attributes and Tags for correlated alerts

3.3.1 (16-12-2014)
------------------

Improvements
++++++++++++

* Refactor Webhooks to reuse common alert processing code
* Add example scripts for test alert generation

3.3.0 (16-12-2014)
------------------

Improvements
++++++++++++

* Add Amazon AWS Cloudwatch web hook integration

3.2.x (11-10-2014)
------------------

Improvements
++++++++++++

* Major refactor and simplification
* Add support for server-side plug-ins with ``pre_receive()`` and ``post_receive()`` hooks
* Add sample plug-ins for alert reject policy, normalisation, enhancement etc

Documentation
+++++++++++++

* Updated README and fixed Heroku button (`#68`_)

Bugfixes
++++++++

* PagerDuty web hook deprecated and removed
* Lots of pylint fixes
* Fixed tests

.. _`#68`: https://github.com/guardian/alerta/issues/68