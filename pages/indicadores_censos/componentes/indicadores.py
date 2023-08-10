import dash_bootstrap_components as dbc
from dash import dcc, html
from dash_loading_spinners import Hash
import plotly.express as px
import textwrap


from .formatos import *
from ..data import VAR_ANIO_CENSO, VAR_PARTIDO, VAR_EAPS_Q, VAR_TAMANIO_EAPS

class Indicador:
    """
        Clase para crear los diferentes indicadores
    """

    LETRA_DEFAULT = "Arial"
    LETRA_COLOR = 'black'
    TAMANIO_FUENTE = 16

    def __init__(
        self,
        df, 
        id_indicador="", 
        colores=[], 
        tipo_grafico="bar",
        titulo_grafico="" ,
        y="", 
        y_titulo="",
        x="",
        x_titulo="",
        z="",
        hover="",
        porcentaje=False,

    ) -> None:
        self.id = id_indicador
        self.df = df 
        self.colores = colores
        self.tipo_grafico = tipo_grafico
        self.titulo_grafico = titulo_grafico
        self.y_var = y
        self.y_titulo = y_titulo or y
        self.x_var = x
        self.x_titulo = x_titulo or x
        self.z_var = z
        self.hover = hover
        self.porcentaje = porcentaje

    def inicializar(self):
        """
            Esto es para la carga inicial. Lo que va fuera del callback
        """
        return html.Div([
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
                                    id=f"modal-open-{self.id}", 
                                    style={
                                        "background-color": 'rgb(150, 79, 71)', 
                                        "border-color": "#FFFFFF", 
                                        "color": "#FFFFFF", 
                                        "font-family": self.LETRA_DEFAULT
                                        }
                                    ), 
                                    className="text-center", 
                                    style={"background-color": "light","border": "none", "color": "light"}),
                    
                ],
                color="light", 
                class_name="shadow mb-5",    
                outline=True,
                id=f"tarjeta-{self.id}"
            ),
            dbc.Modal(
                    [
                        
                        dbc.ModalBody(
                            dcc.Graph(id=f"modal-graph-{self.id}"),
                        ),
                        dbc.ModalFooter(
                            dbc.Button("CERRAR GRÁFICO", 
                                        id=f"modal-close-{self.id}", 
                                        color="light",style={"background-color": COLOR_NARANJA, "border-color": "#FFFFFF", "color": "#FFFFFF", "font-family": "Arial"},  
                                        className="mx-auto"), className="text-center", style={"background-color": "none","border": "none", "color": "none"}
                        ),
                    ],
                    id=f"modal-{self.id}",
                    size="lg",
                    is_open=False,
                )
        ])

    def bar(self):
        return px.bar(
            self.df, 
            x=self.x_var, 
            y=self.y_var, 
            color_discrete_sequence=[self.colores[0]], 
            text=self.y_var
        )

    def histogram(self):
        return px.histogram(
            self.df, 
            x=self.x_var, 
            y=self.y_var, 
            color=self.z_var, 
            # color='Tamaño EAPs',
            barnorm='percent' if self.porcentaje else None,  
            text_auto=True, 
            color_discrete_sequence=self.colores            
        )
        
    def area(self):
        return px.area(
            self.df, 
            x=self.x_var, 
            y=self.y_var, 
            color=self.z_var,  
            color_discrete_sequence=self.colores
        )

    def actualizar(self, partidos):
        """
            Esto va para el callback
        """
        if VAR_ANIO_CENSO in self.df.columns:
            self.df[VAR_ANIO_CENSO] = self.df[VAR_ANIO_CENSO].astype(int).astype(str)

        if VAR_EAPS_Q in self.df.columns:
            self.df[VAR_EAPS_Q]= round(self.df[VAR_EAPS_Q],2)
        
        sel_partido = [c for c in partidos if c != '']
        
        if len(sel_partido) >0:
            mask = self.df[VAR_PARTIDO]==partidos
            self.df = self.df[mask]
        
        gruposs = [self.x_var, VAR_PARTIDO]
        if self.z_var:
            gruposs.append(self.z_var)

        self.df = self.df.groupby(by = gruposs)[self.y_var].sum().reset_index()
        
        fig = getattr(self, self.tipo_grafico)()
        fig.update_xaxes( title_text = self.x_titulo, title_font=dict(size=self.TAMANIO_FUENTE, family=self.LETRA_DEFAULT, color=self.LETRA_COLOR), tickfont=dict(family=self.LETRA_DEFAULT, color=self.LETRA_COLOR, size=11))
        fig.update_yaxes(title_text = self.y_titulo,  title_font=dict(size=self.TAMANIO_FUENTE,family=self.LETRA_DEFAULT,color=self.LETRA_COLOR), tickfont=dict(family=self.LETRA_DEFAULT, color=self.LETRA_COLOR, size=11))
        fig.update_layout(yaxis=dict(tickformat='.0f',ticksuffix='')) #se le saca la K a los números del eje de las y
        
        #Armar el texto de las etiquetas emergentes
        fig.update_traces(hovertemplate=self.hover)
    
    
        # Actualizar el diseño del gráfico
        fig.update_layout(
            title={
            "text": f"<b>{'<br>'.join(textwrap.wrap(self.titulo_grafico, width=35))}</b>",
            "x": 0.5,
            "y": 0.95,
            "xanchor": "center",
            "yanchor": "top",
            "font": {
                "size": 17,
                "color": "black",
                "family": self.LETRA_DEFAULT
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