from dash import dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.express as px
import pandas as pd
from .modal_tierra import modal_tierra
import textwrap
from pages.indicadores_censos.data_censo.base_indicadores import VAR_ANIO_CENSO, VAR_PARTIDO
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_concentracion_tierra_1, color_concentracion_tierra_2

##### VARIABLES ######

VAR_EAPS_Q = 'Cantidad de EAPs'
VAR_SEXO_PROPIETARIE = 'Sexo'

x_titulo = "Año del censo"
y_titulo = "Cantidad de EAPs"

# Titulos
graph_title =  "Propiedad de EAPs según sexo, Año 2018 "

df_base = pd.read_csv('pages/indicadores_censos/data_censo/tierra/propiedad_x_sexo.csv', sep=';'  )

df_base[VAR_ANIO_CENSO] = df_base[VAR_ANIO_CENSO].astype(int).astype(str) 
df_base[VAR_EAPS_Q] = df_base[VAR_EAPS_Q].astype(int)

###### GRAFICO  #####  
 
PropiedadEAPSexo =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="eaps-sexo-propiedad"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", 
                                               id="open-modal-button-eaps-sexo", 
                                               style={"background-color": color_concentracion_tierra_2, 
                                                      "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="eaps-propiedad-sexo"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-sexo",
    
)                

@callback(
        Output("eaps-sexo-propiedad", "figure"),
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

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_SEXO_PROPIETARIE])[VAR_EAPS_Q].sum().reset_index()
    df[VAR_EAPS_Q]= round(df[VAR_EAPS_Q],2)

    fig = px.pie(df, values=VAR_EAPS_Q, names=VAR_SEXO_PROPIETARIE, color_discrete_sequence=[color_concentracion_tierra_1, color_concentracion_tierra_2 ])
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
    
    #Armar el texto de las etiquetas emergentes # Falta agregar tipo juridico
    #fig.update_traces(hovertemplate='Cantidad de EAPs: %{values}<br>Año del censo: 2018')
 
 

    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>{'<br>'.join(textwrap.wrap(graph_title, width=25))}</b>",
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