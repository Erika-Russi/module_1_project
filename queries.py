from classes import *
from sqlalchemy import create_engine
from sqlalchemy.sql import func

engine = create_engine('sqlite:///games.db')

Session = sessionmaker(bind=engine)
session = Session()

def team_with_highest_ball_poss():
    max_bp= session.query(Statistics,func.max(Statistics.ball_possession)).join(Team).first()
    return max_bp.Statistics.name

def team_with_longest_dist_covered():
    max_dc= session.query(Statistics,func.max(Statistics.distance_covered)).join(Team).first()
    return max_dc.Statistics.name

def team_with_shortest_dist_covered():
    min_dc= session.query(Statistics,func.min(Statistics.distance_covered)).join(Team).first()
    return min_dc.Statistics.name

def team_with_lowest_ball_poss():
    min_bp= session.query(Statistics,func.min(Statistics.ball_possession)).join(Team).first()
    return min_bp.Statistics.name

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
