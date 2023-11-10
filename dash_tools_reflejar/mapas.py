import dash_leaflet as dl
import dash_leaflet.express as dlx

# import plotly.io as pio
from dash_extensions.javascript import arrow_function, assign
from dash_extensions.javascript import Namespace

ns = Namespace("dash_props", "module")

#Transformar a geobuf

js_func = assign("""function(feature, context){
                        const {classes, colorscale, style, colorProp} = context.props.hideout;
                        const value = feature.properties[colorProp];
                        if (value === null || isNaN(value)) {
                            // Asigna color gris para observaciones sin datos
                            style.fillColor = 'rgb(128, 128, 128)';
                            style.weight = 1;
                            style.dashArray = false;
                        } else {
                            for (let i = 0; i < classes.length; ++i) {
                                if (value >= classes[i]) {
                                    style.fillColor = colorscale[i];
                                    style.weight = 1;
                                    style.dashArray = false;
                                }
                            }
                        }
                        return style;
                    }""")

class Mapa:
    """
        Clase para crear las diferentes tablas
    """

    def __init__(
            self,
            geojson,
            colores=[],
            classes=[],
            centro=[],
            id_map="",
            color_prop=""
    ) -> None:
        self.geobuf = dlx.geojson_to_geobuf(geojson)
        self.colores = colores
        self.classes= classes
        self.centro=centro
        self.id = id_map
        self.color_prop = color_prop

    def inicializar(self):

        return dl.Map(
            id=self.id,
            dragging=False,
            # touchZoom=False,
            zoomControl=False,
            scrollWheelZoom=False,
            doubleClickZoom=False,
            attributionControl=False,   
            zoom=6,
            center=self.centro,
            children=[
                dl.GeoJSON(
                    data=self.geobuf,
                    format='geobuf',
                    zoomToBoundsOnClick=False,
                    options=dict(style=js_func, onEachFeature=ns("on_each_feature")),
                    hoverStyle=arrow_function(dict(weight=8, dashArray='')),
                    hideout=dict(
                        colorscale=self.colores, 
                        classes=self.classes, 
                        style=dict(
                            weight=3, 
                            opacity=1, 
                            color='white', 
                            dashArray='4', 
                            fillOpacity=1
                            ), 
                        colorProp=self.color_prop
                    )
                ),
                
            ],
            className="min-vh-50 bg-white"
        )

