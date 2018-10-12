from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, session

from flask_debugtoolbar import DebugToolbarExtension

from model import *

from sqlalchemy import func

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

#Make sure jinja tells you if you're using an undifined variable
app.jinja_env.undefined = StrictUndefined


if __name__ == "__main__": 
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app, 'postgres:///parks')

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5000, host='0.0.0.0')