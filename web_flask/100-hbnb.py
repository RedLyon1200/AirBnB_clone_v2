#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User

app = Flask(__name__)
ss = {'strict_slashes': False}


@app.teardown_appcontext
def teardown_db(e):
    """closes the storage"""
    storage.close()


@app.route('/hbnb', **ss)
def hbnb():
    """ places """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)

    amenities = sorted(list(storage.all(Amenity).values()),
                       key=lambda x: x.name)

    places = sorted(list(storage.all(Place).values()), key=lambda x: x.name)

    users = storage.all(User)

    return render_template(
        '100-hbnb.html', states=states,
        amenities=amenities, places=places, users=users)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
