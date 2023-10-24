import pandas as pd
from dash import dash_table, html


class Tabla:
    """
        Clase para crear las diferentes tablas
    """

    def __init__(
            self,
            id_tabla="", 
            color_id="",
            df=pd.DataFrame(),
    ) -> None:
        self.id = id_tabla
        self.color=color_id
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
                'height': '500px',
                'borderCollapse': 'separate',
                'borderSpacing': '0 10px',
            },
            style_cell={'whiteSpace': 'pre',
                        'fontFamily': 'Arial',
                        'textAlign':'center',
                        'verticalAlign': 'middle',
                        'maxWidth': '300px'
                        },
            style_header={
                'backgroundColor': "#eceeef",
                'textAlign':'center',
            },
            style_header_conditional=[
                {'if': {'column_id': c}, 'fontWeight': 'bold', 'textAlign':'left'}
                for c in self.columns[:3]  # Primeros tres encabezados en negritas y alineados a la izquierda
            ],
            style_data_conditional = [
                {
                    'if': {'state': 'active'},
                    'backgroundColor': 'rgba(0,0,0,0.05)',
                    'border': f'1px solid {self.color}',
                    'color' : 'rgba(0,0,0,1)',
                }
            ],
            sort_action='native',

    )
