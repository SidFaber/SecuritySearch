#!/usr/bin/env python
#
# Start with:
#  export FLASK_APP=api.py
#  flask run --host=0.0.0.0
#
# This flask project includes code from:
# https://github.com/miguelgrinberg/flask-video-streaming
# for setting up a streaming camera
#
from flask import Flask, render_template
import logging
from searchProvider import IpapiSearch


app = Flask(__name__)
searchProviders = {}


@app.route('/')
@app.route('/search')
def homepage():
    return render_template('search.html', searchProviders=searchProviders)


def addSearchProvider(provider):
    if provider.name in searchProviders.keys():
        # only allow a single search provider of each type
        raise KeyError("Search provider %s has already been added"
                       % (provider.name))

    searchProviders[provider.name] = provider
    logging.debug("Registered search provider " + provider.name)
    return True


if __name__ == '__main__':

    addSearchProvider(IpapiSearch())
    # app.run(host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0', port=5000)
    app.run(port=5000)

    logging.debug("Shutting down")
