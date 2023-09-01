from dash import html, dcc

import dash_bootstrap_components as dbc
import dash_daq as daq

from .colores import *

from ..data import MUNICIPIOS

Filtros = html.Div(
    [
        html.H4("MAPA NORMATIVO", className="text-white pt-3"),
        html.P([
            "Seleccioná el municipio de tu interés.",
            html.Br(),
            "Activá y desactivá las capas de los diferentes elementos. De momento está disponible Mar Chiquita."
        ]),
        dbc.Row([dbc.Col([
                    html.Label(htmlFor="select-municipio", title='Municipio'),
                    dcc.Dropdown(
                        id="select-municipio",
                        options=MUNICIPIOS,
                        multi=False,
                        searchable = False,
                        placeholder = 'Selecciona un municipio.',
                        value="Mar Chiquita",
                        clearable=False,
                    )        
            ], md=12), 
                         
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_cursos", labelPosition="bottom",color=CURSOS_CUERPOS_AGUA), md=3),
            dbc.Col(html.Span("Cursos de agua"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_cuerpos", labelPosition="bottom",color=CURSOS_CUERPOS_AGUA), md=3),
            dbc.Col(html.Span("Cuerpos de agua"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_localidades", labelPosition="bottom",color=LOCALIDADES), md=3),
            dbc.Col(html.Span("Localidades"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_reservas", labelPosition="bottom",color=RESERVAS), md=3),
            dbc.Col(html.Span("Reservas"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_escuelas", labelPosition="bottom",color=ESCUELAS), md=3),
            dbc.Col(html.Span("Escuelas"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_excl", labelPosition="bottom",color=ZONA_EXCLUSIÓN), md=3),
            dbc.Col(html.Span("Zonas de Exclusión"), md=9)
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_amort", labelPosition="bottom",color=ZONA_AMORTIGUAMIENTO), md=3),
            dbc.Col(html.Span("Zonas de Amortiguamiento"), md=9)
        ], className="mb-2"),
        
        
    ],
    id="filtros",
    className="mt-5"
)