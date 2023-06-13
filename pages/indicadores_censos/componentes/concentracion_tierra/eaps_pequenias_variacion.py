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

color_concentracion_tierra_1 = '#89370B'

# Titulos
graph_title =  'EAPs PEQUEÑAS (<=500ha)'

# BASE DE DATOS
df_base_original = base_censos.copy()

pequenias_df_base = df_base_original[[VAR_EAPS_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]

df_base = pequenias_df_base.copy()

###### GRAFICO  #####  
 
EAPs_pequenias =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="eaps-pequenias"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("Ampliar", id="open-modal-button-pequenias", color="warning",style={"background-color": "#89370B", "border-color": "#DEDE7C"}),
                                ),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-eaps-pequenias"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-pequenias",
    
)                

@callback(
        Output("eaps-pequenias", "figure"),
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

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_EAPS_PEQ].sum().reset_index()
    df[VAR_EAPS_PEQ]= round(df[VAR_EAPS_PEQ],2)

    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_PEQ, text_auto=VAR_EAPS_PEQ)
    fig.update_traces(marker_color=color_concentracion_tierra_1)  # Modificar el color de las barras
    fig.update_layout(title={"text": graph_title,"font": {"size": 20, "color": "black", "family": "Arial"}}, showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_layout(yaxis=dict(tickformat=',',ticksuffix='k'))
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))

    return fig


EAPs_pequenias_texto = html.H6(id="texto-eaps-pequenias" , style={'font-size': '20px'}, className="text-white")



@callback(
     Output("texto-eaps-pequenias", "children"), 
     [
         Input("select-partido", "value"),
     ]
 )


def update_epas_pequenias_text(partidos):
    df = df_base.copy()
    sel_partido = [c for c in partidos if c != '']
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_EAPS_PEQ].sum().reset_index()
    df[VAR_EAPS_PEQ]= round(df[VAR_EAPS_PEQ],2)

    df_2018 = df[df[VAR_ANIO_CENSO]== VAR_ULTIMO_ANIO_CENSO].copy()
    cantidad_eaps_2018 = int(df_2018[VAR_EAPS_PEQ].sum())
    cantidad_eaps_2002 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_2002][VAR_EAPS_PEQ].sum())
    cantidad_eaps_1988 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_1988][VAR_EAPS_PEQ].sum())

    var_intercensal = round(((cantidad_eaps_2018 - cantidad_eaps_1988)/cantidad_eaps_1988)*100, 2)

    var_texto = 'una disminución' if  var_intercensal<=0 else 'un aumento'

    partido_seleccionado = partidos

    mensaje = f"""En {partido_seleccionado} se registraron {cantidad_eaps_2018} explotaciones agropecuarias con un tamaño menor o igual a 500 hectáreas según 
    el CNA de 2018. Además, se observa {var_texto} de EAPS pequeñas del {var_intercensal}% si se compara con las EAPs del CNA del año 1988."""

    return mensaje  