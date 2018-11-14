from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# add configurations and database URI
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



# from flask import Flask, jsonify
# # import SQLAlchemy from flask_sqlalchemy
# from flask_sqlalchemy import SQLAlchemy
#
# # initialize new flask app
# app = Flask(__name__)
# # add configurations and database URI
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # connect SQLAlchemy to the configured flask app
# db = SQLAlchemy(app)

# #import our routes after our database has been configured
# from ourpackage import routes
