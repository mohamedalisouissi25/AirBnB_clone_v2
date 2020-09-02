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
def funC(text="is cool"):
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


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def hbnboddeven(num):
    """ Display odd or even """
    if num % 2 == 0:
        i = "even"
    else:
        i = "odd"
    return render_template(
        "6-number_odd_or_even.html",
        number=num,
        output=i)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')