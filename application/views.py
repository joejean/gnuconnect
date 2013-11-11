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

from flask import render_template, redirect, url_for, g, request

from flask_cache import Cache

from application import app

from functools import wraps

# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)

#Things that are executed before each request.
@app.before_request
def before_request():
    #put the current user in the global g
    g.user = users.get_current_user()

    #put the logout url in the global g
    g.logout = users.create_logout_url('/')

    #put the login url in the global g. 
    g.login = users.create_login_url('home') 

    
##
##      DECORATORS
##


#       login_required decorator

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        login_url = users.create_login_url(request.url)
        if g.user is None:
            return redirect(login_url)
        return f(*args, **kwargs)
    return decorated_function



##
##	HANDLERS
##

#	A public landing page
def index():
    
    if g.user:
        return render_template('home.html', user=g.user)
    else:
        return render_template('index.html')

#	Home page for a user after a successful login
@login_required
def home():
    return render_template('home.html', user = g.user)

#	Profile page for a user
@login_required
def profile():
    return render_template('profile.html', user = g.user)

#   Notifications page for a user
@login_required
def notifications():
    return render_template('notifications.html', user = g.user)

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

