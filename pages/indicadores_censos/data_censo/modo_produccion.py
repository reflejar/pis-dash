import pandas as pd
from .base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO

VAR_EAPS_HA = 'Cantidad HA'
VAR_CEREALES_HA = 'Cantidad de hectáreas implantadas de Cereales'
VAR_OLEAGINOSAS_HA = 'Cantidad de hectáreas implantadas de Oleaginosas'
VAR_FORRAJERAS_HA = 'Cantidad de hectáreas implantadas de Forrajeras'
VAR_TIPO_CULTIVO = 'Tipo de cultivo'

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

df_base = pd.concat([oleginosas_df_base, cereales_df_base, forrajeras_df_base])

df_base.to_csv('pages/indicadores_censos/data_censo/modo_produccion/hectareas_tipo_cultivo.csv', sep=';')
















