from dash import html
import dash_bootstrap_components as dbc
from .componentes.solapas import SolapasRanking
from .componentes.acordeon import AcordeonRanking

layout =dbc.Container([ 
            dbc.Row([
                dbc.Col([
                    html.H4("NORMATIVA COMPARADA",className="text-white mt-5"),
                    html.P(["Para el comparativo de normativas se establecieron cuatro dimensiones analíticas,"]),
                    html.P(["1) Transparencia, 2) Protección de poblados, 3) Protección de escuelas rurales y 4) Protección del agua."]),
                ],  md=12, class_name="text-white mt-5"),
            ], class_name="my-5"),
            dbc.Row([
                dbc.Col(SolapasRanking, md=12)
            ], class_name="my-5"),
            dbc.Row([
                dbc.Col([
                    html.P(
                        "Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, "
                        "pero como toda selección de criterios esta puede ser arbitraria. El objetivo del mismo no es dar "
                        "cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, "
                        "sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. "
                        "Esta herramienta fue pensada para: redactar nuevas ordenanzas, mejorar las ordenanzas existentes y estudiar "
                        "el marco legal en cada distrito.",
                        style={"text-align": "justify"}
                    ),
                    html.P("Podes descargar el data set completo AQUÍ.."),                    
                ], md=12, class_name="text-white mt-5")
            ], class_name="my-5"),            
            dbc.Row([
                dbc.Col(AcordeonRanking, md=12)
            ], class_name="my-5")

            ],className="my-5 min-vh-100 justify-content-center"
    ) 