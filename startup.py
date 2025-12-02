"""In this sample, the Flask app object is contained within the
``hello_app`` module. That module contains an ``__init__.py`` and uses
relative imports. Because of that structure, a file like ``webapp.py``
cannot be run directly as the startup file through Gunicorn; you will see
"Attempted relative import in non-package".

Provide this alternate startup file that simply imports the app object so
you can use ``startup:app`` with Gunicorn.
"""

from hello_app.webapp import app  # noqa: F401
