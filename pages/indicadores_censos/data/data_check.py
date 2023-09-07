import pandas as pd
from constantes import *

df_base_original=pd.read_csv(f'{FOLDER}/base_censo.csv', sep=";", encoding='latin1')

def check(total, var_1, var_2):
    df = df_base_original.copy()
    df['Suma'] = df[var_1] + df[var_2]
    df['Diferencia'] = df[total] - df['Suma']
    df_corregir = df[df['Diferencia']!=0]
    check = (df['Diferencia'].sum())==0
    check_texto =  f'Si se suma {var_1} y {var_2} y se compara con {total} no hay diferencia' if check else f'[Corregir] Si se suma {var_1} y {var_2} y se compara con {total} hay diferencia'
    a_corregir = '' if check else df_corregir
    return print(check_texto), print(a_corregir)

tamanio_texto_eaps, base_a_corregir_tamanio_eaps = check(VAR_TOTAL_EAPS, VAR_EAPS_PEQ, VAR_EAPS_GRANDES)
tamanio_texto_ha, base_a_corregir_tamanio_ha = check(VAR_TOTAL_HA_EAPS, VAR_EAPS_HA_PEQ, VAR_EAPS_HA_GRANDES)
juridico_texto_eaps, base_a_corregir_juridico_eaps = check(VAR_TOTAL_EAPS, VAR_EAPS_EMPRESAS, VAR_EAPS_PERSONAS)
juridico_texto_ha, base_a_corregir_juridico_ha = check(VAR_TOTAL_HA_EAPS, VAR_EAPS_HA_EMPRESAS, VAR_EAPS_HA_PERSONAS)