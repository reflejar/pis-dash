from dash import html

import dash_bootstrap_components as dbc

FooterNormativo = dbc.Row(dbc.Col(
    [
        html.H4(html.Strong("Detalle de las distancias protegidas según la ordenanza citada"), className="text-white"),
        dbc.Table([
            html.Thead(
                html.Tr([
                    html.Th("Bienes Protegidos"), html.Th("Zona de Exclusión Aérea") , html.Th("Zona de Exclusión"), html.Th("Zona de Amortiguamiento"),
                ],
                className="text-primary border-primary")
            , className="bg-black"),
            html.Tbody([
                html.Tr([html.Td("Zonas Urbanas"), html.Td("2000 m"), html.Td("150 m"), html.Td("500 m")], className="text-white"),
                html.Tr([html.Td("Población Rural"), html.Td("300 m"), html.Td("50 m"), html.Td("500 m")], className="text-white"),
                html.Tr([html.Td("Escuelas Rurales"), html.Td("300 m"), html.Td("200 m"), html.Td("500 m")], className="text-white"),
                html.Tr([html.Td("Cursos de Agua"), html.Td("0 m"), html.Td("25 m"), html.Td("0 m")], className="text-white"),
                html.Tr([html.Td("Superficies de Agua"), html.Td("0 m"), html.Td("25 m"), html.Td("0 m")], className="text-white"),
                html.Tr([html.Td("Bombas de Agua*"), html.Td("0 m"), html.Td("50 m"), html.Td("0 m")], className="text-white"),                
                ], className="bg-black bg-opacity-75 border-white"
                )
        ],  bordered=True, responsive=True),
        html.I([
            "*Las estaciones de bombeo contemplan también las cámaras de inspección de agua y abastecimiento público."
        ]),
        html.Br(),  
        html.Br(),      
        html.H4(html.Strong("EXCLUSIÓN AÉREA:"), className="text-white"),
        html.P([
            "La regulación provincial prohíbe operar (pulverizaciones aéreas) en los primeros 2000 metros desde el limite de las áreas urbanas en toda la Provincia de Buenos Aires. La ordenanza municipal de Mar Chiquita respeta el presupuesto mínimo provincial de 2000 metros para zonas urbanas, además protege escuelas y poblados rurales donde se prohíbe la pulverización aérea de agroquímicos desde los primeros 300 metros.", html.Br(), "*(Normado en el Articulo N°38 del Decreto de Reglamentación N°499/91 de la Ley Provincial N°10699/88)"
        ]),
        html.Br(),
        html.H4(html.Strong("ZONA DE EXCLUSIÓN:"), className="text-white"),
        html.P([
            "Área en la que se prohíbe la aplicación de agroquímicos de cualquier forma."
        ]),
        html.Br(),
        html.H4(html.Strong("ZONA DE AMORTIGUAMIENTO:"), className="text-white"),
        html.P([
            """Área en la que sólo está permitida la aplicación de agroquímicos bajo estrictas pautas. Estas son:"""
        ]),
        html.Ul([
                html.Li("Vientos mayores a 5 kilómetros por hora y menores a 15 kilómetros por hora."),
                html.Li("Los vientos siempre deben ser provenientes desde la zona resguardada hacia la zona rural."),
                html.Li("Humedad relativa mayor al 50%."),
                html.Li("Temperatura no mayor a 25°C."),
                html.Li("Sólo se permiten agroquímicos banda verde y/o azul  (clase toxicológica IV, SENASA)."),
                html.Li("Las aplicaciones sólo podrán hacer aplicaciones con receta agronómica válida y presencia  de un profesional habilitado.")
            ]),
        html.Br(),
        html.H4(html.Strong("SOBRE ESCUELAS RURALES:"), className="text-white"),
        html.P([
            """Se aplican todas las pautas de zonas de exclusión y amortiguamiento establecidas en la ordenanza a nivel general, y 
            en particular en la cercanía de escuelas rurales también se suman las siguientes exigencias:""",
            html.Ul([
                html.Li("Es obligatorio el aviso directo al director del establecimiento previo a la aplicación (pasando el mouse sobre cada escuela se muestra el whatsapp del director/a y el email oficial de la escuela)."),
                html.Li("Es obligatoria la presencia de un profesional habilitado al momento de la pulverización."),
                html.Li("Estas sólo pueden realizarse a contra horario escolar, es decir sin niños en los establecimientos."),
                html.Li("La persona titular de dominio del sector rural deberá generar barreras forestales necesarias para que resguarden a la escuela.")
            ])
        ]),
        html.Br(),
        html.H4(html.Strong("REGISTROS DE APLICADORES Y EQUIPOS TERRESTRES:"), className="text-white"),
        html.P([
            html.Ul([
                html.Li("Todas las personas físicas y jurídicas que hagan aplicaciones a nombre propio o de terceros deberán estar inscriptos en el registro municipal."),
                html.Li("Todos los equipos de aplicación deberán estar registrados y exhibir la identificación alfanumérica en el frente ambos laterales y en la parte posterior de cada equipo con material reflectivo y en un tamaño no inferior a 20 cm x 12 cm."),
            ])
        ]),
        html.Br(),
        html.H4(html.Strong("REGISTROS DE APLICADORES Y EQUIPOS TERRESTRES:"), className="text-white"),
        html.P([
            html.Ul([
                html.Li("Todas las personas físicas y jurídicas que hagan aplicaciones a nombre propio o de terceros deberán estar inscriptos en el registro municipal."),
                html.Li("Todos los equipos de aplicación deberán estar registrados y exhibir la identificación alfanumérica en el frente ambos laterales y en la parte posterior de cada equipo con material reflectivo y en un tamaño no inferior a 20 cm x 12 cm."),
            ])
        ]),
        html.Br(),        
        html.H4(html.Strong("JURISPRUDENCIA MUNICIPAL:"), className="text-white"),
        html.P([
            "ORGANISMO: Juzgado Civil y Comercial Nº 4. Departamento Judicial de Mar del Plata. Provincia de Buenos Aires.", html.Br(),
            "AUTOS: Corrado Souto Guillermo Cristian y otros c/ Agropecuaria SA y otros s/ Acción Preventivo Daños.", html.Br(),
            "Síntesis del fallo: Se interpone ante la justicia provincial una acción preventiva de daño por un grupo de vecinos y vecinas solicitando protección de las fumigaciones/pulverizaciones con agrotóxicos respecto a las viviendas, escuelas y cursos de agua.- En razón de que los cursos de agua derivan al Mar Argentino (recurso interjurisdiccional), el juez se declara incompetente por considerar que el caso corresponde que sea tramitado ante la justicia federal. No obstante hace lugar a la cautelares solicitadas:", html.Br()
        ]),
        html.P([
            html.Ol([
                html.Li("Prohibición de fumigar a menos de 1.500 mts de zonas pobladas, escuelas rurales, núcleos de viviendas habitadas, cursos de agua tales como arroyos lagunas y mar argentino, postas sanitarias, centros asistenciales, villas recreativas y deportivas."),
                html.Li("Requerir a las demandadas informen si poseen plantas de almacenamiento, tratamiento y/o disposición final de agroquímicos determinando su ubicación y en su caso justificando su habilitación municipal e inscripción en el Registro Provincial de Generadores y Operadores de Residuos Especiales con la totalidad de la información exigible;"),
                html.Li("Ordenar a las demandadas y/o a las empresas que se dediquen a la aplicación terrestre de agroquímicos con fines comerciales se abstengan de circular con los equipos de aplicación terrestre por centros poblados y en caso de extrema necesidad, hacerlo sin carga, limpios y sin picos pulverizadores;"),
                html.Li("Ordenar a las demandadas que se realice el procedimiento obligatorio para reducir los residuos fitosanitarios en los envases vacíos y para el lavado de envases rígidos de plaguicidas miscibles o dispersables en agua y"),
                html.Li("Requerir a las demandadas que presenten: estudio de impacto ambiental por la actividad desarrollada, póliza de Seguro Ambiental Obligatorio e inscripciones obligatorias en registros de generadores de residuos especiales y productores agropecuarios."),
            ])
        ]),
        html.Br(),
        html.H4(html.Strong("BARRERAS FORESTALES:"), className="text-white"),
        html.P([
            html.Ul([
            html.Li("El titular de dominio del sector rural deberá generar barreras forestales cuando su propiedad rural linde con zonas urbanas y/o establecimientos educativos a fin de lograr una defensa de protección natural permanente.")
            ])
        ]),
        html.Br(),
        html.H4(html.Strong("CANAL DE DENUNCIAS"), className="text-white"),
        html.P("Etchemendy Alejandro (Director de Higiene y Bromatología)"),
        html.P([ html.B('Whatsapp:') ,"+54 9 2235 69-6563"]),
        html.Br(),
        html.H4(html.Strong("ORDENANZA:"), className="text-white"),
        html.A("Link a ordenanza", href="https://drive.google.com/file/d/1SVmW-3-_LIpqGGVsO2Ud4o3vmxoja5mo/view", target="_blank"),
        html.Br(),
        html.Br(),
        
        html.Br(),
        html.I([
            "**Este mapa integra información de diversidad de fuentes: ",
        html.A("Datos abiertos de escuelas de la Provincia de Buenos Aires", href="https://catalogo.datos.gba.gob.ar/dataset/establecimientos-educativos/archivo/3951210e-7e0e-4fed-bbf1-0183e704c9ae", target="_blank"),  
            """, la georreferenciación de cursos de agua, parajes rurales y poblados urbanos a 
            partir de imágenes satelitales, """,
        html.A("información poblacional", href="https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos-6", target="_blank"),
            """ proveniente del INDEC, en suma a un conjunto de correcciones y precisiones 
            reportadas desde el territorio. Las distancias de protección utilizadas (zonas de exclusión/amortiguamiento) 
            se obtienen del texto original de cada """,
        html.A("ordenanza municipal.", href="https://drive.google.com/file/d/1SVmW-3-_LIpqGGVsO2Ud4o3vmxoja5mo/view", target="_blank")
        ]),

    ],
    id="footer-normativo",
    className="text-white mt-5"
))





