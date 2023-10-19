from dash import html
import dash_bootstrap_components as dbc

Encabezado = dbc.Row([
                dbc.Col([
                    html.H4("NORMATIVA COMPARADA",className="text-white mt-5"),
                    html.P(["Para el comparativo de normativas se establecieron cuatro dimensiones analíticas,"]),
                    html.P(["1) Transparencia, 2) Protección de poblados, 3) Protección de escuelas rurales y 4) Protección del agua."]),
                ],  md=12, class_name="text-white mt-5"),
            ], class_name="my-5")