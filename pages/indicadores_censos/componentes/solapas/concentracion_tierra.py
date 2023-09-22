
from dash import html
import dash_bootstrap_components as dbc
from ..constantes import *
import dash_tools_reflejar as dtr

from ...data import *


indicadores = [
    dtr.Indicador(
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
    dtr.Indicador(
        id_indicador="eaps-superficie",
        df=df_superficie_promedio,
        tipo_grafico="bar",
        titulo_grafico='Superficie promedio de EAPs en hectáreas',
        x="Año del censo",
        y="Superficie promedio",
        y_titulo="Superficie promedio (ha)",
        colores=[LIMA, LILA],
        hover='Superficie promedio: %{text} hectáreas<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_PROMEDIO
    ),
    dtr.Indicador(
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
        hover='Participación: %{y}%<br>Cantidad de EAPs: %{text} <br>Año del censo: %{x}',
        texto_descriptivo= TEXTO_EAPS_TAMANIO
    ),    
    dtr.Indicador(
        id_indicador="superficie-eaps-tamanio",
        df=df_eaps_ha_por_tamanio,
        tipo_grafico="histogram",
        titulo_grafico='Superficie ocupada por EAPs según tamaño',
        x="Año del censo",
        y='HA de EAPs',
        y_titulo="Superficie ocupada",
        z='Tamaño EAPs',
        colores=[LILA, LIMA],
        hover='Superficie ocupada: %{text}<br>Año del censo: %{x}',
        texto_descriptivo=TEXTO_SUPERFICIE_TAMANIO,
        divisor = 1000,
        PBAexception=True
    ),        
    dtr.Indicador(
        id_indicador="q-eaps-juridico",
        df=df_eaps_tipo_juridico,
        tipo_grafico="area",
        titulo_grafico='Cantidad de Explotaciones Agropecuarias según tipo jurídico',
        x="Año del censo",
        y='Cantidad de EAPs',
        z='Tipo jurídico',
        colores=[LILA, LIMA],
        hover='Cantidad de EAPs: %{text}<br>Año del censo: %{x}',
        texto_descriptivo= TEXTO_TIPO_JURIDICO

    ),
    dtr.Indicador(
        id_indicador="superficie-eaps-juridico",
        df=df_ha_tipo_juridico,
        tipo_grafico="histogram",
        titulo_grafico='Superficie ocupada por EAPs según tipo jurídico',
        x="Año del censo",
        y='HA de EAPs',
        y_titulo="Superficie ocupada",
        z='Tipo jurídico',
        colores=[LILA, LIMA],
        hover='Superficie ocupada: %{text}<br>Año del censo: %{x}',
        texto_descriptivo =TEXTO_HA_TIPO_JURIDICO,
        divisor = 1000,
        PBAexception=True
    ),
    dtr.Indicador(
        id_indicador="eaps-sexo-propiedad",
        df=df_propiedad_x_sexo,
        tipo_grafico="pie",
        titulo_grafico='Propiedad de EAPs según sexo Año 2018',
        x='Sexo',
        y='Cantidad de EAPs',
        colores=[LILA, LIMA],
        texto_descriptivo= TEXTO_EAPS_SEXO
    ),                
]


ConcentracionTierra = html.Div([
            dbc.Row([
                html.H6('Concentración de tierras', style={'font-size': '25px', 'color': LILA}, className="space-grotesk"),
                dbc.Container(dbc.Row(
                              dbc.Col(html.H6(["La unidad de referencia de los Censos son las ",
                       html.Strong("Explotaciones Agropecuarias"),
                     """ o EAP. Podemos pensarlos como los "campos" de Argentina (se considera como EAPs grandes a aquellas que posean más de 500 hectáreas, 
                       mientras que las EAPs pequeñas serán las que tengan menos de 500 hectáreas). 
                       """], className="text-white"), md=9))),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



dtr.Indicador.generar_callbacks(indicadores)
 