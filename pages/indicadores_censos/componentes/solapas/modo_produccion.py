from dash import html
import dash_bootstrap_components as dbc
# from .tipo_cultivo_ha import CULTIVOS_HA
from ..constantes import *

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
        colores=[LILA, LIMA, NARANJA, CELESTE ],
        hover='Hectareas cultivadas: %{y} mil<br>Año del censo: %{x}',
        texto_descriptivo = TEXTO_HA_TIPO_CULTIVO
    ),      
]


Produccion = html.Div([
            dbc.Row([
                html.H6('Modo de producción', style={'font-size': '25px', 'color': LIMA}),
                html.P("""
                       Según el CNA 2018 los cultivos en Argentina estan categorizados de la siguiente manera: 
                       cereales, oleaginosas, legumbres, cultivos industriales, forrajeras anuales y perennes, frutales, y 
                       bosques y montes implantados. La razón por la cual se analizaran sólo cereales (maíz y trigo pan), 
                       oleaginosas (soja) y forrajeras es debido a la gran cantidad de superficie que ocupan ya que son cultivos 
                       destinados a exportación y a ganadería.
                        """, className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



Indicador.generar_callbacks(indicadores)