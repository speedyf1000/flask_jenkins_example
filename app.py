#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""Here is simple flask project."""

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World!\n'

if __name__ == '__main__':
    app.run()

