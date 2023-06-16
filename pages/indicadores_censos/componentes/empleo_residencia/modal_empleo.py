import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash

modal_empleo=dbc.Modal(
                    [
                        dbc.ModalHeader(id="titulo-modal-empleo"),
                        dbc.ModalBody(
                           dcc.Graph(id="modal-graph-empleo"),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Cerrar", id="close-modal-button-empleo", className="ml-auto", color="warning",style={"background-color": '#EF7418', "border-color": "#DEDE7C"}),
                        ),
                    ],
                    id="modal-empleo",
                    is_open=False,
                )

@callback(
    [Output("modal-empleo", "is_open"), 
     Output("modal-graph-empleo", "figure" ), 
     Output("open-modal-button-residentes-mujeres", "n_clicks"), 
     Output("open-modal-button-residentes-varones", "n_clicks")],
    [Input("open-modal-button-residentes-mujeres", "n_clicks"), Input("open-modal-button-residentes-varones", "n_clicks"), Input("close-modal-button-empleo", "n_clicks")],
    [State("modal-empleo", "is_open"), State("grafico-residentes-mujeres", "figure"), State("grafico-residentes-varones", "figure")],
)
def toggle_modal(open_clicks_eaps, open_clicks_tamanio, close_clicks, is_open, figure_eaps, figure_tamanio):
    if open_clicks_eaps:
        return not is_open,figure_eaps,0,0
    elif open_clicks_tamanio:
        return not is_open,figure_tamanio,0,0
    elif close_clicks:
        return False, dash.no_update,0,0
    return is_open, dash.no_update,0,0