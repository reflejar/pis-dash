from dash import html

import dash_bootstrap_components as dbc

TextoIndicadores = dbc.Container(
    [      
        html.H4("CENSO NACIONAL AGROPECUARIO", className="text-white"),
        html.P(["Aquí podrás ver diferentes datos de los censos agropecuarios"]),
        html.P(["Recorre las diferentes visualizaciones para conocerlas en mas detalle."]),
        html.P(["Podes descargar el data set completo aqui"]),
    ],
    id="texto-indicadores",
    className=" text-white mt-5"
)




