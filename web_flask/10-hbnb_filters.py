#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
ss = {'strict_slashes': False}


@app.teardown_appcontext
def teardown_db(e):
    """closes the storage"""
    storage.close()


@app.route('/hbnb_filters', **ss)
def hbnb_filters():
    """ dinamic filters """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all(Amenity).values()),
                       key=lambda x: x.name)
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
