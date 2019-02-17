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
import plotly.graph_objs as go


avg_goals_and_distances= average_dc_vs_goals_per_game()
avg_pa_and_distances = average_dc_vs_pa_per_game()
avg_bp_and_distances= average_dc_vs_bp_per_game()
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
        dcc.Tab(label='Average Distance Covered vs. Average Goals Scored ', children=[
            html.Div([
                dcc.Graph(
                    id='avg-goals-avg-goals',
                    figure={
                        'data': [
                            go.Scatter(
                                x=[i[1] for i in avg_goals_and_distances],
                                y=[i[2] for i in avg_goals_and_distances],
                                text=[i[0] for i in avg_goals_and_distances],
                                mode='markers',
                                opacity=0.7,
                                marker={
                                    'size': 10,
                                    'line': {'width': 1, 'color': 'white'}
                                },
                                name='worldcupstring'
                            )
                        ],
                        'layout': go.Layout(
                            xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
                            yaxis={'title': 'Average Goals Scored per Game'},
                            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                ),
])
]),
dcc.Tab(label='Average Distance Covered vs. Average Pass Accuracy', children=[
    html.Div([
        dcc.Graph(
            id='avg-dist-avg-accuracy',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_pa_and_distances],
                        y=[i[2] for i in avg_pa_and_distances],
                        text=[i[0] for i in avg_pa_and_distances],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'line': {'width': 1, 'color': 'white'}
                        },
                        name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
                    yaxis={'title': 'Average Pass Accuracy (%) per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
])
]),

    dcc.Tab(label='Average Distance Covered vs. Average Ball Possession', children=[
        html.Div([
dcc.Graph(
    id='avg-dist-avg-bp',
    figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_bp_and_distances],
                y=[i[2] for i in avg_bp_and_distances],
                text=[i[0] for i in avg_bp_and_distances],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
            yaxis={'title': 'Average Ball Possession (%) per Game'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }
)
])
])






#paste new tabs above here
])
])
