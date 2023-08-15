from dash import html
import dash_bootstrap_components as dbc
from .mapa_transparencia import mapa_card
color_transparencia = '#EF7286'

Transparencia = html.Div([
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