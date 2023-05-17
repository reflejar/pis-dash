
from dash import html

import dash_bootstrap_components as dbc
from .componentes.texto_inicial_indicadores import TextoIndicadores


layout = html.Div([
        dbc.Row([
            dbc.Col(TextoIndicadores, md=12),
        ])


        ],
        className="my-5 mx-5 min-vh-100",
    ) 