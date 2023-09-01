from dash import html
import dash_bootstrap_components as dbc
from .componentes.texto_inicial_ranking import TextoRanking_1
from .componentes.solapa_ranking import SolapasRanking
from .componentes.solapa_acordeon import AcordeonRanking

layout = html.Div([
                dbc.Row([
                    dbc.Col(TextoRanking_1,  md=12),
                ]),
                html.Br(),
                html.Br(),
                dbc.Container(
                children=[
                dbc.Row([
                    dbc.Col(SolapasRanking, md=12)
                    ]),
                ]),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.Container(
                children=[
                dbc.Row([
                    dbc.Col(AcordeonRanking, md=12)
                    ]),
                ]),
                
        ],className="my-5 mx-5 min-vh-100"
    ) 