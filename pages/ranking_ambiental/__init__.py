from dash import html
import dash_bootstrap_components as dbc
from .componentes.texto_inicial_ranking import TextoRanking
from .componentes.solapa_ranking import SolapasRanking

layout = html.Div([
        dbc.Row([
            dbc.Col(TextoRanking,  md=12),
        ]),
        html.Br(),
        html.Br(),
        dbc.Container(
        children=[
        dbc.Row([
            dbc.Col(SolapasRanking, md=12)
            # dbc.Col("", md=1),            
            # dbc.Col(Q_EAPs_tamanio, md=5),                                      
                            ]),
        # dbc.Row(dbc.Col(EAPS_HA, md=6),)
                            
                            ]),
        ],
        className="my-5 mx-5 min-vh-100",
    ) 