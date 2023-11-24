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
                        id="select-voces-tematicas",
                        options=DATA['filtros']['voces-tematicas'],
                        searchable = True,
                        placeholder = 'Voces temáticas',
                        className="mt-1"
                        )
                    ], 
                    md=6, lg=3, xs=12
                ),
                dbc.Col([
                    dcc.Dropdown(
                        id="select-provincia",
                        options=DATA['filtros']['provincia'],
                        searchable = True,
                        placeholder = 'Provincia',
                        className="mt-1"
                        )
                    ], 
                    md=6, lg=3, xs=12
                ),
                dbc.Col([
                    dcc.Dropdown(
                        id="select-tipo-fallo",
                        options=DATA['filtros']['tipo-fallo'],
                        searchable = True,
                        placeholder = 'Tipo de fallo',
                        className="mt-1"
                        )
                    ], 
                    md=6, lg=3, xs=12
                ),
                dbc.Col([
                    dcc.Dropdown(
                        id="select-organismo",
                        options=DATA['filtros']['organismo'],
                        searchable = True,
                        placeholder = 'Organismo',
                        className="mt-1"
                        )
                    ], 
                    md=6, lg=3, xs=12
                ),
            ])