import pandas as pd
from constantes import *

base_censos=pd.read_csv(f'{FOLDER}/base_censo.csv', sep=";", encoding='latin1')

# BASE DE DATOS

df_base_original = base_censos.copy()

######################### Participacion Cantidad de EAPS segun tamaño #############################

cereales_df_base = df_base_original[[VAR_CEREALES_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
cereales_df_base = cereales_df_base.rename(columns = {VAR_CEREALES_HA: VAR_EAPS_HA})
cereales_df_base[VAR_TIPO_CULTIVO] = '1.Cereales'

oleginosas_df_base = df_base_original[[VAR_OLEAGINOSAS_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
oleginosas_df_base = oleginosas_df_base.rename(columns = {VAR_OLEAGINOSAS_HA: VAR_EAPS_HA})
oleginosas_df_base[VAR_TIPO_CULTIVO] = '2.Oleaginosas'

forrajeras_df_base = df_base_original[[VAR_FORRAJERAS_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
forrajeras_df_base = forrajeras_df_base.rename(columns = {VAR_FORRAJERAS_HA: VAR_EAPS_HA})
forrajeras_df_base[VAR_TIPO_CULTIVO] = '3.Forrajeras'

otras_plantaciones_df_base = df_base_original[[VAR_OTRAS_PLANTACIONES_HA, VAR_ANIO_CENSO, VAR_PARTIDO]]
otras_plantaciones_df_base = otras_plantaciones_df_base.rename(columns = {VAR_OTRAS_PLANTACIONES_HA: VAR_EAPS_HA})
otras_plantaciones_df_base[VAR_TIPO_CULTIVO] = '4.Otros cultivos'

df_platanciones = pd.concat([oleginosas_df_base, cereales_df_base, forrajeras_df_base, otras_plantaciones_df_base])
df_platanciones.to_csv('pages/indicadores_censos/data/modo_produccion/hectareas_tipo_cultivo.csv', sep=';')


######################### Participacion Cantidad de EAPS segun tamaño #############################


bosques_montes_df_base = df_base_original[[VAR_BOSQUES_MONTES, VAR_ANIO_CENSO, VAR_PARTIDO]]
bosques_montes_df_base = bosques_montes_df_base.rename(columns = {VAR_BOSQUES_MONTES: VAR_EAPS_HA})
bosques_montes_df_base[VAR_TIPO_SUELO] = 'Bosques y Montes Naturales'
bosques_montes_df_base.to_csv('pages/indicadores_censos/data/modo_produccion/cultivos_bosques.csv', sep=';')

######################## PRACTICAS AGROECOLOGICAS ##########################

practicas_organicas_df_base = df_base_original[[VAR_PRACTICAS_ORGANICAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
practicas_organicas_df_base.to_csv('pages/indicadores_censos/data/modo_produccion/practicas_organicas.csv', sep=';')


######################## OLEAGINOSAS ##########################

soja_df_base = df_base_original[[VAR_SOJA, VAR_ANIO_CENSO, VAR_PARTIDO]]
soja_df_base = soja_df_base.rename(columns = {VAR_SOJA: VAR_EAPS_HA})
soja_df_base[VAR_TIPO_OLEAGINOSA] = '1.Soja'

otras_oleaginosas_df_base = df_base_original[[VAR_OTRAS_OLEAGINOSAS, VAR_ANIO_CENSO, VAR_PARTIDO]]
otras_oleaginosas_df_base = otras_oleaginosas_df_base.rename(columns = {VAR_OTRAS_OLEAGINOSAS: VAR_EAPS_HA})
otras_oleaginosas_df_base[VAR_TIPO_OLEAGINOSA] = '2.Otras oleaginosas'

df_oleaginosas = pd.concat([soja_df_base, otras_oleaginosas_df_base])
df_oleaginosas.to_csv('pages/indicadores_censos/data/modo_produccion/oleaginosas.csv', sep=';')



######################## CEREALES ##########################

maiz_df_base = df_base_original[[VAR_MAIZ, VAR_ANIO_CENSO, VAR_PARTIDO]]
maiz_df_base = maiz_df_base.rename(columns = {VAR_MAIZ: VAR_EAPS_HA})
maiz_df_base[VAR_TIPO_CEREAL] = '2.Maíz'

trigo_pan_df_base = df_base_original[[VAR_TRIGO, VAR_ANIO_CENSO, VAR_PARTIDO]]
trigo_pan_df_base = trigo_pan_df_base.rename(columns = {VAR_TRIGO: VAR_EAPS_HA})
trigo_pan_df_base[VAR_TIPO_CEREAL] = '1.Trigo pan'

otros_cereales_df_base = df_base_original[[VAR_OTROS_CEREALES, VAR_ANIO_CENSO, VAR_PARTIDO]]
otros_cereales_df_base = otros_cereales_df_base.rename(columns = {VAR_OTROS_CEREALES: VAR_EAPS_HA})
otros_cereales_df_base[VAR_TIPO_CEREAL] = '3.Otros cereales'

df_cereales = pd.concat([maiz_df_base, trigo_pan_df_base ,otros_cereales_df_base])
df_cereales.to_csv('pages/indicadores_censos/data/modo_produccion/cereales.csv', sep=';')


######################## FORRAJERAS ##########################

anuales_df_base = df_base_original[[VAR_FORRAJES_ANUALES, VAR_ANIO_CENSO, VAR_PARTIDO]]
anuales_df_base = anuales_df_base.rename(columns = {VAR_FORRAJES_ANUALES: VAR_EAPS_HA})
anuales_df_base[VAR_TIPO_FORRAJERA] = '2.Forrajeras anuales'

perennes_df_base = df_base_original[[VAR_FORRAJES_PERENNES, VAR_ANIO_CENSO, VAR_PARTIDO]]
perennes_df_base = perennes_df_base.rename(columns = {VAR_FORRAJES_PERENNES: VAR_EAPS_HA})
perennes_df_base[VAR_TIPO_FORRAJERA] = '1.Forrajeras perennes'

df_forrajeras = pd.concat([anuales_df_base, perennes_df_base])
df_forrajeras.to_csv('pages/indicadores_censos/data/modo_produccion/forrajeras.csv', sep=';')

























