#!/usr/bin/python3
"""Script to run a flask web application"""
import models
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Listing all the states on a webpage"""
    st = sorted(storage.all(models.state.State).values())
    return render_template("7-states_list.html", states=st)

@app.teardown_appcontext
def teardown_db(exception):
    """"Remove the current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
