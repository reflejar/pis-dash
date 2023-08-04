from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
# from .cultivos_hectareas_1988 import CULTIVOS_1988
# from .cultivos_hectareas_2002 import CULTIVOS_2002
# from .cultivos_hectareas_2018 import CULTIVOS_2018

from .tipo_cultivo_ha import CULTIVOS_HA
from ..formatos import color_cultivos_1

Produccion = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('Modo de producción', style={'font-size': '25px', 'color': color_cultivos_1}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                
                 dbc.Row([dbc.Col([
                            dbc.Row(CULTIVOS_HA)                         
                            ], md=4, className="justify-content-center align-items-center")                         
                    ]),
                ]),
                
            
            ])