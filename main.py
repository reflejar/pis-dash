############################
### Se inicia Flask
############################
from flask import Flask
server = Flask(__name__)
# Se incorporan endpoints necesarios para k8s
@server.route('/k8s/readiness/')
def readiness(): return "OK", 200 
@server.route('/k8s/liveness/') 
def liveness(): return "OK", 200  

############################
### Se inicia Dash
############################
import dash
import dash_bootstrap_components as dbc
from dash import html

from componentes.navbar import Navbar
from componentes.footer import Footer
from componentes.filtros import Filtros
from componentes.mapa import MapaNormativo

# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP], # COSMO, FLATLY, LUX, MINTY
	update_title="Actualizando...",
	prevent_initial_callbacks=True,
	title="PIS | Mapa normativo"
)


# Se agregan los componentes de la web
app.layout = html.Div(
	children=[
		Navbar,     
		html.Div([
				dbc.Row([
					dbc.Col(Filtros, md=3),
					dbc.Col(MapaNormativo, md=9)
				]),
				html.Hr(),
				],
				className="my-5 mx-5 min-vh-100",
			),
		Footer
	]
)


# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)