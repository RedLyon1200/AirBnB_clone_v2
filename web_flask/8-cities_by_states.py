#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""
from flask import Flask
from flask import render_template
from models import storage
from models.place import Place
from models.state import State
from models.city import City

import models

app = Flask(__name__)
ss = {'strict_slashes': False}


@app.teardown_appcontext
def teardown_db(e):
    """closes the storage"""
    storage.close()


@app.route('/cities_by_states', **ss)
def cities_by_states():
    """ """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
