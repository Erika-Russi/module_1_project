# import requests
# url = 'https://worldcup.sfg.io/matches'
# r = requests.get(url)
# all_games = r.json()

from datetime import datetime as dt
from flask import Flask
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship, backref
from flask_sqlalchemy import SQLAlchemy
from ourpackage import *

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.String)
    winner = db.Column(db.String)
    statistics = db.relationship('Statistics', back_populates="game")
    teams = db.relationship(
        'Team',
        secondary='statistics',
        back_populates='games'
    )
    # def to_dict(self):
    #     game = {'id': self.id, 'venue': self.venue, 'winner': self.winner} #'statistics': [tweet.to_dict() for tweet in self.tweets]
    #     return game

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    statistics = db.relationship('Statistics', back_populates="team")
    games = db.relationship(
        'Game',
        secondary='statistics',
        back_populates='teams'
    )
    # def to_dict(self):
    #     team = {'id': self.id, 'country': self.country,}
    #     return team

class Statistics(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    name = db.Column(db.String)
    goals = db.Column(db.Integer)
    game = db.relationship('Game', back_populates='statistics')
    team = db.relationship('Team', back_populates='statistics')

    ball_possession=db.Column(db.Integer)
    distance_covered=db.Column(db.Integer)
    on_target=db.Column(db.Integer)
    pass_accuracy=db.Column(db.Integer)
    # def to_dict(self):
    #     tweet = {'id': self.id, 'game_id': self.game_id, 'team_id': self.team_id,'name': self.name,'goals': self.goals}
    #     return tweet


db.create_all()
