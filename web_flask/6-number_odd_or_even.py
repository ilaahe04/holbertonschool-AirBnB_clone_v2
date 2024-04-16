#!/usr/bin/python3
"""save this as app.py"""

from flask import Flask, render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    display_text = text.replace('_', ' ')
    return 'Python ' + display_text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    t = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, type_of_number=t)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
