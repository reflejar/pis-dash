import dash_bootstrap_components as dbc
from pages.constantes import *


Solapas = dbc.Row(dbc.Col([
        dbc.Tabs(id="tabs-ranking", active_tab='escuelas', children=[
            dbc.Tab(label='ESCUELAS', tab_id='escuelas', label_style={'background-color':ROJO,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='TRANSPARENCIAS', tab_id='transparencia', label_style={'background-color':LILA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='AGUA', tab_id='agua', label_style={'background-color':VERDE_AGUA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='POBLACIONES', tab_id='poblaciones', label_style={'background-color':LIMA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='APIARIOS', tab_id='apiarios', label_style={'background-color':NARANJA,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
            dbc.Tab(label='AGROECOLOGÍA', tab_id='agroecologia', label_style={'background-color':CELESTE,  'border-radius': '40px', 'color': '#000', 'margin-top': "7px"},active_label_style={'border': '4px solid white'}),
        ], 
        style={'borderBottom': '0px'}, 
        class_name="justify-content-center nav nav-pills nav-fill nav-justified"),
]))
