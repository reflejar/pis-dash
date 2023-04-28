from dash import html, Input, Output, callback, State
import dash_bootstrap_components as dbc


Footer = html.Footer([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(
                    [
                        html.A(html.I(className="bi bi-twitter"), href="https://twitter.com/fundacionDER",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                        html.A(html.I(className="bi bi-instagram"), href="https://www.instagram.com/democraciaenred/",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                        html.A(html.I(className="bi bi-facebook"), href="https://www.facebook.com/democraciaenred",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                        html.A(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/company/democracia-en-red/",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                    ],
                    className="text-center"
                )
            ],
            md=12),
        ]),
    ])
    ],
    className="text-white position-relative",
    id="footer"
)


