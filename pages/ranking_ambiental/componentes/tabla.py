from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash

from pages.constantes import *
import dash_tools_reflejar as dtr
from ..data import DATA

Tabla = Hash(html.Div(id='card-tabla-ranking'), size=24, color=LIMA)


@callback(
        Output('card-tabla-ranking','children'),
        Input('tabs-ranking','active_tab')
)
def render_content(tab):
    selected = DATA[tab]
    return dbc.Card([
        dbc.CardHeader(html.H5(tab.upper(),className="fw-bolder rm-3 lm-3 text-center"), style={"background-color": selected['color'], "border-radius": "0.5rem"}),
        dbc.CardBody(html.Div([
            dbc.Row([html.P("* Regido por Ley Provincial N°10699, Decreto Reglamentario 499/91, Artículo N° 38.", className="text-end")]) if tab == "poblaciones" else "",
            dbc.Row([dtr.Tabla('tabla-ranking',selected['color'],selected['color_claro'],   selected['data'] ).inicializar()]),
            dbc.Row([html.P("Las unidades de Exclusión y Amortiguamiento se encuentran expresadas en metros.", className="text-start mt-3")]),
        ]))
    ], style={"border-radius": "0.5rem"})