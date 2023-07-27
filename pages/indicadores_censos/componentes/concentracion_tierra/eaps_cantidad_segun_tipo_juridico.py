from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.express as px
import pandas as pd
from .modal_tierra import modal_tierra


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO, VAR_ULTIMO_ANIO_CENSO, VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002

##### VARIABLES ######

VAR_EAPS_EMPRESAS= 'EAPS en manos de Empresas'
VAR_EAPS_PERSONAS = 'EAPS en manos de Personas Humanas'
VAR_TOTAL_EAPS = 'Total EAPS'

VAR_EAPS_Q = 'Cantidad de EAPs'
VAR_EAPS_TIPO_JURICIO = 'Tipo jurídico'

letra = 'Arial'
tamanio_fuente_titulo = 17
tamanio_fuente = 16
tamanio_fuente_tick = 11
color_letra = 'black'
x_titulo = "Año del censo"
y_titulo = "Cantidad de EAPs"


color_concentracion_tierra_1 = '#89370B'
color_concentracion_tierra_2 = '#DEDE7C'


# Titulos
graph_title =  "Explotaciones Agropecuarias según su tamaño"

df_base = pd.read_csv('pages/indicadores_censos/data_censo/tierra/eaps_tipo_juridico.csv', sep=';'  )

df_base[VAR_ANIO_CENSO] = df_base[VAR_ANIO_CENSO].astype(int).astype(str) 

###### GRAFICO  #####  
 
Q_EAPs_juridico =dbc.Container(
            [
                dbc.Card(
                            [  
                                #dbc.CardHeader(html.H6(graph_title,style={'font-size': '20px'}, className="text-dark")),
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="q-eaps-juridico"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", 
                                               id="open-modal-button-eaps-juridico", 
                                               style={"background-color": color_concentracion_tierra_1, 
                                                      "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-q-eaps-juridico"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-juridico",
    
)                

@callback(
        Output("q-eaps-juridico", "figure"),
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

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_EAPS_TIPO_JURICIO])[VAR_EAPS_Q].sum().reset_index()
    df[VAR_EAPS_Q]= round(df[VAR_EAPS_Q],2)

    fig = px.area(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_Q, color=VAR_EAPS_TIPO_JURICIO,  color_discrete_sequence=[color_concentracion_tierra_1, color_concentracion_tierra_2 ])
    #fig.update_layout(title={"text": graph_title,"font": {"size": 20, "color": "black", "family": "Arial"}},  showlegend=False, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y

    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>Cantidad de Explotaciones <br>Agropecuarias según tipo jurídico</br></b>",
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


# EAPs_tamanio_texto = html.H6(id="texto-eaps-juridico" , style={'font-size': '20px'}, className="text-white")



# @callback(
#      Output("texto-eaps-juridico", "children"), 
#      [
#          Input("select-partido", "value"),
#      ]
#  )


# def update_epas_tamanio_text(partidos):
    df = df_base.copy()
    sel_partido = [c for c in partidos if c != '']
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_EAPS_TIPO_JURICIO])[VAR_EAPS_Q].sum().reset_index()
    df[VAR_EAPS_Q]= round(df[VAR_EAPS_Q],2)

    df_2018 = df[df[VAR_ANIO_CENSO]== VAR_ULTIMO_ANIO_CENSO].copy()
    cantidad_eaps_2018 = int(df_2018[VAR_EAPS_Q].sum())
    cantidad_peq_eaps_2018 = int(df_2018[df_2018[VAR_EAPS_TIPO_JURICIO]== 'Pequeñas (<=500 ha)'][VAR_EAPS_Q].sum())
    cantidad_grandes_eaps_2018 = int(df_2018[df_2018[VAR_EAPS_TIPO_JURICIO]== 'Grandes (>500 ha)'][VAR_EAPS_Q].sum())

    proporcion_grandes_2018 = round((cantidad_grandes_eaps_2018/cantidad_eaps_2018)*100,2)
    proporcion_peq_2018 = round((cantidad_peq_eaps_2018/cantidad_eaps_2018)*100,2)

    cantidad_eaps_2002 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_2002][VAR_EAPS_Q].sum())
    cantidad_eaps_1988 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_1988][VAR_EAPS_Q].sum())

    var_intercensal = ((cantidad_eaps_2018 - cantidad_eaps_1988)/cantidad_eaps_1988)*100

    partido_seleccionado = partidos

    mensaje = f"""En {partido_seleccionado} se registraron {cantidad_eaps_2018} Explotaciones Agropecuarias según 
    el CNA de 2018. También podemos observar que {cantidad_peq_eaps_2018} EAPS, es decir, el {proporcion_peq_2018}% son pequeñas. 
    Mientras que {cantidad_grandes_eaps_2018} EAPS, es decir el {proporcion_grandes_2018}% son grandes."""



    return mensaje  