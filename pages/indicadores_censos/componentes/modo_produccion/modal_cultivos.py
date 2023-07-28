import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra,color_cultivos_1,color_cultivos_2, color_cultivos_3, color_cultivos_4



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
     Output("open-modal-button-cultivos_1988", "n_clicks"), 
     Output("open-modal-button-cultivos_2002", "n_clicks"),
     Output("open-modal-button-cultivos_2018", "n_clicks")
     ],
    [Input("open-modal-button-cultivos_1988", "n_clicks"),
     Input("open-modal-button-cultivos_2002", "n_clicks"),
     Input("open-modal-button-cultivos_2018", "n_clicks"), 
     Input("close-modal-button-cultivos", "n_clicks")
     ],
    [State("modal-cultivos", "is_open"), 
     State("grafico_cultivos_1988", "figure"),
     State("grafico_cultivos_2002", "figure"),
     State("grafico_cultivos_2018", "figure")
     ],
)
def toggle_modal(open_clicks_cultivos_1988,
                 open_clicks_cultivos_2002,
                 open_clicks_cultivos_2018,
                 close_clicks,
                 is_open, 
                 figure_cultivos_1988, 
                 figure_cultivos_2002,
                 figure_cultivos_2018,):
    if open_clicks_cultivos_1988:
        return not is_open,figure_cultivos_1988,0,0,0
    elif  open_clicks_cultivos_2002:
        return not is_open,figure_cultivos_2002,0,0,0
    elif  open_clicks_cultivos_2018:
        return not is_open,figure_cultivos_2018,0,0,0
    elif close_clicks:
        return False, dash.no_update,0,0,0
    return is_open, dash.no_update,0,0,0