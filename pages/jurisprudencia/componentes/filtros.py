from dash import html, dcc
import dash_bootstrap_components as dbc

from ..data import DATA

Filtros = dbc.Row([      
                dbc.Col(
                    html.H5("Filtrar por", className="text-white fw-bold"),
                    xs=12,
                    class_name="mt-3"
                ),    
                dbc.Col([
                    dcc.Dropdown(
                        id="select-provincia",
                        options=['Todos los distritos'] + DATA['filtros']['provincia'],
                        searchable = True,
                        placeholder = 'Distrito',
                        className="mt-1",
                        )
                    ], 
                    md=12, lg=4
                ),
                dbc.Col([
                    dcc.Dropdown(
                        id="select-voces-tematicas",
                        options=['Todas las voces temáticas'] + DATA['filtros']['voces-tematicas'],
                        searchable = True,
                        placeholder = 'Voces temáticas',
                        className="mt-1",
                        optionHeight=50,
                        )
                    ], 
                    md=12, lg=4
                ),                
                dbc.Col([
                    dcc.Dropdown(
                        id="select-tipo-fallo",
                        options=['Todos los tipos de fallos'] + DATA['filtros']['tipo-fallo'],
                        searchable = True,
                        placeholder = 'Tipo de fallo',
                        className="mt-1",
                        optionHeight=50,
                        )
                    ], 
                    md=12, lg=4
                ),
            ])