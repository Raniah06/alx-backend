#!/usr/bin/env python3
"""
3-app.py - Flask app with i18n support
This app demonstrates using Flask-Babel for translations in templates.
"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)


@app.route('/')
def index():
    """
    Render the index page with translated content.
    The translations are managed using Flask-Babel's `_` function.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
