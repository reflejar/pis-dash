from dash import html
import dash_bootstrap_components as dbc

Encabezado = dbc.Row([
                dbc.Col([
                    html.H3(['Zonificación', html.A("V 1.0", href="#metodologia-normativa", className="btn btn-sm text-primary")], className="text-white pt-3 fw-bolder space-grotesk"),
                    html.Br(),
                    html.P(["""Clasificación interactiva de ordenanzas municipales de regulación de agroquímicos y 
                    promoción de la agroecología. Seleccioná la dimensión analítica de tu interés y compara entre municipios
                    """
                    ], className="text-white poppins"),
                    ],  md=12, class_name="text-white mt-5"),
            ], class_name="mt-5")
