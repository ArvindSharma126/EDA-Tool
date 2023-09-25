from dash import html, dcc
from components.graph_info import *


def get_inputs(columns):
    column_option = [{"label": "None", "value": None}] + [
        {"label": col, "value": col} for col in columns
    ]
    return html.Div(
        [
            html.Div(
                [
                    html.H2("Graph : ", style={"font-size": 20}),
                    html.Div(
                        dcc.Dropdown(
                            id="gtype",
                            options=Graph_types,
                            value=Graph_types[0]["value"],
                            placeholder="Select the Graph type",
                        ),
                        style={"width": "40%"},
                    ),
                ]
            ),
            html.Div(
                [
                    html.H2("X : ", id="X_attr", style={"font-size": 20}),
                    html.Div(
                        dcc.Dropdown(
                            id="X",
                            options=column_option,
                            value=None,
                            placeholder="Select the x axis",
                        ),
                        style={"width": "80%"},
                    ),
                ],
                style={"display": "inline-block", "width": "50%"},
            ),
            html.Div(
                [
                    html.H2("Y : ", id="Y_attr", style={"font-size": 20}),
                    html.Div(
                        dcc.Dropdown(
                            id="Y",
                            options=column_option,
                            value=None,
                            placeholder="Select the y axis",
                        ),
                        style={"width": "80%"},
                    ),
                ],
                style={"display": "inline-block", "width": "50%"},
            ),
            html.Div(
                [
                    html.H2("Color : ", id="C_attr", style={"font-size": 20}),
                    html.Div(
                        dcc.Dropdown(
                            id="C",
                            options=column_option,
                            value=None,
                            placeholder="Select the Color",
                        ),
                        style={"width": "80%"},
                    ),
                ],
                style={"display": "inline-block", "width": "50%"},
            ),
            html.Div(
                [
                    html.H2("Size : ", id="S_attr", style={"font-size": 20}),
                    html.Div(
                        dcc.Dropdown(
                            id="S",
                            options=column_option,
                            value=None,
                            placeholder="Select the Size",
                        ),
                        style={"width": "80%"},
                    ),
                ],
                style={"display": "inline-block", "width": "50%"},
            ),
        ]
    )


def get_graph(data, gtype, X, Y, C, S):
    fig = Graphs[gtype](data, X, Y, C, S)
    return fig
