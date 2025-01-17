#!/usr/bin/python3
from flask import Flask, render_template
from flask_babel import Babel

# Create an instance of the Flask class
app = Flask(__name__)

# Babel setup
babel = Babel(app)

class Config:
    """
    Configuration class to set up languages and locales.
    """
    LANGUAGES = ['en', 'fr']  # Available languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale (English)
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone (UTC)

# Set up the app config to use the Config class
app.config.from_object(Config)

@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL ("/").
    It renders an HTML page (1-index.html) located in the 'templates' directory.
    """
    return render_template('1-index.html')

# Ensure the app runs when the script is executed directly
if __name__ == "__main__":
    app.run()
