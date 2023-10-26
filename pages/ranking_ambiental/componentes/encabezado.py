from dash import html
import dash_bootstrap_components as dbc

Encabezado = dbc.Row([
                dbc.Col([
                    html.H3("Ranking",className="text-white fw-bolder pt-3"),
                    html.Br(),
                    html.P(["Clasificación interactiva de ordenanzas municipales de regulación de agroquímicos y promoción de la agroecología. Seleccioná la dimensión analítica de tu interés y compara entre municipios"], className="text-white poppins"),
                    html.P(html.A("V 1.0 (métodologia & producto)", href="#metodologia-ranking", className="text-primary text-uppercase"))],  md=12, class_name="text-white mt-5"),
            ], class_name="my-5")

