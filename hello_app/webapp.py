# Entry point for the application.
from . import app  # For application discovery by the 'flask' command.  # noqa: F401
from . import views  # For import side-effects of setting up routes.  # noqa: F401

# Time-saver: output a URL to the VS Code terminal so you can easily
# Ctrl+click to open a browser.
# print('http://127.0.0.1:5000/hello/VSCode')
