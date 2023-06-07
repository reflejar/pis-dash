import pandas as pd

URL_DATA_CENSO = 'pages/indicadores_censos/data_censo'
#Variables
VAR_ANIO_CENSO = 'Año del censo'
VAR_PARTIDO = 'Partido'
VAR_ULTIMO_ANIO_CENSO = '2018'
VAR_ANIO_CENSO_1988 = '1988'
VAR_ANIO_CENSO_2002 = '2002'

base_censos=pd.read_csv(f'{URL_DATA_CENSO}/base_censo.csv', sep=";", encoding='latin1')

#Limpieza de datos
base_censos[VAR_ANIO_CENSO]=base_censos[VAR_ANIO_CENSO].astype(int).astype(str)

#Listado de opciones de filtros
anio_censo=base_censos[VAR_ANIO_CENSO].sort_values(ascending=True).unique().tolist()
partidos=base_censos[VAR_PARTIDO].sort_values(ascending=True).unique().tolist()

