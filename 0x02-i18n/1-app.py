#!/usr/bin/env python3
"""
A Flask application demonstrating basic Babel setup for internationalization.

This script configures Flask-Babel to support English and French languages with
a default locale of English and a default timezone of UTC.
"""

from flask import Flask, render_template
from flask_babel import Babel

# Initialize Flask application
app = Flask(__name__)

# Configuration class
class Config:
    """
    Configuration class for Flask and Babel.

    Attributes:
        LANGUAGES (list): Supported languages for the application.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply configuration
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@app.route('/')
def hello_world():
    """
    Handle requests to the root URL ("/").

    Returns:
        str: Renders the 1-index.html template.
    """
    return render_template('1-index.html')


# Run the Flask application
if __name__ == "__main__":
    app.run()
