#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def homesh():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def welcomeh():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def funC(text):
    """ C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnbiscool(text="is cool"):
    """Display text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def hbnbrte(num):
    """Display  number """
    return '{} is a number'.format(num)


@app.route('/number_template/<int:num>', strict_slashes=False)
def hbnbtmpl(num):
    """ display a HTML """
    return render_template("5-number.html", number=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
