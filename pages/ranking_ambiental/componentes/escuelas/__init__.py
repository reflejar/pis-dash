from dash import html
import dash_bootstrap_components as dbc
from .mapa_escuelas import mapa_card


Escuelas = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
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