from dash import html, dcc

import dash_bootstrap_components as dbc
import dash_daq as daq

from ._data import MUNICIPIOS

Filtros = html.Div(
    [
        html.H4("MAPA NORMATIVO", className="text-white"),
        html.P([
            "Seleccioná el municipio de tu interés.",
            html.Br(),
            "Activá y desactivá las capas de los diferentes elementos."
        ]),
        dbc.Row([dbc.Col([
                    html.Label(htmlFor="select-municipio", title='Municipio'),
                    dcc.Dropdown(
                        id="select-municipio",
                        options=MUNICIPIOS,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un municipio..',
                        value=["Mar Chiquita"],
                        clearable=True,
                        style={'background-color': 'black'}
                    )        
            ], md=12), 
                         
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_cursos", labelPosition="bottom",color="#134dab"), md=3),
            dbc.Col(html.Span("Cursos de agua"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_cuerpos", labelPosition="bottom",color="#134dab"), md=3),
            dbc.Col(html.Span("Cuerpos de agua"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_localidades", labelPosition="bottom",color="purple"), md=3),
            dbc.Col(html.Span("Localidades"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_reservas", labelPosition="bottom",color="#06660b"), md=3),
            dbc.Col(html.Span("Reservas"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_escuelas", labelPosition="bottom",color="#cfc817"), md=3),
            dbc.Col(html.Span("Escuelas"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_excl", labelPosition="bottom",color="#8c0d22"), md=3),
            dbc.Col(html.Span("Zonas de Exclusión"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_amort", labelPosition="bottom",color="#8c0d22"), md=3),
            dbc.Col(html.Span("Zonas de Amortiguamiento"), md=9)
        ], className="mb-2"),
        
        
    ],
    id="filtros",
    className=" text-white mt-5"
)