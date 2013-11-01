"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template

from flask_cache import Cache

from application import app


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def index():
    return render_template('index.html')

def home():
    return render_template('home.html')

def newsfeed():
    return render_template('newsfeed.html')


