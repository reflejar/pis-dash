import json
from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from ..data import bsas

import dash_tools_reflejar as dtr

from pages.constantes import *

colorscale = ['#fff', '#E51A48']

# Agregar informacion de etiquetas
bsas["tooltip"] = bsas["nam"]

bsas_geojson = json.loads(bsas.to_json(na="keep"))

Mapa = dbc.Card(dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.H6("PROVINCIA DE BUENOS AIRES", className="fw-bolder rm-3 lm-3 text-center"),
                        html.Div(id='mapa-ranking-bsas'),
                    ]), 
                    dbc.Col([
                        html.H6("CONURBANO", className="fw-bolder rm-3 tm-3 text-center"),
                        html.Div(id='mapa-ranking-caba'),
                    ])
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
    )

@callback(
        [
            Output('mapa-ranking-bsas','children'),
            Output('mapa-ranking-caba','children'),
            Output('colorscale-ranking','style'),
        ],
        Input('tabs-ranking','active_tab')
)
def render_content(tab):
    


    mapas = {
        'escuelas': [bsas_geojson, dtr.hacer_colorscale(ROJO, 10, 8)],
        'transparencia': [bsas_geojson, dtr.hacer_colorscale(NARANJA, 10, 8)],
        'agua': [bsas_geojson, dtr.hacer_colorscale(VERDE_AGUA, 10, 8)],
        'poblaciones': [bsas_geojson, dtr.hacer_colorscale(LIMA, 10, 8)],
        'apiarios': [bsas_geojson, dtr.hacer_colorscale(LILA, 10, 8)],
        'agroecologia': [bsas_geojson, dtr.hacer_colorscale(CELESTE, 10, 8)],
    }
    select = mapas[tab]
    MapaBuenosAires = dtr.Mapa(select[0], select[1]).inicializar()
    MapaCABA = dtr.Mapa(select[0], select[1]).inicializar()

    EstiloColorScale = {
            'width': '100%',
            'height': '25px', 
            'background': f'linear-gradient(to right, {", ".join(select[1])})',
            'border': "1px solid"
        }
    
    return MapaBuenosAires, MapaCABA, EstiloColorScale
    # return dtr.Mapa(mapas[tab][0]), dtr.Mapa(mapas[tab][0]), 
