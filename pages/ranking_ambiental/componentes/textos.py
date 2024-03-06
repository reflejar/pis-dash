from dash import html
import dash_bootstrap_components as dbc

# Explicacion = dbc.Row(
#         dbc.Col([
#             html.P(
#                 "Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, "
#                 "pero como toda selección de criterios esta puede ser arbitraria. El objetivo del mismo no es dar "
#                 "cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, "
#                 "sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. "
#                 "Esta herramienta fue pensada para: redactar nuevas ordenanzas, mejorar las ordenanzas existentes y estudiar "
#                 "el marco legal en cada distrito.",
#                 style={"text-align": "justify"}
#             ),
#             html.P("Podes descargar el data set completo AQUÍ.."),                    
#         ], md=12, class_name="text-white mt-5 my-5")
#     )


Metodologia = dbc.Row(dbc.Col([
        html.H5([html.Strong("METODOLOGÍA & PRODUCTO"), html.Span("V1.0",className='badge bg-primary text-black mx-3')], className="text-white pt-3 space-grotesk"),
        html.P('En la Argentina los municipios poseen (o no) ordenanzas que regulan el uso de agroquímicos y/o la promoción de la agroecología en sus territorios. "Ranking" es una sistematización de todas las normativas de regulación de agroquímicos y de promoción a la agroecología.'),
        html.P('Para facilitar el análisis normativo se establecieron 6 dimensiones: Transparencia, Poblaciones, Escuelas Rurales, Agua, Apiarios y Agroecología. No todos los municipios legislan todos los puntos, ni responden a las mismas realidades territoriales, por lo que se analiza cada dimensión de manera diferenciada. Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, pero como toda selección de criterios esta puede ser arbitraria.'),
        html.P('El objetivo del mismo no es dar cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. Esta herramienta fue pensada para: '),
        html.Ul([
            html.Li('Inspirar a los municipios que no tienen ordenanza'),
            html.Li('Mejorar las ordenanzas vigentes'),
            html.Li('Entender el marco legal en cada distrito'),
        ]),
        html.P('Esta información fue relevada de manera colectiva, participativa y abierta.'),
        html.P('Aclaración I: En la dimensión de poblaciones la exclusión aérea de zonas urbanas se encuentra también afectada por normativa provincial (Decreto de Reglamentación N°499/91 de la Ley Provincial N°10699/88). Por lo tanto esta columna indica la exclusión aérea de las ordenanzas municipales, y en los casos en que esta es menor a lo estipulado por la normativa provincial se indica en color rojo los 2000 metros del presupuesto mínimo provincial vigente con la aclaración debajo de lo que dicta la normativa municipal.'),
        html.P('Aclaración II: En diferentes casos existen amparos, medidas cautelares u otros fallos judiciales que dictan medidas de protección en territorios parciales o totales de los distintos municipios.Estos lineamientos no se tienen en cuenta para la confección de la base de RANKING, ya que el fin último de estas es la comparación de las ordenanzas municipales en la regulación de agroquímicosSi encontraste algún error o información desactualizada comunícate a contacto. También se puede acceder al texto de cada una de las ordenanzas haciendo click sobre el número de la misma, dentro de la tabla. Priorizamos links a repositorios oficiales. En el caso de no existir se linkea al texto de la ordenanza alojado en servidores propios. El dataset utilizado para la construcción de la herramienta es de libre acceso, podes encontrarlo acá.'),
        html.P('*Puntaje - Nota metodológica resumida: Para el cálculo del puntaje se otorga 1 punto por cada metro de exclusión y 0.5 por cada metro de amortiguamiento. Mientras que la obligatoriedad de notificación tiene un efecto multiplicador de x2 en el puntaje previo cada municipio. En el caso de las prohibiciones totales a las pulverizaciones aéreas se imputan en esos municipios 10.000 puntos en el indicador de la dimensión de “Poblaciones” y 5000 puntos para el de “Escuelas Rurales” y “Agua”. Las dimensiones con variables categóricas, “Transparencia” y “Agroecología”, suman 1 punto por afirmativo y 0 por cada negativo (excepto la participación en RENAMA que otorga 5 puntos en la dimensión de Agroecología). Todos los indicadores fueron normalizados, utilizando una fórmula de estandarización entre máximos y mínimos, para que los puntajes se expresen en valores entre 0 y 1'),
        html.P(['Si queres saber más en detalle por la construcción de los indicadores comunícate a ', html.A("contacto@democraciaenred.org",href="mailto:contacto@democraciaenred.org")]),
        html.P(html.I(['*Este proyecto posee un enfoque colectivo, participativo y abierto. Si encontraste algún error o información desactualizada comunícate a ', html.A("contacto@democraciaenred.org",href="mailto:contacto@democraciaenred.org")])),
        html.P(html.I(['Acede al data set de esta herramienta ', html.A("acá", href="https://docs.google.com/spreadsheets/d/1BeoqHejaV44T_LfF-OJNnFQninCThHwUkR_j5bnZB8U/edit#gid=0", target="_blank")])),
    ],
    id="metodologia-ranking",
    className=" text-white mt-5"
))