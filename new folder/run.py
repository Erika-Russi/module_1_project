# import Flask and jsonify from flask
from flask import Flask, jsonify
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import * #Column, Integer, String, ForeignKey, DateTime, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from ourpackage import *
from ourpackage.models import Game, Team, Statistics

#define routes and their respective functions that return the correct data
# remember that each function must have a unique name

@app.route('/team/')
def user_index():
    all_teams = db.session.query(Team).all()
    all_teams_dicts = [team.to_dict() for team in all_teams]
    return jsonify(all_teams_dicts)

# run the server
if __name__ == "__main__":
    app.run()
