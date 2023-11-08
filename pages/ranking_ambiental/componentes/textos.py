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
        html.P('En la Argentina los municipios poseen (o no) ordenanzas que egulan el uso de agroquímicos y/o promociones la agroecología en sus territorios. "Ranking" es una sistematización de todas las normativas de regulación de agroquímicos y de promoción a la agroecologia.'),
        html.P('Para facilitar el analisis normativo se establecieron 6 dimensiones: Transparencia, Poblaciones, Escuelas Rurales, Agua, Apiarios y agroecologia. No todos los municipios legislan todos los puntos, ni responden a las mismas realidades territoriales, por lo que se analiza cada dimensión de manera diferenciada. Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, pero como toda selección de criterios esta puede ser arbitraria.'),
        html.P('El objetivo del mismo no es dar cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. Esta herramienta fue pensada para: '),
        html.Ul([
            html.Li('Inspirar a los municipios que no tienen ordenanza'),
            html.Li('Mejorar las ordenanzas vigentes'),
            html.Li('Entender el marco legal en cada distrito'),
        ]),
        html.P('Esta información fue relevada de manera colectiva, participativa y abierta.'),
        html.P('Si encontraste algún error o información desactualizada comunícate a contacto. También se puede acceder al texto de cada una de las ordenanzas haciendo click sobre el numero de la misma, dentro de la tabla. Priorizamos links a repositorios oficiales. En el caso de no existir se linkea al texto de la ordenanza alojado en servidores propios. El dataset utilizado para la construcción de la herramienta es de libre acceso, podes encontrarlo acá.'),
    ],
    id="metodologia-ranking",
    className=" text-white mt-5"
))