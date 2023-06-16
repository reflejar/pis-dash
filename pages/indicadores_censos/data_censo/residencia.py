import pandas as pd

URL_DATA_CENSO = 'pages/indicadores_censos/data_censo'

#Variables
VAR_ANIO_CENSO = 'Año del censo'
VAR_PARTIDO = 'Buenos Aires'
VAR_SEXO_NACIMIENTO= 'Sexo de nacimiento'
VAR_ULTIMO_ANIO_CENSO = '2018'
VAR_ANIO_CENSO_1988 = '1988'
VAR_ANIO_CENSO_2002 = '2002'
VAR_MUJERES= 'Mujeres'
VAR_VARONES= 'Varones'
VAR_TOTAL='Total'

base_residencia=pd.read_csv(f'{URL_DATA_CENSO}/residencia.csv')

#Limpieza de datos
base_residencia[VAR_ANIO_CENSO]=base_residencia[VAR_ANIO_CENSO].astype(int).astype(str)

#Listado de opciones de filtros
anio_censo=base_residencia[VAR_ANIO_CENSO].sort_values(ascending=True).unique().tolist()

#Se crean bases residencia mujeres y varones
base_mujeres=base_residencia[base_residencia[VAR_SEXO_NACIMIENTO]==VAR_MUJERES]
base_varones=base_residencia[base_residencia[VAR_SEXO_NACIMIENTO]==VAR_VARONES]