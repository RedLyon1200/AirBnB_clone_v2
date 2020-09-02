#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
ss = {'strict_slashes': False}


@app.teardown_appcontext
def teardown_db(e):
    """closes the storage"""
    storage.close()


@app.route('/states', **ss)
def states_list():
    """list states in HTML"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def state_by_id():
    """ """
    states = storage.all(State).values()
    print(type(states))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
