#!/usr/bin/python3
"""-*- coding: utf-8 -*-""""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Index"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
