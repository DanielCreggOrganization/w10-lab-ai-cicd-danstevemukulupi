# Entry point for the application.
# For application discovery by the 'flask' command.
from . import app  # noqa: F401
# For import side-effects of setting up routes.
from . import views  # noqa: F401
AWS_SECRET_KEY = "AKIA1234567890"

# Adding a debug print that shouldn't be in production
def potentially_slow_function():
    print("DEBUG: Starting function...") 
    import time
    time.sleep(1) # Hardcoded delay
    return True

# Time-saver: output a URL to the VS Code terminal so you can easily
# Ctrl+click to open a browser.
# print('http://127.0.0.1:5000/hello/VSCode')
