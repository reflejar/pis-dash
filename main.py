import sys
import importlib
import os
import datetime
from logger import logger

############################
### Se inicia Flask
############################

from flask import Flask, request

server = Flask(__name__)


############################
### Se inicia Dash
############################

import dash
import dash_bootstrap_components as dbc
from dash import html, Output, Input, dcc

# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'],
	use_pages=False,
	update_title="Actualizando...",
	prevent_initial_callbacks=True,
	title="PIS",
	suppress_callback_exceptions=True,
)

# Se elige la herramienta
try:
    APP_CONFIG = os.environ["APP_CONFIG"]
    herramienta = importlib.import_module(f'.{APP_CONFIG}', 'pages')
except:
    APP_CONFIG = sys.argv[1] if len(sys.argv) > 1 else 'indicadores_censos'
    herramienta = importlib.import_module(f'.{APP_CONFIG}', 'pages')

# Analytics
with open('index.html', 'r') as file:
    html_content = file.read()
    GTAG_ANALYTICS = os.environ.get("GTAG_ANALYTICS", "")
    app.index_string = html_content.replace('GTAG_ANALYTICS', GTAG_ANALYTICS)

# Se agregan los componentes de la web
ISOLOGOTIPO = html.Img(src="assets/img/PIS_isologo_negro.png", alt="Isotipo de PIS", height="70px")

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    dbc.Navbar(
        dbc.Container(
            [
                html.A(ISOLOGOTIPO),
                dbc.Nav([html.A("Volver a PIS", href="https://pis.org.ar", className="btn text-uppercase poppins")]),
            ],
        ),
        fixed="top",
        className="text-primary",
    ),
    html.Div(id='contenido-herramienta'),
	html.Footer([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    ISOLOGOTIPO,
                    html.P([
                        "PIS es un proyecto de ", html.A("Democracia en Red", target="_blank", href="https://democraciaenred.org"), ",", html.Br(),
                        "una ONG con base en Buenos Aires, Argentina."
                    ], className="mx-4")
                ], className="d-flex align-items-center"),
                dbc.Col(
                    html.A("Explorá las demás herramientas", href="https://pis.org.ar", className="btn btn-outline-light text-uppercase"), 
                    class_name="text-end mt-3", 
                    lg=6)
        ])
        ],
        className="text-white position-relative py-4",
        id="footer"
    )]),
    
])

@app.callback(Output('contenido-herramienta', 'children'),Input('url', 'pathname'))
def display_page(url):
    # Fecha y hora actual
    now = datetime.datetime.now()
    logger.info(f'{request.host} {url} - {now.strftime("%Y-%m-%d %H:%M:%S")}')
    # Fecha y hora actual
    return herramienta.layout
# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)