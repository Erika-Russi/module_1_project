# import Flask and jsonify from flask
#csv files are just plaintext seperated by commas)
# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *
# from sqlalchemy.orm import sessionmaker, relationship, backref
# import dash
# # import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import plotly.graph_objs as go
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

from erikakyleproject import * #app, db

if __name__ == "__main__":
    app.run_server(debug=True)
