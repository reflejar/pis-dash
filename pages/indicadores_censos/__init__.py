from dash import html
import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros_censos
from .componentes.solapas import Solapas
from .componentes.solapas.resumen_general import PERDIDA_EMPLEO_X_MES, PERDIDA_EAPS_X_MES, PERDIDA_RESIDENCIA_X_MES


layout = html.Div([
        dbc.Row([
                dbc.Col(dbc.Container([      
                        html.H4('CENSO NACIONAL AGROPECUARIO', className="text-white"),
                        html.Br(),
                        html.H5('Entre el 2002 y el 2018, en la Provincia de Buenos Aires, cada mes:', className="text-white"),
                        html.H5([f'Se cerraban ', html.Strong(f"{PERDIDA_EAPS_X_MES}", className="text-primary"), " EAP"], className="text-white px-5"),
                        html.H5([html.Strong(f'{PERDIDA_RESIDENCIA_X_MES}', className='text-primary'), ' personas se veían expulsadas de su residencia'], className="text-white px-5"),
                        html.H5([html.Strong(f'{PERDIDA_EMPLEO_X_MES}', className='text-primary'), ' personas perdían su puesto de trabajo permanente'], className="text-white px-5"),
                        html.Br(),
                        html.H6(["Aquí podrás ver diferentes datos de los censos agropecuarios. Recorré las diferentes visualizaciones para conocerlas en mas detalle."], className="text-white"),
                        html.H6(["Podes descargar el data set completo aqui"], className="text-white"),
                    ],
                    className="text-white mt-5"
                )
                , md=12),
                dbc.Col(Filtros_censos, md=12),
            ], 
            class_name="mb-5"
        ),
        dbc.Row(
            dbc.Col(Solapas, md=12)
        ),
        ],
        className="my-5 mx-5 min-vh-100",
    ) 