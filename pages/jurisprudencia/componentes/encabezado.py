from dash import html
import dash_bootstrap_components as dbc

Encabezado = dbc.Row(dbc.Col([      
                    html.H3(['Jurisprudencia', html.A("V 1.0", href="#metodologia-jurisprudencia", className="btn btn-sm text-primary")], className="text-white pt-3 fw-bolder space-grotesk"),
                    html.Br(),
                    html.H6("""
                        Compendio jurídico sobre el uso de agroquímicos en la Argentina. 
                        Podrás encontrar fallos judiciales, resoluciones, administrativas, dictámenes y más. 
                        Buscá por palabras clave o aplica filtros para encontrar el caso que sea de tu interés
                    """, className="text-white poppins"),                       
                ],
                className="text-white mt-5", md=12
            )
        )