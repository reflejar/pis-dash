from dash import html
import dash_bootstrap_components as dbc

from .componentes.encabezado import Encabezado
from .componentes.filtros import Filtros
from .componentes.fallos import Fallos


layout = dbc.Container([
            Encabezado,
            Filtros,
            Fallos
        ],
        className="my-5 min-vh-100",
    ) 