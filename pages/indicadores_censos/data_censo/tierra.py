
import pandas as pd
from base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO

##### VARIABLES ######

VAR_EAPS_PEQ = 'EAPS pequeñas (<= 500ha)'
VAR_EAPS_GRANDES = 'EAPS grandes (>500 ha)'
VAR_TOTAL_EAPS = 'Total EAPS'
VAR_EAPS_HA_PEQ = 'HA ocupadas por EAPS pequeñas'
VAR_EAPS_HA_GRANDES = 'HA ocupadas por EAPS grandes'
VAR_TOTAL_HA_EAPS = 'Total de HA'
VAR_EAPS_HA = 'HA de EAPs'

VAR_EAPS_Q = 'Cantidad de EAPs'
VAR_TAMANIO_EAPS = 'Tamaño EAPs'
# BASE DE DATOS
df_base_original = base_censos.copy()

######################### Participacion Cantidad de EAPS segun tamaño #############################
pequenias_df_base = df_base_original[[VAR_EAPS_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]
pequenias_df_base = pequenias_df_base.rename(columns = {VAR_EAPS_PEQ: VAR_EAPS_Q})
pequenias_df_base[VAR_TAMANIO_EAPS] = 'Pequeñas (<=500 ha)'

grandes_df_base = df_base_original[[VAR_EAPS_GRANDES, VAR_ANIO_CENSO, VAR_PARTIDO]]
grandes_df_base = grandes_df_base.rename(columns = {VAR_EAPS_GRANDES: VAR_EAPS_Q})
grandes_df_base[VAR_TAMANIO_EAPS] = 'Grandes (>500 ha)'

df_base = pd.concat([pequenias_df_base, grandes_df_base])

df_base.to_csv('pages/indicadores_censos/data_censo/tierra/eaps_por_tamanio.csv', sep=';')


######################### Participacion Superficies de EAPS segun tamaño #############################
pequenias_ha_df_base = df_base_original[[VAR_EAPS_HA_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]
pequenias_ha_df_base = pequenias_ha_df_base.rename(columns = {VAR_EAPS_HA_PEQ: VAR_EAPS_HA})
pequenias_ha_df_base[VAR_TAMANIO_EAPS] = 'Pequeñas (<=500 ha)'

grandes_ha_df_base = df_base_original[[VAR_EAPS_HA_GRANDES, VAR_ANIO_CENSO, VAR_PARTIDO]]
grandes_ha_df_base = grandes_ha_df_base.rename(columns = {VAR_EAPS_HA_GRANDES: VAR_EAPS_HA})
grandes_ha_df_base[VAR_TAMANIO_EAPS] = 'Grandes (>500 ha)'

df_base_ha = pd.concat([pequenias_ha_df_base, grandes_ha_df_base])
df_base_ha[VAR_EAPS_HA] = df_base_ha[VAR_EAPS_HA].fillna(0.).astype(float)

df_base_ha.to_csv('pages/indicadores_censos/data_censo/tierra/eaps_ha_por_tamanio.csv', sep=';')
