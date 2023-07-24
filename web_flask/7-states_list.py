#!/usr/bin/python3
"""7-states_list module
Starts a Flask web application
"""
from flask import Flask
from flask import render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    '''
    Cleans-up app resources after request
    '''
    storage.close()


@app.route('/states_list/', strict_slashes=False)
def states_list():
    '''
    Renders a html page with a list of states
    '''
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
