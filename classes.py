import requests
url = 'https://worldcup.sfg.io/matches'
r = requests.get(url)
all_games = r.json()
from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

# Write your classes below
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    venue = Column(String)
    winner = Column(String)
    statistics = relationship('Statistics', back_populates="game")
    teams = relationship(
        'Team',
        secondary='statistics',
        back_populates='games'
    )

#home_team = relationship('Team',secondary='statistics', back_populates='games')
#away_team = relationship('Team',secondary='statistics', back_populates='games')

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    country = Column(String)
    statistics = relationship('Statistics', back_populates="team")
    games = relationship(
        'Game',
        secondary='statistics',
        back_populates='teams'
    )

class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    name = Column(String)
    goals = Column(Integer)
    game = relationship('Game', back_populates='statistics')
    team = relationship('Team', back_populates='statistics')

    ball_possession=Column(Integer)
    distance_covered=Column(Integer)
    on_target=Column(Integer)
    pass_accuracy=Column(Integer)

engine = create_engine('sqlite:///games.db')
Base.metadata.create_all(engine)
