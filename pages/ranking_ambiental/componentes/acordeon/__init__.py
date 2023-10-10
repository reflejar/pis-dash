from dash import html,Input, Output, callback, State
import dash_bootstrap_components as dbc
from dash import Dash
import dash_mantine_components as dmc
from ..escuelas.tabla_escuelas import tabla_escuelas
from pages.constantes import *


# table_header = [
#     html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name"), html.Th("Last Name") ,html.Th("Last Name") ,html.Th("Last Name")]))
# ]

# row1 = html.Tr([html.Td("Arthur"), html.Td("Dent"), html.Td("Dent"), html.Td("Dent"), html.Td("Dent")])
# row2 = html.Tr([html.Td("Ford"), html.Td("Prefect"), html.Td("Prefect"), html.Td("Prefect"), html.Td("Prefect")])
# row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox"), html.Td("Beeblebrox"), html.Td("Beeblebrox"), html.Td("Beeblebrox")])
# row4 = html.Tr([html.Td("Trillian"), html.Td("Astra"), html.Td("Astra"), html.Td("Astra"), html.Td("Astra")])

# table_body = [html.Tbody([row1, row2, row3, row4])]

# tabla_escuelas = dbc.Table(table_header + table_body, bordered=True, responsive=True, class_name="dt-responsive nowrap", style={"border-collapse": "collapse", "border-spacing": 0, "width": 100%})


AcordeonRanking = dmc.Accordion([
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Escuelas", style={"backgroundColor": ROJO,}, className="text-center"),
                                dmc.AccordionPanel(
                                    tabla_escuelas
                                ),
                                
                            ],
                            value="escuelas",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Transparencia", style={"backgroundColor": NARANJA,}, className="text-center"),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="transparencia",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Agua", style={"backgroundColor": VERDE_AGUA,}, className="text-center"),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="agua",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Poblaciones", style={"backgroundColor": LIMA,}, className="text-center"),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="poblaciones",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Apiarios", style={"backgroundColor": LILA,}, className="text-center"),
                                dmc.AccordionPanel(
                                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                                ),
                            ],
                            value="apiarios",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Agroecología", style={"backgroundColor": CELESTE,}, className="text-center"),
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



