
import dash_core_components as dcc
# import dash_html_components as html
# from Flaskclasses import Team,Statistics,Game


from models import * #ourpackage.?
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine('sqlite:///games.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def getKey(item):
    return item[1]

def return_country_and_its_total_goals():
    return sorted(session.query(Team.country, func.sum(Statistics.goals)).join(Statistics).group_by(Team.country).all(),key=getKey,reverse=True)

def return_average_goals_per_game():
    return sorted(session.query(Team.country, func.avg(Statistics.goals)).join(Statistics).group_by(Team.country).all(),key=getKey,reverse=True)

def return_average_ot_per_game():
    return sorted(session.query(Team.country, func.avg(Statistics.on_target)).join(Statistics).group_by(Team.country).all(),key=getKey,reverse=True)

def return_average_pa_per_game():
    return sorted(session.query(Team.country, func.avg(Statistics.pass_accuracy)).join(Statistics).group_by(Team.country).all(),key=getKey,reverse=True)

def return_average_dc_per_game_desc():
    return session.query(Team.country, func.avg(Statistics.distance_covered)).join(Statistics).group_by(Team.country).order_by(Statistics.distance_covered.desc()).all()

def return_dc_per_team_desc():
    return session.query(Team.country, func.sum(Statistics.distance_covered)).group_by(Statistics.name).order_by(func.sum(Statistics.distance_covered).desc()).join(Statistics).all()

def return_venue_by_sum_goals_desc():
    return session.query(Game.venue, func.sum(Statistics.goals)).join(Statistics).group_by(Game.venue).order_by(func.sum(Statistics.goals).desc()).all()

def return_venue_by_avg_goals_desc():
    return session.query(Game.venue, func.avg(Statistics.goals)).join(Statistics).group_by(Game.venue).order_by(func.sum(Statistics.goals).desc()).all()

def return_top_eight_teams_by_num_wins():
    return session.query(Game.winner, func.count(Game.winner)).group_by(Game.winner).order_by(func.count(Game.winner).desc())[1:9]

def return_goals_per_team_desc():
    return session.query(Team.country, func.sum(Statistics.goals)).group_by(Statistics.name).order_by(func.sum(Statistics.goals).desc()).join(Statistics).all()

def return_avg_goals_per_team_pergame_desc():
    return session.query(Team.country, func.avg(Statistics.goals)).group_by(Statistics.name).order_by(func.avg(Statistics.goals).desc()).join(Statistics).all()

##scatter charts start here:
#distance_covered vs other stats tab:
def average_dc_vs_goals_per_game():
    return session.query(Team.country, func.avg(Statistics.distance_covered), func.avg(Statistics.goals)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.distance_covered).asc()).all()

def average_dc_vs_pa_per_game():
    return session.query(Team.country, func.avg(Statistics.distance_covered), func.avg(Statistics.pass_accuracy)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.distance_covered).asc()).all()

def average_dc_vs_bp_per_game():
    return session.query(Team.country, func.avg(Statistics.distance_covered), func.avg(Statistics.ball_possession)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.distance_covered).asc()).all()

def average_dc_vs_ot_per_game():
    return session.query(Team.country, func.avg(Statistics.distance_covered), func.avg(Statistics.on_target)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.distance_covered).asc()).all()

#goals vs other stats tab:
def average_goals_vs_dc_per_game():
    return session.query(Team.country, func.avg(Statistics.goals), func.avg(Statistics.distance_covered)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.goals).asc()).all()

def average_goals_vs_bp_per_game():
    return session.query(Team.country, func.avg(Statistics.goals), func.avg(Statistics.ball_possession)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.goals).asc()).all()

def average_goals_vs_pa_per_game():
    return session.query(Team.country, func.avg(Statistics.goals), func.avg(Statistics.pass_accuracy)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.goals).asc()).all()

def average_goals_vs_ot_per_game():
    return session.query(Team.country, func.avg(Statistics.goals), func.avg(Statistics.on_target)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.goals).asc()).all()

#Possession vs other stats tab:
def average_bp_vs_pa_per_game():
    return session.query(Team.country, func.avg(Statistics.ball_possession), func.avg(Statistics.pass_accuracy)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.ball_possession).asc()).all()

def average_bp_vs_ot_per_game():
    return session.query(Team.country, func.avg(Statistics.ball_possession), func.avg(Statistics.on_target)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.ball_possession).asc()).all()

def average_bp_vs_goals_per_game():
    return session.query(Team.country, func.avg(Statistics.ball_possession), func.avg(Statistics.goals)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.ball_possession).asc()).all()

def average_bp_vs_dc_per_game():
    return session.query(Team.country, func.avg(Statistics.ball_possession), func.avg(Statistics.distance_covered)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.ball_possession).asc()).all()

#PassAcc v other stats tab:
def average_pa_vs_ot_per_game():
    return session.query(Team.country, func.avg(Statistics.pass_accuracy), func.avg(Statistics.on_target)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.pass_accuracy).asc()).all()
def average_pa_vs_dc_per_game():
    return session.query(Team.country, func.avg(Statistics.pass_accuracy), func.avg(Statistics.distance_covered)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.pass_accuracy).asc()).all()
def average_pa_vs_goals_per_game():
    return session.query(Team.country, func.avg(Statistics.pass_accuracy), func.avg(Statistics.goals)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.pass_accuracy).asc()).all()
def average_pa_vs_bp_per_game():
    return session.query(Team.country, func.avg(Statistics.pass_accuracy), func.avg(Statistics.ball_possession)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.pass_accuracy).asc()).all()

#OT v other stats tab:
def average_ot_vs_pa_per_game():
    return session.query(Team.country, func.avg(Statistics.on_target), func.avg(Statistics.pass_accuracy)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.on_target).asc()).all()

def average_ot_vs_bp_per_game():
    return session.query(Team.country, func.avg(Statistics.on_target), func.avg(Statistics.ball_possession)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.on_target).asc()).all()

def average_ot_vs_dc_per_game():
    return session.query(Team.country, func.avg(Statistics.on_target), func.avg(Statistics.distance_covered)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.on_target).asc()).all()

def average_ot_vs_goals_per_game():
    return session.query(Team.country, func.avg(Statistics.on_target), func.avg(Statistics.goals)).join(Statistics).group_by(Team.country).order_by(func.avg(Statistics.on_target).asc()).all()
