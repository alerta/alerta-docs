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


Requirements
------------

  * ReadTheDocs: https://readthedocs.org/
  * Alabaster: https://github.com/bitprophet/alabaster

License
-------

Copyright (c) 2015 by Nick Satterly.

This work is licensed under the Creative Commons Attribution 3.0 Unported
License (CC BY 3.0). To view a copy of this license, visit
http://creativecommons.org/licenses/by/3.0/ or send a letter to Creative
Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
