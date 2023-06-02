from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from .concentracion_tierra import Concentracion_Tierra
from .empleo_residencia import Empleo

color_concentracion_tierra = '#89370B'
color_empleo_residencia = '#EF7418'
color_cultivos = '#316397'
color_modo_produccion = '#006101'
color_resumen = '#4C4C4C'


SolapasIndicadores = html.Div([
    dbc.Tabs(id="tabs", active_tab='tab-1', children=[
        dbc.Tab(label='Concentración de tierras', tab_id='tab-1', label_style={"color":'#FFFFFF' , 'font-size': '22px', 'background-color':color_concentracion_tierra ,'border-top-left-radius': '0px','border-top-right-radius': '0px'}),
        dbc.Tab(label='Empleo y residencia', tab_id='tab-2',label_style={"color":'#FFFFFF' , 'font-size': '22px', 'background-color':color_empleo_residencia ,'border-top-left-radius': '0px','border-top-right-radius': '0px'}),
        dbc.Tab(label='Cultivos', tab_id='tab-3', label_style={"color":'#FFFFFF' , 'font-size': '22px', 'background-color':color_cultivos ,'border-top-left-radius': '0px','border-top-right-radius': '0px'}),
        dbc.Tab(label='Modo de producción', tab_id='tab-4', label_style={"color":'#FFFFFF' , 'font-size': '22px', 'background-color':color_modo_produccion ,'border-top-left-radius': '0px','border-top-right-radius': '0px'}),
        dbc.Tab(label='Resumen', tab_id='tab-5', label_style={"color":'#FFFFFF' , 'font-size': '22px', 'background-color':color_resumen ,'border-top-left-radius': '0px','border-top-right-radius': '0px'}),
    ]),
    html.Div(id='tabs-content')
])

@callback(Output('tabs-content', 'children'), Input('tabs', 'active_tab'))
def render_content(tab):
    if tab == 'tab-1':
        return Concentracion_Tierra
    
    elif tab == 'tab-2':
        return Empleo