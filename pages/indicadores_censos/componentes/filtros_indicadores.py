from dash import html, dcc
import dash_bootstrap_components as dbc

from pages.indicadores_censos.data_censo.base_indicadores import partidos

Filtros_censos = html.Div([
    dbc.Container(
        children=[
            dbc.Row([                        
                dbc.Col([
                    html.Label(htmlFor="select-partidos", title='partidos'),
                    dcc.Dropdown(
                        id="select-partido",
                        options=partidos,
                        multi=False,
                        searchable = True,
                        placeholder = 'Provincia de Buenos Aires',
                        value='Provincia de Buenos Aires',
                        clearable=False,
                        
                        
                        )], 
                        className='col-md-3'),
                ]),
        ]),
    ],
    id="filtros-censo",
)