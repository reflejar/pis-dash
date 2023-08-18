from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from .concentracion_tierra import ConcentracionTierra
from .empleo_residencia import Empleo
from .modo_produccion import Produccion
from dash import Dash
from ..constantes import *



Solapas = dbc.Container([
    dbc.Tabs(id="tabs", active_tab='tab-1', children=[
        dbc.Tab(label='Concentración de tierras', tab_id='tab-1', label_style={"color": NEGRO , "font-weight": "bold", 'font-size': '20px', 'background-color':LILA,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='Modo de producción', tab_id='tab-2', label_style={"color":NEGRO , "font-weight": "bold", 'font-size': '20px', 'background-color':LIMA ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' , "text-align": "center" }, active_label_style={'border': '4px solid white'},className='nav-tabs-custom'),
        dbc.Tab(label='Empleo y residencia', tab_id='tab-3',label_style={"color":NEGRO , "font-weight": "bold",  'font-size': '20px', 'background-color':NARANJA ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' , "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
    ],style={'borderBottom': '0px'}),
    html.Div(id='tabs-content'),
  
])


@callback(Output('tabs-content', 'children'), Input('tabs', 'active_tab'))
def render_content(tab):
    return {
        'tab-1':ConcentracionTierra,
        'tab-2':Produccion,
        'tab-3':Empleo,
    }[tab]