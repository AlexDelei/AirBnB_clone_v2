#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def display_states(id=""):
    """Cities with state_id and all states"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    if id != "":
        id = "State.{}".format(id)
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def display_states_close(error):
    """Closes each query session"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
