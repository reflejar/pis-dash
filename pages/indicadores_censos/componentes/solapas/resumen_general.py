from datetime import datetime
import locale

# Establecer la configuración regional según tu preferencia (por ejemplo, en_US para inglés en Estados Unidos)
locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

numero = 1234567  # Tu número entero

### CALCULOS DE RESUMEN GENERAL

VAR_EMPLEO_2018 = 53782
VAR_EMPLEO_2002 = 67316

VAR_RESIDENCIA_2018 = 88402
VAR_RESIDENCIA_2002 = 150923

VAR_CANTIDAD_EAPS_2018 = 36744
VAR_CANTIDAD_EAPS_2002 = 51107

caida_empleo = abs(int(VAR_EMPLEO_2018 - VAR_EMPLEO_2002))

caida_residencia = abs(int(VAR_RESIDENCIA_2018 - VAR_RESIDENCIA_2002))
caida_eaps = abs(int(VAR_CANTIDAD_EAPS_2018 - VAR_CANTIDAD_EAPS_2002))

# fecha_censo_2002 = '31/12/2002'
# fecha_censo_2018 = '31/03/2019'

# start = datetime.strptime(fecha_censo_2018, "%d/%m/%Y")
# end =   datetime.strptime(fecha_censo_2002, "%d/%m/%Y")

# Obtener la diferencia en dias
# diff = end.date() - start.date()
# cantidad_mes = abs(diff.days)/30

PERDIDA_EMPLEO_X_MES = locale.format_string('%d', caida_empleo, grouping=True)
PERDIDA_RESIDENCIA_X_MES = locale.format_string('%d', caida_residencia, grouping=True) 
PERDIDA_EAPS_X_MES = locale.format_string('%d', caida_eaps, grouping=True)



















 