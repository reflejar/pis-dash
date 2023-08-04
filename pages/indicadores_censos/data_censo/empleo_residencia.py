import pandas as pd
from base_indicadores import base_censos, VAR_ANIO_CENSO, VAR_PARTIDO

# BASE DE DATOS
df_base_original = base_censos.copy()

#############################################Variables de RESIDENCIA ####################

VAR_SEXO_NACIMIENTO= 'Sexo de nacimiento'
VAR_MUJERES_RESIDENTES= 'Mujeres Residentes del campo'
VAR_VARONES_RESIDENTES= 'Varones Residentes del campo'
VAR_CANTIDAD_PERSONAS = 'Cantidad de personas'

######### RESIDENCIA TOTAL POR SEXO

mujeres_residentes_df_base = df_base_original[[VAR_MUJERES_RESIDENTES, VAR_ANIO_CENSO, VAR_PARTIDO]]
mujeres_residentes_df_base = mujeres_residentes_df_base.rename(columns = {VAR_MUJERES_RESIDENTES: VAR_CANTIDAD_PERSONAS})
mujeres_residentes_df_base[VAR_SEXO_NACIMIENTO] = VAR_MUJERES_RESIDENTES

varones_residentes_df_base = df_base_original[[VAR_VARONES_RESIDENTES, VAR_ANIO_CENSO, VAR_PARTIDO]]
varones_residentes_df_base = varones_residentes_df_base.rename(columns = {VAR_VARONES_RESIDENTES: VAR_CANTIDAD_PERSONAS})
varones_residentes_df_base[VAR_SEXO_NACIMIENTO] = VAR_VARONES_RESIDENTES


df_base_residentes = pd.concat([mujeres_residentes_df_base, varones_residentes_df_base])

df_base_residentes.to_csv('pages/indicadores_censos/data_censo/empleo-y-residencia/residentes_por_sexo.csv', sep=';')


'Mujeres Residentes (Personas Humanas)'
'Mujeres Residente (Empresas)'

'Varones Residentes (Personas Humanas)'
'Varones Residentes (Empresas)'


#################################################BASE DE DATOS DE  EMPLEO

#Variables
VAR_EMPLEO = 'Empleo'

empleo_df_base = df_base_original[[VAR_EMPLEO, VAR_ANIO_CENSO, VAR_PARTIDO]]
empleo_df_base.to_csv('pages/indicadores_censos/data_censo/empleo-y-residencia/evolucion_empleo.csv', sep=';')
