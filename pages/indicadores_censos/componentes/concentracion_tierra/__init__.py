from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from .eaps_cantidad import EAPS_HA
from .eaps_segun_tamanio import Q_EAPs_tamanio


Concentracion_Tierra = html.Div([
            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H6('CONCENTRACIÓN DE LA TIERRA', style={'font-size': '25px'}, className="text-white"),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.Col([
                    html.H6('Cantidad de EAPs según año del censo', style={'font-size': '20px'}, className="text-white"),
                    html.Br(),
                    html.P("""Las explotaciones agropecuarias.. Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""", className="text-white"),
                    dbc.Row(EAPS_HA),
                    html.Br(),
                    dbc.Row(html.P(""" [Este texto se modificaría según el/los partidos de PBA seleccionados] Podemos observar cómo en los últimos 30 años, la Provincia de Buenos Aires perdió xxxx EAPS, representando una caída del xxxx del total de EAPS.""", className="text-white")),
                    ], md=5),
                dbc.Col(md=1),
                dbc.Col([
                    html.H6('Cantidad de EAPs según tamaño', style={'font-size': '20px'}, className="text-white"),
                    html.Br(),
                    html.P("""El tamaño de las explotaciones agropecuarias.. Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""", className="text-white"),
                    dbc.Row(Q_EAPs_tamanio),
                    html.Br(),
                    dbc.Row(html.P(""" [Este texto se modificaría según el/los partidos de PBA seleccionados] 
                    Si bien pudimos observar en el gráfico anterior que las EAPS pequeñas representaban una 
                    mayor cantidad de EAPS que las grandes, se puede apreciar que las EAPS grandes poseen el 
                    XX.XX de la superficie, es decir, poseen la mayor cantidad de tierras. Mientras que las EAPS pequeñas 
                    alcanzan a ocupar apenas el XX.XX de la superficie.""", className="text-white")),
                    ], md=5),                    
            ])
            
       ]), 
