#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with list of City objects for a given State"""
    states_tmp = storage.all(State)
    state_by_id = None
    states = []

    if id:
        state = states_tmp[f"State.{id}"]
        state_by_id = state
    else:
        for obj in states_tmp.values():
            states.append(obj)

    return render_template(
                            "8-cities_by_states.html",
                            states=states,
                            single_state=state_by_id
                          )


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
