from dash import html
import dash_bootstrap_components as dbc
from .residentes_por_sexo import ResidentesPorSexo
from .evolucion_empleo import Empleo
from ..formatos import color_empleo_1

Empleo = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('Empleo y Residencia', style={'font-size': '25px', 'color': color_empleo_1}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                
                 dbc.Row([dbc.Col([
                            dbc.Row(ResidentesPorSexo)                         
                            ], md=4, className="justify-content-center align-items-center"),
                        dbc.Col([
                            dbc.Row(Empleo)
                            ], md=4,  className="justify-content-center align-items-center"),
                    ]),
                ]),
                
            
            ])
                