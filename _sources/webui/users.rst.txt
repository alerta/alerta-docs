.. _webui users groups:

Users and Groups
================

The users and groups pages allow administrators to manage user accounts and
organize users into groups. Navigate to these pages from the main menu under
*Configuration > Users* and *Configuration > Groups*.

Users
-----

Creating Users
~~~~~~~~~~~~~~

Click the **+** button to create a new user. The following fields are required:

- **Name** -- the user's display name
- **Login/Email** -- the login identifier (typically an email address)
- **Password** -- the initial password (basic auth only)
- **Roles** -- one or more roles to assign (e.g. ``admin``, ``user``, ``ops``)
- **Text** -- an optional description

.. note:: User creation through the web UI only applies to basic auth. When
          using OAuth2 or SAML, user accounts are provisioned automatically
          on first login.

Listing Users
~~~~~~~~~~~~~

The user list shows all registered users with the following columns:

- **Name** and **Login**
- **Status** -- ``active``, ``inactive``, or ``unknown``
- **Roles** -- the roles assigned to the user
- **Last Login** -- the date and time of the user's last authentication
- **Email verified** -- whether the user's email has been verified

Editing Users
~~~~~~~~~~~~~

Click on a user to edit their details. You can change the name, email,
roles, status (active/inactive), and email verification flag. Changing a
user's roles immediately affects their permissions on the next API request.

Deleting Users
~~~~~~~~~~~~~~

Click the delete icon to remove a user account. This prevents the user from
authenticating but does not remove their historical activity from alert
histories or notes.

Groups
------

Groups allow you to organize users and assign permissions at the group level
rather than per user.

Creating Groups
~~~~~~~~~~~~~~~

Click the **+** button on the groups page to create a new group. Provide a
group name and optional description.

Managing Members
~~~~~~~~~~~~~~~~

Click on a group to view its members. Use the **Add User** button to add
existing users to the group, or click the remove icon next to a member to
remove them.

Group names can be used in :ref:`permission <webui permissions>` match rules
to grant scopes to all members of a group at once.
