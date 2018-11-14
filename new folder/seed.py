from models import Game, Team, Statistics
import requests
from sqlalchemy.orm import sessionmaker, relationship, backref
from flask_sqlalchemy import SQLAlchemy
from ourpackage import db
from sqlalchemy.orm import sessionmaker

all_games = requests.get('http://worldcup.sfg.io/matches').json()

all_games_tuples= [(game['venue'], game['home_team_country'], game['away_team_country'], game['winner']) for game in all_games]
h_teams = set([t[1] for t in all_games_tuples])
a_teams = set([t[2] for t in all_games_tuples])
teams = h_teams.union(a_teams)
team_objects = [Team(country = t) for t in teams]
# db.session.add_all(team_objects)
# db.session.commit()

all_game_objects = []
all_stats = []
for game in all_games:
    h_team = db.session.query(Team).filter(Team.country == game['home_team_statistics']['country']).one()
    a_team = db.session.query(Team).filter(Team.country == game['away_team_statistics']['country']).one()
    game_object = Game(venue= game['venue'],
                       winner = game['winner'])
    all_game_objects.append(game_object)

    h_goals = game['home_team']['goals']
    h_name=game['home_team']['country']
    h_ball_possession = game['home_team_statistics']['ball_possession']
    a_goals = game['away_team']['goals']
    a_name=game['away_team']['country']
    a_ball_possession = game['away_team_statistics']['ball_possession']
    h_distance_covered = game['home_team_statistics']['distance_covered']
    a_distance_covered = game['away_team_statistics']['distance_covered']
    h_pass_accuracy = game['home_team_statistics']['pass_accuracy']
    a_pass_accuracy = game['away_team_statistics']['pass_accuracy']
    h_on_target = game['home_team_statistics']['on_target']
    a_on_target = game['away_team_statistics']['on_target']

    h_stats = Statistics(name=h_name,game = game_object,
                         team = h_team,
                        ball_possession =h_ball_possession,
                        goals = h_goals,
                        distance_covered = h_distance_covered,
                        pass_accuracy = h_pass_accuracy,
                        on_target = h_on_target)
    a_stats = Statistics(name=a_name,game = game_object,
                        team = a_team,
                        ball_possession =a_ball_possession,
                        goals = a_goals,
                        distance_covered = a_distance_covered,
                        pass_accuracy = a_pass_accuracy,
                        on_target = a_on_target)
    all_stats.append(h_stats)
    all_stats.append(a_stats)
# db.session.add_all(all_game_objects)
# db.session.commit()
