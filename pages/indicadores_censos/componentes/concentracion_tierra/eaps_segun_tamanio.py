from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle
from .modal_tierra import modal_tierra


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO, VAR_ULTIMO_ANIO_CENSO, VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002

##### VARIABLES ######

VAR_EAPS_PEQ = 'EAPS pequeñas (<= 500ha)'
VAR_EAPS_GRANDES = 'EAPS grandes (>500 ha)'
VAR_TOTAL_EAPS = 'Total EAPS'

VAR_EAPS_Q = 'Cantidad de EAPs'
VAR_TAMANIO_EAPS = 'Tamaño EAPs'


color_concentracion_tierra_1 = '#89370B'
color_concentracion_tierra_2 = '#DEDE7C'


# Titulos
graph_title =  'Proporción de EAPs según tamaño'

# BASE DE DATOS
df_base_original = base_censos.copy()

pequenias_df_base = df_base_original[[VAR_EAPS_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]
pequenias_df_base = pequenias_df_base.rename(columns = {VAR_EAPS_PEQ: VAR_EAPS_Q})
pequenias_df_base[VAR_TAMANIO_EAPS] = 'Pequeñas (<=500 ha)'

grandes_df_base = df_base_original[[VAR_EAPS_GRANDES, VAR_ANIO_CENSO, VAR_PARTIDO]]
grandes_df_base = grandes_df_base.rename(columns = {VAR_EAPS_GRANDES: VAR_EAPS_Q})
grandes_df_base[VAR_TAMANIO_EAPS] = 'Grandes (>500 ha)'

df_base = pd.concat([pequenias_df_base, grandes_df_base])

###### GRAFICO  #####  
 
Q_EAPs_tamanio =dbc.Container(
            [
                dbc.Card(
                            [  
                                #dbc.CardHeader(html.H6(graph_title,style={'font-size': '20px'}, className="text-dark")),
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="q-eaps-tamanio"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("Ampliar", id="open-modal-button-tamanio", color="warning",style={"background-color": "#89370B", "border-color": "#DEDE7C"}),
                                ),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-q-eaps-tamanio"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-tamanio",
    
)                

@callback(
        Output("q-eaps-tamanio", "figure"),
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

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_TAMANIO_EAPS])[VAR_EAPS_Q].sum().reset_index()
    df[VAR_EAPS_Q]= round(df[VAR_EAPS_Q],2)

    fig = px.histogram(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_Q, color=VAR_TAMANIO_EAPS, barnorm='percent',  text_auto=True, color_discrete_sequence=[color_concentracion_tierra_1, color_concentracion_tierra_2 ])
    fig.update_layout(title={"text": graph_title,"font": {"size": 20, "color": "black", "family": "Arial"}}, showlegend=False, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_yaxes(title_text = "Distribución de EAPs según tamaño",  title_font=dict(size=12,family='Verdana',color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    

    return fig


EAPs_tamanio_texto = html.H6(id="texto-eaps-tamanio" , style={'font-size': '20px'}, className="text-white")



@callback(
     Output("texto-eaps-tamanio", "children"), 
     [
         Input("select-partido", "value"),
     ]
 )


def update_epas_tamanio_text(partidos):
    df = df_base.copy()
    sel_partido = [c for c in partidos if c != '']
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_TAMANIO_EAPS])[VAR_EAPS_Q].sum().reset_index()
    df[VAR_EAPS_Q]= round(df[VAR_EAPS_Q],2)

    df_2018 = df[df[VAR_ANIO_CENSO]== VAR_ULTIMO_ANIO_CENSO].copy()
    cantidad_eaps_2018 = int(df_2018[VAR_EAPS_Q].sum())
    cantidad_peq_eaps_2018 = int(df_2018[df_2018[VAR_TAMANIO_EAPS]== 'Pequeñas (<=500 ha)'][VAR_EAPS_Q].sum())
    cantidad_grandes_eaps_2018 = int(df_2018[df_2018[VAR_TAMANIO_EAPS]== 'Grandes (>500 ha)'][VAR_EAPS_Q].sum())

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