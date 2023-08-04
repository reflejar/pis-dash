import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash
from ..formatos import color_cultivos_1

modal_cultivos=dbc.Modal(
                    [
                        
                        dbc.ModalBody(
                           dcc.Graph(id="modal-graph-cultivos" ),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("CERRAR GRÁFICO", id="close-modal-button-cultivos", color="light",style={"background-color": color_cultivos_1, "border-color": "#FFFFFF", "color": "#000000", "font-family": "Arial"},  className="mx-auto"), className="text-center", style={"background-color": "none","border": "none", "color": "none"}
                        ),
                    ],
                    id="modal-cultivos",
                    is_open=False,
                )

@callback(
    [Output("modal-cultivos", "is_open"), 
     Output("modal-graph-cultivos", "figure" ), 
     Output("open-modal-button-cultivos-ha", "n_clicks"),
     ],
    [Input("open-modal-button-cultivos-ha", "n_clicks"),
     Input("close-modal-button-cultivos", "n_clicks")
     ],
    [State("modal-cultivos", "is_open"), 
     State("grafico-cultivos-ha", "figure"),
     ],
)
def toggle_modal(open_clicks_cultivos_ha,
                 close_clicks,
                 is_open, 
                 figure_cultivos_ha
                 ):
    if open_clicks_cultivos_ha:
        return not is_open,figure_cultivos_ha,0
    elif close_clicks:
        return False, dash.no_update,0
    return is_open, dash.no_update,0