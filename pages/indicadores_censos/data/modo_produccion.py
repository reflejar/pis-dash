import pandas as pd
from constantes import *

base_censos=pd.read_csv(f'{FOLDER}/base_censo.csv', sep=";", encoding='latin1')

# BASE DE DATOS

df_base_original = base_censos.copy()

######################### Participacion Cantidad de EAPS segun tamaño #############################

cereales_df_base = df_base_original[[VAR_CEREALES_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
cereales_df_base = cereales_df_base.rename(columns = {VAR_CEREALES_HA: VAR_EAPS_HA})
cereales_df_base[VAR_TIPO_CULTIVO] = 'Cereales'

oleginosas_df_base = df_base_original[[VAR_OLEAGINOSAS_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
oleginosas_df_base = oleginosas_df_base.rename(columns = {VAR_OLEAGINOSAS_HA: VAR_EAPS_HA})
oleginosas_df_base[VAR_TIPO_CULTIVO] = 'Oleaginosas'

forrajeras_df_base = df_base_original[[VAR_FORRAJERAS_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
forrajeras_df_base = forrajeras_df_base.rename(columns = {VAR_FORRAJERAS_HA: VAR_EAPS_HA})
forrajeras_df_base[VAR_TIPO_CULTIVO] = 'Forrajeras'

otras_plantaciones_df_base = df_base_original[[VAR_OTRAS_PLANTACIONES_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
otras_plantaciones_df_base = otras_plantaciones_df_base.rename(columns = {VAR_OTRAS_PLANTACIONES_HA: VAR_EAPS_HA})
otras_plantaciones_df_base[VAR_TIPO_CULTIVO] = 'Otros cultivos'

df_platanciones = pd.concat([oleginosas_df_base, cereales_df_base, forrajeras_df_base, otras_plantaciones_df_base])

df_platanciones[VAR_EAPS_HA] = df_platanciones[VAR_EAPS_HA].fillna(0.).astype(float)
df_platanciones[VAR_EAPS_HA] = df_platanciones[VAR_EAPS_HA]/1000

df_platanciones.to_csv('pages/indicadores_censos/data/modo_produccion/hectareas_tipo_cultivo.csv', sep=';')


######################### Participacion Cantidad de EAPS segun tamaño #############################


bosques_montes_df_base = df_base_original[[VAR_BOSQUES_MONTES, VAR_ANIO_CENSO, VAR_PARTIDO]]
bosques_montes_df_base = bosques_montes_df_base.rename(columns = {VAR_BOSQUES_MONTES: VAR_EAPS_HA})
bosques_montes_df_base[VAR_TIPO_SUELO] = 'Bosques y Montes Naturales'

area_cultivada_df_base = df_base_original[[VAR_AREA_CULTIVADA, VAR_ANIO_CENSO, VAR_PARTIDO]]
area_cultivada_df_base = area_cultivada_df_base.rename(columns = {VAR_AREA_CULTIVADA: VAR_EAPS_HA})
area_cultivada_df_base[VAR_TIPO_SUELO] = 'Área cultivada'

df_areas_cultivadas_bosques = pd.concat([bosques_montes_df_base, area_cultivada_df_base])

df_areas_cultivadas_bosques[VAR_EAPS_HA] = df_areas_cultivadas_bosques[VAR_EAPS_HA].fillna(0.).astype(float)
df_areas_cultivadas_bosques[VAR_EAPS_HA] = df_areas_cultivadas_bosques[VAR_EAPS_HA]/1000

df_areas_cultivadas_bosques.to_csv('pages/indicadores_censos/data/modo_produccion/cultivos_bosques.csv', sep=';')















