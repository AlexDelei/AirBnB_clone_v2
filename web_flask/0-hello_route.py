#!/usr/bin/python3
from flask import Flask
"""
A simple demostration of creating a flask web app
using the the flask framework
"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	"""
	Return hello hbnb
	"""
	return "Hello HBNB!"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
