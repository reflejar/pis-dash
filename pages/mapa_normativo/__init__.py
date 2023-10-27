
from dash import html

import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros
from .componentes.flechita import Flecha
from .componentes.mapa import MapaNormativo
from .componentes.footer_normativo import FooterNormativo
from .componentes.footer_normativo import Metodologia
from .componentes.encabezado import Encabezado

layout =dbc.Container([ 
            Encabezado,
            dbc.Row([
                dbc.Col(Filtros, lg=3),
                dbc.Col(MapaNormativo, lg=9)
                ]),
            Flecha,
            html.Hr(),
            FooterNormativo,
            Metodologia
        ],
        className="my-5 min-vh-100 justify-content-center"
    ) 