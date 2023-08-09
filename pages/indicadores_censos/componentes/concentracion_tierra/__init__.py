from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from .eaps_cantidad_segun_tamanio import Q_EAPs_tamanio
from .eaps_superficie_segun_tamanio import Superficie_EAPs_tamanio
from .eaps_cantidad_segun_tipo_juridico import Q_EAPs_juridico
from .eaps_superficie_segun_tipo_juridico import Superficie_EAPs_JURIDICO
from .propietaries_eaps_sexo import PropiedadEAPSexo
from ..formatos import color_concentracion_tierra_1, color_concentracion_tierra_2
from ..indicadores import Indicador

from ...data.base_indicadores import *

# from .eaps_cantidad import EAPS_CANTIDAD
# from .eaps_superficie_ha import EAPs_SUPERFICIE

indicadores = [
    Indicador(
        id_indicador="q-eaps-total",
        df=df_eaps_cantidad,
        titulo_grafico='Cantidad de Explotaciones Agropecuarias' ,
        x="Año del censo",
        y="Cantidad de EAPs",
        colores=[color_concentracion_tierra_1, color_concentracion_tierra_2],
    ),
    Indicador(
        id_indicador="eaps-superficie",
        df=df_superficie_promedio,
        titulo_grafico='Superficie promedio de EAPs (ha)',
        x="Año del censo",
        y="Superficie promedio",
        y_titulo="Superficie promedio (ha)",
        colores=[color_concentracion_tierra_2, color_concentracion_tierra_1],
    ),    
]


Concentracion_Tierra = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('Concentración de la tierra', style={'font-size': '25px', 'color': color_concentracion_tierra_1}),
                html.P("""Siguiendo al INDEC, se utilizará como unidad de referencia a las explotaciones agropecuarias (EAP). Para entenderlo más fácilmente, 
                    podemos pensar a las EAPs como los "campos" de Argentina. Se tomará como EAPS grandes a aquellas 
                    que posean más de 500 hectáreas, mientras que las EAPs pequeñas serán las que tengan menos de 500 hectáreas.""", className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                ]),
                #html.H6('Cantidad de EAPs según año del censo', style={'font-size': '20px'}, className="text-white"),
                html.Br(),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=4) for i in indicadores]),
        ])         
                




# for i in indicadores:
#     @callback(
#         Output(i.id, "figure"),
#         Input("select-partido", "value"),
#     )
#     def update_graph(selected_value): return i.update(selected_value)


@callback(
    Output(indicadores[0].id, "figure"),
    Input("select-partido", "value"),
)
def update_graph(selected_value): return indicadores[0].update(selected_value)


@callback(
    Output(indicadores[1].id, "figure"),
    Input("select-partido", "value"),
)
def update_graph(selected_value): return indicadores[1].update(selected_value)