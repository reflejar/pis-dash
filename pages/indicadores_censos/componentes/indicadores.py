import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback, State, no_update
from dash_loading_spinners import Hash
import plotly.express as px
import textwrap


from .formatos import *
from .concentracion_tierra.modal_tierra import modal_tierra
from ..data.base_indicadores import VAR_ANIO_CENSO, VAR_PARTIDO

class Indicador:
    """
        Clase para crear los diferentes indicadores
    """

    LETRA_DEFAULT = "Arial"

    def __init__(
        self,
        df, 
        id_indicador="", 
        colores=[], 
        titulo_grafico="" ,
        y="", 
        y_titulo="",
        x="",
        x_titulo="",

    ) -> None:
        self.id = id_indicador
        self.df = df 
        self.colores = colores
        self.titulo_grafico = titulo_grafico
        self.y_var = y
        self.y_titulo = y_titulo or y
        self.x_var = x
        self.x_titulo = x_titulo or x

    def inicializar(self):
        """
            Esto es para la carga inicial. Lo que va fuera del callback
        """
        return dbc.Container([
            dbc.Card(
                [
                    dbc.CardBody(
                        Hash(dbc.Row(
                            [
                            dbc.Col(dcc.Graph(id=self.id), md=12),                
                            ]
                        ),
                        size=24,
                        color=self.colores[0],
                        )
                        
                    ),
                    dbc.CardFooter(
                        dbc.Button("AMPLIAR GRÁFICO", 
                                    id=f"open-modal-{self.id}", 
                                    style={
                                        "background-color": self.colores[0], 
                                        "border-color": "#FFFFFF", 
                                        "color": "#FFFFFF", 
                                        "font-family": self.LETRA_DEFAULT
                                        }
                                    ), 
                                    className="text-center", 
                                    style={"background-color": "light","border": "none", "color": "light"}),
                    
                ],
                color="light", 
                class_name="shadow",    
                outline=True,
                id=f"tarjeta-{self.id}"
            ),
            modal_tierra,
        ],
        className=f"contenedor-{self.id}",
        
    )
        

    def update(self, partidos):
        """
            Esto va para el callback
        """
        if VAR_ANIO_CENSO in self.df.columns:
            self.df[VAR_ANIO_CENSO] = self.df[VAR_ANIO_CENSO].astype(int).astype(str)
        
        sel_partido = [c for c in partidos if c != '']
        
        if len(sel_partido) >0:
            mask = self.df[VAR_PARTIDO]==partidos
            self.df = self.df[mask]
        

        self.df = self.df.groupby(by = [VAR_ANIO_CENSO, VAR_PARTIDO])[self.y_var].sum().reset_index()

        fig = px.bar(self.df, x=self.x_var, y=self.y_var, color_discrete_sequence=[self.colores[0]], text=self.y_var)
        fig.update_xaxes( title_text = self.x_var, title_font=dict(size=tamanio_fuente, family=letra, color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
        fig.update_yaxes(title_text = self.y_var,  title_font=dict(size=tamanio_fuente,family=letra,color=color_letra), tickfont=dict(family=letra, color=color_letra, size=tamanio_fuente_tick))
        fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
        
        #Armar el texto de las etiquetas emergentes
        fig.update_traces(hovertemplate='hoverrrrrr falta hacer')
    
    
        # Actualizar el diseño del gráfico
        fig.update_layout(
            title={
            "text": f"<b>{'<br>'.join(textwrap.wrap(self.titulo_grafico, width=25))}</b>",
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