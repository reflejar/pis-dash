from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from .empleo_prueba_1 import EMPLEO_PRUEBA
from .empleo_prueba_2 import EMPLEO_PRUEBA_2


Empleo = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('EMPLEO Y RESIDENCIA', style={'font-size': '25px'}, className="text-white"),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H6('Cantidad de EAPs según año del censo', style={'font-size': '20px'}, className="text-white"),
                html.Br(),
                dbc.Col([
                    dbc.Row(EMPLEO_PRUEBA),
                    html.Br(),
                    html.Br(),
                    ], md=5),
                dbc.Col( html.P(""" Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                        irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", className="text-white")
                        ,md=5),
                        ]),
                html.H6('Cantidad de EAPs según tamaño', style={'font-size': '20px'}, className="text-white"),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                    dbc.Row(EMPLEO_PRUEBA_2),
                    html.Br(),
                    html.Br(),
                     ], md=5),
                    dbc.Col( html.P(""" Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                        irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", className="text-white")
                        ,md=5),                       
            ])])
                