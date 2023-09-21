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
        html.P([
            """Las visualizaciones y los análisis aquí comprendidos tienen como """,
             html.A("fuente", href="https://docs.google.com/spreadsheets/d/1UdK8i1dcfgTkCAIg-tWHSZVoNEDUhGkO-D1d5opgrEo/edit#gid=157269157", target="_blank"),
            """ los principales indicadores de los últimos tres 
            censos agropecuarios (1998, 2002 y 2018), los datos se encuentran procesados a nivel municipal para poder ver los indicadores 
            tanto a nivel provincial como local."""
        ]),
        html.Br(),
        html.I(["""*Este proyecto posee un enfoque colectivo, participativo y abierto. Si encontraste algún error o información desactualizada 
               comunícate a contacto. También se puede acceder al """,
               html.A("dataset", href="https://docs.google.com/spreadsheets/d/1zY0iOwGfm5hIg7eYTm1EAQBamPN7mzLm-9U1PxjwiNg/edit?usp=sharing", target="_blank"),
                " utilizado para la construcción de la herramienta."])
        ],
    id="metodologia-censo",
    className=" text-white mt-5"
)