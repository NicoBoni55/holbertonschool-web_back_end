#!/usr/bin/env python3
"""
App flask
"""
from flask import Flask
import flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def login():
    welcome = {"message": "Bienvenue"}
    return flask.jsonify(welcome)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
