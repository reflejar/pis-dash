import pandas as pd
from dash import dcc, html, Input, Output, callback, State, no_update
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
from pages.indicadores_censos.data.modo_produccion import VAR_ANIO_CENSO, VAR_PARTIDO
import plotly.graph_objects as go
import plotly.express as px
import plotly.colors as colors
from .modal_cultivos import modal_cultivos
import textwrap
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra,color_cultivos_1,color_cultivos_2, color_cultivos_3, color_cultivos_4

##### VARIABLES ######

VAR_TIPO_CULTIVO = 'Tipo de cultivo'
VAR_EAPS_HA = 'Cantidad HA'

x_titulo = "Año del censo"
y_titulo = "Tipo de cultivo"

# Titulos
graph_title =  "Héctareas implantadas según tipo de cultivo"

df_base = pd.read_csv('pages/indicadores_censos/data/modo_produccion/hectareas_tipo_cultivo.csv', sep=';' )

df_base[VAR_ANIO_CENSO] = df_base[VAR_ANIO_CENSO].astype(int).astype(str)

CULTIVOS_HA= dbc.Container(
    [
        dbc.Card(
            [   
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="grafico-cultivos-ha"), md=12),                   
                        ]
                    ),
                    size=24,
                    )
                    
                ),
                dbc.CardFooter(
                    dbc.Button("AMPLIAR GRÁFICO", 
                                id="open-modal-button-cultivos-ha", 
                                style={"background-color": color_cultivos_1, 
                                        "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": letra}), 
                                className="text-center", style={"background-color": "light","border": "none", "color": "light"}),
                
            ],
            color="light", 
            class_name="shadow",    
            outline=True,
            id="tipo-cultivos-ha"
        ),
        modal_cultivos,
    ],
    className="contenedor-cultivos",
    
)

@callback(
        
        Output('grafico-cultivos-ha', 'figure'),
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

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_TIPO_CULTIVO])[VAR_EAPS_HA].sum().reset_index()
    df[VAR_EAPS_HA]= round(df[VAR_EAPS_HA],2)


    fig = px.area(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_HA, color=VAR_TIPO_CULTIVO, color_discrete_sequence=[color_cultivos_1, color_cultivos_2, color_cultivos_3 ])
    #fig.update_layout(title={"text": graph_title,"font": {"size": 20, "color": "black", "family": "Arial"}},  showlegend=False, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
    
    #Armar el texto de las etiquetas emergentes # Falta agregar tipo juridico
    fig.update_traces(hovertemplate='Cantidad de Hectareas cultivadas: %{y}<br>Año del censo: %{x}')


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
       