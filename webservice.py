#!/usr/bin/env python
#
#  Start with 
# export FLASK_APP=api.py
# flask run --host=0.0.0.0
#
# This flask project includes code from 
# https://github.com/miguelgrinberg/flask-video-streaming
# for setting up a streaming camera
#
from flask import Flask, render_template, Response, make_response
from flask import request
import logging

import sys
import time



#logging.basicConfig(level=logging.DEBUG,
#                            format='(%(threadName)-9s) %(message)s',)
app = Flask(__name__)
logging.debug ("Created app object")


@app.route('/')
def homepage():
    return render_template ('search.html')


@app.route('/api/search')
def apiStatus():
    return arm.json_status()


if __name__ == '__main__':
    #app.run (host='0.0.0.0', port=80)
    app.run (host='0.0.0.0', port=5000)

    logging.debug ("Shutting down")

