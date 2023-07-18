from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from .residencia import residencia
from .empleo import empleo


color_empleo= 'rgb(225, 134, 95)'

Empleo = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('Empleo y Residencia', style={'font-size': '25px', 'color': color_empleo}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                
                 dbc.Row([dbc.Col([
                            dbc.Row(residencia)                         
                            ], md=4, className="justify-content-center align-items-center"),
                        dbc.Col([
                            dbc.Row(empleo)
                            ], md=4,  className="justify-content-center align-items-center"),
                    ]),
                ]),
                
            
            ])
                