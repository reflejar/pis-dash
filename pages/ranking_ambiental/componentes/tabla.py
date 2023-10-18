from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc

import dash_tools_reflejar as dtr

from ..data import escuelas
from pages.constantes import *


Tabla = html.Div(id='tabla-ranking')

@callback(
        Output('tabla-ranking','children'),
        Input('tabs-ranking','active_tab')
)
def render_content(tab):
    tables = {
        'escuelas': [escuelas, ROJO],
        'transparencia': [escuelas, NARANJA],
        'agua': [escuelas, VERDE_AGUA],
        'poblaciones': [escuelas, LIMA],
        'apiarios': [escuelas, LILA],
        'agroecologia': [escuelas, CELESTE],
    }
    return dbc.Card([
        dbc.CardHeader(tab.upper(), style={"background-color": tables[tab][1]}, class_name="text-center"),
        dbc.CardBody(dtr.Tabla(tables[tab][0]).inicializar())
    ])