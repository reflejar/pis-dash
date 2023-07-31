import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO
import plotly.graph_objects as go
import plotly.express as px
import plotly.colors as colors
from .modal_tierra import modal_tierra
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_concentracion_tierra_1, color_concentracion_tierra_2


##### VARIABLES ######

VAR_TOTAL_EAPS = 'Total EAPS'
VAR_EAPS_Q = 'Cantidad de EAPs'
x_titulo = "Año del censo"
y_titulo = "Cantidad de EAPs"



# Titulos
graph_title =  'Explotaciones Agropecuarias'

# BASE DE DATOS
df_base_original = base_censos.copy()

df_eaps_q = df_base_original[[VAR_ANIO_CENSO, VAR_PARTIDO, VAR_TOTAL_EAPS]]
df_eaps_q = df_eaps_q.rename(columns = {VAR_TOTAL_EAPS: VAR_EAPS_Q})


EAPS_CANTIDAD = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="q-eaps-total"), md=12),
                        #dbc.Col("""En los últimos 30 años, en [partido_seleccionado] han [disminuido] en un [XX%] la cantidad de EAPS. 
                        #En 1988 el numero de EAPS era de [XX] y en 2018 ese numero paso a ser de [XX] implicando una caida de [XX] 
                        #explotaciones agropecuarias.""", md=12)                        
                        ]
                    ),
                    size=24,
                    color=color_concentracion_tierra_1,
                    )
                    
                ),
                dbc.CardFooter(
                    dbc.Button("AMPLIAR GRÁFICO", 
                                id="open-modal-button-eaps", 
                                style={"background-color": color_concentracion_tierra_2, 
                                        "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                
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
    fig.update_layout(title=graph_title, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
    
    #Armar el texto de las etiquetas emergentes
    fig.update_traces(hovertemplate='Cantidad de EAPs: %{text}<br>Año del censo: %{x}')
 
   
    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>Cantidad de <br> Explotaciones Agropecuarias</br></b>",
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
        "yanchor": "top"
        },
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45,
        hovermode="x",
        legend=dict(
            title='',
            orientation="v",
            xanchor='right',
            x=1.05,
            y=1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            tracegroupgap=10
        )
    )

    return fig

EAPs_cantidad_texto = html.H6(id="texto-eaps-cantidad" , style={'font-size': '20px'}, className="text-white")
