#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_silashes=False)
def states_list():
    states = list(storage.all("State").values())
    states.sort(key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
