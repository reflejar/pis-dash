from dash import html
import dash_bootstrap_components as dbc

from .componentes.encabezado import Encabezado
from .componentes.solapas import Solapas
from .componentes.mapa import Mapa
from .componentes.textos import Explicacion, Metodologia
from .componentes.tabla import Tabla

layout =dbc.Container([ 
            Encabezado,
            Solapas,
            Mapa,
            Explicacion,
            Tabla,
            Metodologia
        ],
        className="my-5 min-vh-100 justify-content-center"
    ) 