############################
### Se inicia Flask
############################
from flask import Flask
server = Flask(__name__)

# Se incorporan endpoints necesarios para k8s
@server.route('/')
def readiness(): return "OK", 200 

############################
### Se inicia Dash
############################
import dash
import dash_bootstrap_components as dbc
from dash import html

from pages import (
	mapa_normativo,
	ranking_ambiental
)


# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP], # COSMO, FLATLY, LUX, MINTY
	use_pages=True,
	update_title="Actualizando...",
	prevent_initial_callbacks=True,
	title="PIS | Mapa normativo"
)

dash.register_page(mapa_normativo.__name__, title="Mapa Normativo", path='/mapa-normativo', layout=mapa_normativo.layout)
dash.register_page(ranking_ambiental.__name__, title="Mapa Normativo", path='/ranking-ambiental', layout=ranking_ambiental.layout)


# Se agregan los componentes de la web
app.layout = html.Div(children=[dash.page_container])


# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)