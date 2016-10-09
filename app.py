#!/usr/bin/env python
# encoding: utf-8
from bottle import run, post, get
@post('/hello')
def hello():
    return 'Hi World!'
@get('/hello')
def hello():
    return 'Hi World!'
if __name__ == '__main__':
    run(host='0.0.0.0', port=5000)