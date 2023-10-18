import dash_leaflet as dl
import dash_leaflet.express as dlx

# import plotly.io as pio
from dash_extensions.javascript import arrow_function, assign

from pages.ranking_ambiental.data import bsas,VAR_PUNTAJE,  classes

# Establecer el renderizador predeterminado para Plotly.
# pio.renderers.default = 'browser'

# Agregar informacion de etiquetas


#Transformar a geobuf


style = dict(weight=3, opacity=1, color='white', dashArray='4', fillOpacity=0.8)

aver = assign("""function(feature, context){
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

# Crear colorbar.
ctg = ["{}+".format(cls, classes[i + 1]) for i, cls in enumerate(classes[:-1])] + ["{}+".format(classes[-1])]

class Mapa:
    """
        Clase para crear las diferentes tablas
    """

    def __init__(
            self,
            geojson,
            colores=[]
    ) -> None:
        self.geobuf = dlx.geojson_to_geobuf(geojson)
        self.colores = colores

    def inicializar(self):
        return dl.Map(
            id="mapa-ranking",
            zoom=15,
            dragging=False,
            # touchZoom=False,
            zoomControl=False,
            scrollWheelZoom=False,
            doubleClickZoom=False,
            children=[
                dl.GeoJSON(
                    data=self.geobuf,
                    format='geobuf',
                    zoomToBounds=True,
                    zoomToBoundsOnClick=False,
                    options=dict(style=aver),
                    hoverStyle=arrow_function(dict(weight=8, dashArray='')),
                    hideout=dict(colorscale=self.colores, classes=classes, style=style, colorProp=VAR_PUNTAJE)
                ),
                
            ],
            className="min-vh-50 bg-white"
        )

