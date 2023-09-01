from dash import html
import dash_bootstrap_components as dbc


TextoRanking_1 = dbc.Container(
    [      
        html.H4("NORMATIVA COMPARADA",className="text-white mt-5"),
        html.P(["Para el comparativo de normativas se establecieron cuatro dimensiones analíticas,"]),
        html.P(["1) Transparencia, 2) Protección de poblados, 3) Protección de escuelas rurales y 4) Protección del agua."]),
    ],
    id="texto-ranking-1",
    className=" text-white mt-5"
)

TextoRanking_2 = dbc.Container(
    [      
        html.P(
            "Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, "
            "pero como toda selección de criterios esta puede ser arbitraria. El objetivo del mismo no es dar "
            "cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, "
            "sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. "
            "Esta herramienta fue pensada para: redactar nuevas ordenanzas, mejorar las ordenanzas existentes y estudiar "
            "el marco legal en cada distrito.",
            style={"text-align": "justify"}
        ),
        html.Br(),
        html.P("Podes descargar el data set completo AQUÍ.."),
    ],
    id="texto-ranking-2",
    className="text-white mt-5"
)