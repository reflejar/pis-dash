from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from .concentracion_tierra import Concentracion_Tierra
from .empleo_residencia import Empleo
from dash import Dash

color_concentracion_tierra = '#89370B'
color_empleo_residencia = 'rgb(225, 134, 95)'
color_cultivos = '#316397'
color_modo_produccion = '#006101'
color_resumen = '#4C4C4C'



SolapasIndicadores = html.Div([
    dbc.Tabs(id="tabs", active_tab='tab-1', children=[
        dbc.Tab(label='CONCENTRACIÓN DE TIERRAS', tab_id='tab-1', label_style={"color":'#FFFFFF' , 'font-size': '18px', 'background-color':color_concentracion_tierra,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '290px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='EMPLEO Y RESIDENCIA', tab_id='tab-2',label_style={"color":'#FFFFFF' , 'font-size': '18px', 'background-color':color_empleo_residencia ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' ,'width': '290px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='MODO DE PRODUCCIÓN', tab_id='tab-3', label_style={"color":'#FFFFFF' , 'font-size': '18px', 'background-color':color_cultivos  ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' ,'width': '290px', "text-align": "center" }, active_label_style={'border': '4px solid white'},className='nav-tabs-custom'),
        dbc.Tab(label='RESUMEN', tab_id='tab-4', label_style={"color":'#FFFFFF' , 'font-size': '18px', 'background-color':color_resumen ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' , 'width': '290px', "text-align": "center" }, active_label_style={'border': '4px solid white'},className='nav-tabs-custom'),
    ],style={'borderBottom': '0px'}),
    html.Div(id='tabs-content'),
  
])


@callback(Output('tabs-content', 'children'), Input('tabs', 'active_tab'))
def render_content(tab):
    if tab == 'tab-1':
        return Concentracion_Tierra
    
    elif tab == 'tab-2':
        return Empleo