#!/usr/bin/python3
"""save this as app.py"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    display_text = text.replace('_', ' ')
    return 'C ' + display_text 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
