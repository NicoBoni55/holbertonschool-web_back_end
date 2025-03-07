#!/usr/bin/env python3
"""
Basic app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def home():
    """ basic route
    """
    return render_template('2-index.html')


def get_locale():
    """ get locale
    """
    return request.accept_languages.best_match(app.config['LENGUAGES'])


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
