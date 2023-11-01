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
            color_claro_id="",
            df=pd.DataFrame(),
    ) -> None:
        self.id = id_tabla
        self.color=color_id,
        self.colorclaro=color_claro_id,
        self.df = df.copy()
        self.columns = self.df.columns
       

    def inicializar(self):
        return dash_table.DataTable(
            id=self.id,
            data=self.df.to_dict('records'),
            columns=[{"name": i, "id": i, "presentation": 'markdown'} for i in self.columns],
            style_as_list_view=True,
            fixed_rows={'headers': True},
            fixed_columns={'headers': True,'data': 1},
            style_table={
                # 'overflowX': 'scroll',
                # 'position': 'sticky',
                # 'overflowY': 'scroll',
                'minWidth': '100%',
                'height': '500px',
                'borderCollapse': 'separate',
                'borderSpacing': '0 10px',
            },
            style_header={
                'backgroundColor': self.colorclaro,
                'height': '50px',
                'fontWeight': 'bold',
                'textAlign':'center',
                'fontFamily': 'Arial',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
           
            style_data_conditional = [
                {
                    'if': {
                        'filter_query': '{{Puntaje}} = {}'.format(self.df['Puntaje'].min()),
                    },
                    'backgroundColor': '#EEEEEE',
                },
                {
                    'if': {'state': 'active'},
                    'backgroundColor': 'rgba(0,0,0,0.05)',
                    'border': f'1px solid {self.color}',
                    'color' : 'rgba(0,0,0,1)',
                },
            ],

            sort_action='native',
            
            style_data={'minWidth': '100%', 
                        'textAlign':'center',
                        'fontFamily': 'Arial',
                        'verticalAlign': 'middle',
                        },
            style_cell={'whiteSpace': 'pre-line',
                        'minWidth':'100%',
                        'width':'200px',
                        'textAlign':'center',
                        },

    )
