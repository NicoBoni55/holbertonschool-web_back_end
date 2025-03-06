#!/usr/bin/env python3
"""
Basic app
"""

from flask import Flask, request, render_template
from flask_babel import Babel


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app)


@app.route("/", methods=["GET"])
def home():
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
