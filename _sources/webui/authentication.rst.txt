.. _webui auth:

Authentication
==============

The Alerta web UI supports multiple authentication providers. When
``AUTH_REQUIRED`` is set to ``True`` on the API server, users must
log in before accessing the console.

Login Page
----------

The login page is displayed when authentication is required and no valid
token is present. The appearance of the login page depends on the configured
authentication provider.

For **Basic Auth**, a username/password form is shown with an optional
*Sign Up* link (when ``SIGNUP_ENABLED`` is ``True``).

For **OAuth2/OIDC** providers (Google, GitHub, GitLab, Keycloak, Azure,
Cognito, PingFederate), a provider-specific login button redirects the user
to the external identity provider. After successful authentication, the
user is redirected back to the web console with a valid token.

For **SAML**, the login button redirects to the configured SAML identity
provider.

Sign Up
-------

When basic auth is enabled and ``SIGNUP_ENABLED`` is ``True``, new users can
create an account by clicking the *Sign Up* link on the login page. The sign
up form requires a name, email address, and password.

.. note:: Sign up is only available for the basic auth provider. When using
          OAuth2 or SAML, user accounts are created automatically on first
          login.

Token Handling
--------------

After successful authentication, the web UI stores a JWT access token in
the browser's local storage. The token is included in all subsequent API
requests as a ``Bearer`` token in the ``Authorization`` header.

Tokens have a configurable expiry time. The web UI will attempt to refresh
the token before it expires. If the token cannot be refreshed, the user is
redirected to the login page.

Logout
------

Click your user avatar in the top-right corner and select *Sign Out* to
log out. This clears the stored token from the browser and redirects to
the login page.
