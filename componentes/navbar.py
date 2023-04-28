from dash import html, Input, Output, callback, State
import dash_bootstrap_components as dbc


PIS_ISOLOGOTIPO = "/assets/img/PIS_isologo_negro.png"


Navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                html.Img(src=PIS_ISOLOGOTIPO, height="80px"),
                href="/",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav([
                        dbc.NavItem(html.A("Proyecto", className="text-white text-uppercase navitem-decoration mx-3", href="/#index-proyecto"), class_name="text-end"),
                        dbc.NavItem(html.A("Testeos", className="text-white text-uppercase navitem-decoration mx-3", href="/#index-testeando"), class_name="text-end"),
                        dbc.NavItem(html.A("Herramientas", className="text-white text-uppercase navitem-decoration mx-3", href="/#index-herramientas"), class_name="text-end"),
                        dbc.NavItem(html.A("FAQS", className="text-white text-uppercase navitem-decoration mx-3", href="/#index-faqs"), class_name="text-end"),
                        dbc.NavItem(html.A("Donar", className="text-white text-uppercase navitem-decoration mx-3", href="/#index-donar"), class_name="text-end"),
                        # dbc.NavItem(dbc.NavLink(dbc.Button("Donar", size="sm", class_name="bg-grey border-grey"), active="exact", class_name="text-white mx-3", href="/donar")),
                    ],
                    className="ms-auto",
                    navbar=True,
                    pills=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
        className=""
    ),
    
    fixed="top",
    className="text-white",
    id="navbar"
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

callback(
    Output(f"navbar-collapse", "is_open"),
    [Input(f"navbar-toggler", "n_clicks")],
    [State(f"navbar-collapse", "is_open")],
)(toggle_navbar_collapse)

