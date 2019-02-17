#4.
import dash
import dash_core_components as dcc #will produce error here
import dash_html_components as html
from __init__ import app, db  #db
from models import *
from query import *

import plotly.graph_objs as go
from flask import render_template, jsonify, json
import pandas as pd #Delete?
from dash.dependencies import Input, Output

def country_goals():
    country= [x[0] for x in return_country_and_its_total_goals()]
    goals=[ x[1] for x in return_country_and_its_total_goals()]
    return [country,goals]


app.layout = html.Div(children=[
  html.H1(children='Country and total goals during Tournament!'),

  html.Div(children='''
      Top team by Goals
  '''), #delete?

  dcc.Graph(
      id='countrygoals',
      figure={
          'data': [{'x': country_goals()[0], 'y': country_goals()[1], 'type': 'bar'}],

          'layout': {'title': 'Total Goals By Country'}

              }
  )
])

# from dash_package import *
#
# if __name__ == '__main__':
#    server.run(debug = True)










#
# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),
#
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     )
# ])
#
#
#
#
#




#

# data = [ #delete later
# #     {'name': "Brooklyn",
# #     'x': [0.86, 1.5, 2.2, 2.6, 2.7, 3, 3.67],
#     'y': [6.40, 8.34, 9.46, 11.13, 12.55, 18.68],
#     'type': "line"},
#     {'name': "Manhattan",
#     'x': [0.93, 1.33, 2.4, 2.6, 2.94, 3.34, 4.11],
#     'y': [9.34, 10.09, 13.24, 16.53, 15.64, 25.65],
#     'type': "line"}
# ]
#
# #uncomment and write the code for our Dash app below:
