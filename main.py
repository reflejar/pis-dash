import sys

############################
### Se inicia Flask
############################

from flask import Flask, request
server = Flask(__name__)
import dash

############################
### Se inicia Dash
############################

import dash_bootstrap_components as dbc
from dash import html, Output, Input, dcc

from pages import (
	mapa_normativo,
	ranking_ambiental,
	indicadores_censos
)

# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP], # COSMO, FLATLY, LUX, MINTY
	use_pages=True,
	update_title="Actualizando...",
	prevent_initial_callbacks=True,
	title="PIS",
	suppress_callback_exceptions=True,
)

# Se agregan los componentes de la web
ISOLOGOTIPO = html.Img(src="assets/img/PIS_isologo_negro.png", alt="Isotipo de PIS", height="70px")

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    dbc.Navbar(
        dbc.Container(
            [
                html.A(ISOLOGOTIPO),
                dbc.Nav([html.A("Volver a PIS", href="https://pis.org.ar", className="btn text-uppercase")]),
            ],
        ),
        fixed="top",
        className="text-primary",
    ),
	html.Div(id='page-content'),
	html.Footer([
        dbc.Container([
            dbc.Row([
                dbc.Col(dbc.Row(
                    [
                    dbc.Col(ISOLOGOTIPO, lg=2), 
                    dbc.Col([
                        "PIS es un proyecto de ", html.A("Democracia en Red", target="_blank", href="https://democraciaenred.org"), ",", html.Br(),
                        "una ONG con base en Buenos Aires, Argentina."
                    ], lg=10)
                ]
                ),lg=6),
                dbc.Col(html.A("Explorá las demás herramientas", href="https://pis.org.ar", className="btn btn-outline-light text-uppercase"), class_name="text-end", lg=6),
            ]),
        ])
        ],
        className="text-white position-relative py-4",
        id="footer"
    )
])



@app.callback(Output('page-content', 'children'),Input('url', 'pathname'))
def display_page(_):
    sections = {
            'zonificacion': mapa_normativo.layout,
            'censos': indicadores_censos.layout,
            'ranking': ranking_ambiental.layout
    }
    try:
        return sections[request.host.split(".")[0]]
    except:
        tool = sys.argv[1]
        return sections[tool]


# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)