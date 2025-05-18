"""
When rendering Plotly graphs as the children of tabs, sometimes the graph will
not be sized correctly if it wasn't initially visible. The solution to this
problem is to render the tab content dynamically using a callback.

This example shows how to do that, and also shows how to use a dcc.Store
component to cache the graph data so that if the generating process is slow,
the graph still renders quickly when the user switches tabs.
"""

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
import pandas as pd
from dash import Input, State, Output, dcc, html
import settings as st

EXPLAINER = """This example shows how to use callbacks to render graphs inside
tab content to ensure that they are sized correctly when switching tabs. It
also demonstrates use of a `dcc.Store` component to cache graph data so that
if the data generating process is expensive, switching tabs is still quick."""

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.read_csv('data/us_data.csv')
app.layout = dbc.Container(
    [
        html.H1("Dynamically rendered tab content"),
        dcc.Markdown(EXPLAINER),
        dbc.Button(
            "Anamnesis",
            id="collapse-button",
            className="mb-3",
            color="secodary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card([
                dbc.Button(
                "Regenerate graphs",
                color="secodary",
                id="button",
                className="mb-3",
                disabled=False),
                html.H2("Данные анамнеза", className="h2-label"),
                html.Label("Диагноз", className="filter-label"), 
                dcc.Dropdown(id="diagnosis_primary-filter",
                                  options=[{'label': dp, 'value': dp } for dp in df['diagnosis_primary'].unique()],
                                  value=df['diagnosis_primary'].unique(),
                                  multi=True, 
                                  className="filter-dropdown",
                            
                                  ),
                                  html.Div(
    [
        dbc.Label("Choose one"),
        dbc.Select(
            options=[{'label': dp, 'value': dp } for dp in df['diagnosis_primary'].unique()],
                                  value=df['diagnosis_primary'].unique(),
            id="radioitems-input",
        ),
    ]
)
                                  ]
                ),
            id="collapse",
            is_open=False,
        ),
    
        dbc.Tabs(
            [
                dbc.Tab(label="Scatter", tab_id="scatter"),
                dbc.Tab(label="Histograms", tab_id="histogram"),
            ],
            id="tabs",
            active_tab="scatter",
        ),
        # we wrap the store and tab content with a spinner so that when the
        # data is being regenerated the spinner shows. delay_show means we
        # don't see the spinner flicker when switching tabs
        dbc.Spinner(
            [
                dcc.Store(id="store"),
                html.Div(id="tab-content", className="p-4"),
            ],
            delay_show=100,
        ),
    ]
)

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab and data is not None:
        if active_tab == "scatter":
            return dcc.Graph(figure=data["scatter"])
        elif active_tab == "histogram":
            return dbc.Row(
                [
                    dbc.Button(
            "Regenerate graphs",
            color="primary",
            id="button",
            className="mb-3",
            
        ),
                    dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
                    dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
                    # dbc.Col(data["message"])
                    
                ]
            )
    return "No tab selected"


@app.callback(Output("store", "data"), 
              Input('radioitems-input', 'value'),
              Input("button", "n_clicks"))
def generate_graphs(selected_input,n):
    """
    This callback generates three simple graphs from random data.
    """
    if not n:
        # generate empty graphs when app loads
        return {k: go.Figure(data=[]) for k in ["scatter", "hist_1", "hist_2"]}

    # simulate expensive graph generation process
    time.sleep(2)

    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

    scatter = go.Figure(data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")])
    hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
    hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])
    df1 = pd.DataFrame({'name': selected_input})
    message = html.P(df1['name'][1])

    # save figures in a dictionary for sending to the dcc.Store
    return {"scatter": scatter, "hist_1": hist_1, "hist_2": hist_2, "message":message}


if __name__ == "__main__":
    app.run(debug=True, port=8888)