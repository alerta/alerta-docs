Alerta Docs
===========

To view the docs locally:

    $ pip install -r requirements.txt
    $ make livehtml
    >> browse to http://localhost:8000

The website will be automatically updated whenever an `.rst` file changes.

To update the docs website:

    $ make html
    $ git add .
    $ git commit -m '...'
    $ git push

Dependencies
------------

The spelling extension uses `enchant`.

    $ brew install enchant


References
----------

  * ReadTheDocs https://readthedocs.org/
  * RTD Theme https://sphinx-rtd-theme.readthedocs.io/en/stable/
  * Alabaster https://github.com/bitprophet/alabaster
  * Pygments syntax highlighter https://pygments.org/languages/
  * MyST Parser https://myst-parser.readthedocs.io/en/latest/intro.html
  * https://raw.githubusercontent.com/executablebooks/MyST-Parser/602470ebdaf81fbea999fcc0f0cf1b8e7784ec15/tests/test_renderers/fixtures/sphinx_roles.md

License
-------

Copyright (c) 2015-2019 by Nick Satterly.

This work is licensed under the Creative Commons Attribution 3.0 Unported
License (CC BY 3.0). To view a copy of this license, visit
http://creativecommons.org/licenses/by/3.0/ or send a letter to Creative
Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
