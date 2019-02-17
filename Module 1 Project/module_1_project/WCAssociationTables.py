from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

# Write your classes below
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    venue = Column(String)
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
    game = relationship('Game', back_populates='statistics')
    team = relationship('Team', back_populates='statistics')


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
