import pandas as pd
from dash import dash_table, html


class Tabla:
    """
        Clase para crear las diferentes tablas
    """

    def __init__(
            self,
            id_tabla="", 
            df=pd.DataFrame(),
    ) -> None:
        self.id = id_tabla
        self.df = df.copy()
        self.columns = self.df.columns


    def inicializar(self):
        return dash_table.DataTable(
            id=self.id,
            data=self.df.to_dict('records'),
            columns=[{"name": i, "id": i, "presentation": 'markdown'} for i in self.columns],
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
                'backgroundColor': "#eceeef",
                'textAlign':'center',
            },
            style_header_conditional=[
                {'if': {'column_id': c}, 'fontWeight': 'bold'}
                for c in self.columns[:3]  # Primeros dos encabezados en negritas
            ],
            style_cell_conditional=[
                {'if': {'column_id': c},  'textAlign':'left'}
                for c in self.columns[:3]  # Primeros dos encabezados en negritas
            ],
            sort_action='native',
    )
