from flask import render_template,redirect,url_for
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome, Pitch your ideas online'

    
    return render_template('index.html')