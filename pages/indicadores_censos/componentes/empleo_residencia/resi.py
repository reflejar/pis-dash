# from dash import html, dcc, Input, Output, callback
# import dash_bootstrap_components as dbc
# from dash_loading_spinners import Hash
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import pickle
# from .modal_empleo import modal_empleo


# #from tools.componentes import NoHayDatos, Alert

# from pages.indicadores_censos.data_censo.residencia import base_varones, VAR_ANIO_CENSO, VAR_PARTIDO, VAR_TOTAL,VAR_ULTIMO_ANIO_CENSO, VAR_ANIO_CENSO_1988, VAR_ANIO_CENSO_2002, VAR_SEXO_NACIMIENTO

# ##### VARIABLES ######


# color_empleo_1 = 'rgb(225, 134, 95)'

# # Titulos
# graph_title =  'Varones residentes del campo'

# # BASE DE DATOS
# df_base_original = base_varones.copy()



# ###### GRAFICO  #####  
 
# residencia_varones =dbc.Container(
#             [
#                 dbc.Card(
#                             [  
#                                 dbc.CardBody(
#                                     Hash(dbc.Row(
#                                         [
#                                         dbc.Col(dcc.Graph(id="grafico-residentes-varones"), md=12),
#                                         ]
#                                     ),
#                                     size=24,
#                                     color=color_empleo_1,
#                                     )
                                    
#                                 ),
#                                 dbc.CardFooter(
#                                     dbc.Button("Ampliar", id="open-modal-button-residentes-varones", color="warning",style={"background-color": color_empleo_1, "border-color": "#DEDE7C"}),
#                                 ),
#                             ],
#                             color="light", 
#                             class_name="shadow",
#                             outline=True,
#                             id="censo-residentes-varones"
#                     ),
#                     modal_empleo,
#     ],
#     className="contenedor-residentes-varones",
    
# )                

# @callback(
#         Output("grafico-residentes-varones", "figure"),
#         Input("select-partido", "value"),
# )

# def update_bar_chart(partidos):

#     df = df_base_original.copy()
    
#     fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_TOTAL)
#     fig.update_traces(marker_color=color_empleo_1)  # Modificar el color de las barras
#     fig.update_layout(title={"text": graph_title,"font": {"size": 20, "color": "black", "family": "Arial"}}, showlegend=False, plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
#     fig.update_layout(yaxis=dict(tickformat=',',ticksuffix='k'))
#     fig.update_xaxes( title_text = "Año del censo", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))
#     fig.update_yaxes( title_text = "Varones residentes", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))

#     return fig


# texto_residentes_varones = html.H6(id="texto-residentes-varones" , style={'font-size': '20px'}, className="text-white")



# @callback(
#      Output("texto-residentes-varones", "children"), 
#      [
#          Input("select-partido", "value"),
#      ]
#  )


# def update_epas_pequenias_text(partidos):
#     df = df_base_original.copy()
    
#     # var_cantidad_2018= int( df[df[VAR_ANIO_CENSO]==VAR_ULTIMO_ANIO_CENSO][VAR_TOTAL]- df[df[VAR_ANIO_CENSO]==VAR_ANIO_CENSO_2002][VAR_TOTAL])
#     # var_porcentual=(var_cantidad_2018/df[df[VAR_ANIO_CENSO]==VAR_ANIO_CENSO_2002][VAR_TOTAL]) *100
    

#     mensaje = f"""Para el año 2018,  en la Provincia de Buenos Aires ...."""

#     return mensaje  