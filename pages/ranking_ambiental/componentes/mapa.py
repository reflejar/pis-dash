import json
from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from ..data import DATA

from dash_loading_spinners import Hash

import dash_tools_reflejar as dtr
from pages.constantes import *

Mapa = Hash(dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.H6("PROVINCIA DE BUENOS AIRES", className="fw-bolder rm-3 lm-3 text-center"),
                        html.Div(id='mapa-ranking-bsas'),
                    ], lg=6, xs=12), 
                    dbc.Col([
                        html.H6("CONURBANO", className="fw-bolder rm-3 tm-3 text-center"),
                        html.Div(id='mapa-ranking-caba'),
                    ], lg=6, xs=12)
                ]),
                dbc.Row(
                    dbc.Col([
                        html.H5("PROTECCIÓN", className="fw-bolder rm-3 lm-3 text-center"),
                            dbc.Row([
                                dbc.Col("MENOR", class_name="text-end", xs=3),
                                dbc.Col(html.Div(id="colorscale-ranking"), xs=6),
                                dbc.Col("MAYOR", class_name="text-start", xs=3),
                            ])
                    ], lg={'size': 6, 'offset': 3}
                ), class_name="mt-4"),  
            ],
        ),
        color="light", 
        class_name="shadow my-5",
        outline=True,
    ), size=24, color=ROJO)

@callback(
        [
            Output('mapa-ranking-bsas','children'),
            Output('mapa-ranking-caba','children'),
            Output('colorscale-ranking','style'),
        ],
        Input('tabs-ranking','active_tab')
)
def render_content(tab):
    selected = DATA[tab]
    colorscale = dtr.hacer_colorscale(selected['color'], 10, 8)

    MapaBuenosAires = dtr.Mapa(selected['geojson_bsas'], colorscale).inicializar()
    MapaCABA = dtr.Mapa(selected['geojson_bsas'], colorscale).inicializar()
    EstiloColorScale = {
            'width': '100%',
            'height': '25px', 
            'background': f'linear-gradient(to right, {", ".join(colorscale)})',
            'border': "1px solid"
        }
    
    return MapaBuenosAires, MapaCABA, EstiloColorScale
