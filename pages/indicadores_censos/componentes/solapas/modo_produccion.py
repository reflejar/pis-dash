from dash import dash, html, dcc, Input, State, Output, callback
import dash_bootstrap_components as dbc
# from .tipo_cultivo_ha import CULTIVOS_HA
from ..colores import VERDE, MARRON, NARANJA, GRIS

from ..indicadores import Indicador
from ...data import df_ha_tipo_cultivo

indicadores = [
    Indicador(
        id_indicador="ha-tipo-cultivo",
        df=df_ha_tipo_cultivo,
        tipo_grafico="area",
        titulo_grafico="Héctareas implantadas según tipo de cultivo (en miles)" ,
        x="Año del censo",
        y='HA de EAPs',
        y_titulo = 'Héctáreas implantadas (en miles)',
        z='Tipo de cultivo',
        colores=[VERDE, MARRON, NARANJA, GRIS ],
        hover='Hectareas cultivadas: %{y} mil<br>Año del censo: %{x}'
    ),      
]


Produccion = html.Div([
            dbc.Row([
                html.H6('Modo de producción', style={'font-size': '25px', 'color': VERDE}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



Indicador.generar_callbacks(indicadores)