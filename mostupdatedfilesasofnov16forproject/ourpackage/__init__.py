from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

# initialize new Flask app
server = Flask(__name__)
# add configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect flask_sqlalchemy to the configured flask app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# connect flask_sqlalchemy to the configured flask app
db = SQLAlchemy(server)

#create new Dash app and use existing Flask app as our Dash app's server
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/', external_stylesheets=external_stylesheets) # external_stylesheets
#import our routes after our database has been configured

from ourpackage.dashboard import *
from query import *
