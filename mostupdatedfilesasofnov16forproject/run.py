# # import Flask and jsonify from flask
# from flask import Flask, jsonify
# # import SQLAlchemy from flask_sqlalchemy
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import * #Column, Integer, String, ForeignKey, DateTime, create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship, backref
# # from ourpackage import db
# # from ourpackage.models import Game,Team,Statistics
# # from ourpackage.routes  import *
from ourpackage import *


if __name__ == "__main__":
    app.run_server(debug=True)

#bug fixing?
# 1)moved db out of ourpackage
# 2)
