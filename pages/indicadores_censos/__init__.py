from dash import html
import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros_censos
from .componentes.solapas import Solapas
from .componentes.solapas.resumen_general import *
from .componentes.metodologia import MetodologiaCenso, IndicadoresCenso


layout = dbc.Container([
            dbc.Row([
                    dbc.Col(html.Div([      
                            html.H4(html.Strong('Censo Nacional Agropecuario'), className="text-white pt-3 space-grotesk"),
                            html.Br(),
                            html.H6(["""Visualizaciones y análisis de los principales indicadores de los últimos tres censos agropecuarios sistematizados por municipio. 
                                    Información histórica con perspectiva local. Podés descargar el dataset completo """, 
                                    html.A("aquí", href="https://docs.google.com/spreadsheets/d/1zY0iOwGfm5hIg7eYTm1EAQBamPN7mzLm-9U1PxjwiNg/edit?usp=sharing", target="_blank")
                                    , "."], className="text-white poppins"),                     
                            html.H6([html.H6('Entre el 1988 y el 2018, en la Provincia de Buenos Aires:', style={'line-height': '2'}, className="text-white"),
                                html.Ul(
                                    [
                                    html.Li([f"las explotaciones agropecuarias se redujeron a la mitad (de {VAR_CANTIDAD_EAPS_1988} a {VAR_CANTIDAD_EAPS_2018})"], style={'line-height': '1.5'}),
                                    html.Li([f"la superficie promedio de las EAP aumentó en un 78% (de {VAR_SUPERFICIE_1988} ha a {VAR_SUPERFICIE_2018} ha)"], style={'line-height': '1.5'}),
                                    html.Li([f"más de la mitad de la población rural fue expulsada de su residencia (de {VAR_RESIDENCIA_1988} personas a {VAR_RESIDENCIA_2018} personas)"], style={'line-height': '1.5'}),
                                    html.Li([f"hubo una caída de más del 70% del empleo rural (de {VAR_EMPLEO_1988} trabajadores a {VAR_EMPLEO_2018} trabajadores)" ], style={'line-height': '1.5'}),
                                    ])], className="text-white"),
                            html.A("V 1.0 (METODOLOGÍA & PRODUCTO)", href="#metodologia-censo")
                        ],
                        className="text-white mt-5"
                    )
                    , md=12),
                    dbc.Col(Filtros_censos, md=12),
                ], 
                class_name="mb-5"
            ),
            dbc.Row(
                dbc.Col(Solapas, md=12)
            ),
            dbc.Row(
                dbc.Col(IndicadoresCenso, md=12)
            ),
            dbc.Row(
                dbc.Col(MetodologiaCenso, md=12)
            )
        ],
        className="my-5 min-vh-100",
    ) 