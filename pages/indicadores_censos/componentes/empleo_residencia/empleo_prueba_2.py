from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO

##### VARIABLES ######

VAR_EAPS_PEQ = 'EAPS pequeñas (<= 500ha)'
VAR_EAPS_GRANDES = 'EAPS grandes (>500 ha)'
VAR_TOTAL_EAPS = 'Total EAPS'

VAR_EAPS_Q = 'Cantidad de EAPs'
VAR_TAMANIO_EAPS = 'Tamaño EAPs'


color_empleo_residencia = '#EF7418'
color_concentracion_tierra_2 = '#DEDE7C'


# Titulos
graph_title =  'Cantidad de EAPS según tamaño'

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
EMPLEO_PRUEBA_2 = dbc.Card(
            [  
                #dbc.CardHeader(graph_title),
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="q-empleo-prueba-2"), md=12),
                        ]
                    ),
                    size=24,
                    color=color_empleo_residencia,
                    )
                    
                )
            ],
            color="light", 
            class_name="shadow",
            outline=True,
            id="empleo_prueba_2"
    )

@callback(
    Output("q-empleo-prueba-2", "figure"), 
    [
        Input("select-partido", "value"),
        Input("select-periodo", "value")
    ]
)

def update_bar_chart(partidos, periodos):

    sel_partido = [c for c in partidos if c != '']
    sel_periodo = [c for c in periodos if c != '']

    df = df_base.copy()
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO].isin(sel_partido)
        df = df[mask]
    if len(sel_periodo) >0:
        mask = df[VAR_ANIO_CENSO].isin(sel_periodo)
        df = df[mask]

#    if len(df) == 0:
#        return NoHayDatos['linea']

    df = df.groupby(by = [VAR_ANIO_CENSO, VAR_TAMANIO_EAPS])[VAR_EAPS_Q].sum().reset_index()

    fig = px.histogram(df, x=VAR_ANIO_CENSO, y=VAR_EAPS_Q, color=VAR_TAMANIO_EAPS, barnorm='percent', text_auto=True, color_discrete_sequence=[color_empleo_residencia, color_concentracion_tierra_2 ])
    fig.update_layout(barmode='stack', plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x", legend=dict(title='Tamaño',orientation="h", xanchor='center'))
    fig.update_xaxes( title_text = "", title_font=dict(size=12, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=10))
    fig.update_yaxes(title_text = "Distribución de EAPs según tamaño",  title_font=dict(size=12,family='Verdana',color='black'), tickfont=dict(family='Calibri', color='black', size=10))

    return fig


# @callback(
#     Output("texto-por-partido", "children"), 
#     [
#         Input("select-partidoes", "value"),
#         Input("select-periodo", "value")
#     ]
# )
# # def update_por_partido_text(partidoes, periodos):
    sel_partido = [c for c in partidoes if c != '']
    sel_periodos = [c for c in periodos if c != '']

    df = df_territorial.copy().reset_index()

    if len(sel_partido) >0:

        #CALCULO
        mask = df[VAR_PARTIDO].isin(sel_partido)
        df = df[mask]


    if len(sel_periodos) >0:
        mask = df[VAR_ANIO_CENSO].isin(sel_periodos)
        df = df[mask]

    if len(df) == 0:
        return NoHayDatos['alert']

    cantidad_fem_mes = df[var_fem].sum()
    participacion= df.groupby(by = VAR_PARTIDO)[var_fem].sum().reset_index()
    participacion['PARTICIPACIÓN'] = (participacion[var_fem]/cantidad_fem_mes)*100
    max_part = participacion['PARTICIPACIÓN'].max()
    partido_max_part = participacion[participacion['PARTICIPACIÓN']==max_part][VAR_PARTIDO].astype(str).unique().tolist()
    max_part = round(max_part, 1)
    max_partido_text = agregar_y_list(sel_partido, partido_max_part)

    partido_list = sel_partido if len(sel_partido)>0 else ['América Latina y el Caribe']
    partido_text = agregar_y_list(sel_partido, partido_list)

    anos = df.copy()
    anos_list = anos[VAR_ANIO_CENSO].astype(str).unique().tolist()
    anos_text = agregar_y_list(sel_periodos, anos_list)

    ano_en_curso = [c for c in anos_list if c == str(ano_corriente)]
    anos_enteros = [c for c in anos_list if c != str(ano_corriente)]

    
    mensaje = Alert([
        html.P(f'Durante {anos_text} en {partido_text} se registraron {cantidad_fem_mes} feminicidios, el {max_part}% de ellos sucedieron en {max_partido_text}.', style={'font-size': '20px'}),       
    ])


    return mensaje  