"""
WSGI wrapper for the flask app.
"""
from app import app as application

if __name__ == "__main__":
    application.run()
