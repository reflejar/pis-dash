import dash
from dash import dash_table
import pandas as pd
from ...data import escuelas
import dash_bootstrap_components as dbc 
from dash import html, dcc, callback, Input, Output
import os as o

color_columnas = '#F2A4B6'



tabla_escuelas = dash_table.DataTable()

# tabla_escuelas =  dash_table.DataTable(
#         data=y.to_dict('records'),
#         columns=[{"name": i, "id": i} for i in y.columns],
#         style_as_list_view=True,
#         style_table={
#             'height': '400px',            # Altura de la tabla
#             'overflowX': 'scroll',       # Ocultar scroll horizontal
#             'overflowY': 'scroll',       # Mostrar scroll vertical
#             'width': '100%',
#             'borderCollapse': 'separate', # Separar filas
#             'borderSpacing': '0 10px',    # Espacio entre filas
#         },
#         style_cell={'whiteSpace': 'pre',
#                     'fontFamily': 'Arial',
#                     'textAlign':'center',
#                     'minWidth': '150px', 
#                     'width': '150px', 
#                     'maxWidth': '300px'
#                     },  # Cambiar la fuente a Arial
#         style_header={
#             'fontWeight': 'normal',
#             'whiteSpace': 'normal',
#             'backgroundColor': color_columnas,
#             'color': 'rgb(76,30,39)',
#             'textAlign':'center',
#         },
#         style_header_conditional=[
#             {'if': {'column_id': c}, 'fontWeight': 'bold'}
#             for c in y.columns[:3]  # Primeros dos encabezados en negritas
#         ],
#         style_cell_conditional=[
#             {'if': {'column_id': c},  'textAlign':'left'}
#             for c in y.columns[:3]  # Primeros dos encabezados en negritas
#         ],
        
        
#         id='ordenador_de_filas',
#         sort_action='native',
#     )

