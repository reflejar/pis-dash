from datetime import datetime
import locale

# Establecer la configuración regional según tu preferencia (por ejemplo, en_US para inglés en Estados Unidos)
locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

### CALCULOS DE RESUMEN GENERAL

VAR_EMPLEO_2018 = 53295
VAR_EMPLEO_1988 = 181679

VAR_RESIDENCIA_2018 = 87920
VAR_RESIDENCIA_1988 = 193615

VAR_CANTIDAD_EAPS_2018 = 36744
VAR_CANTIDAD_EAPS_1988 = 75479

VAR_SUPERFICIE_2018 = 642
VAR_SUPERFICIE_1988 = 361

caida_empleo_negativo = int(VAR_EMPLEO_2018 - VAR_EMPLEO_1988)
caida_empleo = abs(caida_empleo_negativo)
porc_caida_empleo = round(caida_empleo_negativo / VAR_EMPLEO_1988, 2)*100

caida_residencia_negativo = abs(int(VAR_RESIDENCIA_2018 - VAR_RESIDENCIA_1988))
caida_residencia = abs(caida_residencia_negativo)
porc_caida_residencia = round(caida_residencia_negativo / VAR_RESIDENCIA_1988, 2)*100

caida_eaps_negativo = abs(int(VAR_CANTIDAD_EAPS_2018 - VAR_CANTIDAD_EAPS_1988))
caida_eaps = abs(caida_eaps_negativo)
porc_caida_eaps = round(caida_eaps_negativo / VAR_CANTIDAD_EAPS_1988, 2)*100


var_superficie_negativo = int(VAR_SUPERFICIE_2018 - VAR_SUPERFICIE_1988)
var_superficie = abs(var_superficie_negativo)
porc_var_superficie = round(var_superficie_negativo / VAR_SUPERFICIE_1988, 2)*100

PERDIDA_EMPLEO = locale.format_string('%d', caida_empleo, grouping=True)
PERDIDA_RESIDENCIA = locale.format_string('%d', caida_residencia, grouping=True) 
PERDIDA_EAPS = locale.format_string('%d', caida_eaps, grouping=True)


VAR_CANTIDAD_EAPS_2018 = locale.format_string('%d', VAR_CANTIDAD_EAPS_2018, grouping=True)
VAR_CANTIDAD_EAPS_1988 = locale.format_string('%d', VAR_CANTIDAD_EAPS_1988, grouping=True)

VAR_RESIDENCIA_2018 = locale.format_string('%d', VAR_RESIDENCIA_2018, grouping=True)
VAR_RESIDENCIA_1988 = locale.format_string('%d', VAR_RESIDENCIA_1988, grouping=True)

VAR_EMPLEO_2018 = locale.format_string('%d', VAR_EMPLEO_2018, grouping=True)
VAR_EMPLEO_1988 = locale.format_string('%d', VAR_EMPLEO_1988, grouping=True)


VAR_SUPERFICIE_2018 = locale.format_string('%d', VAR_SUPERFICIE_2018, grouping=True)
VAR_SUPERFICIE_1988 = locale.format_string('%d', VAR_SUPERFICIE_1988, grouping=True)
















 