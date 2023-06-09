import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO
import plotly.graph_objects as go
import plotly.express as px
import plotly.colors as colors
from .modal_tierra import modal_tierra


##### VARIABLES ######

VAR_TOTAL_EAPS = 'Total EAPS'
VAR_EAPS_Q = 'Cantidad de EAPs'
#COLOR
color_concentracion_tierra_1 = '#89370B'

# Titulos
graph_title =  'Cantidad de EAPs'

# BASE DE DATOS
df_base_original = base_censos.copy()

df_eaps_q = df_base_original[[VAR_ANIO_CENSO, VAR_PARTIDO, VAR_TOTAL_EAPS]]
df_eaps_q = df_eaps_q.rename(columns = {VAR_TOTAL_EAPS: VAR_EAPS_Q})


EAPS_HA = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="q-eaps-total"), md=12),
                        ]
                    ),
                    size=24,
                    color=color_concentracion_tierra_1,
                    )
                    
                ),
                dbc.CardFooter(
                    dbc.Button("Ampliar", id="open-modal-button-eaps", color="warning",style={"background-color": "#89370B", "border-color": "#DEDE7C"}),
                ),
                
            ],
            color="light", 
            class_name="shadow",
            outline=True,
            id="tarjeta_eaps_cantidad"
        ),
        modal_tierra,
    ],
    className="contenedor-eaps-cantidad",
    
)


@callback(
        Output("q-eaps-total", "figure"),
        
        Input("select-partido", "value"),
        
)

def update_bar_chart(partidos):

    sel_partido = [c for c in partidos if c != '']
    

    df = df_eaps_q.copy()
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]
    

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_EAPS_Q].sum().reset_index()

    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_Q, color_discrete_sequence=[color_concentracion_tierra_1],text=VAR_EAPS_Q)
    fig.update_layout(barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_yaxes(title_text = "Cantidad de EAPS",  title_font=dict(size=12,family='Verdana',color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_layout(yaxis=dict(tickformat="."))

    return fig
    
    
