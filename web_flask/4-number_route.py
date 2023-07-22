#!/usr/bin/python3
"""0-hello_route module
Starts a Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''hello route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''hbnb route
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''c route
    Displays "C " followed by the value of the 'text' variable
    '''
    text = escape(text).replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    '''python route
    Displays "Python " followed by the value of the 'text' variable
    '''
    text = escape(text).replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''number route
    Displays "<n> is a number" only if 'n' is an integer
    '''
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
