from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from .residencia_mujeres import residencia_mujeres
from .residencia_mujeres import texto_residentes_mujeres
from .residencia_varones import residencia_varones
from .residencia_varones import texto_residentes_varones

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
                html.H6('Cantidad de mujeres residentes en zonas rurales', style={'font-size': '20px'}, className="text-white"),
                html.Br(),
                html.Br(),
                dbc.Col([
                    dbc.Row(residencia_mujeres),
                    html.Br(),
                    html.Br(),
                    ], md=5),
                dbc.Col( texto_residentes_mujeres,md=5),
                        ]),
                html.H6('Cantidad de varones residentes en zonas rurales', style={'font-size': '20px'}, className="text-white"),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                    dbc.Row(residencia_varones),
                    html.Br(),
                    html.Br(),
                     ], md=5),
                    dbc.Col( texto_residentes_varones,md=5),                       
            ]),

            
            ])
                