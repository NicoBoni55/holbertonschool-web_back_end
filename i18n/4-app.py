#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,
    Parametrize templates """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """


class Config(object):
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Use that class as config for Flask app """


@app.route('/')
def root():
    """ basic Flask app """
    return render_template("4-index.html")


def get_locale():
    """ to determine the best match with our supported languages """
    locale = request.args.get('locale')
    leng = app.config['LANGUAGES']
    if locale in leng:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)
""" init app with locale_selector
"""


if __name__ == "__main__":
    app.run()
