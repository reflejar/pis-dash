import pandas as pd
from dash import dash_table, html


# Función para establecer la altura del encabezado
def estilo_encabezado(column_name):
    num_palabras = len(column_name.split())
    if num_palabras > 5:
        return '150px'
    else:
        return  '75px' # Altura por defecto
    
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
            columns=[{'id': i, 'name': i, 'presentation': 'markdown'} if (i == 'Ordenanza')
                  else {'id': i, 'name': i} for i in self.columns],
            style_as_list_view=True,
            fixed_rows={'headers': True},
            fixed_columns={'headers': True,'data': 1},
            style_table={
                'minWidth': '100%',
                'height': '500px',
                'borderCollapse': 'separate',
                'borderSpacing': '0 10px',
            },
            style_header={
                'backgroundColor': self.colorclaro,
                'height':estilo_encabezado(self.columns[5]),
                'fontWeight': 'bold',
                'textAlign':'center',
                'fontFamily': 'Arial',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            style_data_conditional = [
                {
                      'if': {
                        'filter_query': '{Ordenanza} = "Sin Ordenanza"',
                    },
                    'backgroundColor': '#EEEEEE',

                },
                {
                    'if': {'state': 'active'},
                    'backgroundColor': 'rgba(0,0,0,0.025)',
                    'border': f'1px solid {self.color}',
                    'color' : 'rgba(0,0,0,1)',
                },          
            ],

            sort_action="native",

    )
