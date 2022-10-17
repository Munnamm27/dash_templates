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









app.layout = dbc.Container(
    [

    ],
    fluid=True
)





if __name__ == "__main__":
    app.run_server(debug=True, port=8050)