from dash import html
import dash_bootstrap_components as dbc

from .componentes.encabezado import Encabezado


layout = dbc.Container([
            Encabezado,
        ],
        className="my-5 min-vh-100",
    ) 