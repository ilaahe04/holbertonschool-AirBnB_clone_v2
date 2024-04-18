#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a HTML page with states and cities"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
