from dash import html

import dash_bootstrap_components as dbc

FooterNormativo = dbc.Container(
    [
        html.H4("Detalle de las distancias protegidas según la ordenanza citada", className="text-white"),
        dbc.Table([
            html.Thead(
                html.Tr([
                    html.Th("BIENES PROTEGIDOS"), html.Th("EXCLUSIÓN AÉREA") , html.Th("ZONA DE EXCLUSIÓN"), html.Th("ZONA DE AMORTIGUAMIENTO"),
                ],
                className="text-white")
            , className="bg-secondary"),
            html.Tbody([
                html.Tr([html.Td("Zonas urbanas"), html.Td("2000 m"), html.Td("1000 Mts"), html.Td("500 Mts")], className="text-dark"),
                html.Tr([html.Td("Población Rural"), html.Td("2000 m"), html.Td("1000 Mts"), html.Td("500 Mts")], className="text-dark"),
                html.Tr([html.Td("Escuelas Rurales"), html.Td("300 m"), html.Td("200 Mts"), html.Td("100 Mts")], className="text-dark"),
                html.Tr([html.Td("Estaciones de bombeo*"), html.Td("0 m"), html.Td("50 Mts"), html.Td("100 Mts")], className="text-dark"),
                html.Tr([html.Td("Superficies de agua"), html.Td("0 m"), html.Td("50 Mts"), html.Td("50 Mts")], className="text-dark"), 
                ], className="bg-white bg-opacity-75"
                )
        ],  bordered=True),
        html.I([
            "*Las estaciones de bombeo contemplan tambien las camaras de inspeccion de agua abastecimiento público."
        ]),
        html.Br(),  
        html.Br(),      
        html.H4("EXCLUSIÓN AÉREA:", className="text-white"),
        html.P([
            "Se prohíbe la pulverización aérea de agroquímicos desde la distancia establecida al bien protegido."
        ]),
        html.Br(),
        html.H4("ZONA DE EXCLUSIÓN:", className="text-white"),
        html.P([
            "Área en la que se prohíbe la aplicación de agroquímicos de cualquier forma."
        ]),
        html.Br(),
        html.H4("ZONA DE AMORTIGUAMIENTO:", className="text-white"),
        html.P([
            """Área en la que solo está permitida la aplicación de agroquímicos bajo estrictas pautas. Estas son: que los vientos sean mayores a 5
 kilómetros por hora y menores a 15 kilómetros por hora. Además estos siempre deben ser provenientes desde la zona resguardada
 hacia zona rural. Por otra parte la humedad relativa debe ser mayor al 50%. Y la temperatura no mayor a 25°C."""
        ]),
        html.Br(),
        html.H4("SOBRE ESCUELAS RURALES:", className="text-white"),
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
        html.H4("REGISTRO DE APLICADORES Y EQUIPOS TERRESTRES:", className="text-white"),
        html.P([
            html.Ul([
                html.Li("Todas las personas físicas y jurídicas que hagan aplicaciones a nombre propio o de terceros deberán estar inscriptos en el registro municipal"),
                html.Li("Todos los equipos de aplicación deberán estar registrados y ehibir la identificación alfanumérica en el frente ambos laterales y en la parte posterior de cada equipo con material reflectivo y en un tamaño no inferiores a 20 cm  12cm"),
            ])
        ]),
        html.Br(),
        html.H4("CONTROL MÉDICO:", className="text-white"),
        html.P([
            html.Ul([
                html.Li("Titular de dominio del sector rural deberá generar barreras forestales cuando su propiedad rural linde con zonas urbanas y/o establecimientos educativos a fin de lograr una defensa de protección natural permanente."),
            ])
        ]),
        html.Br(),
        html.H4("BARRERAS FORESTALES:", className="text-white"),
        html.P([
            "Titular de dominio del sector rural deberá generar barreras forestales cuando su propiedad rural linde con zonas urbanas y/o establecimientos educativos a fin de lograr una defensa de protección natural permanente."
        ]),
        html.Br(),
        html.H4("ORDENANZA:", className="text-white"),
        html.P([
            "FALTA LINK, NO FUNCIONA"
        ]),
        html.Br(),
        html.H4("CANAL DE DENUNCIAS:", className="text-white"),
        html.P([
            "+54 9 2265 41-8289"
        ]),
        html.Br(),
        html.I([
            """*Los datos mostrados en este mapa se obtuvieron de esta fuente, y las distancias de protección utilizadas
(zonas de exclusión) se obtuvieron de la siguiente fuente."""
        ]),

    ],
    id="footer-normativo",
    className=" text-white mt-5"
)




