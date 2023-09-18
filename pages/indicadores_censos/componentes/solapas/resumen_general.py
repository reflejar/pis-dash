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

caida_empleo = abs(int(VAR_EMPLEO_2018 - VAR_EMPLEO_1988))

caida_residencia = abs(int(VAR_RESIDENCIA_2018 - VAR_RESIDENCIA_1988))
caida_eaps = abs(int(VAR_CANTIDAD_EAPS_2018 - VAR_CANTIDAD_EAPS_1988))

# fecha_censo_1988 = '31/12/1988'
# fecha_censo_2018 = '31/03/2019'

# start = datetime.strptime(fecha_censo_2018, "%d/%m/%Y")
# end =   datetime.strptime(fecha_censo_1988, "%d/%m/%Y")

# Obtener la diferencia en dias
# diff = end.date() - start.date()
# cantidad_mes = abs(diff.days)/30

PERDIDA_EMPLEO_X_MES = locale.format_string('%d', caida_empleo, grouping=True)
PERDIDA_RESIDENCIA_X_MES = locale.format_string('%d', caida_residencia, grouping=True) 
PERDIDA_EAPS_X_MES = locale.format_string('%d', caida_eaps, grouping=True)



















 