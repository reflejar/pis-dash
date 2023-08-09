from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle
from .modal_tierra import modal_tierra


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO, VAR_ULTIMO_ANIO_CENSO, VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_concentracion_tierra_1, color_concentracion_tierra_2
##### VARIABLES ######

VAR_SUPERFICIE_HA = 'Superficie promedio'
x_titulo = "Año del censo"
y_titulo = "Superficie promedio (ha)"

# Titulos
graph_title =  'Superficie promedio de EAPs (ha)'

# BASE DE DATOS
df_base_original = base_censos.copy()

superficie_promedio_df = df_base_original[[VAR_SUPERFICIE_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]

df_base = superficie_promedio_df.copy()

###### GRAFICO  #####  
 
EAPs_SUPERFICIE =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="eaps-superficie"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_concentracion_tierra_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", 
                                               id="open-modal-button-superficie", 
                                               style={"background-color": color_concentracion_tierra_2, 
                                                      "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-eaps-superficie"
                    ),
                    modal_tierra,
    ],
    className="contenedor-eaps-superficie",
    
)                

@callback(
        Output("eaps-superficie", "figure"),
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

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_SUPERFICIE_HA].sum().reset_index()
    #df[VAR_SUPERFICIE_HA]= round(df[VAR_SUPERFICIE_HA],2)

    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_SUPERFICIE_HA, text_auto=VAR_SUPERFICIE_HA)
    fig.update_traces(marker_color=color_concentracion_tierra_2)  # Modificar el color de las barras
    fig.update_layout(title={"text": graph_title,"font": {"size": tamanio_fuente_titulo, "color": color_letra, "family": letra}}, showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
  #Armar el texto de las etiquetas emergentes
    fig.update_traces(hovertemplate='Superficie promedio: %{y} hectáreas<br>Año del censo: %{x}')
 
        # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>Superficie promedio de EAPs <br> en hectáreas</br> </b>",
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


EAPs_superficie_texto = html.H6(id="texto-eaps-superficie" , style={'font-size': '20px'}, className="text-white")



@callback(
     Output("texto-eaps-superficie", "children"), 
     [
         Input("select-partido", "value"),
     ]
 )


def update_epas_superficie_text(partidos):
    df = df_base.copy()
    sel_partido = [c for c in partidos if c != '']
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_SUPERFICIE_HA].sum().reset_index()
    df[VAR_SUPERFICIE_HA]= round(df[VAR_SUPERFICIE_HA],2)

    df_2018 = df[df[VAR_ANIO_CENSO]== VAR_ULTIMO_ANIO_CENSO].copy()
    cantidad_eaps_2018 = int(df_2018[VAR_SUPERFICIE_HA].sum())
    cantidad_eaps_2002 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_2002][VAR_SUPERFICIE_HA].sum())
    cantidad_eaps_1988 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_1988][VAR_SUPERFICIE_HA].sum())

    var_intercensal = round(((cantidad_eaps_2018 - cantidad_eaps_1988)/cantidad_eaps_1988)*100, 2)

    var_texto = 'una disminución' if  var_intercensal<=0 else 'un aumento'

    partido_seleccionado = partidos

    mensaje = f"""Al mismo tiempo, en [la provincia de Buenos Aires] la superficie promedio de las EAPs 
        [aumentó] XX hectáreas. Esto explica la caída en cantidad de EAPs a lo largo del tiempo, dado que las explotaciones 
        agropecuarias tienen cada vez una mayor superficie en promedio. Se puede apreciar con claridad que existe una gran acumulacion de tierra en pocas EAPs. """

    return mensaje  