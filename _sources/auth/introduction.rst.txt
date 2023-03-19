
Getting Started
===============


Scenarios
---------

* :ref:`LDAP Authentication <ldap auth>`
* :ref:`Using Custom Scopes <ldap auth>`
* :ref:`Default Roles <ldap auth>`
* :ref:`Guest Roles <ldap auth>`
* :ref:`Readonly Logins <ldap auth>`
* :ref:`Role Mapping <ldap auth>`
* :ref:`Customer Lookups <ldap auth>`
* :ref:`Delete Scopes <ldap auth>`


    AUTH_PROXY = False
    AUTH_PROXY_USER_HEADER = 'X-Proxy-User'  # header field containing the authenticated username
    AUTH_PROXY_ROLES_HEADER = 'X-Proxy-Roles'  # comma-separated list of authenticated role names
    AUTH_PROXY_ROLES_SEPARATOR = ','
