from dash import html

import dash_bootstrap_components as dbc

Metodologia = dbc.Row(dbc.Col([
    html.H5([html.Strong("METODOLOGÍA & PRODUCTO"), html.Span("V1.0",className='badge bg-primary text-black mx-3')], className="text-white pt-3 space-grotesk"),
    html.P('La herramienta recopila y sistematiza: Fallos judiciales, Resoluciones administrativas, Dictámenes, Recomendaciones de la defensoría del pueblo y Relatorías de la ONU, entre otras, sobre el uso de agroquímicos en Argentina'),
    html.P('Jurisprudencia tiene como fuente la recopilación realizada por Fernando Cabaleiro (Naturaleza en Derechos) en “Praxis Jurídica sobre el uso de Agrotóxicos en la Argentina”, por lo que su información llega hasta Abril de 2022'),
    html.P('Esta herramienta recopila la información proveniente de la investigación y la sistematiza para permitir que se acceda a una síntesis del caso de interés siguiendo criterios de búsqueda deseados. Para que luego si lo desea acceda a la fuente original. Los criterios por los que se agrupó para facilitar la búsqueda son:  A) Año, B) Provincia, C) Ciudad, D) Voces temáticas, E) Autos, F) Organismo judicial o administrativo, G) Jurisdicción territorial y H) Tipo de fallo.'),
    html.P([
        'Cita:',
        html.Br(),
        '[“Praxis Jurídica sobre el uso de Agrotóxicos en la Argentina”.  Recopilación de fallos judiciales, resoluciones administrativas, dictámenes y recomendaciones de las Defensorías del Pueblo y Relatorías Especiales y Comités de DD.HH de la ONU. Cabaleiro, Fernando. 5º Edición. 16 de Abril de 2022. Naturaleza de Derechos. 1637 páginas.]',
        html.Br(),
        'Conoce sobre la fuente en: https://naturaleza.ar/contenido/164/praxis-juridica-sobre-los-agrotoxicos-fernando-cabaleiro'
    ]),
    html.P('*Este proyecto posee un enfoque colectivo, participativo y abierto. Si encontraste algún error o información desactualizada comunícate a contacto. También se puede acceder al dataset utilizado para la construcción de la herramienta.')
    ],
    id="metodologia-jurisprudencia",
    className=" text-white mt-5"
))