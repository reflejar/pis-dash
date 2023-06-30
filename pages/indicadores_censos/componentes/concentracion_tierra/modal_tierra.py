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
                            dbc.Button("CERRAR GRÁFICO", id="close-modal-button", className="ml-auto", color="warning",style={"background-color": "#89370B", "border-color": "#DEDE7C"}),
                        ),
                    ],
                    id="modal-tierra",
                    is_open=False,
                )

@callback(
    [
        Output("modal-tierra", "is_open"), 
        Output("modal-graph", "figure" ),
        Output("open-modal-button-eaps", "n_clicks"), 
        Output("open-modal-button-tamanio", "n_clicks"), 
        Output("open-modal-button-superficie", "n_clicks"), 
    ],
    [
        Input("open-modal-button-eaps", "n_clicks"), 
        Input("open-modal-button-tamanio", "n_clicks"), 
        Input("open-modal-button-superficie", "n_clicks"), 
        Input("close-modal-button", "n_clicks")
    ],
    [
        State("modal-tierra", "is_open"), 
        State("q-eaps-total", "figure"), 
        State("q-eaps-tamanio", "figure"),
        State("eaps-superficie", "figure"), 
    ],
)
def toggle_modal(
    open_clicks_eaps, 
    open_clicks_tamanio,
    open_clicks_superficie, 
    close_clicks, 
    is_open, 
    figure_eaps, 
    figure_tamanio,
    figure_superficie
):
    if open_clicks_eaps:
        return not is_open,figure_eaps,0,0,0
    elif open_clicks_tamanio:
        return not is_open,figure_tamanio,0,0,0
    elif open_clicks_superficie:
        return not is_open,figure_superficie,0,0,0
    elif close_clicks:
        return False, dash.no_update,0,0,0
    return is_open, dash.no_update,0,0,0