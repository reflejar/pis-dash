from dash import html
import dash_bootstrap_components as dbc
from .mapa_transparencia import mapa_card
color_transparencia = '#EF7286'

Transparencia = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                
                 dbc.Row([dbc.Col([
                            dbc.Row(mapa_card)                         
                            ], 
                            md=12,
                            xs=12,
                            className="justify-content-center align-items-center",
                        ),
                    ]),
                ]),
                
            
            ])