#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,
    Parametrize templates """
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template("5-index.html")


def get_locale():
    """ to determine the best match with our supported languages """
    locale = request.args.get('locale')
    leng = app.config['LANGUAGES']
    if locale in leng:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    try:
        userID = request.args.get('login_as')
        return users[int(userID)]
    except Exception:
        return None


@app.before_request
def before_request():
    """ get user
    """
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale)
""" init app with locale_selector
"""


if __name__ == "__main__":
    app.run()
