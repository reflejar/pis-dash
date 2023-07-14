from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from .eaps_cantidad import EAPS_CANTIDAD
from .eaps_cantidad_segun_tamanio import Q_EAPs_tamanio
from .eaps_superficie_ha import EAPs_SUPERFICIE
from .eaps_superficie_segun_tamanio import Superficie_EAPs_tamanio

color_concentracion_tierra_1 = '#89370B'

Concentracion_Tierra = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('Concentración de la tierra', style={'font-size': '25px', 'color': color_concentracion_tierra_1}),
                html.P("""Siguiendo al INDEC, se utilizará como unidad de referencia a las explotaciones agropecuarias (EAP). Para entenderlo más fácilmente, 
                    podemos pensar a las EAPs como los "campos" de Argentina. Se tomará como EAPS grandes a aquellas 
                    que posean más de 500 hectáreas, mientras que las EAPs pequeñas serán las que tengan menos de 500 hectáreas.""", className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                ]),
                #html.H6('Cantidad de EAPs según año del censo', style={'font-size': '20px'}, className="text-white"),
                html.Br(),
            dbc.Row([
                    dbc.Col([
                    dbc.Row(EAPS_CANTIDAD),
                        html.Br(),
                        html.Br(),
                        ], md=4),                   
                    dbc.Col([
                        dbc.Row(EAPs_SUPERFICIE),
                        html.Br(),
                        html.Br(),
                        ], md=4),
                    dbc.Col([
                    dbc.Row(Q_EAPs_tamanio),
                        html.Br(),
                        html.Br(),
                        ], md=4)             
                ]),
                dbc.Row([
                    dbc.Col([
                    dbc.Row(Superficie_EAPs_tamanio),
                        html.Br(),
                        html.Br(),
                        ], md=4),                              
                ])])
                # html.Br(),
                # dbc.Col([
                #     dbc.Row(EAPs_SUPERFICIE),
                #     html.Br(),
                #     html.Br(),
                #     ], md=5),
                # dbc.Col([
                #     html.Br(),
                #     html.Br(),    
                #     dbc.Row(EAPs_superficie_texto)],
                #         md=5),
                #         ]),
                # #html.H6('Partipación de EAPs pequeñas y grandes', style={'font-size': '20px'}, className="text-white"),
                # html.Br(),
                # dbc.Row([
                #     dbc.Col([
                #     dbc.Row(Q_EAPs_tamanio),
                #     html.Br(),
                #     html.Br(),
                #      ], md=5),
                #     dbc.Col([
                #     html.Br(),
                #     html.Br(),    
                #     dbc.Row(EAPs_tamanio_texto)],md=5),                       
                # ]),
                # html.Div([modal_tierra]),
            #])