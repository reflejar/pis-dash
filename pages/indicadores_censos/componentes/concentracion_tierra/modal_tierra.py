import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash

color_concentracion_tierra_1 = '#89370B'

modal_tierra=dbc.Modal(
                    [
                        
                        dbc.ModalBody(
                           dcc.Graph(id="modal-graph-tierra"),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("CERRAR GRÁFICO", 
                                       id="close-modal-button-tierra", 
                                       color="light",style={"background-color": color_concentracion_tierra_1, "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": "Arial"},  
                                       className="mx-auto"), className="text-center", style={"background-color": "none","border": "none", "color": "none"}
                        ),
                    ],
                    id="modal-tierra",
                    is_open=False,
                )

@callback(
    [
        Output("modal-tierra", "is_open"), 
        Output("modal-graph-tierra", "figure" ),
        Output("open-modal-button-eaps", "n_clicks"), 
        Output("open-modal-button-tamanio", "n_clicks"), 
        Output("open-modal-button-superficie", "n_clicks"), 
    ],
    [
        Input("open-modal-button-eaps", "n_clicks"), 
        Input("open-modal-button-tamanio", "n_clicks"), 
        Input("open-modal-button-superficie", "n_clicks"), 
        Input("close-modal-button-tierra", "n_clicks")
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