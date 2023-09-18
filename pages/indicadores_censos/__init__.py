from dash import html
import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros_censos
from .componentes.solapas import Solapas
from .componentes.solapas.resumen_general import PERDIDA_EMPLEO_X_MES, PERDIDA_EAPS_X_MES, PERDIDA_RESIDENCIA_X_MES
from .componentes.metodologia import MetodologiaCenso, IndicadoresCenso


layout = html.Div([
        dbc.Row([
                dbc.Col(dbc.Container([      
                        html.H4(html.Strong('Censo Nacional Agropecuario'), className="text-white pt-3 space-grotesk"),
                        html.Br(),
                        html.H6(["""Visualizaciones y análisis de los principales indicadores de los últimos tres censos agropecuarios sistematizados por municipio. 
                                Información histórica con perspectiva local. Podés descargar el dataset completo """, 
                                html.A("aquí", href="https://docs.google.com/spreadsheets/d/1zY0iOwGfm5hIg7eYTm1EAQBamPN7mzLm-9U1PxjwiNg/edit?usp=sharing", target="_blank")
                                , "."], className="text-white poppins"),                     
                        html.H6([html.H6('Entre el 1988 y el 2018, en la Provincia de Buenos Aires:', style={'line-height': '2'}, className="text-white"),
                            html.Ul(
                                [
                                html.Li([html.Strong(f"{PERDIDA_EAPS_X_MES}"), " EAP fueron cerradas" ], style={'line-height': '1.5'}),
                                html.Li([html.Strong(f"{PERDIDA_RESIDENCIA_X_MES}"), " personas fueron expulsadas de su residencia" ], style={'line-height': '1.5'}),
                                html.Li([html.Strong(f"{PERDIDA_EMPLEO_X_MES}"), " personas perdieron su puesto de trabajo permanente" ], style={'line-height': '1.5'}),
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
        dbc.Container(
            dbc.Row(
                dbc.Col(Solapas, md=12)
            )),
        dbc.Container(
            dbc.Row(
                dbc.Col(IndicadoresCenso, md=12)
            )),
        dbc.Container(
            dbc.Row(
                dbc.Col(MetodologiaCenso, md=12)
            ))
        ],
        className="my-5 mx-5 min-vh-100",
    ) 