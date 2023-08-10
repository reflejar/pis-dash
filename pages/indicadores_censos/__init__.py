from dash import html
import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros_censos
from .componentes.solapas import SolapasIndicadores


layout = html.Div([
        dbc.Row([
                dbc.Col(dbc.Container([      
                        html.H4("CENSO NACIONAL AGROPECUARIO", className="text-white"),
                        html.P(["Aquí podrás ver diferentes datos de los censos agropecuarios"]),
                        html.P(["Recorre las diferentes visualizaciones para conocerlas en mas detalle."]),
                        html.P(["Podes descargar el data set completo aqui"]),
                    ],
                    className="text-white mt-5"
                )
                , md=12),
                dbc.Col(Filtros_censos, md=12),
            ], 
            class_name="mb-5"
        ),
        dbc.Row(
            dbc.Col(SolapasIndicadores, md=12)
        ),
        ],
        className="my-5 mx-5 min-vh-100",
    ) 