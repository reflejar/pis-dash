from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc


# Definir el diseño de la aplicación
EAPS_HA = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H5("Gráfico de Barras", className="card-title"),
                        dcc.Graph(
                            id="bar-chart",
                            figure={
                                "data": [
                                    {
                                        "x": ["A", "B", "C"],
                                        "y": [4, 6, 3],
                                        "type": "bar",
                                    }
                                ],
                                "layout": {
                                    "title": "Ejemplo de Gráfico de Barras",
                                    "plot_bgcolor": "rgba(0,0,0,0)",
                                    "paper_bgcolor": "rgba(0,0,0,0)",
                                    "font": {"color": "white"},
                                },
                            },
                        ),
                        dbc.Button("Ver Detalles", id="open-modal-button", color="primary"),
                    ]
                ),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Tarjeta Ampliada"),
                        dbc.ModalBody(
                            dcc.Graph(
                                id="expanded-chart",
                                figure={
                                    "data": [
                                        {
                                            "x": ["A", "B", "C"],
                                            "y": [4, 6, 3],
                                            "type": "bar",
                                        }
                                    ],
                                    "layout": {
                                        "title": "Gráfico Ampliado",
                                        "plot_bgcolor": "rgba(0,0,0,0)",
                                        "paper_bgcolor": "rgba(0,0,0,0)",
                                        "font": {"color": "white"},
                                    },
                                },
                            )
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Cerrar", id="close-modal-button", className="ml-auto")
                        ),
                    ],
                    id="modal",
                    size="xl",
                ),
            ],
            style={"width": "18rem"},
        )
    ],
    className="p-5",
)

@callback(
    Output("modal", "is_open"),
    [Input("open-modal-button", "n_clicks"), Input("close-modal-button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if open_clicks:
        return not is_open
    elif close_clicks:
        return False
    return is_open