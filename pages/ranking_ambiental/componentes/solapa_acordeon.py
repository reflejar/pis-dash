from dash import html,Input, Output, callback
import dash_bootstrap_components as dbc
from dash import Dash
import dash_mantine_components as dmc
from .escuelas.tabla_escuelas import tabla_escuelas



color_transparencia = '#FF865F'
color_escuelas = '#EF7286'
color_agua = '#6FBFB5'
color_poblaciones = '#D8D87C'
color_apiarios = '#C3A4E7'
color_agroecologia= '#9AD5FF'

# AcordeonRanking = html.Div([
#     dbc.Row([
#         dbc.Accordion([
#             dbc.AccordionItem(title="ESCUELAS", className="mb-0"),
#             dbc.AccordionItem(title="TRANSPARENCIAS", className="mb-0"),
#             dbc.AccordionItem(title="AGUA", className="mb-0"),
#             dbc.AccordionItem(title="POBLACIONES", className="mb-0"),
#             dbc.AccordionItem(title="APIARIOS", className="mb-0"),
#             dbc.AccordionItem(title="AGROECOLOGÍA", className="mb-0"),
#         ],
#         className="accordion-horizontal",  # Agregar una clase de estilo personalizada
#         flush=True, # Eliminar bordes de los elementos del acordeóN
#         ),  
#     ], style={'borderBottom': '0px', 'width': '100%'})
# ])

AcordeonRanking = html.Div([
        dbc.Row([
                dmc.Accordion(
                    value="accordion_ranking",
                    children=[
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Escuelas", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_escuelas,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    dbc.Col([html.Div(tabla_escuelas)], md=12)
                                ),
                                
                            ],id="accordion_escuelas",
                            value="on",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Transparencia", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_transparencia,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="transparencia",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Agua", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_agua,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="agua",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Poblaciones", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_poblaciones,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="poblaciones",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Apiarios", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_apiarios,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="apiarios",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Agroecología", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_agroecologia,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="agroecologia",
                        ),
                        
                    ],
                    styles={
                        "root": {
                            "backgroundColor": dmc.theme.DEFAULT_COLORS["gray"][0],
                            "borderRadius": 5,
                        },
                        "item": {
                            "backgroundColor":  dmc.theme.DEFAULT_COLORS["gray"][0],
                            "border": "1px solid transparent",
                            "position": "relative",
                            "zIndex": 0,
                            "transition": "transform 150ms ease",
                            "&[data-active]": {
                                "transform": "scale(1.03)",
                                "backgroundColor": "white",
                                "boxShadow": 5,
                                "borderColor":  dmc.theme.DEFAULT_COLORS["gray"][0],
                                "borderRadius": 5,
                                "zIndex": 1,
                            },
                        },
                        "chevron": {
                            "&[data-rotate]": {
                                "transform": "rotate(-90deg)",
                            },
                        },
                    },
                )
    ], style={'borderBottom': '0px', 'width': '100%'})
])


