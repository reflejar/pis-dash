
from dash import dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from ..constantes import *
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
        colores=[LILA, LIMA],
        hover='Cantidad de EAPs: %{text}<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_EAPS_CANTIDAD
    ),
    Indicador(
        id_indicador="eaps-superficie",
        df=df_superficie_promedio,
        tipo_grafico="bar",
        titulo_grafico='Superficie promedio de EAPs en hectáreas',
        x="Año del censo",
        y="Superficie promedio",
        y_titulo="Superficie promedio (ha)",
        colores=[LIMA, LILA],
        hover='Superficie promedio: %{y} hectáreas<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_PROMEDIO
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
        colores=[LILA, LIMA],
        hover='Participación: %{y}%<br>Año del censo: %{x}',
        texto_descriptivo= TEXTO_EAPS_TAMANIO
    ),    
    Indicador(
        id_indicador="superficie-eaps-tamanio",
        df=df_eaps_ha_por_tamanio,
        tipo_grafico="histogram",
        titulo_grafico='Superficie ocupada por EAPs según tamaño (en miles)',
        x="Año del censo",
        y='HA de EAPs',
        y_titulo="Superficie ocupada (miles de ha) ",
        z='Tamaño EAPs',
        colores=[LILA, LIMA],
        hover='Superficie ocupada: %{y:.0f} mil<br>Año del censo: %{x}',
        texto_descriptivo=TEXTO_SUPERFICIE_TAMANIO
    ),        
    Indicador(
        id_indicador="q-eaps-juridico",
        df=df_eaps_tipo_juridico,
        tipo_grafico="area",
        titulo_grafico='Cantidad de Explotaciones Agropecuarias según tipo jurídico',
        x="Año del censo",
        y='Cantidad de EAPs',
        z='Tipo jurídico',
        colores=[LILA, LIMA],
        hover='Cantidad de EAPs: %{y}<br>Año del censo: %{x}',
        texto_descriptivo= TEXTO_TIPO_JURIDICO

    ),
    Indicador(
        id_indicador="superficie-eaps-juridico",
        df=df_ha_tipo_juridico,
        tipo_grafico="histogram",
        titulo_grafico='Superficie ocupada por EAPs según tipo jurídico (en miles)',
        x="Año del censo",
        y='HA de EAPs',
        y_titulo="Superficie ocupada (en miles de ha)",
        z='Tipo jurídico',
        colores=[LILA, LIMA],
        hover='Superficie ocupada: %{y:.0f} mil<br>Año del censo: %{x}',
        texto_descriptivo =TEXTO_HA_TIPO_JURIDICO
    ),
    Indicador(
        id_indicador="eaps-sexo-propiedad",
        df=df_propiedad_x_sexo,
        tipo_grafico="pie",
        titulo_grafico='Propiedad de EAPs según sexo Año 2018',
        x='Sexo',
        y='Cantidad de EAPs',
        colores=[LILA, LIMA],
        #hover='Cantidad de Hectareas: %{y} ha<br>Sexo: %{x}',
        texto_descriptivo= TEXTO_EAPS_SEXO
    ),                
]




ConcentracionTierra = html.Div([
            dbc.Row([
                html.H6('Concentración de la tierra', style={'font-size': '25px', 'color': LILA}),
                html.P("""
                       Siguiendo al INDEC, se utilizará como unidad de referencia a las explotaciones agropecuarias (EAP). 
                       Para entenderlo más fácilmente, podemos pensar a las EAPs como los "campos" de Argentina. Se tomará como 
                       EAPS grandes a aquellas que posean más de 500 hectáreas, mientras que las EAPS pequeñas serán las que tengan menos de 500 hectáreas. 
                       """, className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



Indicador.generar_callbacks(indicadores)
 