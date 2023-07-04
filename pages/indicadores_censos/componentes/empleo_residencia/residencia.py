from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle
from .modal_empleo import modal_empleo


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.residencia import base_mujeres, base_varones, VAR_ANIO_CENSO, VAR_TOTAL

##### VARIABLES ######


color_empleo_1 = 'rgb(225, 134, 95)'
color_empleo_2= 'rgb(77, 130, 133)'
# Titulos
graph_title =  'Residentes del campo'
#Tipo de letra
letra="Arial"
# BASE DE DATOS
df_mujeres = base_mujeres.copy()
df_varones = base_varones.copy()


###### GRAFICO  #####  
 
residencia =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="grafico-residentes"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_empleo_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("AMPLIAR GRÁFICO", id="open-modal-button-residentes", style={"background-color": color_empleo_1, "border-color": "#FFFFFF", "color": "#000000", "font-family": letra}), className="text-center", style={"background-color": "light","border": "none", "color": "light"}
                                ),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-residentes",
                            
                    ),
                    modal_empleo,
    ],
    className="contenedor-residentes",
    
)                

@callback(
        Output("grafico-residentes", "figure"),
        Input("select-partido", "value"),
)

def update_bar_chart(partidos):

    
    fig = px.bar(x=df_mujeres[VAR_ANIO_CENSO], y=[df_mujeres[VAR_TOTAL], df_varones[VAR_TOTAL]])

    # Calcular el porcentaje del total, que luego aparecen en las etiquetas emergentes 
    total = df_mujeres[VAR_TOTAL].to_numpy() + df_varones[VAR_TOTAL].to_numpy()
    porcentaje_mujeres = df_mujeres[VAR_TOTAL] / total * 100
    porcentaje_varones = df_varones[VAR_TOTAL] / total * 100    
    
    nombres_variables=["Mujeres", "Varones"]
    
    for i, (var, nombre) in enumerate(zip([df_mujeres[VAR_TOTAL], df_varones[VAR_TOTAL]], nombres_variables)):
        fig.data[i].text = [nombre] * len(var)
        fig.update_traces(textposition='none')
        fig.data[i].customdata =  [porcentaje_mujeres, porcentaje_varones][i] #se establecen los porcentajes que luego salen en las etiquetas emergentes
    
    #Armar el texto de las etiquetas emergentes
    fig.update_traces(hovertemplate='Residentes %{text}<br>Año del censo: %{x}<br>Cantidad de residentes:  %{y:.0f}<br>Porcentaje del total: %{customdata:.2f}%<extra></extra>')
    
    fig.update_layout(yaxis=dict(tickformat=',',ticksuffix='k'))
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=16, family=letra, color='black'), tickfont=dict(family=letra, color='black', size=11))
    fig.update_yaxes( title_text = "Cantidad de residentes", title_font=dict(size=16, family=letra, color='black'), tickfont=dict(family=letra, color='black', size=11))
    fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y

    colors = [color_empleo_1, color_empleo_2]  # Colores personalizados para cada categoría
    for i, data in enumerate(fig.data):
        data.marker.color = colors[i]
        data.name = nombres_variables[i]

    fig.update_traces(marker=dict(line=dict(width=0), )) # Eliminar el borde de las barras
    # Ajustar el espaciado entre las barras para dar la apariencia de redondez
    fig.update_layout(bargap=0.2)
    
    # Actualizar el diseño del gráfico
    fig.update_layout(
        title={
        "text": f"<b>{graph_title}</b>",
        "x": 0.5,
        "y": 0.95,
        "xanchor": "center",
        "yanchor": "top",
        "font": {
            "size": 20,
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


 