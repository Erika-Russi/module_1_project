#callbacks?
# re order graphs?
#pip install dash-table

import dash
import dash_core_components as dcc #will produce error here
import dash_html_components as html
import dash_table
from ourpackage import app  #db
from models import *
from query import *
import pandas as pd
import plotly.graph_objs as go
from flask import render_template, jsonify, json
import pandas as pd #Delete?
from dash.dependencies import Input, Output
import requests
import json

# scatter tabs variables start here:
# distance_covered v other stats
avg_goals_and_distances= average_dc_vs_goals_per_game()
avg_pa_and_distances = average_dc_vs_pa_per_game()
avg_bp_and_distances= average_dc_vs_bp_per_game()
avg_ot_and_distances= average_dc_vs_ot_per_game()
# Goals v other stats
avg_goals_v_ot= average_goals_vs_ot_per_game()
avg_goals_v_dc= average_goals_vs_dc_per_game()
avg_goals_v_pa= average_goals_vs_pa_per_game()
avg_goals_v_bp= average_goals_vs_bp_per_game()
# Possession v other stats
avg_bp_v_pa = average_bp_vs_pa_per_game()
avg_bp_v_ot= average_bp_vs_ot_per_game()
avg_bp_v_goals = average_bp_vs_goals_per_game()
avg_bp_v_dc = average_bp_vs_dc_per_game()
# Pass Acc v other stats
avg_pa_v_bp = average_pa_vs_bp_per_game()
avg_pa_v_ot= average_pa_vs_ot_per_game()
avg_pa_v_goals = average_pa_vs_goals_per_game()
avg_pa_v_dc = average_pa_vs_dc_per_game()
# OT v other stats
avg_ot_v_bp = average_ot_vs_bp_per_game()
avg_ot_v_pa= average_ot_vs_pa_per_game()
avg_ot_v_goals = average_ot_vs_goals_per_game()
avg_ot_v_dc = average_ot_vs_dc_per_game()

#return_country_and_its_total_goals... done
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
def average_ot():
    country= [x[0] for x in return_average_ot_per_game()]
    ot=[ x[1] for x in return_average_ot_per_game()]
    return [country,ot]
def venue_goals():
    venue= [x[0] for x in return_venue_by_sum_goals_desc()]
    total_goals=[ x[1] for x in return_venue_by_sum_goals_desc()]
    return [venue,total_goals]

def venue_average_goals():
    venue= [x[0] for x in return_venue_by_avg_goals_desc()]
    avg_goals=[ x[1] for x in return_venue_by_avg_goals_desc()]
    return [venue,avg_goals]

# def all_stats_table():

# app.layout = html.Div([
#     dcc.Dropdown(id='my-dropdown', ...),
#     dt.DataTable(id='my-datatable')
# ])
#
# @app.callback(Output('my-datatable', 'rows'), [Input('my-dropdown', 'value')])
# def update_rows(selected_value):
#     dff = df[df['some-column'] == value]
#     return dff.to_dict('records')
#
# df_teams = pd.DataFrame(all_games, columns=['attendance', 'away_team_country','home_team_country', 'location','status', 'time', 'venue', 'weather', 'winner'])
# team_data=df.to_dict()
#
# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict("rows"),



