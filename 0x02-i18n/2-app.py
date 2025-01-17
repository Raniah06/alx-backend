#!/usr/bin/env python3
"""
A Flask application demonstrating localization with Babel.

This script sets up Babel to support English and French, and determines the
locale based on the `Accept-Language` header from the request.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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


# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the best matching locale from the request's Accept-Language.

    Returns:
        str: The best matching language from the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Handle requests to the root URL ("/").

    Returns:
        str: Renders the 2-index.html template.
    """
    return render_template('2-index.html')


# Run the Flask application
if __name__ == "__main__":
    app.run()
