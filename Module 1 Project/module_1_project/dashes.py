import dash
import dash_core_components as dcc
import dash_html_components as html

#similar to app = Flask(__name__)
app = dash.Dash(__name__)

#5:40pm
app.layout = html.Div(children = [
        html.H2 ('hello')
        html.H2 ('world')]

#~5:30pm
if __name == '__main__':
    app.run_server(debug = True)
