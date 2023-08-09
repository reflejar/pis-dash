from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from .concentracion_tierra import Concentracion_Tierra
from .empleo_residencia import Empleo
from .modo_produccion import Produccion
from dash import Dash

color_concentracion_tierra = 'rgb(150, 79, 71)'
color_empleo_residencia = 'rgb(225, 134, 95)'
color_modo_produccion = 'rgb(77, 130, 133)'
color_resumen = 'rgb(170, 166, 163)'


SolapasIndicadores = html.Div([
    dbc.Tabs(id="tabs", active_tab='tab-1', children=[
        dbc.Tab(label='CONCENTRACIÓN DE TIERRAS', tab_id='tab-1', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_concentracion_tierra,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '400px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='MODO DE PRODUCCIÓN', tab_id='tab-2', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_modo_produccion  ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' ,'width': '400px', "text-align": "center" }, active_label_style={'border': '4px solid white'},className='nav-tabs-custom'),
        dbc.Tab(label='EMPLEO Y RESIDENCIA', tab_id='tab-3',label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_empleo_residencia ,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px' ,'width': '400px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
    ],style={'borderBottom': '0px'}),
    html.Div(id='tabs-content'),
  
])


@callback(Output('tabs-content', 'children'), Input('tabs', 'active_tab'))
def render_content(tab):
    return {
        'tab-1':Concentracion_Tierra,
        'tab-2':Produccion,
        'tab-3':Empleo,
    }[tab]