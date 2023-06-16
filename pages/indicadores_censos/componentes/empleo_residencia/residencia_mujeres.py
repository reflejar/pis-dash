from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle
from .modal_empleo import modal_empleo


#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.residencia import base_mujeres, VAR_ANIO_CENSO, VAR_PARTIDO, VAR_TOTAL,VAR_ULTIMO_ANIO_CENSO, VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002, VAR_SEXO_NACIMIENTO

##### VARIABLES ######


color_empleo_1 = '#EF7418'

# Titulos
graph_title =  'Mujeres residentes del campo'

# BASE DE DATOS
df_base_original = base_mujeres.copy()



###### GRAFICO  #####  
 
residencia_mujeres =dbc.Container(
            [
                dbc.Card(
                            [  
                                dbc.CardBody(
                                    Hash(dbc.Row(
                                        [
                                        dbc.Col(dcc.Graph(id="grafico-residentes-mujeres"), md=12),
                                        ]
                                    ),
                                    size=24,
                                    color=color_empleo_1,
                                    )
                                    
                                ),
                                dbc.CardFooter(
                                    dbc.Button("Ampliar", id="open-modal-button-residentes-mujeres", color="warning",style={"background-color": '#EF7418', "border-color": "#DEDE7C"}),
                                ),
                            ],
                            color="light", 
                            class_name="shadow",
                            outline=True,
                            id="censo-residentes-mujeres"
                    ),
                    modal_empleo,
    ],
    className="contenedor-residentes-mujeres",
    
)                

@callback(
        Output("grafico-residentes-mujeres", "figure"),
        Input("select-partido", "value"),
)

def update_bar_chart(partidos):

    df = df_base_original.copy()
    
    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_TOTAL)
    fig.update_traces(marker_color=color_empleo_1)  # Modificar el color de las barras
    fig.update_layout(title={"text": graph_title,"font": {"size": 20, "color": "black", "family": "Arial"}}, showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_layout(yaxis=dict(tickformat=',',ticksuffix='k'))
    fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_yaxes( title_text = "Mujeres residentes", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))

    return fig


texto_residentes_mujeres = html.H6(id="texto-residentes-mujeres" , style={'font-size': '20px'}, className="text-white")



@callback(
     Output("texto-residentes-mujeres", "children"), 
     [
         Input("select-partido", "value"),
     ]
 )


def update_epas_pequenias_text(partidos):
    df = df_base_original.copy()
    
    var_cantidad_2018=  (df[df[VAR_ANIO_CENSO]==VAR_ULTIMO_ANIO_CENSO][VAR_TOTAL][5]- df[df[VAR_ANIO_CENSO]==VAR_ANIO_CENSO_2002][VAR_TOTAL][3])*(-1)
    var_porcentual=int((var_cantidad_2018/df[df[VAR_ANIO_CENSO]==VAR_ANIO_CENSO_2002][VAR_TOTAL][3]) *100)*(-1)
    

    mensaje = f"""Entre el año 2002 y el año 2018 se dió una expulsión masiva de {var_cantidad_2018} residentes mujeres del campo, lo que significa una disminución del {var_porcentual}%. Es fácil observar cómo viene disminuyendo la cantidad de residentes mujeres en el campo en los últimos 30 años. La expulsión masiva de residentes es una consecuencia de las pérdidas de EAPS y una mayor concentración de tierras en pocas personas y empresas."""

    return mensaje  