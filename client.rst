
`alert` is the unified command-line tool for alerta.


Configuration Options
=====================

Command-line options have precedence over environment variables, which have precedence over the
configuration file.

Within the configuration file profile-specific sections have precedence over the `DEFAULT` section.

+-------------+-------------+-------------------------+-------------------------+-----------------------+
| Variable    | Config File | Environment Variable    | Option                  | Default               |
+=============+=============+=========================+=========================+=======================+
| config_file |     n/a     | ALERTA_CONF_FILE        |     n/a                 | ~/.alerta.conf        |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
| profile     |     n/a     | ALERTA_DEFAULT_PROFILE  | `--profile`             | None                  |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
| endpoint    |  endpoint   | ALERTA_DEFAULT_ENDPOINT | `--endpoint-url`        | http://localhost:8080 |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
| timezone    |  timezone   | n/a                     | n/a                     | Europe/London         |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
| output      |  output     | n/a                     | `--output`, `--json`    | text                  |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
| color       |  color      | CLICOLOR                | `--color`, `--no-color` | color on              |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
| debug       |  debug      | n/a                     | `--debug`               | no debug              |
+-------------+-------------+-------------------------+-------------------------+-----------------------+
