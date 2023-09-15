from dash import html

import dash_bootstrap_components as dbc

IndicadoresCenso = dbc.Container(
    [  
        html.H5(html.Strong("Indicadores del Censo"), className="text-white pt-3 space-grotesk"),
        html.P([
            """Los indicadores del Censo agropecuario nos permiten una visión estructural y a 
            la vez detallada de la actividad agropecuaria en nuestro país. Contrastando los datos de las distintas ediciones 
            podemos identificar tendencias, comprender patrones y dar cuenta de relaciones causales que se sostienen o se modifican a 
            lo largo del tiempo. La información del Censo nos permite enmarcar de forma sistémica el modelo agrícolo-ganadero, y 
            así problematizar la conexión entre la concentración de tierras, el decrecimiento del empleo rural y distintas características 
            del modo de producción imperante con los impactos de los agroquímicos en la salud humana y de los territorios. Entenderlas como 
            partes más o menos conectados (partes interrelacionadas de un mismo sistema o no), otorgando una visión multidimensional 
            necesaria a la hora de pensar la mitigación de los impactos o postular las posibilidades alternativas del uso del suelo y la 
            producción"""
        ]),
        html.Br(),
        html.I("""*No ignoramos que los resultados de los Censos agropecuarios en ocasiones pueden no ser un reflejo idéntico de la realidad. 
               De todas formas son el único dato oficial y por tanto son el mejor acercamiento a una comprensión integral de las tendencias y 
               modificaciones estructurales en la producción agropecuaria.""")
    ], 
    className=" text-white mt-5")


MetodologiaCenso = dbc.Container([
      html.H5([html.Strong("METODOLOGÍA & PRODUCTO"), html.Span("V1.0",className='badge bg-primary text-black mx-3')], className="text-white pt-3 space-grotesk"),
      html.H6(html.H6(html.I('En la V1 del producto, se han implementado función 1, 2, 3 para enriquecer la experiencia. Estas funcionalidades incluyen:'), style={'line-height': '2'}, className="text-white")),
      html.Ul([
        html.Li(html.I("Función 1: Permite usuarios compartir contenido desde la aplicación, facilitando difusión de información")),
        html.Li(html.I("Función 2: Agrega asistente de organización personalizado que sugiere horarios y recordatorios.")),
        html.Li(html.I("Función 3: Algoritmo de recomendación basado en preferencias y análisis semántico para sugerencias relevantes.")),
        html.Li(html.I("Función 4: Suite de herramientas colaborativas para trabajo en equipo remoto."))
            ]),
        html.I([
            """Las fuentes de datos utilizadas provienen de fuente no oficiales encontrados en diversos portales. 
               Puede consultar las fuentes utilizadas """,
               html.A("aquí.", href="https://www.indec.gob.ar/", target='blank'),
               """ Si posee otras fuentes para verificar o refutar, alentamos contacto. 
               Reconocemos valor de verificación en búsqueda de información confiable."""
      ])],
    id="metodologia-censo",
    className=" text-white mt-5"
)