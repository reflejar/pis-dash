import pandas as pd

URL_DATA_CENSO = 'pages/indicadores_censos/data_censo'

#Variables
VAR_ANIO_CENSO = 'Año del censo'
VAR_PARTIDO = 'Buenos Aires'
VAR_TOTAL='Total'


base_empleo=pd.read_csv(f'{URL_DATA_CENSO}/empleo.csv')

#Limpieza de datos
base_empleo[VAR_ANIO_CENSO]=base_empleo[VAR_ANIO_CENSO].astype(int).astype(str)

#Listado de opciones de filtros
anio_censo=base_empleo[VAR_ANIO_CENSO].sort_values(ascending=True).unique().tolist()
