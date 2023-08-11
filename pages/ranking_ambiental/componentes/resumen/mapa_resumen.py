import dash
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash.dependencies import Input, Output
import geopandas as gpd
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from shapely.geometry import box, Point, Polygon
from dash_extensions.javascript import arrow_function, assign

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
colorscale = ['#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026']
style = dict(weight=2, opacity=1, color='white', dashArray='3', fillOpacity=0.7)

# Crear colorbar.
ctg = ["{}+".format(cls, classes[i + 1]) for i, cls in enumerate(classes[:-1])] + ["{}+".format(classes[-1])]
colorbar = dlx.categorical_colorbar(categories=ctg, colorscale=colorscale, width=300, height=30, position="bottomleft")

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



Mapa_resumen = dl.Map(
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
        )
    ],
    style={
        'width': '1500px',
        'height': '500px'
    }
)
