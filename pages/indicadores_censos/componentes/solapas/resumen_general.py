from datetime import datetime

### CALCULOS DE RESUMEN GENERAL

VAR_EMPLEO_2018 = 53782
VAR_EMPLEO_2002 = 67316

VAR_RESIDENCIA_2018 = 88402
VAR_RESIDENCIA_2002 = 150923

VAR_CANTIDAD_EAPS_2018 = 36744
VAR_CANTIDAD_EAPS_2002 = 51107

caida_empleo = VAR_EMPLEO_2018 - VAR_EMPLEO_2002
caida_residencia = VAR_RESIDENCIA_2018 - VAR_RESIDENCIA_2002
caida_eaps = VAR_CANTIDAD_EAPS_2018 - VAR_CANTIDAD_EAPS_2002

fecha_censo_2002 = '31/12/2002'
fecha_censo_2018 = '31/03/2019'

start = datetime.strptime(fecha_censo_2018, "%d/%m/%Y")
end =   datetime.strptime(fecha_censo_2002, "%d/%m/%Y")

# Obtener la diferencia en dias
diff = end.date() - start.date()
cantidad_mes = abs(diff.days)/30

PERDIDA_EMPLEO_X_MES = abs(int(caida_empleo/cantidad_mes))
PERDIDA_RESIDENCIA_X_MES = abs(int(caida_residencia/cantidad_mes))
PERDIDA_EAPS_X_MES = abs(int(caida_eaps/cantidad_mes))



















 