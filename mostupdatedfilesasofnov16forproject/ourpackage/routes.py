from ourpackage import *
from ourpackage.models import *
from flask import render_template, jsonify, json
#new
from ourpackage import db, app
from ourpackage.dashboard import app


# 
# @app.server.route('/team/')
# def user_index():
#     all_teams = db.session.query(Team).all()
#     all_teams_dicts = [team.to_dict() for team in all_teams]
#     return jsonify(all_teams_dicts)



#
# external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css', 'https://codepen.io/chriddyp/pen/bWLwgP.css']
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
#
#
# df = pd.read_sql_table('teams', engine)
#
#
# def simple_team_table():
#     table_headers = Team.__table__.columns.keys()[2:-1]
#     row_values = [[item.position for item in team_list()], [item.name for item in team_list()], [item.GP for item in team_list()], [item.W for item in team_list()], [item.D for item in team_list()], [item.L for item in team_list()], [item.points for item in team_list()], [item.GF for item in team_list()], [item.GA for item in team_list()], [item.GD for item in team_list()], [item.player_points for item in team_list()]]
#     trace = go.Table(
#     header=dict(values=table_headers),
#     cells=dict(values=row_values))
#     return dict(data = [trace])
#
# def simple_player_table():
#     table_headers = Player.__table__.columns.keys()[2:-2]
#     slice1 = table_headers[1:]
#     row_values = [[item.name for item in get_money_team_objects()], [item.team.name for item in get_money_team_objects()], [item.position for item in get_money_team_objects()], [item.cost for item in get_money_team_objects()], [item.total_points for item in get_money_team_objects()], [item.bonus for item in get_money_team_objects()], [item.minutes for item in get_money_team_objects()], [item.status for item in get_money_team_objects()], [item.roi for item in get_money_team_objects()]]
#     trace = go.Table(
#     header=dict(values=table_headers),
#     cells=dict(values=row_values))
#     return dict(data = [trace])
