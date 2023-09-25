import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import sys
import pandas as pd
from components import *
from components.graph_info import Graph_attributes as ga

data = pd.read_csv(sys.argv[1])
columns_ = data.columns
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "EDA",
            style={
                "textAlign": "center",
                "font-size": 40,
            },
        ),
        get_inputs(columns_),
        html.Br(),
        html.Div(dcc.Graph(id="EDA_graph")),
    ]
)


@app.callback(
    Output("EDA_graph", "figure"),
    [
        Input("gtype", "value"),
        Input("X", "value"),
        Input("Y", "value"),
        Input("C", "value"),
        Input("S", "value"),
    ],
)
def update_graph(gtype, X, Y, C, S):
    return get_graph(data, gtype, X, Y, C, S)


@app.callback(
    [
        Output("X_attr", "children"),
        Output("Y_attr", "children"),
        Output("C_attr", "children"),
        Output("S_attr", "children"),
    ],
    Input("gtype", "value"),
)
def update_attr(gtype):
    return ga[gtype]


if __name__ == "__main__":
    app.run_server()
