from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import pickle
from .modal_empleo import modal_empleo
import textwrap

from pages.indicadores_censos.data_censo.base_indicadores import VAR_ANIO_CENSO, VAR_PARTIDO
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_empleo_1, color_empleo_2
##### VARIABLES ######

VAR_SEXO_NACIMIENTO= 'Sexo de nacimiento'
VAR_CANTIDAD_PERSONAS = 'Cantidad de personas'

x_titulo = "Año del censo"
y_titulo = "Residentes por sexo"

# Titulos
graph_title =  "Evolución de residentes del campo por sexo"

df_base = pd.read_csv('pages/indicadores_censos/data_censo/empleo-y-residencia/residentes_por_sexo.csv', sep=';' )

df_base[VAR_ANIO_CENSO] = df_base[VAR_ANIO_CENSO].astype(int).astype(str) 

###### GRAFICO  #####  
 
ResidentesPorSexo =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="grafico-residentes"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_empleo_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", id="open-modal-button-residentes", style={"background-color": color_empleo_1, "border-color": "#FFFFFF", "color": "#000000", "font-family": letra}), className="text-center", style={"background-color": "light","border": "none", "color": "light"}
                                ),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-residentes",
                            
                    ),
                    modal_empleo,
    ],
    className="contenedor-residentes",
    
)                

@callback(
        Output("grafico-residentes", "figure"),
        Input("select-partido", "value"),
)

def update_bar_chart(partidos):

    df = df_base.copy()
    sel_partido = [c for c in partidos if c != ""]
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]

#    if len(df) == 0:
#        return NoHayDatos['linea']

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_SEXO_NACIMIENTO])[VAR_CANTIDAD_PERSONAS].sum().reset_index()
    df[VAR_CANTIDAD_PERSONAS]= round(df[VAR_CANTIDAD_PERSONAS],2)

    fig = px.histogram(df, x=VAR_ANIO_CENSO, y=VAR_CANTIDAD_PERSONAS, color=VAR_SEXO_NACIMIENTO,  text_auto=True, color_discrete_sequence=[color_empleo_1, color_empleo_2 ])
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
    
    #Armar el texto de las etiquetas emergentes # Falta agregar sexo
    fig.update_traces(hovertemplate='Cantidad de Residentes: %{y}<br>Año del censo: %{x}')
    
    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>{'<br>'.join(textwrap.wrap(graph_title, width=25))}</b>",
        "x": 0.5,
        "y": 0.95,
        "xanchor": "center",
        "yanchor": "top",
        "font": { 
            "size": 17,
            "color": "black",
            "family": letra
        },
        "yref": "container",
        "yanchor": "top"
        },
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45,
        hovermode="x",
        legend=dict(
            title='',
            orientation="h",
            xanchor='center',
            x=0.5,
            y=-0.3,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            tracegroupgap=10
        )
    )


    return fig


 