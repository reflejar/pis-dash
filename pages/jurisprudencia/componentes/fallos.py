from dash import dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from ..data import DATA

Fallos = dbc.Row(dbc.Col(html.Div(id='fallos-judiciales'), class_name="mt-5"))

@callback(
        Output('fallos-judiciales','children'),
        [
            Input("select-voces-tematicas",'value'),
            Input("select-provincia",'value'),
            Input("select-tipo-fallo",'value'),
            Input("select-organismo",'value')
        ]
)
def update_fallos(voces, provincia, tipo, organismo):
    df = DATA['contenido'].copy()
    cards = []

    if voces:
        df = df[df['Voces temáticas']==voces]
    if provincia:
        df = df[df['Provincia']==provincia]
    if tipo:
        df = df[df['Tipo de fallo']==tipo]
    if organismo:
        df = df[df['Organismo judicial o administrativo']==organismo]        

    for _, row in df.iterrows():
        cards.append(dbc.Card(dbc.CardBody(
            html.Div([
                html.Div([
                    html.Span([html.B('AÑO: '), f"{row['Año']}"], className="mx-3"),
                    html.Span([html.B('PROVINCIA: '), f"{row['Provincia']}"], className="mx-3"),
                    html.Span([html.B('CIUDAD: '), f"{row['Ciudad']}"], className="mx-3"),
                ], className="text-end"),
                html.Hr(),
                html.P([html.B("VOCES TEMÁTICAS: "), row['Voces temáticas']]),
                html.P([html.B("JURISDICCIÓN TERRITORIAL: "), row['Jurisdicción territorial']]),
                html.P([html.B("ORGANISMO: "), row['Organismo judicial o administrativo']]),
                html.P([html.B("AUTOS: "), row['Autos']]),
                html.Hr(),
                html.P([html.B("TIPO DE FALLO: "), row['Tipo de fallo']]),
                html.P([html.B("SÍNTESIS DE FALLO: "), html.U(f"Página: {row['Página']}")]),
                html.P(row['Sintesis del fallo']),
                html.A("Ver fallo completo", className="btn btn-primary text-dark")
            ], className="poppins small mx-2")
        ), className="mt-4"))
            
    return cards