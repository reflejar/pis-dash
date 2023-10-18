from dash import html
import dash_bootstrap_components as dbc

Explicacion = dbc.Row(
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
        ], md=12, class_name="text-white mt-5 my-5")
    )