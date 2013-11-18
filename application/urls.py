"""
urls.py

URL dispatch route mappings and error handlers

"""

##
##	Copyright (C) 2013 GNU Connect. All Rights Reserved.
##
##	@author			Francis Sowani (Frathoso) <frathoso@gmail.com>
##	@author			Joe Jean <jj1347@nyu.edu>
##	@copyright 		Copyright 2013, GNU Connect
##  @link			http://gnuconnect.appspot.com
##	@version 		1.0
##	@description	URL dispatch route mappings and error handlers
##


from flask import render_template
from application import app
from application import views


##
## 	URL dispatch rules
##

# Home page
app.add_url_rule('/projects', 'projects', view_func=views.home)
app.add_url_rule('/projects/<page>', 'projects', view_func=views.home)
app.add_url_rule('/events', 'events', view_func=views.home)
app.add_url_rule('/events/<page>', 'events', view_func=views.home)

# Profile page
app.add_url_rule('/profile', 'profile', view_func=views.profile)

# Notifications page
app.add_url_rule('/notifications', 'notifications', view_func=views.notifications)

# Privacy statements page
app.add_url_rule('/privacy', 'privacy', view_func=views.privacy)

# Terms and conditions page
app.add_url_rule('/terms', 'terms', view_func=views.terms)

# About GNUConnect page
app.add_url_rule('/about', 'about', view_func=views.about)

# Sign up page
app.add_url_rule('/register', 'register', view_func=views.register)

# Landing page
app.add_url_rule('/', '*', view_func=views.index)



##
## 	Errors handlers
##

# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

