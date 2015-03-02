Alerta Documentation
====================

To view the docs locally:

    $ pip install -r requirements.txt
    $ make livehtml
    >> browse to http://localhost:8000

The website will be automatically updated whenever an `.rst` file changes.

To update the docs website:

    $ make html
    $ git push


Dependencies
------------

  * ReadTheDocs: https://readthedocs.org/
  * Alabaster: https://github.com/bitprophet/alabaster
