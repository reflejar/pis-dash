from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.express as px
import pandas as pd
from .modal_tierra import modal_tierra


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO, VAR_ULTIMO_ANIO_CENSO, VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002

##### VARIABLES ######
VAR_EAPS_HA_PEQ = 'HA ocupadas por EAPS pequeñas'
VAR_EAPS_HA_GRANDES = 'HA ocupadas por EAPS grandes'
VAR_TOTAL_HA_EAPS = 'Total de HA'

VAR_EAPS_HA = 'HA de EAPs'
VAR_TAMANIO_EAPS = 'Tamaño EAPs'

letra = 'Arial'
tamanio_fuente_titulo = 17
tamanio_fuente = 16
tamanio_fuente_tick = 11
color_letra = 'black'
x_titulo = "Año del censo"
y_titulo = "Superficie ocupada (ha) según tamaño"

color_concentracion_tierra_1 = '#89370B'
color_concentracion_tierra_2 = '#DEDE7C'


# Titulos
graph_title =  "Explotaciones Agropecuarias según su tamaño"
df_base_ha = pd.read_csv('pages/indicadores_censos/data_censo/tierra/eaps_ha_por_tamanio.csv', sep=';', decimal=',')
df_base_ha[VAR_ANIO_CENSO] = df_base_ha[VAR_ANIO_CENSO].astype(int).astype(str) 
###### GRAFICO  #####  
 
Superficie_EAPs_tamanio =dbc.Container(
            [
                dbc.Card(
                            [  
                                #dbc.CardHeader(html.H6(graph_title,style={'font-size': '20px'}, className="text-dark")),
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="superficie-eaps-tamanio"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", 
                                               id="open-modal-button-superficie-tamanio", 
                                               style={"background-color": color_concentracion_tierra_1, 
                                                      "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-superficie-eaps-tamanio"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-superficie-tamanio",
    
)                

@callback(
        Output("superficie-eaps-tamanio", "figure"),
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

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_TAMANIO_EAPS])[VAR_EAPS_HA].sum().reset_index()
    #df[VAR_EAPS_HA]= round(df[VAR_EAPS_HA],2)

    fig = px.histogram(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_HA, color=VAR_TAMANIO_EAPS,  text_auto=True, color_discrete_sequence=[color_concentracion_tierra_1, color_concentracion_tierra_2 ])
    fig.update_layout(title={"text": graph_title,"font": {"size": tamanio_fuente_titulo, "color": color_letra, "family": letra}},  showlegend=False, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y

    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>Superficie ocupada <br> por EAPs según tamaño</br></b>",
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

