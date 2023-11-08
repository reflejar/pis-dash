from dash import html
import dash_bootstrap_components as dbc

Encabezado = dbc.Row([
                dbc.Col([
                    html.H3(['Zonificación', html.A("V 1.0", href="#metodologia-normativa", className="btn btn-sm text-primary")], className="text-white pt-3 fw-bolder space-grotesk"),
                    html.P(["""Mapa de Áreas pobladas, escuelas rurales , cursos y superficies e agua, zonas de exclusión y 
                            amortiguamiento según normativa vigente.""", html.Br(), """Seleccioná el municipio de tu interés, activá y desactivá las capas para ver el ordenamiento territorial."""
                    ], className="text-white poppins"),

                    ],  md=12, class_name="text-white mt-5"),
            ], class_name="mt-5")