from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from dash import Dash
from ..escuelas import Escuelas

color_transparencia = '#FF865F'
color_escuelas = '#EF7286'
color_agua = '#6FBFB5'
color_poblaciones = '#D8D87C'
color_apiarios = '#C3A4E7'
color_agroecologia= '#9AD5FF'

SolapasRanking = html.Div([
        dbc.Tabs(id="tabs-ranking", active_tab='escuelas', children=[
            dbc.Tab(label='ESCUELAS', tab_id='escuelas', label_style={'background-color':color_escuelas,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='TRANSPARENCIAS', tab_id='transparencia', label_style={'background-color':color_transparencia,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='AGUA', tab_id='agua', label_style={'background-color':color_agua,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='POBLACIONES', tab_id='poblaciones', label_style={'background-color':color_poblaciones,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='APIARIOS', tab_id='apiarios', label_style={'background-color':color_apiarios,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='AGROECOLOGÍA', tab_id='agroecologia', label_style={'background-color':color_agroecologia,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
        ], 
        style={'borderBottom': '0px'}, 
        class_name="justify-content-center nav nav-pills nav-fill nav-justified"),
    html.Div(id='tabs-content-ranking'),
])





@callback(
        [
        Output('tabs-content-ranking','children'), 
        Output('accordion-tabla','value')
        ],
        Input('tabs-ranking','active_tab')
        )
def render_content(tab):
   
    MapaEscuelas= Escuelas

    return {
        'escuelas':MapaEscuelas,
        'transparencia':MapaEscuelas,
        'agua':MapaEscuelas,
        'poblaciones':MapaEscuelas,
        'apiarios':MapaEscuelas,
        'agroecologia':MapaEscuelas,
        }[tab], tab