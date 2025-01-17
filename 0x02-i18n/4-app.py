#!/usr/bin/env python3
"""
4-app.py - Flask app with locale forced via URL parameter.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.
    If `locale` is provided in the URL and is valid, use it.
    Otherwise, fall back to the default behavior.
    """
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    """
    Render the index page with translations.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
