from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from dash import Dash
from .resumen import Resumen

color_transparencia = '#B2794B'
color_escuelas = 'rgb(240, 140, 104)'
color_agua = 'rgb(129, 189, 181)'
color_poblaciones = '#C3A4E7'
color_resumen = 'rgb(170, 166, 163)'


SolapasRanking = html.Div([
    dbc.Tabs(id="tabs-ranking", active_tab='tab-A', children=[
        dbc.Tab(label='RESUMEN', tab_id='tab-A', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_resumen,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '225px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='TRANSPARENCIA', tab_id='tab-B', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_transparencia,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '225px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='ESCUELAS', tab_id='tab-C', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_escuelas,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '225px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='AGUA', tab_id='tab-D', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_agua,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '225px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
        dbc.Tab(label='POBLACIONES', tab_id='tab-E', label_style={"color":'#FFFFFF' , 'font-size': '20px', 'background-color':color_poblaciones,  'border-top-left-radius': '40px','border-bottom-left-radius': '40px','border-bottom-right-radius': '40px','border-top-right-radius': '40px', 'width': '225px', "text-align": "center"},active_label_style={'border': '4px solid white'}, className='nav-tabs-custom'),
    ],style={'borderBottom': '0px'}),
    html.Div(id='tabs-content-ranking'),
  
])


@callback(Output('tabs-content-ranking', 'children'), Input('tabs-ranking', 'active_tab'))
def render_content(tab):
   if tab == 'tab-A':
       return Resumen
#    
#    elif tab == 'tab-2':
#        return Produccion
#    
#    elif tab == 'tab-3':
#        return Empleo