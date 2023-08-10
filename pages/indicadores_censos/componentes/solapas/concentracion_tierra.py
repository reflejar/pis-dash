
from dash import dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from ..formatos import COLOR_NARANJA, COLOR_MARRON
from ..indicadores import Indicador

from ...data import *


indicadores = [
    Indicador(
        id_indicador="q-eaps-total",
        df=df_eaps_cantidad,
        tipo_grafico="bar",
        titulo_grafico='Cantidad de Explotaciones Agropecuarias' ,
        x="Año del censo",
        y="Cantidad de EAPs",
        colores=[COLOR_NARANJA, COLOR_MARRON],
        hover='Cantidad de EAPs: %{text}<br>Año del censo: %{x}'
    ),
    Indicador(
        id_indicador="eaps-superficie",
        df=df_superficie_promedio,
        tipo_grafico="bar",
        titulo_grafico='Superficie promedio de EAPs en hectáreas',
        x="Año del censo",
        y="Superficie promedio",
        y_titulo="Superficie promedio (ha)",
        colores=[COLOR_MARRON, COLOR_NARANJA],
        hover='Superficie promedio: %{y} hectáreas<br>Año del censo: %{x}'
    ),
    Indicador(
        id_indicador="q-eaps-tamanio",
        df=df_eaps_por_tamanio,
        tipo_grafico="histogram",
        titulo_grafico='Participación de Explotaciones Agropecuarias según tamaño',
        x="Año del censo",
        y='Cantidad de EAPs',
        y_titulo="Distribución de EAPs según tamaño",
        z='Tamaño EAPs',
        porcentaje=True,
        colores=[COLOR_NARANJA, COLOR_MARRON],
        hover='Participación: %{y}%<br>Año del censo: %{x}'
    ),    
    Indicador(
        id_indicador="superficie-eaps-tamanio",
        df=df_eaps_ha_por_tamanio,
        tipo_grafico="histogram",
        titulo_grafico='Superficie ocupada por EAPs según tamaño',
        x="Año del censo",
        y='HA de EAPs',
        y_titulo="Superficie ocupada (ha) según tamaño",
        z='Tamaño EAPs',
        colores=[COLOR_NARANJA, COLOR_MARRON],
        hover='Superficie ocupada: %{y:.0f} ha<br>Año del censo: %{x}'
    ),        
    Indicador(
        id_indicador="q-eaps-juridico",
        df=df_eaps_tipo_juridico,
        tipo_grafico="area",
        titulo_grafico='Cantidad de Explotaciones Agropecuarias según tipo jurídico',
        x="Año del censo",
        y='Cantidad de EAPs',
        z='Tipo jurídico',
        colores=[COLOR_NARANJA, COLOR_MARRON],
        hover='Cantidad de EAPs: %{y}<br>Año del censo: %{x}'
    ),
    Indicador(
        id_indicador="superficie-eaps-juridico",
        df=df_ha_tipo_juridico,
        tipo_grafico="histogram",
        titulo_grafico='Superficie ocupada por EAPs según tipo jurídico',
        x="Año del censo",
        y='HA de EAPs',
        y_titulo="Superficie ocupada (ha)",
        z='Tipo jurídico',
        colores=[COLOR_NARANJA, COLOR_MARRON],
        hover='Superficie ocupada: %{y:.0f} ha<br>Año del censo: %{x}'
    ),                
]




ConcentracionTierra = html.Div([
            dbc.Row([
                html.H6('Concentración de la tierra', style={'font-size': '25px', 'color': COLOR_NARANJA}),
                html.P("""Siguiendo al INDEC, se utilizará como unidad de referencia a las explotaciones agropecuarias (EAP). Para entenderlo más fácilmente, 
                    podemos pensar a las EAPs como los "campos" de Argentina. Se tomará como EAPS grandes a aquellas 
                    que posean más de 500 hectáreas, mientras que las EAPs pequeñas serán las que tengan menos de 500 hectáreas.""", className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



for i in range(len(indicadores)):
    id_indicador = indicadores[i].id
    @callback(
        Output(id_indicador, "figure"),
        Input("select-partido", "value"),
    )
    def update_graph(selected_value, i=i):
        return indicadores[i].actualizar(selected_value)
    
    @callback(
        [
            Output(f"modal-{id_indicador}", "is_open"),
            Output(f"modal-graph-{id_indicador}", "figure"),
            Output(f"modal-open-{id_indicador}", "n_clicks"),
        ],
        [
            Input(f"modal-open-{id_indicador}", 'n_clicks'),
            Input(f"modal-close-{id_indicador}", "n_clicks"),
        ],
        [
            State(f"modal-{id_indicador}", "is_open"),
            State(f"{id_indicador}", "figure")
        ]
    )
    def toggle_modal(open_modal, close_modal, is_open_modal, figure, i=i):
        if is_open_modal:
            return False, dash.no_update, 0
        if open_modal:
            return True, figure, 1
        return is_open_modal, dash.no_update,0
