
from dash import html

import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros
from .componentes.mapa import MapaNormativo


layout = html.Div([
        dbc.Row([
            dbc.Col(Filtros, md=3),
            dbc.Col(MapaNormativo, md=9)
        ]),
        html.Hr(),
        ],
        className="my-5 mx-5 min-vh-100",
    ) 