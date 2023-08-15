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

# Establecer el renderizador predeterminado para Plotly.
pio.renderers.default = 'browser'

# Leer archivo geojson y cargar datos.
bsas = gpd.read_file('pages/ranking_ambiental/limite_partidos_expandido.geojson', encoding="ASCI")
bsas["tooltip"] = bsas["nam"]
bsas_geojson = json.loads(bsas.to_json(na="keep"))
geobuf = dlx.geojson_to_geobuf(bsas_geojson)

# Crear valores medios y clases.
min_value = bsas["arl"].min()
max_value = bsas["arl"].max()
middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
classes = list(middle_values)

# Definir colores para las clases.
colorscale = [ '#F5BBCB', '#F2A4B6', '#EF8DA1', '#ED769C', '#EB5F87', '#E94872', '#E7315D', '#E51A48']
style = dict(weight=2, opacity=1, color='white', dashArray='3', fillOpacity=0.7)

# Crear colorbar.
ctg = ["{}+".format(cls, classes[i + 1]) for i, cls in enumerate(classes[:-1])] + ["{}+".format(classes[-1])]
# Barra de colores categóricos personalizada
colorbar = dlx.categorical_colorbar(
    categories=ctg,
    colorscale=colorscale,
    width=200,  # Ancho personalizado
    height=20,  # Altura personalizada
    position="bottomleft",  # Posición
)

# Lógica de representación del GeoJSON.
style_handle = assign("""function(feature, context){
    const {classes, colorscale, style, colorProp} = context.props.hideout;
    const value = feature.properties[colorProp];
    for (let i = 0; i < classes.length; ++i) {
        if (value > classes[i]) {
            style.fillColor = colorscale[i];
            style.weight = 1;
            style.dashArray = false;
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


colorscale_reference = html.Div(
    id='colorscale-reference',
    children=[dbc.Row([html.Div("PROTECCIÓN", style={'text-align': 'center','font-size': '12px','color': 'black'})]),
              dbc.Row([dbc.Col([html.Div("MENOR", style={'text-align':'right','color': 'black'})], md=3),
                       dbc.Col([color_bar], md=6),
                       dbc.Col([html.Div("MAYOR", style={'text-align': 'left','color': 'black'})], md=3),
                    ]),     
            ],
    style={
        'position': 'absolute',
        'bottom': '0px',
        'right': '510px',
        'width': '25%',
        'display': 'flex',
        'flex-direction': 'column',
        
        'font-size': '12px',
        # 'background': f'linear-gradient(to top, {", ".join(colorbar)})',
        # Añade espacio entre el texto y la barra de colores
    }
)


Mapa_transparencia =dl.Map(
                            zoom=13,
                            dragging=False,
                            # touchZoom=False,
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
                                    hideout=dict(colorscale=colorscale, classes=classes, style=style, colorProp="arl")
                                ),
                               
                            ],
                            style={
                                'width': '1200px',
                                'height': '500px',
                                'background-color': 'white'
                            }
                        )







titulo_del_mapa_1 = html.H6(
    "PROVINCIA DE BUENOS AIRES",
    style={
        'position': 'absolute',
        'top': '0px',
        'left': '225px',
        'font-size': '18px',
        'font-weight': 'bold',
        'color': 'black',
        'white-space': 'pre-line',  # Forzar el salto de línea
    }
)
titulo_del_mapa_2 = html.H6(
    "CONURBANO",
    style={
        'position': 'absolute',
        'top': '0px',
        'left': '700px',
        'font-size': '18px',  # Ajustar el tamaño de fuente
        'font-weight': 'bold',  # Hacer que el texto sea negrita
        'color': 'black',
    }
)

mapa_layout = html.Div(
    id="mapa-container",
    children=[
        Mapa_transparencia,
        titulo_del_mapa_1,
        titulo_del_mapa_2,  
        colorscale_reference   
    ],
    style={'display':'flex', 'position': 'relative', 'width': '100%', 'height': '100%'}
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