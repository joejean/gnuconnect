"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""

##
##	Copyright (C) 2013 GNU Connect. All Rights Reserved.
##
##	@author			Francis Sowani (Frathoso) <frathoso@gmail.com>
##	@author			Joe Jean <jj1347@nyu.edu>
##	@copyright 		Copyright 2013, GNU Connect
##  @link			http://gnuconnect.appspot.com
##	@version 		1.0
##	@description	URL route handlers
##

from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template

from flask_cache import Cache

from application import app


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


##
##	HANDLERS
##

#	A public landing page
def index():
    return render_template('index.html')

#	Home page for a user after a successful login
def home():
    return render_template('home.html')

#	Newsfeed page for a user
def profile():
    return render_template('profile.html')

#   Privacy statements page for the website
def terms():
    return render_template('terms.html')

#   Terms and conditions page for the website
def privacy():
    return render_template('privacy.html')

#   About GNUConnect page for the website
def about():
    return render_template('about.html')

#   Registration page for the website
def register():
    return render_template('register.html')

#   Login page for the website
def login():
    return render_template('login.html')