Metodologia = dbc.Row(dbc.Col([
        html.H5([html.Strong("METODOLOGÍA"), html.Span("V1.0",className='badge bg-primary text-black mx-3')], className="text-white pt-3 space-grotesk"),
        html.P(html.I("""
        Las normativas de regulación de agroquímicos a nivel local protegen distintos bienes delimitando zonas en las que se prohíbe 
        la aplicación de agroquímicos (zonas de exclusión) o se requieren cuidados específicos para hacer aplicaciones (zonas de 
        amortiguamiento). El Mapa de Zonificación Normativa es una herramienta que permite por medio de información geográfica (GIS) 
        visualizar las restricciones de aplicación de agroquímicos de cada municipio. Esta herramienta está pensada para que:       
        """)),
        html.Ul([
            html.Li(html.I("Gobiernos tenga un mejor instrumento de control")),
            html.Li(html.I("Productores sepan en qué lotes deben adecuar sus manejos")),
            html.Li(html.I("Comunidades puedan controlar el cumplimiento")),
        ]),
        html.P(html.I("""
        A falta de un mapa oficial esta herramienta GIS integra información de diversas fuentes: 
        escuelas de la Provincia de Buenos Aires (Datos Abiertos PBA) la georreferenciación de cursos de agua (Datos Abiertos PBA), 
        parajes rurales y poblados urbanos a partir de imágenes satelitales (OpenStreetMap y ArcGIS) , información poblacional (INDEC), 
        contactos de las escuelas rurales (Datos Abiertos PBA y relevamiento propio) en suma a un conjunto de correcciones y precisiones 
        reportadas desde el territorio. Las distancias de protección utilizadas (zonas de exclusión/amortiguamiento) se obtienen del 
        texto original de cada ordenanza municipal.     
        """)),
        html.H5(html.Strong("PRODUCTO"),className="text-white pt-3 space-grotesk" ),
        html.P(html.I("""La versión 1.0 sólo mapea Mar Chiquita. Ya estamos trabajando en una versión mejorada para Mar Chiquita 
                      (que incluya la exclusión aérea, las zonificación de parajes rurales y las zonas protegidas por amparo judicial) 
                      y en versiones que incorporen a otros municipios.""")),
        html.P(html.I(['*Este proyecto posee un enfoque colectivo, participativo y abierto. Si encontraste algún error o información desactualizada comunícate a ', html.A("contacto@democraciaenred.org",href="mailto:contacto@democraciaenred.org")])),
        html.P(html.I(['Acede al data set de esta herramienta ', html.A("acá", href="https://docs.google.com/spreadsheets/d/12XSBKP4HuxNt0YmsBfmm_j_3vbJUfSLN/edit#gid=1355391810", target="_blank")])),
    ],
    id="metodologia-normativa",
    className=" text-white mt-5"
))


 


