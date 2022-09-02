# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


import plotly as py
from plotly.graph_objs import *

trace1 = {
  "uid": "39d834", 
  "name": "Electric Force (mN)", 
  "type": "scatter", 
  "x": [".1", ".2", ".3", ".5", ".7", ".8"], 
  "y": ["500", "125", "56", "20.2", "10.2", "7.8"]
}
data = Data([trace1])
layout = {
  "title": "Table 4: Hyperbola", 
  "width": 1119, 
  "xaxis": {
    "type": "linear", 
    "range": [0.05770219728845254, 0.8422978027115475], 
    "title": "Distance (cm)", 
    "autorange": True
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-25.933333333333334, 533.7333333333333], 
    "title": "Electric Force (mN)", 
    "autorange": True
  }, 
  "height": 545, 
  "autosize": True
}
fig = Figure(data=data, layout=layout)
fig.show()

import plotly.express as px
fig = px.scatter(x=[0, 0, 1], y=[0, 1, 0])
fig.show()

app.layout = html.Div(children=[
    html.H1(children='RFI Localization'),

    html.Div(children='''
        RFI Localization
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)