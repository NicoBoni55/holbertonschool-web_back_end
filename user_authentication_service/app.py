#!/usr/bin/env python3
"""
App flask
"""
from flask import Flask, jsonify, request, abort
import flask
from auth import Auth


AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    welcome = {"message": "Bienvenue"}
    return flask.jsonify(welcome)


@app.route("/users", methods=["POST"])
def create_user():
    try:
        email = request.form.get("email")
        password = request.form.get("password")
    except KeyError:
        abort(400)
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route("/sessions", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        flask.abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