app.layout = html.Div([
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Country and Goals During Tournament',
        children=[
            html.Div([
                dcc.Graph(
                    id='countrygoals',
                     figure={
          'data': [{'x': country_goals()[0], 'y': country_goals()[1], 'type': 'bar'}],
          'layout': {'title': 'Total Goals By Country'} }
                ),
            dcc.Graph(
                id='averagegoals',
                figure= {
        'data': [{'x': average_goals()[0], 'y': average_goals()[1], 'type': 'bar'}],
      'layout': {'title': 'Average Goals By Country'}}
      )
      ])
      ]),
    dcc.Tab(label='Country Average Shots on Target', children=[
        html.Div([
            dcc.Graph(
                id='averagetargets',
                figure= {
        'data': [{'x': average_ot()[0], 'y': average_ot()[1], 'type': 'bar'}],
      'layout': {'title': 'Average Shots By Country'}}
),
])
]),
    dcc.Tab(label='Game Venue and Goals During Tournament', children=[
    html.Div([
        dcc.Graph(
            id='venue-sum-goals',
             figure={
  'data': [{'x': venue_goals()[0], 'y': venue_goals()[1], 'type': 'bar'}],
  'layout': {'title': 'Total Goals By Venue'} }
        ),
#
#         ])
#     ]),
# dcc.Tab(label='Country and Average Goals During Tournament', children=[
#     html.Div([
    dcc.Graph(
        id='venue-avg-goals',
        figure= {
'data': [{'x': venue_average_goals()[0], 'y': venue_average_goals()[1], 'type': 'bar'}],
'layout': {'title': 'Average Goals Per Game By Venue'}}
),
])
]),
# dcc.Tab(label='Data Table', children=[
#     html.Div([dash_table.DataTable(
#        id='table',
#        columns=[{i} for i in df2.columns],
#        data=df2.to_dict("rows")
#             )])
# ]),
dcc.Tab(label="Country's Average Distance Covered vs. Other Statistics", children=[
    html.Div([
        dcc.Graph(
            id='avg-dist-avg-goals',
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
                            'color':'green',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        # name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Distance Covered vs. Average Goals Scored per Game' },
                    xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
                    yaxis={'title': 'Average Goals Scored per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
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
                            'color': 'red',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Distance Covered vs. Average Pass Accuracy per Game' },
                    xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
                    yaxis={'title': 'Average Pass Accuracy (%) per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),dcc.Graph(
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
                    'color': 'black',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average Distance Covered vs. Average Ball Possession per Game' },
            xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
            yaxis={'title': 'Average Ball Possession (%) per Game'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        ),dcc.Graph(
        id='avg-dist-avg-ot',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_ot_and_distances],
                y=[i[2] for i in avg_ot_and_distances],
                text=[i[0] for i in avg_ot_and_distances],
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
            {'title': 'Average Distance Covered vs. Average On Target Shots per Game' },
            xaxis={'type': 'log', 'title': 'Average Distance Covered per Game (Kilometers)'},
            yaxis={'title': 'Average On Target Shots per Game'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        )
])
]),
dcc.Tab(label="Country's Average Goals Scored vs. Other Statistics ", children=[
    html.Div([
        dcc.Graph(
            id='avg-goals-avg-ot',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_goals_v_ot],
                        y=[i[2] for i in avg_goals_v_ot],
                        text=[i[0] for i in avg_goals_v_ot],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'line': {'width': 1, 'color': 'white'}
                        },
                        # name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Goals Scored vs. Average On Target Shots per Game' },
                    xaxis={'type': 'log', 'title': 'Average Goals Scored per Game'},
                    yaxis={'title': 'Average On Target Shots per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='avg-goals-avg-poss',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_goals_v_bp],
                        y=[i[2] for i in avg_goals_v_bp],
                        text=[i[0] for i in avg_goals_v_bp],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'color': 'black',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Goals Scored vs. Average Ball Possession per Game'},
                    xaxis={'type': 'log', 'title': 'Average Goals Scored per Game'},
                    yaxis={'title': 'Average Ball Possession (%) per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),dcc.Graph(
        id='avg-goals-avg-pa',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_goals_v_pa],
                y=[i[2] for i in avg_goals_v_pa],
                text=[i[0] for i in avg_goals_v_pa],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'red',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average Goals Scored vs. Average Pass Accuracy per Game'},
            xaxis={'type': 'log', 'title': 'Average Goals Scored per Game'},
            yaxis={'title': 'Average Pass Accuracy (%) per Game'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        ),dcc.Graph(
        id='avg-goals-avg-dc',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_goals_v_dc],
                y=[i[2] for i in avg_goals_v_dc],
                text=[i[0] for i in avg_goals_v_dc],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'orange',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average Goals Scored vs. Average Distance Covered per Game'},
            xaxis={'type': 'log', 'title': 'Average Goals Scored per Game'},
            yaxis={'title': 'Average Distance Covered per Game (Kilometers)'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        )
])
]),
# dcc.Tab(label='Average Distance Covered vs. Average Pass Accuracy', children=[
# html.Div([
dcc.Tab(label="Country's Average Ball Possession vs. Other Statistics", children=[
    html.Div([
        dcc.Graph(
            id='avg-bp-avg-pa',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_bp_v_pa],
                        y=[i[2] for i in avg_bp_v_pa],
                        text=[i[0] for i in avg_bp_v_pa],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'color': 'red',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        # name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Ball Possession vs. Average Pass Accuracy per Game'},
                    xaxis={'type': 'log', 'title': 'Average Ball Possession per Game (%)'},
                    yaxis={'title': 'Average Pass Accuracy per Game (%)'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='avg-bp-vs-goals',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_bp_v_goals],
                        y=[i[2] for i in avg_bp_v_goals],
                        text=[i[0] for i in avg_bp_v_goals],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'color': 'green',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Ball Possession vs. Average Goals Scored per Game'},
                    xaxis={'type': 'log', 'title': 'Average Ball Possession per Game (%)'},
                    yaxis={'title': 'Average Goals Scored per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),dcc.Graph(
        id='avg-bp-vs-dc',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_bp_v_dc],
                y=[i[2] for i in avg_bp_v_dc],
                text=[i[0] for i in avg_bp_v_dc],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'orange',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average Ball Possession vs. Average Distance Covered per Game'},
            xaxis={'type': 'log', 'title': 'Average Ball Possession per Game (%)'},
            yaxis={'title': 'Average Distance Covered per Game (Kilometers)'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        ),dcc.Graph(
        id='avg-bp-vs-avg-ot',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_bp_v_ot],
                y=[i[2] for i in avg_bp_v_ot],
                text=[i[0] for i in avg_bp_v_ot],
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
            {'title': 'Average Ball Possession vs. Average Shots on Target per Game'},
            xaxis={'type': 'log', 'title': 'Average Ball Possession per Game (%)'},
            yaxis={'title': 'Average Shots on Target per Game'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        )
])
]),
dcc.Tab(label="Country's Average Pass Accuracy vs. Other Statistics", children=[
    html.Div([
        dcc.Graph(
            id='avg-pa-avg-ot',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_pa_v_ot],
                        y=[i[2] for i in avg_pa_v_ot],
                        text=[i[0] for i in avg_pa_v_ot],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'line': {'width': 1, 'color': 'white'}
                        },
                        # name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Pass Accuracy vs. Average Shots on Target per Game'},
                    xaxis={'type': 'log', 'title': 'Average Pass Accuracy per Game (%)'},
                    yaxis={'title': 'Average On Target Shots per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='avg-pa-vs-goals',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_pa_v_goals],
                        y=[i[2] for i in avg_pa_v_goals],
                        text=[i[0] for i in avg_pa_v_goals],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'color': 'green',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average Pass Accuracy vs. Average Goals Scored per Game'},
                    xaxis={'type': 'log', 'title': 'Average Pass Accuracy per Game (%)'},
                    yaxis={'title': 'Average Goals Scored per Game'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),dcc.Graph(
        id='avg-pa-vs-dc',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_pa_v_dc],
                y=[i[2] for i in avg_pa_v_dc],
                text=[i[0] for i in avg_pa_v_dc],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'orange',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average Pass Accuracy vs. Average Distance Covered per Game'},
            xaxis={'type': 'log', 'title': 'Average Pass Accuracy per Game (%)'},
            yaxis={'title': 'Average Distance Covered per Game (Kilometers)'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        ),dcc.Graph(
        id='avg-pa-vs-avg-bp',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_pa_v_bp],
                y=[i[2] for i in avg_pa_v_bp],
                text=[i[0] for i in avg_pa_v_bp],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'black',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average Pass Accuracy vs. Average Ball Possession per Game'},
            xaxis={'type': 'log', 'title': 'Average Pass Accuracy per Game (%)'},
            yaxis={'title': 'Average Ball Possession per Game (%)'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        )
])
]),
dcc.Tab(label= "Country's Average Shots on Target vs. Other Statistics", children=[
    html.Div([
        dcc.Graph(
            id='avg-ot-avg-pa',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_ot_v_pa],
                        y=[i[2] for i in avg_ot_v_pa],
                        text=[i[0] for i in avg_ot_v_pa],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'color': 'red',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        # name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average On Target Shots vs. Average Pass Accuracy per Game'},
                    xaxis={'type': 'log', 'title': 'Average On Target Shots per Game'},
                    yaxis={'title': 'Average Pass Accuracy per Game (%)'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='avg-ot-vs-dc',
            figure={
                'data': [
                    go.Scatter(
                        x=[i[1] for i in avg_ot_v_dc],
                        y=[i[2] for i in avg_ot_v_dc],
                        text=[i[0] for i in avg_ot_v_dc],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 10,
                            'color': 'orange',
                            'line': {'width': 1, 'color': 'white'}
                        },
                        name='worldcupstring'
                    )
                ],
                'layout': go.Layout(
                    {'title': 'Average On Target Shots vs. Average Distance Covered per Game'},
                    xaxis={'type': 'log', 'title': 'Average On Target Shots per Game'},
                    yaxis={'title': 'Average Distance Covered per Game (Kilometers)'},
                    margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),dcc.Graph(
        id='avg-ot-vs-avg-goals',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_ot_v_goals],
                y=[i[2] for i in avg_ot_v_goals],
                text=[i[0] for i in avg_ot_v_goals],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'green',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average On Target Shots vs. Average Goals Scored per Game'},
            xaxis={'type': 'log', 'title': 'Average On Target Shots per Game'},
            yaxis={'title': 'Average Goals Scored per Game'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
        }
        ),dcc.Graph(
        id='avg-ot-vs-avg-bp',
        figure={
        'data': [
            go.Scatter(
                x=[i[1] for i in avg_ot_v_bp],
                y=[i[2] for i in avg_ot_v_bp],
                text=[i[0] for i in avg_ot_v_bp],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'black',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name='worldcupstring'
            )
        ],
        'layout': go.Layout(
            {'title': 'Average On Target Shots vs. Average Ball Possession per Game'},
            xaxis={'type': 'log', 'title': 'Average On Target Shots per Game'},
            yaxis={'title': 'Average Ball Possession per Game (%)'},
            margin={'l': 100, 'b': 50, 't': 50, 'r': 50},
            legend={'x': 0, 'y': 1},
            hovermode='closest')
        }
        )
])
])

#paste new tabs above here
])
])

#paste new tabs above here
