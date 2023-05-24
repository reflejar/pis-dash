import pandas as pd

URL_DATA_CENSO = 'pages\indicadores_censos\data_censo'
#Variables
VAR_ANIO_CENSO = 'Año del censo'
VAR_PARTIDO = 'Partido'

base_censos=pd.read_csv(f'{URL_DATA_CENSO}/base_censo.csv', sep=";", encoding='latin1')

#Limpieza de datos
base_censos[VAR_ANIO_CENSO]=base_censos[VAR_ANIO_CENSO].astype(int).astype(str)

#Listado de opciones de filtros
anio_censo=base_censos[VAR_ANIO_CENSO].sort_values(ascending=True).unique().tolist()
partidos=base_censos[VAR_PARTIDO].sort_values(ascending=True).unique().tolist()

