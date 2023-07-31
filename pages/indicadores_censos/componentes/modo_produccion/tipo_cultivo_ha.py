import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.indicadores_censos.data_censo.cultivos_ha import base_cultivos, VAR_ANIO_CENSO, VAR_PARTIDO,VAR_VALORES, VAR_CULTIVOS,VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002, VAR_ANIO_CENSO_2018
import plotly.graph_objects as go
import plotly.express as px
import plotly.colors as colors
from .modal_cultivos import modal_cultivos
import textwrap
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra,color_cultivos_1,color_cultivos_2, color_cultivos_3, color_cultivos_4

# Titulos
graph_title =  'Cantidad de hectáreas según el tipo de cultivo'

# BASE DE DATOS
df_base_original = base_cultivos.copy()



CULTIVOS_HA= dbc.Container(
    [
        dbc.Card(
            [   
                html.H4(graph_title, className="card-title"),
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="tipo-cultivos-ha-1988"), md=4),
                        dbc.Col(dcc.Graph(id='tipo-cultivos-ha-2002'), md=4),
                        dbc.Col(dcc.Graph(id="tipo-cultivos-ha-2018"), md=4),                      
                        ]
                    ),
                    size=24,
                    )
                    
                ),
                dbc.CardFooter(
                    dbc.Button("AMPLIAR GRÁFICO", 
                                id="open-modal-button-cultivos-ha", 
                                style={"background-color": color_cultivos_1, 
                                        "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                
            ],
            color="light", 
            class_name="shadow",    
            outline=True,
            id="tipo-cultivos-ha"
        ),
        modal_cultivos,
    ],
    className="contenedor-cultivos-1988",
    
)


@callback(
        [
        Output('tipo-cultivos-ha-1998', 'figure'),
        Output('tipo-cultivos-ha-2002', 'figure'), 
        Output('tipo-cultivos-ha-2018', 'figure')
        ],

        Input("select-partido", "value"),
        
)
def update_bar_chart(partidos):

    figs = []

    for i in [VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002, VAR_ANIO_CENSO_2018]:

        sel_partido = [c for c in partidos if c != '']  

        df = base_cultivos.copy()
        mask=base_cultivos[VAR_ANIO_CENSO]==i
        df = base_cultivos[mask]
        
        if len(sel_partido) >0:
            mask = df[VAR_PARTIDO]==partidos
            df = df[mask]
        
        color_cultivos_personalizados = [color_cultivos_1,color_cultivos_2,color_cultivos_3,color_cultivos_4]


        fig = px.pie(df, values=VAR_VALORES, 
                    names=VAR_CULTIVOS,
                    color=VAR_CULTIVOS, 
                    color_discrete_map=dict(zip(df[VAR_CULTIVOS], color_cultivos_personalizados)))
        
        #Hover
        fig.update_traces(hovertemplate=f"{'<br>'.join(textwrap.wrap('Cantidad de hectáreas cultivadas de <b>%{label}</b>: %{value:.0f}', width=25))}",
            text="<b>"+df[VAR_CULTIVOS].astype(str)+"</b>",  # Obtener los valores totales como texto
            textposition='outside',  # Colocar el texto automáticamente encima de las barras
            textfont=dict(color=color_letra, size=tamanio_fuente, family=letra)
        )                  
    
        # Actualizar el diseño del gráfico
        fig.update_layout(
            title={
            "text": f"<b>{i}</b>",
            "x": 0.5,
            "y": 0.95,
            "xanchor": "center",
            "yanchor": "top",
            "font": {
                "size": tamanio_fuente_titulo,
                "color": "black",
                "family": letra
            },
            "yref": "container",
            "yanchor": "top",
            },
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_tickangle=-45,
            hovermode="x",
            )
        
        figs.append(fig)

    return figs[0], figs[1], figs[2] 