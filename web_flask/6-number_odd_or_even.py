#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""
from flask import Flask
from flask import render_template

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


@app.route('/number/<int:number>')
def number(number):
    """number"""
    return '{} is a number'.format(number)


@app.route('/number_template/<int:number>')
def number_template(number):
    """number_template"""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """number_odd_or_even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
