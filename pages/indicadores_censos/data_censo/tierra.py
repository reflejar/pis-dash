
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
VAR_EAPS_EMPRESAS= 'EAPS en manos de Empresas'
VAR_EAPS_PERSONAS = 'EAPS en manos de Personas Humanas'
VAR_EAPS_HA_EMPRESAS = 'Superficie en manos de Empresas'
VAR_EAPS_HA_PERSONAS = 'Superficie en mano de Personas Humanas'

VAR_EAPS_HA = 'HA de EAPs'
VAR_EAPS_Q = 'Cantidad de EAPs'
VAR_TAMANIO_EAPS = 'Tamaño EAPs'
VAR_EAPS_TIPO_JURICIO = 'Tipo jurídico'
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

#df_base.to_csv('pages/indicadores_censos/data_censo/tierra/eaps_por_tamanio.csv', sep=';')


######################### Participacion Superficies de EAPS segun tamaño #############################
pequenias_ha_df_base = df_base_original[[VAR_EAPS_HA_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]
pequenias_ha_df_base = pequenias_ha_df_base.rename(columns = {VAR_EAPS_HA_PEQ: VAR_EAPS_HA})
pequenias_ha_df_base[VAR_TAMANIO_EAPS] = 'Pequeñas (<=500 ha)'

grandes_ha_df_base = df_base_original[[VAR_EAPS_HA_GRANDES, VAR_ANIO_CENSO, VAR_PARTIDO]]
grandes_ha_df_base = grandes_ha_df_base.rename(columns = {VAR_EAPS_HA_GRANDES: VAR_EAPS_HA})
grandes_ha_df_base[VAR_TAMANIO_EAPS] = 'Grandes (>500 ha)'

df_base_ha = pd.concat([pequenias_ha_df_base, grandes_ha_df_base])
df_base_ha[VAR_EAPS_HA] = df_base_ha[VAR_EAPS_HA].fillna(0.).astype(float)

#df_base_ha.to_csv('pages/indicadores_censos/data_censo/tierra/eaps_ha_por_tamanio.csv', sep=';')


######################### Cantidad de  EAPS segun tipo juridico #############################

empresas_eaps_df_base = df_base_original[[VAR_EAPS_EMPRESAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
empresas_eaps_df_base =empresas_eaps_df_base.rename(columns = {VAR_EAPS_EMPRESAS: VAR_EAPS_Q})
empresas_eaps_df_base[VAR_EAPS_TIPO_JURICIO] = 'Empresas'

personas_eaps_df_base = df_base_original[[VAR_EAPS_PERSONAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
personas_eaps_df_base = personas_eaps_df_base.rename(columns = {VAR_EAPS_PERSONAS: VAR_EAPS_Q})
personas_eaps_df_base[VAR_EAPS_TIPO_JURICIO] = 'Personas Humanas'

df_base_eaps_juridico = pd.concat([empresas_eaps_df_base, personas_eaps_df_base])

df_base_eaps_juridico.to_csv('pages/indicadores_censos/data_censo/tierra/eaps_tipo_juridico.csv', sep=';')


######################### Superficie de EAPS segun tipo juridico #############################

empresas_ha_df_base = df_base_original[[VAR_EAPS_HA_EMPRESAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
empresas_ha_df_base =empresas_ha_df_base.rename(columns = {VAR_EAPS_HA_EMPRESAS: VAR_EAPS_HA})
empresas_ha_df_base[VAR_EAPS_TIPO_JURICIO] = 'Empresas'

personas_ha_df_base = df_base_original[[VAR_EAPS_HA_PERSONAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
personas_ha_df_base = personas_ha_df_base.rename(columns = {VAR_EAPS_HA_PERSONAS: VAR_EAPS_HA})
personas_ha_df_base[VAR_EAPS_TIPO_JURICIO] = 'Personas Humanas'

df_base_ha_juridico = pd.concat([empresas_ha_df_base, personas_ha_df_base])
df_base_ha_juridico[VAR_EAPS_HA] = df_base_ha_juridico[VAR_EAPS_HA].fillna(0.).astype(float)

df_base_ha_juridico.to_csv('pages/indicadores_censos/data_censo/tierra/ha_tipo_juridico.csv', sep=';')