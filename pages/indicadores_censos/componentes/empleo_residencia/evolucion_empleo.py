from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.express as px
import pandas as pd
from .modal_empleo import modal_empleo
import textwrap

from pages.indicadores_censos.data.base_indicadores import VAR_ANIO_CENSO, VAR_PARTIDO
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_empleo_1, color_concentracion_tierra_2

#Variables
VAR_EMPLEO = 'Empleo'

x_titulo = 'Año del censo'
y_titulo = 'Cantidad de personas empleadas'

# Titulos
graph_title =  'Evolución del empleo permanente en el campo'

# BASE DE DATOS
df_base = pd.read_csv('pages/indicadores_censos/data/empleo-y-residencia/evolucion_empleo.csv', sep=';' )

df_base[VAR_ANIO_CENSO] = df_base[VAR_ANIO_CENSO].astype(int).astype(str) 

###### GRAFICO  #####  
 
Empleo =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="grafico-empleo"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_empleo_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", id="open-modal-button-empleo", style={"background-color": color_empleo_1, "border-color": "#FFFFFF", "color": "#000000", "font-family": letra}), className="text-center", style={"background-color": "light","border": "none", "color": "light"}
                                ),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-empleo"
                    ),
                    modal_empleo,
    ],
    className="contenedor-empleo",
    
)                

@callback(
        Output("grafico-empleo", "figure"),
        Input("select-partido", "value"),
)

def update_bar_chart(partidos):

    df = df_base.copy()
    sel_partido = [c for c in partidos if c != '']
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO]==partidos
        df = df[mask]
    

    df = df.groupby(by = [VAR_ANIO_CENSO])[VAR_EMPLEO].sum().reset_index()

    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_EMPLEO, color_discrete_sequence=[color_empleo_1],text=VAR_EMPLEO)
    fig.update_layout(title=graph_title, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = x_titulo, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_yaxes(title_text = y_titulo,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
    
    #Armar el texto de las etiquetas emergentes
    fig.update_traces(hovertemplate='Cantidad de personas empleadas: %{text}<br>Año del censo: %{x}')
 
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
        "yanchor": "top",
        },
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45,
        hovermode="x",
        )

    return fig


