from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


card_example = html.Div([
    #html.H1('Analisis de los Censos Agropecuarios Nacionales'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Concentración de la tierra', value='tab-1-example-graph'),
        dcc.Tab(label='Prácticas agroecológicas', value='tab-2-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
])




@callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))

def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.Br(), 
            html.H6('Cantidad de EAPs según tamaño', className="text-white"),
            html.Br(),
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="text-white"), 
            dcc.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            ),
            html.P("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
            irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", className="text-white")
        ])
    elif tab == 'tab-2-example-graph':
       return html.Div([
            html.Br(), 
            html.H6('Prácticas agroecológicas', className="text-white"),
            html.Br(),
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="text-white"), 
            dcc.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            ),
            html.P("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
            irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", className="text-white")
        ])