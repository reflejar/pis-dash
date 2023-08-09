
from dash import html

import dash_bootstrap_components as dbc
from .componentes.texto_inicial_indicadores import TextoIndicadores
from .componentes.filtros_indicadores import Filtros_censos
from .componentes.solapas_indicadores import SolapasIndicadores


layout = html.Div([
        dbc.Row([
            dbc.Col(TextoIndicadores, md=12),
            dbc.Col(Filtros_censos, md=12),
        ]),
        html.Br(),
        html.Br(),
        dbc.Container(
            dbc.Row(
                dbc.Col(SolapasIndicadores, md=12)
            ),
        ),
        ],
        className="my-5 mx-5 min-vh-100",
    ) 