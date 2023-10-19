from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash

from pages.constantes import *
import dash_tools_reflejar as dtr
from ..data import DATA

Tabla = Hash(html.Div(id='card-tabla-ranking'), size=24, color=ROJO)


@callback(
        Output('card-tabla-ranking','children'),
        Input('tabs-ranking','active_tab')
)
def render_content(tab):
    selected = DATA[tab]
    return dbc.Card([
        dbc.CardHeader(tab.upper(), style={"background-color": selected['color']}, class_name="fw-bolder text-center"),
        dbc.CardBody(dtr.Tabla('tabla-ranking', selected['data']).inicializar())
    ])