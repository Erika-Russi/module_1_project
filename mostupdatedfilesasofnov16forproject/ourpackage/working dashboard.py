#callbacks?
# re order graphs?

import dash
import dash_core_components as dcc #will produce error here
import dash_html_components as html
# from ourpackage import app  #db
from models import *
from query import *

import plotly.graph_objs as go
from flask import render_template, jsonify, json
import pandas as pd #Delete?
from dash.dependencies import Input, Output

#return_country_and_its_total_goals... done

# def avg_goals

def country_goals():
    country= [x[0] for x in return_country_and_its_total_goals()]
    goals=[ x[1] for x in return_country_and_its_total_goals()]
    return [country,goals]

#return_average_goals_per_game
def average_goals():
    country= [x[0] for x in return_average_goals_per_game()]
    goals=[ x[1] for x in return_average_goals_per_game()]
    return [country,goals]
#return_average_ot_per_game
def average_ot_per_game():
    country= [x[0] for x in return_average_ot_per_game()]
    ot=[ x[1] for x in return_average_ot_per_game()]
    return [country,ot]

# #return_average_pa_per_game
# def return_average_pa_per_game

app.layout = html.Div([
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Country and Total Goals During Tournament', children=[
            html.Div([
                dcc.Graph(
                    id='countrygoals',
                     figure={
          'data': [{'x': country_goals()[0], 'y': country_goals()[1], 'type': 'bar'}],
          'layout': {'title': 'Total Goals By Country'} }
                ),
            ])
        ]),
    dcc.Tab(label='Country and Average Goals During Tournament', children=[
        html.Div([
            dcc.Graph(
                id='averagegoals',
                figure= {
        'data': [{'x': average_goals()[0], 'y': average_goals()[1], 'type': 'bar'}],
      'layout': {'title': 'Average Goals By Country'}}
),
])
]),
    dcc.Tab(label='Country Average Shots on Target', children=[
        html.Div([
            dcc.Graph(
                id='averagetargets',
                figure= {
        'data': [{'x': average_ot_per_game()[0], 'y': average_ot_per_game()[1], 'type': 'bar'}],
      'layout': {'title': 'Average Shots By Country'}}
),
])
])






#paste new tabs above here
])
])
