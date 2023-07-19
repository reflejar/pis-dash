import pandas as pd

URL_DATA_CENSO = 'pages/indicadores_censos/data_censo'
#Variables
VAR_ANIO_CENSO ="Año del censo"
VAR_PARTIDO = 'Partido'
VAR_ANIO_CENSO_2018 = '2018'
VAR_ANIO_CENSO_1988 = '1988'
VAR_ANIO_CENSO_2002 = '2002'
VAR_CULTIVOS='Cultivo'
VAR_VALORES='Total'

base_cultivos=pd.read_csv(f'{URL_DATA_CENSO}/cultivos_ha.csv', sep=";")

#Limpieza de datos
base_cultivos[VAR_ANIO_CENSO]=base_cultivos[VAR_ANIO_CENSO].astype(int).astype(str)

#Listado de opciones de filtros
anio_censo=base_cultivos[VAR_ANIO_CENSO].sort_values(ascending=True).unique().tolist()
partidos=base_cultivos[VAR_PARTIDO].sort_values(ascending=True).unique().tolist()