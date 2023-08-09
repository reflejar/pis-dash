from dash import dcc, Input, Output, callback, State
import dash_bootstrap_components as dbc
import dash

color_concentracion_tierra_1 = 'rgb(150, 79, 71)'

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

# @callback(
#     [
#         Output("modal-tierra", "is_open"), 
#         Output("modal-graph-tierra", "figure" ),
#         Output("open-modal-q-eaps-total", "n_clicks"), 
#         Output("open-modal-button-tamanio", "n_clicks"), 
#         Output("open-modal-button-superficie", "n_clicks"),
#         Output("open-modal-button-superficie-tamanio", "n_clicks"), 
#         Output("open-modal-button-eaps-juridico", "n_clicks"), 
#         Output("open-modal-button-superficie-juridico", "n_clicks"), 
#         Output("open-modal-button-eaps-sexo", "n_clicks"), 
#     ],
#     [
#         Input("open-modal-q-eaps-total", "n_clicks"), 
#         Input("open-modal-button-tamanio", "n_clicks"), 
#         Input("open-modal-button-superficie", "n_clicks"),
#         Input("open-modal-button-superficie-tamanio", "n_clicks"),
#         Input("open-modal-button-eaps-juridico", "n_clicks"),
#         Input("open-modal-button-superficie-juridico", "n_clicks"),
#         Input("open-modal-button-eaps-sexo", "n_clicks"),
#         Input("close-modal-button-tierra", "n_clicks")
#     ],
#     [
#         State("modal-tierra", "is_open"), 
#         State("q-eaps-total", "figure"), 
#         State("q-eaps-tamanio", "figure"),
#         State("eaps-superficie", "figure"),
#         State("superficie-eaps-tamanio", "figure"), 
#         State("q-eaps-juridico", "figure"), 
#         State("superficie-eaps-juridico", "figure"),
#         State("eaps-sexo-propiedad", "figure") 
#     ],
# )
# def toggle_modal(
#     open_clicks_eaps, 
#     open_clicks_tamanio,
#     open_clicks_superficie,
#     open_clicks_superficie_tamanio,
#     open_clicks_eaps_juridico,
#     open_clicks_ha_juridico,
#     open_clicks_eaps_sexo,
#     close_clicks, 
#     is_open, 
#     figure_eaps, 
#     figure_tamanio,
#     figure_superficie,
#     figure_superficie_tamanio,
#     figure_eaps_juridico,
#     figure_ha_juridico,
#     figure_eaps_sexo,
# ):
#     if open_clicks_eaps:
#         return not is_open,figure_eaps,0,0,0,0,0,0,0
#     elif open_clicks_tamanio:
#         return not is_open,figure_tamanio,0,0,0,0,0,0,0
#     elif open_clicks_superficie:
#         return not is_open,figure_superficie,0,0,0,0,0,0,0
#     elif open_clicks_superficie_tamanio:
#         return not is_open,figure_superficie_tamanio,0,0,0,0,0,0,0
#     elif open_clicks_eaps_juridico:
#         return not is_open,figure_eaps_juridico,0,0,0,0,0,0,0
#     elif open_clicks_ha_juridico:
#         return not is_open,figure_ha_juridico,0,0,0,0,0,0,0
#     elif open_clicks_eaps_sexo:
#         return not is_open,figure_eaps_sexo,0,0,0,0,0,0,0
#     elif close_clicks:
#         return False, dash.no_update,0,0,0,0,0,0,0
#     return is_open, dash.no_update,0,0,0,0,0,0,0