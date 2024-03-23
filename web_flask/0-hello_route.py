#!/usr/bin/python3
"""
A simple demostration of creating a flask web app
using the the flask framework
"""
from flask import Flask
from Flask import app

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	"""
	Return hello hbnb
	"""
	return "Hello HBNB!"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
