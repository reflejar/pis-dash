import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash

modal_tierra=dbc.Modal(
                    [
                        dbc.ModalHeader(id="titulo-modal-tierra"),
                        dbc.ModalBody(
                           dcc.Graph(id="modal-graph"),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Cerrar", id="close-modal-button", className="ml-auto", color="warning",style={"background-color": "#89370B", "border-color": "#DEDE7C"}),
                        ),
                    ],
                    id="modal-tierra",
                    is_open=False,
                )

@callback(
    [
        Output("modal-tierra", "is_open"), 
        Output("modal-graph", "figure" )
    ],
    [
        Input("open-modal-button-eaps", "n_clicks"), 
        Input("open-modal-button-tamanio", "n_clicks"), 
        Input("open-modal-button-pequenias", "n_clicks"), 
        Input("close-modal-button", "n_clicks")
    ],
    [
        State("modal-tierra", "is_open"), 
        State("q-eaps-total", "figure"), 
        State("q-eaps-tamanio", "figure"),
        State("eaps-pequenias", "figure"), 
    ],
)
def toggle_modal(
    open_clicks_eaps, 
    open_clicks_tamanio,
    open_clicks_pequenias, 
    close_clicks, 
    is_open, 
    figure_eaps, 
    figure_tamanio,
    figure_pequenias
):
    if open_clicks_eaps:
        return not is_open,figure_eaps
    elif open_clicks_tamanio:
        return not is_open,figure_tamanio
    elif open_clicks_pequenias:
        return not is_open,figure_pequenias
    elif close_clicks:
        return False, dash.no_update
    return is_open, dash.no_update