
from dash import html

import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros
from .componentes.mapa import MapaNormativo
from .componentes.footer_normativo import FooterNormativo




layout = html.Div([
        dbc.Row([
            dbc.Col(Filtros, lg=3),
            dbc.Col(MapaNormativo, lg=9)
        ], class_name="my-5"),
        html.Hr(),
        dbc.Row([
            dbc.Col(FooterNormativo, md=12),
        ])


        ],
        className="my-5 mx-5 min-vh-100",
    ) 
