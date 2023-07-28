import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
import dash

color_empleo='rgb(225, 134, 95)'

modal_empleo=dbc.Modal(
                    [
                        
                        dbc.ModalBody(
                           dcc.Graph(id="modal-graph-empleo"),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("CERRAR GRÁFICO", id="close-modal-button-empleo", color="light",style={"background-color": color_empleo, "border-color": "#FFFFFF", "color": "#000000", "font-family": "Arial"},  className="mx-auto"), className="text-center", style={"background-color": "none","border": "none", "color": "none"}
                        ),
                    ],
                    id="modal-empleo",
                    is_open=False,
                )

@callback(
    [Output("modal-empleo", "is_open"), 
     Output("modal-graph-empleo", "figure" ), 
     Output("open-modal-button-residentes", "n_clicks"), 
     Output("open-modal-button-empleo", "n_clicks")
     ],
    [Input("open-modal-button-residentes", "n_clicks"),Input("open-modal-button-empleo", "n_clicks"), Input("close-modal-button-empleo", "n_clicks")],
    [State("modal-empleo", "is_open"), State("grafico-residentes", "figure"), State("grafico-empleo", "figure")],
)
def toggle_modal(open_clicks_residentes, open_clicks_empleo, close_clicks, is_open, figure_residentes, figure_empleo):
    if open_clicks_residentes:
        return not is_open,figure_residentes,0,0
    elif open_clicks_empleo:
        return not is_open,figure_empleo,0,0
    elif close_clicks:
        return False, dash.no_update,0,0
    return is_open, dash.no_update,0,0