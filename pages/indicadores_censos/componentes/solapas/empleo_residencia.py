
from dash import dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from ..colores import NARANJA, VERDE
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
        colores=[NARANJA, VERDE],
        hover='Cantidad de Residentes: %{y}<br>Año del censo: %{x}'
    ),      
    Indicador(
        id_indicador="evolucion-empleo",
        df=df_evolucion_empleo,
        tipo_grafico="bar",
        titulo_grafico='Evolución del empleo permanente en el campo',
        x="Año del censo",
        y='Empleo',
        colores=[NARANJA],
        hover='Cantidad de personas empleadas: %{text}<br>Año del censo: %{x}'
    ),          
          
]




Empleo = html.Div([
            dbc.Row([
                html.H6('Empleo y Residencia', style={'font-size': '25px', 'color': NARANJA}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



Indicador.generar_callbacks(indicadores)