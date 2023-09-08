import dash
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import dcc, html,Input, Output, callback
import geopandas as gpd
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from shapely.geometry import box, Point, Polygon
from dash_extensions.javascript import arrow_function, assign
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.ranking_ambiental.bases_mapa import bsas,VAR_PUNTAJE,  classes

# Establecer el renderizador predeterminado para Plotly.
pio.renderers.default = 'browser'

# Agregar informacion de etiquetas
bsas["tooltip"] = bsas["nam"]

#Transformar a geobuf
bsas_geojson = json.loads(bsas.to_json(na="keep"))
geobuf = dlx.geojson_to_geobuf(bsas_geojson)

# Definir colores para las clases.
colorscale = ['#F5BBCB', '#F2A4B6', '#EF8DA1', '#ED769C', '#EB5F87', '#E94872', '#E7315D', '#E51A48']
style = dict(weight=2, opacity=1, color='white', dashArray='3', fillOpacity=0.7)

# Crear colorbar.
ctg = ["{}+".format(cls, classes[i + 1]) for i, cls in enumerate(classes[:-1])] + ["{}+".format(classes[-1])]

# # Barra de colores categóricos personalizada
# colorbar = dlx.categorical_colorbar(
#     categories=ctg,
#     colorscale=colorscale,
#     width=200,  # Ancho personalizado
#     height=20,  # Altura personalizada
#     position="bottomleft",  # Posición
# )

# Lógica de representación del GeoJSON.
style_handle =  assign("""function(feature, context){
    const {classes, colorscale, style, colorProp} = context.props.hideout;
    const value = feature.properties[colorProp];
    if (value === null || isNaN(value)) {
        // Asigna color gris para observaciones sin datos
        style.fillColor = 'rgb(128, 128, 128)';
        style.weight = 1;
        style.dashArray = false;
    } else {
        for (let i = 0; i < classes.length; ++i) {
            if (value > classes[i]) {
                style.fillColor = colorscale[i];
                style.weight = 1;
                style.dashArray = false;
            }
        }
    }
    return style;
}""")

# Crear la figura rectangular con degradé de colores
color_bar = html.Div(
    style={
        'width': '100%',
        'height': '25px', 
        'background': f'linear-gradient(to right, {", ".join(colorscale)})'
    }
)
color_bar_gris = html.Div(
    style={
        'width': '40px',
        'height': '25px', 
        'background': 'grey'
    }
)

colorscale_reference = html.Div(
    id='colorscale-reference',
    children=[dbc.Col([
                dbc.Row([html.Div("PROTECCIÓN", style={'text-align': 'center','font-size': '12px','color': 'black'})]),
                dbc.Row([dbc.Col([html.Div("MENOR", style={'text-align':'right','color': 'black'})], md=3),
                       dbc.Col([color_bar], md=5),
                       dbc.Col([html.Div("MAYOR", style={'text-align': 'left','color': 'black'})], md=3),
                    ]),  
            ]), 
                html.Br(), 
                dbc.Row([ 
                     dbc.Col([html.Br()], md=3),   
                    dbc.Col([color_bar_gris], md=1),
                    dbc.Col([html.Div("SIN ORDENANZA", style={'text-align': 'right','color': 'black'})], md=3) 
            ]),
        ],
                        
    style={
        'font-size': '12px',
    }
)


Mapa =dl.Map(
                            id="mapa",
                            zoom=15,
                            dragging=False,
                            keyboard=False,
                            zoomControl=False,
                            scrollWheelZoom=False,
                            doubleClickZoom=False,
                            children=[
                                
                                dl.GeoJSON(
                                    data=geobuf,
                                    format='geobuf',
                                    zoomToBounds=True,
                                    zoomToBoundsOnClick=False,
                                    options=dict(style=style_handle),
                                    hoverStyle=arrow_function(dict(weight=5, dashArray='')),
                                    hideout=dict(colorscale=colorscale, classes=classes, style=style, colorProp=VAR_PUNTAJE)
                                ),
                               
                            ],
                            className="min-vh-50 bg-white"
                        )







titulo_del_mapa_1 = html.H6(
    "PROVINCIA DE BUENOS AIRES",
    style={
        'font-weight': 'bold',
        'color': 'black',
        'white-space': 'pre-line',  # Forzar el salto de línea
    },
    className="d-flex justify-content-center align-items-center"
)
titulo_del_mapa_2 = html.H6(
    "CONURBANO",
    style={
        'font-weight': 'bold',  # Hacer que el texto sea negrita
        'color': 'black',
    },
    className="d-flex justify-content-center align-items-center"
)

mapa_layout = html.Div(
    id="mapa-container",
    children=[
        dbc.Row([
            dbc.Row([dbc.Col([titulo_del_mapa_1], md=7), dbc.Col([titulo_del_mapa_2], md=2)]),
            dbc.Row([dbc.Col([Mapa], md=12)]),  
            dbc.Row([dbc.Col([html.Div()], md=3),dbc.Col([colorscale_reference], md=6),dbc.Col([html.Div()], md=3) ]),
            ])  
    ],
)

# Crea la tarjeta centrada
mapa_card = dbc.Card(
    [
        dbc.CardBody(mapa_layout),
    ],
    color="light", 
    class_name="shadow",
    outline=True,
    id="censo-empleo"
)


