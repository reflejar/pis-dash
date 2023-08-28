import dash
import dash_table
from dash import html
import pandas as pd
from pages.ranking_ambiental.bases_mapa import escuelas
import dash_bootstrap_components as dbc

x=escuelas["Link"]
del(escuelas["Link"])

tabla_escuelas = dbc.Container([
    dbc.Card(
        dbc.CardBody([
                    dash_table.DataTable(
                        data=escuelas.to_dict('records'),
                        columns=[{"name": i, "id": i} for i in escuelas.columns],
                        style_table={'height': 'auto', 'overflowX': 'auto','overflowY': 'auto','width': '100%'},  # Ajustar el ancho de la tabla
                        style_cell={'textAlign': 'center'},
                        style_header={'fontWeight': 'bold', 'whiteSpace': 'normal'},  # Estilo del encabezado
                        fixed_columns={'headers': True},   # Centrar el contenido de las celdas
                    )
        ]),
    ),
])