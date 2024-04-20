#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Method to handle teardown
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Route to display a HTML page with a list of all State objects
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """
    Route to display a HTML page with cities of a State
    """
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', state=None)
    else:
        if storage._DBStorage__engine == 'db':
            cities = sorted(state.cities, key=lambda x: x.name)
        else:
            cities = sorted(state.cities(), key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
