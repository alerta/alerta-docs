Authentication
==============

By default, authentication is not enabled. However, in production it would be

Authentication is optional however there are some features that are not availabe unless users login.



API Endpoints
--------------

POST, OPTIONS  /auth/github  github
POST, OPTIONS  /auth/google  google

.. _api_keys:

API Keys
--------

POST, OPTIONS  /key  create_key
POST, OPTIONS, DELETE  /key/<path:key>  delete_key
HEAD, OPTIONS, GET  /keys  get_keys
HEAD, OPTIONS, GET  /keys/<user>  get_user_keys

.. _users:

Users
-----

POST, OPTIONS  /user  create_user
POST, OPTIONS, DELETE  /user/<user>  delete_user
HEAD, OPTIONS, GET  /users  get_users

