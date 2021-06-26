#!/usr/bin/env python3

from flask import Flask

SECRET_MESSAGE = "I am the bone of my sword"
app = Flask( __name__ )

@app.route("/")
def get_secret_message():
	return SECRET_MESSAGE