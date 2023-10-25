from dash import html
import dash_bootstrap_components as dbc

Explicacion = dbc.Row(
        dbc.Col([
            html.P(
                "Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, "
                "pero como toda selección de criterios esta puede ser arbitraria. El objetivo del mismo no es dar "
                "cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, "
                "sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. "
                "Esta herramienta fue pensada para: redactar nuevas ordenanzas, mejorar las ordenanzas existentes y estudiar "
                "el marco legal en cada distrito.",
                style={"text-align": "justify"}
            ),
            html.P("Podes descargar el data set completo AQUÍ.."),                    
        ], md=12, class_name="text-white mt-5 my-5")
    )


Metodologia = dbc.Row(dbc.Col([
        html.H5([html.Strong("METODOLOGÍA & PRODUCTO"), html.Span("V1.0",className='badge bg-primary text-black mx-3')], className="text-white pt-3 space-grotesk"),
        html.P("En la Argentina los municipios poseen (o no) ordenanzas que regulan y zonifican el uso de productos agroquímicos en sus territorios, Normativa Comparada es una sistematización de todas las normativas de promoción a la agroecologia y de regulación de agroquímicos."),
        html.P("Para el comparativo de normativas se establecieron cinco dimensiones analíticas: Transparencia , Poblaciones , Escuelas Rurales , Agua y Apiarios."),
        html.P("No todas las ordenanzas poseen todos los puntos, ni responden a las mismas realidades territoriales, por lo que se analiza cada dimensión de manera diferenciada. Las dimensiones analíticas permiten ordenar las ordenanzas municipales de mayor a menor y viceversa, pero como toda selección de criterios esta puede ser arbitraria. El objetivo del mismo no es dar cuenta en términos absolutos de que una ordenanza efectivamente protege mejor su territorio que otra, sino ser una herramienta de fácil uso para analizar los distintos niveles de protección ambiental existentes. Esta herramienta fue pensada para: "),
        html.Ul([
            html.Li("Inspirar a los municipios que no tienen ordenanza"),
            html.Li("Mejorar las ordenanzas vigentes"),
            html.Li("Estudiar el marco legal en cada distrito. Esta información fue relevada de manera colectivo, participativa y abierta. Si encontraste algún error o información desactualizada comunícate a contacto."),
        ]),
        html.P("También se puede acceder al texto de cada una de las ordenanzas y al dataset utilizado para la construcción de la herramienta")
    ],
    id="metodologia-ranking",
    className=" text-white mt-5"
))