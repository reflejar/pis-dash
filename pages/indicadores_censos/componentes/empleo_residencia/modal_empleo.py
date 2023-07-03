import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash
color_empleo='rgb(225, 134, 95)'

modal_empleo=dbc.Modal(
                    [
                        dbc.ModalHeader(id="titulo-modal-empleo"),
                        dbc.ModalBody(
                           dcc.Graph(id="modal-graph-empleo"),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Cerrar", id="close-modal-button-empleo", className="ml-auto", color="warning",style={"background-color": color_empleo, "border-color": "#DEDE7C"}),
                        ),
                    ],
                    id="modal-empleo",
                    is_open=False,
                )

@callback(
    [Output("modal-empleo", "is_open"), 
     Output("modal-graph-empleo", "figure" ), 
     Output("open-modal-button-residentes", "n_clicks"), 
     ],
    [Input("open-modal-button-residentes", "n_clicks"), Input("close-modal-button-empleo", "n_clicks")],
    [State("modal-empleo", "is_open"), State("grafico-residentes", "figure")],
)
def toggle_modal(open_clicks, close_clicks, is_open, figure):
    if open_clicks:
        return not is_open,figure,0
    elif open_clicks:
        return not is_open,figure,0
    elif close_clicks:
        return False, dash.no_update,0
    return is_open, dash.no_update,0