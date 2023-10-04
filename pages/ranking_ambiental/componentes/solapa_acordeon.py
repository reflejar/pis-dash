from dash import html,Input, Output, callback, State
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


AcordeonRanking = dmc.Accordion([
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Escuelas", style={"color":"#000000" , 'font-size': '18px','font-weight': 'bold',"backgroundColor": color_escuelas,  "text-align": "center"}),
                                dmc.AccordionPanel(
                                    tabla_escuelas
                                ),
                                
                            ],
                            value="escuelas",
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
                    value="",  
                    className="bg-white accordion-item accordion-chevron",
                    id="accordion-tabla",             
                )
    
# @callback (
#         [
#         Output('tabs-ranking','active_tab'), 
#         ],
#         Input('accordion-tabla','value'),
#         State('tabs-ranking','active_tab' )
# )
# def prender_mapas(value, active_tab): 
#     if value!=active_tab:
#         return value
#     else: 
#         return active_tab


