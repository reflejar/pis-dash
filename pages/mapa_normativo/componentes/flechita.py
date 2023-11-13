from dash import html, dcc

import dash_bootstrap_components as dbc
import dash_daq as daq

Flecha = html.Div(
    [
        dbc.Row(
            dbc.Col(html.A(html.Img(src="assets/img/flechita.svg", className="animate__animated animate__fadeInDown animate__slower animate__infinite"), href="#footer-normativo"), class_name="text-center mt-4")
        )
        
    ],
    id="flecha",
)