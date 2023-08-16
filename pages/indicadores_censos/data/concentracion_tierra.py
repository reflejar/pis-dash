import pandas as pd
from constantes import *

base_censos=pd.read_csv(f'{FOLDER}/base_censo.csv', sep=";", encoding='latin1')

# BASE DE DATOS
df_base_original = base_censos.copy()

######################### Cantidad de EAPS #############################

df_eaps_q = df_base_original[[VAR_ANIO_CENSO, VAR_PARTIDO, VAR_TOTAL_EAPS]]
df_eaps_q = df_eaps_q.rename(columns = {VAR_TOTAL_EAPS: VAR_EAPS_Q})

df_eaps_q.to_csv('pages/indicadores_censos/data/tierra/q_eaps.csv', sep=';')

############ SUperficie promedio ########################

df_superficie_promedio = df_base_original[[VAR_SUPERFICIE_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
df_superficie_promedio.to_csv('pages/indicadores_censos/data/tierra/superficie_promedio.csv', sep=';')

######################### Participacion Cantidad de EAPS segun tamaño #############################
pequenias_df_base = df_base_original[[VAR_EAPS_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]
pequenias_df_base = pequenias_df_base.rename(columns = {VAR_EAPS_PEQ: VAR_EAPS_Q})
pequenias_df_base[VAR_TAMANIO_EAPS] = 'Pequeñas (<=500 ha)'

grandes_df_base = df_base_original[[VAR_EAPS_GRANDES, VAR_ANIO_CENSO, VAR_PARTIDO]]
grandes_df_base = grandes_df_base.rename(columns = {VAR_EAPS_GRANDES: VAR_EAPS_Q})
grandes_df_base[VAR_TAMANIO_EAPS] = 'Grandes (>500 ha)'

df_base = pd.concat([pequenias_df_base, grandes_df_base])

#df_base.to_csv('pages/indicadores_censos/data/tierra/eaps_por_tamanio.csv', sep=';')


######################### Superficies de EAPS segun tamaño #############################
pequenias_ha_df_base = df_base_original[[VAR_EAPS_HA_PEQ, VAR_ANIO_CENSO, VAR_PARTIDO]]
pequenias_ha_df_base = pequenias_ha_df_base.rename(columns = {VAR_EAPS_HA_PEQ: VAR_EAPS_HA})
pequenias_ha_df_base[VAR_TAMANIO_EAPS] = 'Pequeñas (<=500 ha)'

grandes_ha_df_base = df_base_original[[VAR_EAPS_HA_GRANDES, VAR_ANIO_CENSO, VAR_PARTIDO]]
grandes_ha_df_base = grandes_ha_df_base.rename(columns = {VAR_EAPS_HA_GRANDES: VAR_EAPS_HA})
grandes_ha_df_base[VAR_TAMANIO_EAPS] = 'Grandes (>500 ha)'

df_base_ha = pd.concat([pequenias_ha_df_base, grandes_ha_df_base])
df_base_ha[VAR_EAPS_HA] = df_base_ha[VAR_EAPS_HA].fillna(0.).astype(float)
df_base_ha[VAR_EAPS_HA] = df_base_ha[VAR_EAPS_HA]/1000
df_base_ha.to_csv('pages/indicadores_censos/data/tierra/eaps_ha_por_tamanio.csv', sep=';')


######################### Cantidad de  EAPS segun tipo juridico #############################

empresas_eaps_df_base = df_base_original[[VAR_EAPS_EMPRESAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
empresas_eaps_df_base =empresas_eaps_df_base.rename(columns = {VAR_EAPS_EMPRESAS: VAR_EAPS_Q})
empresas_eaps_df_base[VAR_EAPS_TIPO_JURICIO] = 'Empresas'

personas_eaps_df_base = df_base_original[[VAR_EAPS_PERSONAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
personas_eaps_df_base = personas_eaps_df_base.rename(columns = {VAR_EAPS_PERSONAS: VAR_EAPS_Q})
personas_eaps_df_base[VAR_EAPS_TIPO_JURICIO] = 'Personas Humanas'

df_base_eaps_juridico = pd.concat([empresas_eaps_df_base, personas_eaps_df_base])

#df_base_eaps_juridico.to_csv('pages/indicadores_censos/data/tierra/eaps_tipo_juridico.csv', sep=';')


######################### Superficie de EAPS segun tipo juridico #############################

empresas_ha_df_base = df_base_original[[VAR_EAPS_HA_EMPRESAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
empresas_ha_df_base =empresas_ha_df_base.rename(columns = {VAR_EAPS_HA_EMPRESAS: VAR_EAPS_HA})
empresas_ha_df_base[VAR_EAPS_TIPO_JURICIO] = 'Empresas'

personas_ha_df_base = df_base_original[[VAR_EAPS_HA_PERSONAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
personas_ha_df_base = personas_ha_df_base.rename(columns = {VAR_EAPS_HA_PERSONAS: VAR_EAPS_HA})
personas_ha_df_base[VAR_EAPS_TIPO_JURICIO] = 'Personas Humanas'

df_base_ha_juridico = pd.concat([empresas_ha_df_base, personas_ha_df_base])
df_base_ha_juridico[VAR_EAPS_HA] = df_base_ha_juridico[VAR_EAPS_HA].fillna(0.).astype(float)
df_base_ha_juridico[VAR_EAPS_HA] = df_base_ha_juridico[VAR_EAPS_HA]/1000

df_base_ha_juridico.to_csv('pages/indicadores_censos/data/tierra/ha_tipo_juridico.csv', sep=';')



######################### Propietaries x sexo #############################

mujeres_propietarias_df_base = df_base_original[[VAR_MUJERES_PROPIETARIAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
mujeres_propietarias_df_base =mujeres_propietarias_df_base.rename(columns = {VAR_MUJERES_PROPIETARIAS: VAR_EAPS_Q})
mujeres_propietarias_df_base[VAR_SEXO_PROPIETARIE] = 'Mujeres propietarias'

varones_propietarios_df_base = df_base_original[[VAR_VARONES_PROPIETARIOS, VAR_ANIO_CENSO, VAR_PARTIDO]]
varones_propietarios_df_base = varones_propietarios_df_base.rename(columns = {VAR_VARONES_PROPIETARIOS: VAR_EAPS_Q})
varones_propietarios_df_base[VAR_SEXO_PROPIETARIE] = 'Varones propietarios'

df_base_propiedad_por_sexo = pd.concat([mujeres_propietarias_df_base, varones_propietarios_df_base])
df_base_propiedad_por_sexo[VAR_EAPS_Q] = df_base_propiedad_por_sexo[VAR_EAPS_Q].fillna(0.).astype(float)

df_base_propiedad_por_sexo.to_csv('pages/indicadores_censos/data/tierra/propiedad_x_sexo.csv', sep=';')


