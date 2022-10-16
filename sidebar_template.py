import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from datetime import date

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)


header = dbc.Row(
    [
        html.H1(
            "This is the Header",
            style={"textAlign": "center", "color": "white", "textWeight": "bold"},
        )
    ],
    align="center",
    justify="center",
    style={
        "backgroundColor": "#14008E",
        "border": "2px white solid",
        'border-radius': '15px',
    },
)


sidebar = dbc.Col(
    [
        html.Label(
            "Select Item",
            style={"marginTop": "20px", "border": "1px red solid"},
        ),
        dcc.Dropdown(
            id="inp1",
            options=["a", "b", "c"],
            value="a",
            style={"marginBottom": "20px", "border": "1px red solid"},
        ),
        html.Label("Select Item"),
        dcc.RadioItems(
            id="inp2",
            options=["a", "b", "c"],
            value="a",
            labelStyle={"display": "block"},
            style={"marginBottom": "20px", "border": "1px red solid"},
        ),
        html.Label("Select Item"),
        dcc.Checklist(
            id="inp3",
            options=["a", "b", "c"],
            value=["a", "b"],
            labelStyle={"display": "block"},
            style={"marginBottom": "20px", "border": "1px red solid"},
        ),
        html.Label("Pick Date", style={"marginRight": "5px"}),
        dcc.DatePickerSingle(
            id="inp4",
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2017, 9, 19),
            initial_visible_month=date(2017, 8, 5),
            date=date(2017, 8, 25),
        ),
    ],
    width={"size": 2, "offset": 0, "order": 1},
    style={
        "backgroundColor": "#d1e9ff",
        "border": "1px solid black",
        'border-radius': '15px',
        "height": "720px",
    },
)


element_col_1 = dbc.Col(
    [
        dcc.Graph(
            id="g1",
            style={"border": "1px solid red","marginBottom": "7px", "height": "350px"},
        ),
        dcc.Graph(
            id="g2",
            style={"border": "1px solid red", "marginBottom": "7px", "height": "350px"},
        ),
    ],
    width={"size": 5, "offset": 0, "order": 2},
)

element_col_2 = dbc.Col(
    [
        dcc.Graph(
            id="g3",
            style={"border": "1px solid red", "marginBottom": "7px", "height": "350px"},
        ),
        dcc.Graph(
            id="g4",
            style={"border": "1px solid red", "marginBottom": "7px", "height": "350px"},
        ),
    ],
    width={"size": 5, "offset": 0, "order": 3},
)


app.layout = dbc.Container(
    [
        header,
        dbc.Row([sidebar, element_col_1, element_col_2], align="center", justify="center"),

    ],
    fluid=True,style={'backgroundColor':'#EAF5FF'}
)




if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
