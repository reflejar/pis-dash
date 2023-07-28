from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle
from .modal_empleo import modal_empleo
import textwrap


from pages.indicadores_censos.data_censo.empleo import base_empleo, VAR_ANIO_CENSO, VAR_TOTAL
from ..formatos import letra, tamanio_fuente_titulo, tamanio_fuente, tamanio_fuente_tick, color_letra, color_empleo_1, color_concentracion_tierra_2


# Titulos
graph_title =  'Evolución del empleo permanente en el campo'

# BASE DE DATOS
df_base_original = base_empleo.copy()

###### GRAFICO  #####  
 
empleo =dbc.Container(
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

    df = df_base_original.copy()
    
    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_TOTAL, color_discrete_sequence=[color_empleo_1])
    fig.update_traces(hovertemplate='Empleo permanente en el campo<br>Año del censo: %{x}<br>Cantidad de empleados:  %{y:.0f}<br>',
        text=df[VAR_TOTAL].astype(str),  # Obtener los valores totales como texto
        textposition='outside',  # Colocar el texto automáticamente encima de las barras
        textfont=dict(color='black', size=12, family=letra)
    )                  
    # Modificar el color de las barras
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=14, family=letra, color='black'), tickfont=dict(family=letra, color='black', size=11))
    fig.update_yaxes( title_text = "Cantidad de empleados", title_font=dict(size=14, family=letra, color='black'), tickfont=dict(family=letra, color='black', size=11))

    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>{'<br>'.join(textwrap.wrap(graph_title, width=25))}</b>",
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


