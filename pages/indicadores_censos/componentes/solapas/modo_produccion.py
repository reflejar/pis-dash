from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from ..constantes import *

import dash_tools_reflejar as dtr
from ...data import df_ha_tipo_cultivo, df_cultivado_bosques, df_practicas_organicas, df_oleaginosas, df_cereales, df_forrajeras

indicadores = [
    dtr.Indicador(
        id_indicador="ha-tipo-cultivo",
        df=df_ha_tipo_cultivo,
        tipo_grafico="area",
        titulo_grafico="Héctareas implantadas según tipo de cultivo" ,
        x="Año del censo",
        y='HA de EAPs',
        y_titulo = 'Héctáreas implantadas',
        z='Tipo de cultivo',
        colores=[NARANJA,LILA, LIMA, CELESTE ],
        hover='Hectareas cultivadas: %{text} mil<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_TIPO_CULTIVO,
        divisor = 1000,
        PBAexception= True
    ),
    dtr.Indicador(
        id_indicador="oleaginosas",
        df=df_oleaginosas,
        tipo_grafico="histogram",
        titulo_grafico="Oleaginosas sembradas" ,
        x="Año del censo",
        y='HA de EAPs',
        y_titulo = 'Héctáreas sembradas',
        z='Tipo de Oleaginosa',
        colores=[NARANJA, LIMA],
        hover='Hectáreas sembradas: %{text} mil<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_OLEAGINOSAS,
        divisor = 1000
    ),
    dtr.Indicador(
        id_indicador="cereales",
        df= df_cereales,
        tipo_grafico="histogram",
        titulo_grafico="Cereales sembrados" ,
        x="Año del censo",
        y='HA de EAPs',
        y_titulo = 'Héctáreas sembradas',
        z='Tipo de cereal',
        colores=[NARANJA, LILA, LIMA],
        hover='Hectáreas sembradas: %{text} mil<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_CEREALES,
        divisor = 1000
    ),
    dtr.Indicador(
        id_indicador="forrajeras",
        df= df_forrajeras,
        tipo_grafico="histogram",
        titulo_grafico="Forrajeras sembradas" ,
        x="Año del censo",
        y='HA de EAPs',
        y_titulo = 'Héctáreas sembradas',
        z='Tipo forrajera',
        colores=[NARANJA, LIMA],
        hover='Hectáreas sembradas: %{text} mil <br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_FORRAJERAS,
        divisor = 1000,
        PBAexception=True
    ),
    dtr.Indicador(
        id_indicador="ha-bosques-cultivos",
        df=df_cultivado_bosques,
        tipo_grafico="bar",
        titulo_grafico="Bosques y Montes Naturales" ,
        x="Año del censo",
        y='HA de EAPs',
        y_titulo = 'Hectáreas',
        z='Tipo de suelo',
        colores=[NARANJA],
        hover='Hectareas: %{text} mil <br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_BOSQUES,
        divisor = 1000

    ),
    dtr.Indicador(
        id_indicador="practicas-organicas",
        df=df_practicas_organicas,
        tipo_grafico="bar",
        x="Año del censo",
        y='Prácticas orgánicasbiodinámicas/agroecológicas_EAPs',
        y_titulo = 'Cantidad de EAPs',
        titulo_grafico="EAPs con prácticas orgánicas y agroecológicas" ,        
        colores=[LIMA],
        hover='EAPs: %{text} <br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_PRACTICAS_AGROECOLOGICAS
        ),   
]

Produccion = html.Div([
            dbc.Row([
                html.H6('Modo de producción', style={'font-size': '25px', 'color': LIMA}, className="space-grotesk"),
                dbc.Container(dbc.Row(
                              dbc.Col(html.H6("""Según el CNA 2018 los cultivos en Argentina estan categorizados de la siguiente manera: 
                       cereales, oleaginosas, legumbres, cultivos industriales, forrajeras anuales y perennes, frutales, y 
                       bosques y montes implantados. La razón por la cual se analizaran sólo cereales (maíz y trigo pan), 
                       oleaginosas (soja) y forrajeras es debido a la gran cantidad de superficie que ocupan ya que son cultivos 
                       destinados a exportación y a ganadería.""", className="text-white"), md=9))),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),   
        ], className="mt-5") 

dtr.Indicador.generar_callbacks(indicadores)