import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO
import plotly.graph_objects as go
import plotly.express as px
import plotly.colors as colors
##### VARIABLES ######

VAR_TOTAL_EAPS = 'Total EAPS'
VAR_EAPS_Q = 'Cantidad de EAPs'

# # colores
# color_territorial = '#6E5FA8'
# color_estatal = '#BDBDBD'

# Titulos
graph_title =  'Cantidad de EAPS según el año del censo'

# BASE DE DATOS
df_base_original = base_censos.copy()

df_eaps_q = df_base_original[[VAR_ANIO_CENSO, VAR_PARTIDO, VAR_TOTAL_EAPS]]
df_eaps_q = df_eaps_q.rename(columns = {VAR_TOTAL_EAPS: VAR_EAPS_Q})


EAPS_HA = dbc.Container(
    [
        dbc.Card(
            [
                
                dbc.CardHeader(graph_title),
                dbc.CardBody(dcc.Graph(id="q-eaps-total")),
                # dbc.CardFooter(
                #     dbc.Button("Ampliar", id="open-modal-button", color="primary"),
                # ),
                # dbc.Modal(
                #     [
                #         dbc.ModalHeader(graph_title),
                #         dbc.ModalBody(
                #            dcc.Graph(id="q-eaps-total"),
                #         ),
                #         dbc.ModalFooter(
                #             dbc.Button("Cerrar", id="close-modal-button", className="ml-auto", n_clicks=0)
                #         ),
                #     ],
                #     id="modal",
                # ),
            ],
            color="light", 
            class_name="shadow",
            outline=True,
            id="tarjeta_eaps_cantidad"
        )
    ],
    className="contenedor-eaps-cantidad",
    
)

@callback(
    Output("q-eaps-total", "figure"), 
    [
        Input("select-partido", "value")
    ]
)

def update_bar_chart(partidos):

    sel_partido = [c for c in partidos if c != '']
    

    df = df_eaps_q.copy()
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO].isin(sel_partido)
        df = df[mask]
    

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_EAPS_Q].sum().reset_index()

    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_Q, color_discrete_sequence=["#316397"])
    fig.update_layout(barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_yaxes(title_text = "Cantidad de EAPS",  title_font=dict(size=12,family='Verdana',color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_layout(yaxis=dict(tickformat="."))
    return fig

# @callback(
#     Output("modal", "is_open"),
#     [Input("open-modal-button", "n_clicks"), Input("close-modal-button", "n_clicks")],
#     [State("modal", "is_open")],
# )
# def toggle_modal(open_clicks, close_clicks, is_open):
#     if open_clicks:
#         return not is_open
#     elif close_clicks:
#         return False
#     return is_open