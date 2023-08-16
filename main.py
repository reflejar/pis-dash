############################
### Se inicia Flask
############################
from flask import Flask, request, redirect
server = Flask(__name__)
import dash

# Se incorporan endpoints necesarios para k8s
@server.route('/')
def index(): 
    host = request.headers['Host']
    if not 'localhost' in host:
        return redirect({
             'normativo': '/mapa-normativo',
             'censo': '/indicadores-censo',
             'ranking': '/ranking-ambiental'
        }[host.split(".")[0]])
    return """
            <h1><a href="/mapa-normativo">Mapa normativo</a></h1>
            <h1><a href="/indicadores-censo">Indicadores censo</a></h1>
            <h1><a href="/ranking-ambiental">Ranking</a></h1>
        """, 200 

############################
### Se inicia Dash
############################

import dash_bootstrap_components as dbc
from dash import html

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

dash.register_page(mapa_normativo.__name__, title="PIS | Mapa Normativo", path='/mapa-normativo', layout=mapa_normativo.layout)
dash.register_page(ranking_ambiental.__name__, title="PIS | Ranking Ambiental", path='/ranking-ambiental', layout=ranking_ambiental.layout)
dash.register_page(indicadores_censos.__name__, title="PIS | Censo Nacional Agropecuario", path='/indicadores-censo', layout=indicadores_censos.layout)

ISOLOGOTIPO = html.Img(src="assets/img/PIS_isologo_negro.png", alt="Isotipo de PIS", height="70px")

# Se agregan los componentes de la web
app.layout = html.Div(children=[
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
	dash.page_container,
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


# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)