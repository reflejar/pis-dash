from dash import html

import dash_bootstrap_components as dbc

FooterNormativo = dbc.Container(
    [
        html.H4("Detalle de las distancias protegidas según la ordenanza citada", className="text-white"),
        dbc.Table([
            html.Thead(
                html.Tr([
                    html.Th("Bienes Protegidos"), html.Th("Zona de Aplicación Aérea") , html.Th("Zona de Exclusión"), html.Th("Zona de Amortiguamiento"),
                ],
                className="text-primary border-primary")
            , className="bg-black"),
            html.Tbody([
                html.Tr([html.Td("Zonas urbanas"), html.Td("2000 m"), html.Td("150 m"), html.Td("500 m")], className="text-white"),
                html.Tr([html.Td("Población Rural"), html.Td("300 m"), html.Td("50 m"), html.Td("500 m")], className="text-white"),
                html.Tr([html.Td("Escuelas Rurales"), html.Td("300 m"), html.Td("200 m"), html.Td("500 m")], className="text-white"),
                html.Tr([html.Td("Cursos de agua"), html.Td("0 m"), html.Td("25 m"), html.Td("0 m")], className="text-white"),
                html.Tr([html.Td("Superficies de agua"), html.Td("0 m"), html.Td("25 m"), html.Td("0 m")], className="text-white"),
                html.Tr([html.Td("Estaciones de bombeo*"), html.Td("0 m"), html.Td("50 m"), html.Td("0 m")], className="text-white"),                
                ], className="bg-black bg-opacity-75 border-white"
                )
        ],  bordered=True),
        html.I([
            "*Las estaciones de bombeo contemplan tambien las camaras de inspeccion de agua abastecimiento público."
        ]),
        html.Br(),  
        html.Br(),      
        html.H4("Zona de Exclusión Aérea:", className="text-white"),
        html.P([
            "Se prohíbe la pulverización aérea de agroquímicos desde la distancia establecida al bien protegido."
        ]),
        html.Br(),
        html.H4("Zona de Exclusión:", className="text-white"),
        html.P([
            "Área en la que se prohíbe la aplicación de agroquímicos de cualquier forma."
        ]),
        html.Br(),
        html.H4("Zona de Amortiguamiento:", className="text-white"),
        html.P([
            """Área en la que solo está permitida la aplicación de agroquímicos bajo estrictas pautas. Estas son: que los vientos sean mayores a 5
 kilómetros por hora y menores a 15 kilómetros por hora. Además estos siempre deben ser provenientes desde la zona resguardada
 hacia zona rural. Por otra parte la humedad relativa debe ser mayor al 50%. Y la temperatura no mayor a 25°C."""
        ]),
        html.Br(),
        html.H4("Sobre Escuelas Rurales:", className="text-white"),
        html.P([
            """En tanto bien protegido en su cuidado se aplican las pautas generales de las zonas de amortiguamiento. Pero además la normativa 
            comprende las siguientes exigencias:""",
            html.Ul([
                html.Li("Es obligatorio el aviso directo al director del establecimiento previo a la aplicación"),
                html.Li("Es obligatoria la presencia de un profesional habilitado al momento de la pulverización"),
                html.Li("Estas solo pueden realizarse o a contra horario escolar, es decir sin niños en los establecimientos"),
                html.Li("La persona titular de dominio del sector rural deberá generar barreras forestales necesarias para que resguarden a la escuela.")
            ])
        ]),
        html.Br(),
        html.H4("Registro de Aplicadores y Equipos Terrestres:", className="text-white"),
        html.P([
            html.Ul([
                html.Li("Todas las personas físicas y jurídicas que hagan aplicaciones a nombre propio o de terceros deberán estar inscriptos en el registro municipal"),
                html.Li("Todos los equipos de aplicación deberán estar registrados y ehibir la identificación alfanumérica en el frente ambos laterales y en la parte posterior de cada equipo con material reflectivo y en un tamaño no inferiores a 20 cm  12cm"),
            ])
        ]),
        html.Br(),
        html.H4("Control Médico:", className="text-white"),
        html.P([
            html.Ul([
                html.Li("Titular de dominio del sector rural deberá generar barreras forestales cuando su propiedad rural linde con zonas urbanas y/o establecimientos educativos a fin de lograr una defensa de protección natural permanente."),
            ])
        ]),
        html.Br(),
        html.H4("Barreras Forestales:", className="text-white"),
        html.P([
            "Titular de dominio del sector rural deberá generar barreras forestales cuando su propiedad rural linde con zonas urbanas y/o establecimientos educativos a fin de lograr una defensa de protección natural permanente."
        ]),
        html.Br(),
        html.H4("Ordenanza:", className="text-white"),
        html.A("Aquí", href="https://drive.google.com/file/d/1SVmW-3-_LIpqGGVsO2Ud4o3vmxoja5mo/view", target="_blank"),
        html.Br(),
        html.Br(),
        html.H4("Canal de Denuncias:", className="text-white"),
        html.P([
            "+54 9 2265 41-8289"
        ]),
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
    className=" text-white mt-5"
)




