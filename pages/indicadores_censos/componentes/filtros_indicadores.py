from dash import html, dcc
import dash_bootstrap_components as dbc

from data.base_indicadores import anio_censo, municipios

Filtros_censos = html.Div([
    dbc.Container(
        children=[
            dbc.Row([
                html.Div(className='col-3'),  # Columna vacía con clase de Bootstrap
                html.Div(className='col-3'), 
                         
                dbc.Col([
                    html.Label(htmlFor="select-municipios", title='Municipios'),
                    dcc.Dropdown(
                        id="select-municipios",
                        options=municipios,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un municipio..',
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
    id="filtros",
)