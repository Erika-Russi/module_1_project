
from sqlalchemy import create_engine, func
from Flaskclasses import Team,Statistics,Game
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine('sqlite:///games.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def return_country_and_its_total_goals():
    return session.query(Team.country, func.sum(Statistics.goals)).join(Statistics).group_by(Team.country).all()

def return_average_goals_per_game():
    return session.query(Team.country, func.avg(Statistics.goals)).join(Statistics).group_by(Team.country).all()

def return_average_ot_per_game():
    return session.query(Team.country, func.avg(Statistics.on_target)).join(Statistics).group_by(Team.country).all()

def return_average_pa_per_game():
    return session.query(Team.country, func.avg(Statistics.pass_accuracy)).join(Statistics).group_by(Team.country).all()

def return_average_dc_per_game_desc():
    return session.query(Team.country, func.avg(Statistics.distance_covered)).join(Statistics).group_by(Team.country).order_by(Statistics.distance_covered.desc()).all()

def return_dc_per_team_desc():
    return session.query(Team.country, func.sum(Statistics.distance_covered)).group_by(Statistics.name).order_by(func.sum(Statistics.distance_covered).desc()).join(Statistics).all()

def return_venue_by_goals_desc():
    return session.query(Game.venue, func.sum(Statistics.goals)).join(Statistics).group_by(Game.venue).order_by(func.sum(Statistics.goals).desc()).all()

def return_goals_per_team_desc():
    return session.query(Team.country, func.sum(Statistics.goals)).group_by(Statistics.name).order_by(func.sum(Statistics.goals).desc()).join(Statistics).all()

# print(return_country_and_its_total_goals())





#
# def most_goals():
#     goalz = session.query(func.max(Statistics)).order_by(Statistics.goals)
#     return goalz
# print(most_goals())
#
# def test1():
#     first_russia_stat = session.query(Statistics).join(Team).filter(Team.country == 'Russia').all()[0]
#
#
# SELECT COUNT(*) FROM (SELECT FROM `statistics` ORDER BY `goals` DESC);
