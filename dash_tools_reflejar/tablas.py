from dash import dash_table


class Tabla:
    """
        Clase para crear las diferentes tablas
    """

    def __init__(
            self,
            df,
            id_tabla="", 
    ) -> None:
        self.id = id_tabla
        self.df = df.copy()

    def inicializar(self):
        return dash_table.DataTable(
            data=self.df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in self.df.columns],
            style_as_list_view=True,
            style_table={
                'overflowX': 'scroll',
                'overflowY': 'scroll',
                'width': '100%',
                'borderCollapse': 'separate',
                'borderSpacing': '0 10px',
            },
            style_cell={'whiteSpace': 'pre',
                        'fontFamily': 'Arial',
                        'textAlign':'center',
                        'maxWidth': '300px'
                        },
            style_header={
                'backgroundColor': "#F2A4B6",
                'color': 'rgb(76,30,39)',
                'textAlign':'center',
            },
            style_header_conditional=[
                {'if': {'column_id': c}, 'fontWeight': 'bold'}
                for c in self.df.columns[:3]  # Primeros dos encabezados en negritas
            ],
            style_cell_conditional=[
                {'if': {'column_id': c},  'textAlign':'left'}
                for c in self.df.columns[:3]  # Primeros dos encabezados en negritas
            ],
        
            id=f"tabla-{self.id}",
            sort_action='native',
    )
