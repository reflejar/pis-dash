
from dash import html
import dash_bootstrap_components as dbc
from ..constantes import *
from ..indicadores import Indicador

from ...data import *


indicadores = [        
    Indicador(
        id_indicador="residentes-sexo",
        df=df_residentes_por_sexo,
        tipo_grafico="histogram",
        titulo_grafico="Evolución de residentes del campo por sexo",
        x="Año del censo",
        y='Cantidad de personas',
        z='Sexo de nacimiento',
        colores=[NARANJA, VERDE_AGUA],
        hover='Cantidad de Residentes: %{y}<br>Año del censo: %{x}',
        texto_descriptivo=TEXTO_RESIDENTES_SEXO
    ),      
    Indicador(
        id_indicador="evolucion-empleo",
        df=df_evolucion_empleo,
        tipo_grafico="area",
        titulo_grafico='Evolución del empleo permanente en el campo',
        x="Año del censo",
        y='Empleo',
        colores=[NARANJA],
        hover='Cantidad de personas empleadas: %{y}<br>Año del censo: %{x}',
        texto_descriptivo=TEXTO_VARIACION_EMPLEO
    ),          
          
]




Empleo = html.Div([
            dbc.Row([
                html.H6('Empleo y Residencia', style={'font-size': '25px', 'color': NARANJA}),
                html.P("""
                       ¿Qué sucedió con la residencia y los puestos de trabajo de los y 
                       las trabajadoras del campo en estos años de fuerte industrialización de la agricultura y concentración de la tierra? 
                       """, className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



Indicador.generar_callbacks(indicadores)