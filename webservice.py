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

from searchProvider import *

import sys
import time



#logging.basicConfig(level=logging.DEBUG,
#                            format='(%(threadName)-9s) %(message)s',)
app = Flask(__name__)
logging.debug ("Created app object")

searchProviders = {}

@app.route('/')
@app.route('/search')
def homepage():
    return render_template ('search.html')


@app.route('/api/search')
def apiStatus():
    return arm.json_status()


def addSearchProvider (provider):
    if provider.name in searchProviders.keys():
        # only allow a single search provider of each type
        raise KeyError ("Search provider %s has already been added" % (provider.name))
        return False
    
    searchProviders['provider.name'] = provider
    return True

if __name__ == '__main__':

    addSearchProvider (IpapiSearch())
    #app.run (host='0.0.0.0', port=80)
    #app.run (host='0.0.0.0', port=5000)
    app.run (port=5000)

    logging.debug ("Shutting down")

