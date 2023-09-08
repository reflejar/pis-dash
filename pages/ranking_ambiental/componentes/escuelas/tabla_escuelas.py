import dash
from dash import dash_table
import pandas as pd
from pages.ranking_ambiental.bases_mapa import escuelas
import dash_bootstrap_components as dbc 
from dash import html, dcc, callback, Input, Output
import os as o

color_columnas = '#F2A4B6'

escuelas["Ordenanza"] = escuelas["Ordenanza"].apply(lambda x: "Ord. " + str(x) if x != "Sin ordenanzas" else "Sin ordenanza")


# Reemplazar valores nulos en columnas de tipo objeto con 'NO'
columna_especifica = "Obligatoriedad de notificación"
escuelas[columna_especifica] = escuelas[columna_especifica].fillna('NO')

# Reemplazar valores nulos en la columna específica con '-'
columna_especifica = 'Puntaje - Escuelas rurales'
escuelas[columna_especifica] = escuelas[columna_especifica].fillna('-')

# Reemplazar valores nulos en columnas numéricas con 0
numeric_columns = escuelas.select_dtypes(include=['number']).columns
escuelas[numeric_columns] = escuelas[numeric_columns].fillna(0)

x = escuelas["Link"]
del escuelas["Link"]



y = escuelas.copy()



tabla_escuelas =  dbc.Container([
    dash_table.DataTable(
        data=y.to_dict('records'),
        columns=[{"name": i, "id": i} for i in y.columns],
        style_as_list_view=True,
        style_table={
            'height': '400px',            # Altura de la tabla
            'overflowX': 'scroll',       # Ocultar scroll horizontal
            'overflowY': 'scroll',       # Mostrar scroll vertical
            'width': '100%',
            'borderCollapse': 'separate', # Separar filas
            'borderSpacing': '0 10px',    # Espacio entre filas
        },
        style_cell={'whiteSpace': 'pre',
                    'fontFamily': 'Arial',
                    'textAlign':'left',
                    'minWidth': '150px', 
                    'width': '150px', 
                    'maxWidth': '150px'
                    },  # Cambiar la fuente a Arial
        style_header={
            'fontWeight': 'normal',
            'whiteSpace': 'normal',
            'backgroundColor': color_columnas,
            'color': 'rgb(76,30,39)',
            'textAlign':'center',
        },
        style_header_conditional=[
            {'if': {'column_id': c}, 'fontWeight': 'bold'}
            for c in y.columns[:2]  # Primeros dos encabezados en negritas
        ],
        
        id='ordenador_de_filas',
        sort_action='native',
    )
])

