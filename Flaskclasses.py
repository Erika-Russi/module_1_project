#done actions
#kyle - 1) changed columns to db.column
#kyle - 2)  import flask_sqlalchemy, added db.create_all,got rid of engine and session and base
#kyle - 1)
#kyle - 1)
#kyle - 1)
import requests
url = 'https://worldcup.sfg.io/matches'
r = requests.get(url)
all_games = r.json()
from datetime import datetime as dt
from sqlalchemy import * #Column, Integer, String, ForeignKey, DateTime, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from flask_sqlalchemy import SQLAlchemy
from run import db
# Base = declarative_base()
# creates the models and tables in the database


# Write your classes below
class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.String)
    winner = db.Column(db.String)
    statistics = relationship('Statistics', back_populates="game")
    teams = relationship(
        'Team',
        secondary='statistics',
        back_populates='games'
    )

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    statistics = relationship('Statistics', back_populates="team")
    games = relationship(
        'Game',
        secondary='statistics',
        back_populates='teams'
    )

class Statistics(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, ForeignKey('games.id'))
    team_id = db.Column(db.Integer, ForeignKey('teams.id'))
    name = db.Column(db.String)
    goals = db.Column(db.Integer)
    game = relationship('Game', back_populates='statistics')
    team = relationship('Team', back_populates='statistics')

    ball_possession=db.Column(db.Integer)
    distance_covered=db.Column(db.Integer)
    on_target=db.Column(db.Integer)
    pass_accuracy=db.Column(db.Integer)

db.create_all()

# engine = create_engine('sqlite:///games.db')
# Base.metadata.create_all(engine)
