from dash import html, dcc
import dash_bootstrap_components as dbc

from pages.indicadores_censos.data_censo.base_indicadores import anio_censo, partidos

Filtros_censos = html.Div([
    dbc.Container(
        children=[
            dbc.Row([
                html.Div(className='col-3'),  # Columna vacía con clase de Bootstrap
                html.Div(className='col-3'), 
                         
                dbc.Col([
                    html.Label(htmlFor="select-partidos", title='partidos'),
                    dcc.Dropdown(
                        id="select-partido",
                        options=partidos,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un partido..',
                        value=[""],
                        clearable=True,
                        
                        )], 
                        className='col-md-3'),

                dbc.Col([
                        html.Label(htmlFor="select-periodo", title='Año del censo'),
                        dcc.Dropdown(
                            id="select-periodo",
                            options=anio_censo,
                            multi=True,
                            searchable=True,
                            placeholder = 'Selecciona el año del censo..',
                            value=[""],
                            clearable=True
                        )],
                        className='col-md-3'),
                ]),
        ]),
    ],
    id="filtros-censo",
)