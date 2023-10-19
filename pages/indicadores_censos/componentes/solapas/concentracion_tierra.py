
from dash import html
import dash_bootstrap_components as dbc
import dash_tools_reflejar as dtr

from ...data import *
from pages.constantes import *


TEXTO_EAPS_CANTIDAD ='Muestra la cantidad de EAP que se encontraban en funcionamiento según cada año en que se realizó el Censo Nacional Agropecuario.'
TEXTO_HA_PROMEDIO = 'Muestra la cantidad de hectáreas promedio por EAP según cada año en que se realizó el Censo Nacional Agropecuario.'
TEXTO_EAPS_TAMANIO = 'Se define como EAP pequeñas a aquellas que tienen 500 hectáreas o menos ya que poseen menos hectáreas que la media del 2018 y es el punto de corte más cercano a la media que habilita el CNA. Se define como EAP grandes a aquellas que tienen más de 500 hectáreas. Se puede observar la cantidad de EAP pequeñas y grandes que hay en cada año que se realizó el Censo Nacional Agropecuario.'
TEXTO_SUPERFICIE_TAMANIO = 'Muestra la superficie ocupada por las EAPs pequeñas y las EAPs grandes según cada año en que se realizó el Censo Nacional Agropecuario.'
TEXTO_TIPO_JURIDICO = 'Muestra la cantidad de EAPs que están en propiedad de Personas y la cantidad que está en propiedad de Empresas según cada año en que se realizó el Censo Nacional Agropecuario.'
TEXTO_HA_TIPO_JURIDICO = 'Muestra la cantidad hectáreas (superficie) que es propiedad de Personas y la cantidad que es propiedad de Empresas.'
TEXTO_EAPS_SEXO = 'Muestra el porcentaje de EAP que está en propiedad de Mujeres y en propiedad de Varones según datos del Censo Nacional Agropecuario 2018.'

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
 