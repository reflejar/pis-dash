from dash import html
import dash_bootstrap_components as dbc
from .mapa_resumen import Mapa_resumen

color_resumen = 'rgb(170, 166, 163)'

Resumen = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('Mapa resumen', style={'font-size': '25px', 'color': color_resumen}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                
                 dbc.Row([dbc.Col([
                            dbc.Row(Mapa_resumen)                         
                            ], 
                            md=12,
                            xs=12,
                            className="justify-content-center align-items-center",
                        ),
                    ]),
                ]),
                
            
            ])