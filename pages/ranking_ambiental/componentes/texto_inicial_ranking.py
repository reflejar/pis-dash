from dash import html
import dash_bootstrap_components as dbc


TextoRanking = dbc.Container(
    [      
        html.H4("RANKING NORMATIVO", className="text-white"),
        html.P(["Para el comparativo de normativas se establecieron cuatro dimensiones analíticas,"]),
        html.P(["1) tranmparencia, 2) protección de poblados, 3) protección de escuelas rurales y 4) protección del agua."]),
        html.P(["Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, pero como toda elección de criterios, esto puede ser arbitrario. El objetivo del mismo no es dar cuenta en términos absolutos de que una ordenanza protege efectivamente mejor un territorio que otra, sino más bien ser una herramienta de uso sencillo para analizar los distintos niveles de protección ambiental existentes. Esta herramienta fue pensada para:"]),
        html.Ul([
            html.Li("redactar nueva ordenanza"),
            html.Li("mejorar la ordenanza existente"),
            html.Li("estudiar el marco legal de cada distrito."),
        ]),
        html.P(["Podes descargar el data set completo aqui"]),
    ],
    id="texto-ranking",
    className=" text-white mt-5"
)
