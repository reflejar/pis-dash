import dash
from dash import dash_table
import pandas as pd
from pages.ranking_ambiental.bases_mapa import escuelas
import dash_bootstrap_components as dbc 
from dash import html, dcc
import os as o

color_columnas = '#F2A4B6'

escuelas["Ordenanza"] = escuelas["Ordenanza"].apply(lambda x: "Ord. " + str(x) if x != "Sin ordenanzas" else x)


x = escuelas["Link"]
del escuelas["Link"]



y = escuelas.copy()



tabla_escuelas =  dbc.Container([
    dash_table.DataTable(
        data=y.to_dict('records'),
        columns=[{"name": i, "id": i} for i in y.columns],
        style_as_list_view=True,
        style_table={
            'height': '500px',            # Altura de la tabla
            'overflowX': 'scroll',       # Ocultar scroll horizontal
            'overflowY': 'scroll',       # Mostrar scroll vertical
            'width': '100%',
            'borderCollapse': 'separate', # Separar filas
            'borderSpacing': '0 10px',    # Espacio entre filas
        },
        style_cell={'textAlign': 'center',
                    'whiteSpace': 'normal',
                    'width': '10%',
                    'fontFamily': 'Arial'},  # Cambiar la fuente a Arial
        style_header={
            'fontWeight': 'normal',
            'whiteSpace': 'pre-wrap',
            'backgroundColor': color_columnas,
            'color': 'rgb(76,30,39)',
            'textAlign':'center',
        },
        style_header_conditional=[
            {'if': {'column_id': c}, 'fontWeight': 'bold'}
            for c in y.columns[:2]  # Primeros dos encabezados en negritas
        ],
        style_cell_conditional=[
            {
                'if': {'column_id': col},
                'textAlign': 'center',
                'height': 'auto',  # Ajuste de altura dinámica
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'fontFamily': 'Arial',  # Cambiar la fuente a Arial
            }  for col in y.columns 
        ],
        style_data_conditional=[
            {
                'if': {'column_id': col},
                'whiteSpace': 'normal',
                'height': 'auto',
                'fontFamily': 'Arial',  # Cambiar la fuente a Arial
            }
            for col in y.columns 
        ],
        fixed_columns={'headers': True},
    )
])