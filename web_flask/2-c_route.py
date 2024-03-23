#!/usr/bin/python3
"""A simple demostration of creating web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
	"""Return hello hbnb"""
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""Return hbnb"""
	return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def routing(text):
	"""printout the text passed as parameter"""
	return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
