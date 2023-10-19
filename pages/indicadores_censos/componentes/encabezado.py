from dash import html
import dash_bootstrap_components as dbc

Encabezado = dbc.Row(dbc.Col([      
                    html.H4([html.Strong('Censo Nacional Agropecuario'), html.A("V 1.0", href="#metodologia-censo", className="btn btn-sm text-primary")], className="text-white pt-3 space-grotesk"),
                    html.Br(),
                    html.H6("""Visualizaciones y análisis de los principales indicadores de los últimos tres Censos Agropecuarios sistematizados por municipio. 
                            Información histórica con perspectiva local. Entre el 1988 y el 2018, en la Provincia de Buenos Aires:  """, className="text-white poppins"),                       
                    html.H6([
                        html.Ul(
                            [
                            html.Li([f"Las EAP se redujeron a la mitad"], style={'line-height': '1.5'}),
                            html.Li([f"La superficie promedio de las EAP aumentó en un 78%"], style={'line-height': '1.5'}),
                            html.Li([f"Más de la mitad de la población rural fue expulsada de su residencia"], style={'line-height': '1.5'}),
                            html.Li([f"Hubo una caída de más del 70% del empleo rural" ], style={'line-height': '1.5'}),
                            ])], className="text-white"),
                ],
                className="text-white mt-5", md=12
            )
        )