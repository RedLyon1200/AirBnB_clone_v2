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


if __name__ == "__main__":
    app.run(port=5000)
