from dash import html
import dash_bootstrap_components as dbc

from .componentes.encabezado import Encabezado
from .componentes.filtros import Filtros
from .componentes.solapas import Solapas
from .componentes.textos import Metodologia, Explicacion


layout = dbc.Container([
            Encabezado,
            Filtros,
            Solapas,
            Explicacion,
            Metodologia
        ],
        className="my-5 min-vh-100",
    ) 