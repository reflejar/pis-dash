from dash import html, dcc

import dash_bootstrap_components as dbc
import dash_daq as daq

from .colores import *

from ..data import MUNICIPIOS

Filtros = html.Div(
    [
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
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_cursos", labelPosition="bottom",color=CURSOS_CUERPOS_AGUA), xs=3),
            dbc.Col(html.Span("Cursos de agua"), xs=9)
        ], className="text-white mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_cuerpos", labelPosition="bottom",color=CURSOS_CUERPOS_AGUA), xs=3),
            dbc.Col(html.Span("Cuerpos de agua"), xs=9)
        ], className="text-white mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_localidades", labelPosition="bottom",color=LOCALIDADES), xs=3),
            dbc.Col(html.Span("Localidades"), xs=9)
        ], className="text-white mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_reservas", labelPosition="bottom",color=RESERVAS), xs=3),
            dbc.Col(html.Span("Reservas"), xs=9)
        ], className="text-white mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_escuelas", labelPosition="bottom",color=ESCUELAS), xs=3),
            dbc.Col(html.Span("Escuelas Rurales"), xs=9)
        ], className="text-white mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_excl", labelPosition="bottom",color=ZONA_EXCLUSIÓN), xs=3),
            dbc.Col(html.Span("Zonas de Exclusión"), xs=9)
        ], className="text-white mb-2"),
        dbc.Row([
            dbc.Col(daq.BooleanSwitch(on=True, id="toggle_amort", labelPosition="bottom",color=ZONA_AMORTIGUAMIENTO), xs=3),
            dbc.Col(html.Span("Zonas de Amortiguamiento"), xs=9)
        ], className="text-white mb-2"),
        
    ],
    id="filtros",
)