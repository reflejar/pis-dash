import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.indicadores_censos.data_censo.cultivos_ha import base_cultivos, VAR_ANIO_CENSO, VAR_PARTIDO,VAR_VALORES, VAR_CULTIVOS,VAR_ANIO_CENSO_2002
import plotly.graph_objects as go
import plotly.express as px
import plotly.colors as colors
from .modal_cultivos import modal_cultivos
import textwrap

##### VARIABLES ######

#COLOR
color_cultivos_1 = 'rgb(77, 130, 133)'
color_cultivos_2 = 'rgb(150, 79, 71)'
color_cultivos_3 = 'rgb(225, 134, 95)'
color_cultivos_4 = 'rgb(170, 166, 163)'
letra = 'Arial'

# Titulos
graph_title =  'Cantidas de hectáreas según el tipo de cultivo para el censo 2002'

# BASE DE DATOS
df_base_original = base_cultivos.copy()



CULTIVOS_2002 = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="grafico_cultivos_2002"), md=12),
                        #dbc.Col("""En los últimos 30 años, en [partido_seleccionado] han [disminuido] en un [XX%] la cantidad de EAPS. 
                        #En 2002 el numero de EAPS era de [XX] y en 2018 ese numero paso a ser de [XX] implicando una caida de [XX] 
                        #explotaciones agropecuarias.""", md=12)                        
                        ]
                    ),
                    size=24,
                    #color=color_concentracion_tierra_1,
                    )
                    
                ),
                dbc.CardFooter(
                    dbc.Button("AMPLIAR GRÁFICO", 
                                id="open-modal-button-cultivos_2002", 
                                style={"background-color": color_cultivos_1, 
                                        "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                
            ],
            color="light", 
            class_name="shadow",    
            outline=True,
            id="tarjeta_cultivos_2002"
        ),
        modal_cultivos,
    ],
    className="contenedor-cultivos-2002",
    
)


@callback(
        Output("grafico_cultivos_2002", "figure"),
        
        Input("select-partido", "value"),
        
)

def update_bar_chart(partidos):

    sel_partido = [c for c in partidos if c != '']
    

    df = base_cultivos.copy()
    mask=base_cultivos[VAR_ANIO_CENSO]==VAR_ANIO_CENSO_2002
    df = base_cultivos[mask]
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]
    

    

    color_cultivos_personalizados = [color_cultivos_1,color_cultivos_2,color_cultivos_3,color_cultivos_4]

    fig = px.pie(df, values=VAR_VALORES, 
                 names=VAR_CULTIVOS,
                 color=VAR_CULTIVOS, 
                 color_discrete_map=dict(zip(df[VAR_CULTIVOS], color_cultivos_personalizados)))
    fig.update_traces(hovertemplate=f"{'<br>'.join(textwrap.wrap('Cantidad de hectáreas cultivadas de <b>%{label}</b>: %{value:.0f}', width=25))}",
        text="<b>"+df[VAR_CULTIVOS].astype(str)+"</b>",  # Obtener los valores totales como texto
        textposition='outside',  # Colocar el texto automáticamente encima de las barras
        textfont=dict(color='black', size=14, family=letra)
    )  
    fig.update_layout(
        title={
        "text": f"<b>{'<br>'.join(textwrap.wrap(graph_title, width=40))}</b>",
        "x": 0.5,
        "y": 0.95,
        "xanchor": "center",
        "yanchor": "top",
        "font": {
            "size": 18,
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

    return fig





# @callback(
#      Output("texto-eaps-cantidad", "children"), 
#      [
#          Input("select-partido", "value"),
#      ]
#  )


# def update_epas_cantidad_text(partidos):
    # df = df_base.copy()
    # sel_partido = [c for c in partidos if c != '']
    
    # if len(sel_partido) >0:
    #     mask = df[VAR_PARTIDO]==partidos
    #     df = df[mask]

    # df = df.groupby(by = [VAR_ANIO_CENSO, VAR_TAMANIO_EAPS])[VAR_EAPS_Q].sum().reset_index()
    # df[VAR_EAPS_Q]= round(df[VAR_EAPS_Q],2)

    # df_2018 = df[df[VAR_ANIO_CENSO]== VAR_ULTIMO_ANIO_CENSO].copy()
    # cantidad_eaps_2018 = int(df_2018[VAR_EAPS_Q].sum())
    # cantidad_peq_eaps_2018 = int(df_2018[df_2018[VAR_TAMANIO_EAPS]== 'Pequeñas (<=500 ha)'][VAR_EAPS_Q].sum())
    # cantidad_grandes_eaps_2018 = int(df_2018[df_2018[VAR_TAMANIO_EAPS]== 'Grandes (>500 ha)'][VAR_EAPS_Q].sum())

    # proporcion_grandes_2018 = round((cantidad_grandes_eaps_2018/cantidad_eaps_2018)*100,2)
    # proporcion_peq_2018 = round((cantidad_peq_eaps_2018/cantidad_eaps_2018)*100,2)

    # cantidad_eaps_2002 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_2002][VAR_EAPS_Q].sum())
    # cantidad_eaps_2002 = int(df[df[VAR_ANIO_CENSO]== VAR_ANIO_CENSO_2002][VAR_EAPS_Q].sum())

    # var_intercensal = ((cantidad_eaps_2018 - cantidad_eaps_2002)/cantidad_eaps_2002)*100

    # partido_seleccionado = partidos

    # mensaje= f"""En los últimos 30 años, en [partido_seleccionado] han [disminuido] en un [XX%] la cantidad de EAPS. 
    #   En 2002 el numero de EAPS era de [XX] y en 2018 ese numero paso a ser de [XX] implicando una caida de [XX] explotaciones agropecuarias."""
 


    # return mensaje  
    
    
