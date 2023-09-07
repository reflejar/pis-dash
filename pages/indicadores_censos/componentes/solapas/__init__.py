from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from .concentracion_tierra import ConcentracionTierra
from .empleo_residencia import Empleo
from .modo_produccion import Produccion
from dash import Dash
from ..constantes import *



Solapas = html.Div([
    dbc.Tabs(id="tabs", active_tab='tab-1', children=[
        dbc.Tab(label='Concentración de tierras', tab_id='tab-1', label_style={'background-color':LILA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
        dbc.Tab(label='Modo de producción', tab_id='tab-2', label_style={'background-color':LIMA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
        dbc.Tab(label='Empleo y residencia', tab_id='tab-3',label_style={'background-color':NARANJA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
        ], 
        style={'borderBottom': '0px'}, 
        class_name="justify-content-center nav nav-pills nav-fill nav-justified"),
    html.Div(id='tabs-content'),
])



@callback(Output('tabs-content', 'children'), Input('tabs', 'active_tab'))
def render_content(tab):
    return {
        'tab-1':ConcentracionTierra,
        'tab-2':Produccion,
        'tab-3':Empleo,
    }[tab]