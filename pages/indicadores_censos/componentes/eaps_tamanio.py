from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash
import plotly.graph_objects as go
import plotly.express as px
#from tools.componentes import NoHayDatos, Alert

from pages.indicadores_censos.data_censo.base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO

##### VARIABLES ######

VAR_EAPS_PEQ = 'EAPS pequeñas (<= 500ha)'
VAR_EAPS_GRANDES = 'EAPS grandes (>500 ha)'
VAR_TOTAL_EAPS = 'Total EAPS'


# colores
color_territorial = '#6E5FA8'
color_estatal = '#BDBDBD'

# Titulos
graph_title =  'Cantidad de EAPS según tamaño'

# BASE DE DATOS
df_base = base_censos.copy()

###### GRAFICO  #####   
Q_EAPs_tamanio = dbc.Card(
            [  
                dbc.CardHeader(graph_title),
                dbc.CardBody(
                    Hash(dbc.Row(
                        [
                        dbc.Col(dcc.Graph(id="q-eaps-tamanio"), md=12),
                        ]
                    ),
                    size=24,
                    color="#6e5fa8",
                    )
                    
                )
            ],
            color="light", 
            class_name="shadow",
            outline=True,
            id="censo-q-eaps-tamanio"
    )

#                        dbc.Col("",id = 'texto-q-eaps-tamanio',md=12)


@callback(
    Output("q-eaps-tamanio", "figure"), 
    [
        Input("select-partido", "value"),
        Input("select-periodo", "value")
    ]
)

def update_bar_chart(partidos, periodos):

    sel_partido = [c for c in partidos if c != '']
    sel_periodo = [c for c in periodos if c != '']

    df = base_censos.copy()
    
    if len(sel_partido) >0:
        mask = df[VAR_PARTIDO].isin(sel_partido)
        df = df[mask]
    if len(sel_periodo) >0:
        mask = df[VAR_ANIO_CENSO].isin(sel_periodo)
        df = df[mask]

#    if len(df) == 0:
#        return NoHayDatos['linea']

    #fig = go.Figure()

    fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_TOTAL_EAPS, height=400)
    
    # fig = px.bar(df, x=VAR_ANIO_CENSO, y=VAR_TOTAL_EAPS,
    #          hover_data=['lifeExp', 'gdpPercap'], color='country',
    #          labels={'pop':'population of Canada'}, height=400)

    
    
    # total_2021=sum(df[var_fem][df[VAR_ANIO_CENSO]==2021])
    # fig.add_trace(go.Bar(x=df[VAR_PARTIDO][df[VAR_ANIO_CENSO]==2021],y=df[var_fem][df[VAR_ANIO_CENSO]==2021],text=df[var_fem][df[VAR_ANIO_CENSO]==2021 ].apply(lambda x:  str(round(x/total_2021*100,1))+"%"),name='Año 2021', marker_color='indianred'))
    
    # total_2022=sum(df[var_fem][df[VAR_ANIO_CENSO]==2022])
    # fig.add_trace(go.Bar(x=df[VAR_PARTIDO][df[VAR_ANIO_CENSO]==2022], y=df[var_fem][df[VAR_ANIO_CENSO]==2022], text=df[var_fem][df[VAR_ANIO_CENSO]==2022].apply(lambda x: str(round(x/total_2022*100,1))+"%"), name='Año 2022', marker_color='rgba(113,90,134,1)'))

    # total_2023=sum(df[var_fem][df[VAR_ANIO_CENSO]==2023])
    # fig.add_trace(go.Bar(x=df[VAR_PARTIDO][df[VAR_ANIO_CENSO]==2023], y=df[var_fem][df[VAR_ANIO_CENSO]==2023], text=df[var_fem][df[VAR_ANIO_CENSO]==2023].apply(lambda x: str(round(x/total_2023*100,1))+"%"), name='Año 2023', marker_color='#40BD72'))    
    
    # fig.update_layout(barmode='group',plot_bgcolor='rgba(0,0,0,0)', xaxis_tickangle=-45,  hovermode="x")
    # fig.update_xaxes( title_text = 'partidoES', title_font=dict(size=16, family='Verdana', color='black'), tickfont=dict(family='Calibri', color='black', size=12))
    # fig.update_yaxes(title_text = "FEMICIDIOS",  title_font=dict(size=16,family='Verdana',color='black'), tickfont=dict(family='Calibri', color='black', size=12))

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