from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from .concetracion_tierra import EAPS_HA

card_example = html.Div([
    #html.H1('Analisis de los Censos Agropecuarios Nacionales'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Concentración de tierras', value='tab-1'),
        dcc.Tab(label='Empleo y residencia', value='tab-2'),
        dcc.Tab(label='Cultivos', value='tab-3'),
        dcc.Tab(label='Modo de producción', value='tab-4'),
        dcc.Tab(label='Resumen', value='tab-5'),
    ]),
    html.Div(id='tabs-content')
])




@callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(), 
                html.H6('  Concentración de la tierra', style={'font-size': '25px'}, className="text-white"),
                html.Br(),
                html.Br(),
                dbc.Col(EAPS_HA, md=6),
                dbc.Col(
                    html.Div([
                        html.H6('Cantidad de EAPS, distribuidas según el año del censo', style={'font-size': '20px'}, className="text-white"),
                        html.Br(),
                        html.Br(),
                        html.P("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                        irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", className="text-white")
                        ]), md=6
                    ), 
            ]),
            
       ]), 
    # elif tab == 'tab-2-example-graph':
    #    return html.Div([
    #         html.Br(), 
    #         html.H6('Prácticas agroecológicas', className="text-white"),
    #         html.Br(),
    #         html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="text-white"), 
    #         dcc.Graph(
    #             figure={
    #                 'data': [{
    #                     'x': [1, 2, 3],
    #                     'y': [3, 1, 2],
    #                     'type': 'bar'
    #                 }]
    #             }
    #         ),
    #         html.P("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    #         sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
    #         quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
    #         irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    #         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", className="text-white")
    #     ])