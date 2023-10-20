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
	external_stylesheets=[dbc.icons.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'], # COSMO, FLATLY, LUX, MINTY
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
                dbc.Nav([html.A("Volver a PIS", href="https://pis.org.ar", className="btn text-uppercase poppins")]),
            ],
        ),
        fixed="top",
        className="text-primary",
    ),
	html.Div(id='page-content'),
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
    )])
])



@app.callback(Output('page-content', 'children'),Input('url', 'pathname'))
def display_page(_):

    sections = {
            'zonificacion': {'layout': mapa_normativo.layout, 'analytics': 'G-4BW9V2HCS0'},
            'censos': {'layout': indicadores_censos.layout, 'analytics': 'G-P4RK1GKTG0'},
            'ranking': {'layout': ranking_ambiental.layout, 'analytics': 'G-FBLLE0SDB7'}
    }

    try:
        page_config = sections[request.host.split(".")[0]]
    except:
        page_config = sections[sys.argv[1]] if len(sys.argv) > 1 else sections['censos']
    
    app.index_string = """<!DOCTYPE html>
        <html>
            <head>
                <!-- Google tag (gtag.js) --> """ + \
                f"""<script async src="https://www.googletagmanager.com/gtag/js?id={page_config['analytics']}"></script>""" + \
                """<script>
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());""" + \
                f"""gtag('config', '{page_config['analytics']}');
                </script>""" + \
                """{%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
            </head>
            <body>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>""" 
    return page_config['layout']


# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)