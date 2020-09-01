#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""
from flask import Flask

app = Flask(__name__)
ss = {'strict_slashes': False}


@app.route('/', **ss)
def index():
    """Index"""
    return ('Hello HBNB!')


@app.route('/hbnb', **ss)
def hbnb():
    """hbnb"""
    return 'HBNB'


@app.route('/c/<text>', **ss)
def c(text):
    """c"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python', **ss)
@app.route('/python/<text>', **ss)
def python(text='is cool'):
    """python"""
    return 'Python {}'.format(text).replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
