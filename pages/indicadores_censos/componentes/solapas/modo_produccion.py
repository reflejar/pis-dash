from dash import dash, html, dcc, Input, State, Output, callback
import dash_bootstrap_components as dbc
# from .tipo_cultivo_ha import CULTIVOS_HA
from ..formatos import COLOR_VERDE, COLOR_MARRON, COLOR_NARANJA

from ..indicadores import Indicador
from ...data import df_ha_tipo_cultivo

indicadores = [
    Indicador(
        id_indicador="ha-tipo-cultivo",
        df=df_ha_tipo_cultivo,
        tipo_grafico="area",
        titulo_grafico="Héctareas implantadas según tipo de cultivo" ,
        x="Año del censo",
        y='Cantidad HA',
        z='Tipo de cultivo',
        colores=[COLOR_VERDE, COLOR_MARRON, COLOR_NARANJA ],
        hover='Cantidad de Hectareas cultivadas: %{y}<br>Año del censo: %{x}'
    ),      
]


Produccion = html.Div([
            dbc.Row([
                html.H6('Modo de producción', style={'font-size': '25px', 'color': COLOR_VERDE}),
                html.P("""En esta sección se muestra.....Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """, className="text-white"),
                ]),
            dbc.Row([dbc.Col(i.inicializar(), sm=12, md=6, xl=4) for i in indicadores], class_name="mt-5"),    
        ], className="mt-5")         



for i in range(len(indicadores)):
    id_indicador = indicadores[i].id
    @callback(
        Output(id_indicador, "figure"),
        Input("select-partido", "value"),
    )
    def update_graph(selected_value, i=i):
        return indicadores[i].actualizar(selected_value)
    
    @callback(
        [
            Output(f"modal-{id_indicador}", "is_open"),
            Output(f"modal-graph-{id_indicador}", "figure"),
            Output(f"modal-open-{id_indicador}", "n_clicks"),
        ],
        [
            Input(f"modal-open-{id_indicador}", 'n_clicks'),
            Input(f"modal-close-{id_indicador}", "n_clicks"),
        ],
        [
            State(f"modal-{id_indicador}", "is_open"),
            State(f"{id_indicador}", "figure")
        ]
    )
    def toggle_modal(open_modal, close_modal, is_open_modal, figure, i=i):
        if is_open_modal:
            return False, dash.no_update, 0
        if open_modal:
            return True, figure, 1
        return is_open_modal, dash.no_update,0
