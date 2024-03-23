#!/usr/bin/python3
"""A simple demostration of creating web app"""
from flask import Flask
from flask import render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def routing_2(text='is_cool'):
    """printout the text passed as a url param
    with default text being is cool"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """return n if its an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    """return n in a html webpage"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """return the number and if is even or odd"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, state="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, state="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
