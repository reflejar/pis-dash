from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.express as px
import pandas as pd
from .modal_tierra import modal_tierra


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.base_indicadores import VAR_ANIO_CENSO, VAR_PARTIDO
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_concentracion_tierra_1, color_concentracion_tierra_2

##### VARIABLES ######
VAR_EAPS_HA_EMPRESAS = 'Superficie en manos de Empresas'
VAR_EAPS_HA_PERSONAS = 'Superficie en mano de Personas Humanas'
VAR_TOTAL_HA_EAPS = 'Total de HA'

VAR_EAPS_HA = 'HA de EAPs'
VAR_EAPS_TIPO_JURICIO = 'Tipo jurídico'
x_titulo = "Año del censo"
y_titulo = "Superficie ocupada (ha)"

# Titulos
graph_title =  "Explotaciones Agropecuarias según su tamaño"
df_base_ha = pd.read_csv('pages/indicadores_censos/data_censo/tierra/ha_tipo_juridico.csv', sep=';', decimal=',')
df_base_ha[VAR_ANIO_CENSO] = df_base_ha[VAR_ANIO_CENSO].astype(int).astype(str) 
###### GRAFICO  #####  
 
Superficie_EAPs_JURIDICO =dbc.Container(
            [
                dbc.Card(
                            [  
                                #dbc.CardHeader(html.H6(graph_title,style={'font-size': '20px'}, className="text-dark")),
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="superficie-eaps-juridico"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", 
                                               id="open-modal-button-superficie-juridico", 
                                               style={"background-color": color_concentracion_tierra_2, 
                                                      "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-superficie-eaps-juridico"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-superficie-juridico",
    
)                

@callback(
        Output("superficie-eaps-juridico", "figure"),
        Input("select-partido", "value"),
)

def update_bar_chart(partidos):

    df = df_base_ha.copy()
    sel_partido = [c for c in partidos if c != ""]
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]

#    if len(df) == 0:
#        return NoHayDatos['linea']

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_EAPS_TIPO_JURICIO])[VAR_EAPS_HA].sum().reset_index()
    #df[VAR_EAPS_HA]= round(df[VAR_EAPS_HA],2)

    fig = px.histogram(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_HA, color=VAR_EAPS_TIPO_JURICIO,  text_auto=True, color_discrete_sequence=[color_concentracion_tierra_1, color_concentracion_tierra_2 ])
    fig.update_layout(title={"text": graph_title,"font": {"size": tamanio_fuente_titulo, "color": color_letra, "family": letra}},  showlegend=False, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y

    #Armar el texto de las etiquetas emergentes
    fig.update_traces(hovertemplate='Superficie ocupada: %{y:.0f} ha<br>Año del censo: %{x}')


    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>Superficie ocupada <br> por EAPs según tipo juridico</br></b>",
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

