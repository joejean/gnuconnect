"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views


## URL dispatch rules

# Home page
app.add_url_rule('/home', 'home', view_func=views.home)

# Newsfeed page
app.add_url_rule('/newsfeed', 'newsfeed', view_func=views.newsfeed)

# Asset
# Landing page
app.add_url_rule('/', '*', view_func=views.index)




## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

