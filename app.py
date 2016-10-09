#!/usr/bin/env python
# encoding: utf-8
from bottle import run, post, get, os
@post('/hello')
def hello():
    return 'Hi World!'
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)