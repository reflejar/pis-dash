import pandas as pd
from .constantes import *

base_censos=pd.read_csv(f'{FOLDER}/base_censo.csv', sep=";", encoding='latin1')

#Limpieza de datos
base_censos[VAR_ANIO_CENSO]=base_censos[VAR_ANIO_CENSO].astype(int).astype(str)

#Listado de opciones de filtros
anio_censo=base_censos[VAR_ANIO_CENSO].sort_values(ascending=True).unique().tolist()
partidos=base_censos[VAR_PARTIDO].sort_values(ascending=True).unique().tolist()

# Lecturas de bases de datos particulares
df_eaps_cantidad = pd.read_csv(f'{FOLDER}/tierra/q_eaps.csv', sep=';', decimal=',')
df_eaps_por_tamanio = pd.read_csv(f'{FOLDER}/tierra/eaps_por_tamanio.csv', sep=';')
df_eaps_tipo_juridico = pd.read_csv(f'{FOLDER}/tierra/eaps_tipo_juridico.csv', sep=';')
df_superficie_promedio = pd.read_csv(f'{FOLDER}/tierra/superficie_promedio.csv', sep=';')
df_eaps_ha_por_tamanio = pd.read_csv(f'{FOLDER}/tierra/eaps_ha_por_tamanio.csv', sep=';', decimal=',')
df_propiedad_x_sexo = pd.read_csv(f'{FOLDER}/tierra/propiedad_x_sexo.csv', sep=';'  )
df_ha_tipo_juridico = pd.read_csv(f'{FOLDER}/tierra/ha_tipo_juridico.csv', sep=';', decimal=',')


df_ha_tipo_cultivo = pd.read_csv(f'{FOLDER}/modo_produccion/hectareas_tipo_cultivo.csv', sep=';' )
df_cultivado_bosques = pd.read_csv(f'{FOLDER}/modo_produccion/cultivos_bosques.csv', sep=';' )
df_practicas_organicas = pd.read_csv(f'{FOLDER}/modo_produccion/practicas_organicas.csv', sep=';' )




df_residentes_por_sexo = pd.read_csv(f'{FOLDER}/empleo-y-residencia/residentes_por_sexo.csv', sep=';' )
df_evolucion_empleo = pd.read_csv(f'{FOLDER}/empleo-y-residencia/evolucion_empleo.csv', sep=';' )