import geopandas as gpd
import pandas as pd


# VARIABLES FIJAS UTILIZADAS PARA EL MERGE Y PARA EL TOOLTIP
FILTRO_PARTIDOS = "Mar Chiquita"

VAR_CUE = 'cue'
VAR_SEDE_ANEXO_EXT = 'sede/axo/ext'
VAR_COD_POSTAL = 'código postal'
VAR_TELEFONO = 'Tel'
VAR_MAIL = 'email'
VAR_CODIGO_UNICO = 'codigo_unico_pis'
VAR_DIRECCION = 'direccion'
VAR_NOM_ESTABLEC = 'nombre.establecimiento'
VAR_LATITUD = 'latitud'
VAR_LONGITUD = 'longitud'
VAR_GEOMETRIA = 'geometry'
VAR_LOCALIDAD = 'localidad'
VAR_PARTIDO= 'partido'
VAR_NUEVA_EXISTENTE = 'nueva_existente'
VAR_NIVEL = 'nivel'

# Variables manuales
VAR_CP_MANUAL = 'codigo_postal_manual'
VAR_LOCALIDAD_MANUAL = 'localidad_manual'

# VAR INDEC
VAR_CP_INDEC = 'codigo_postal_indec'
VAR_DIRECCION_INDEC = 'direccion_indec'
VAR_TELEFONO_INDEC = 'telefono_indec'

# ARCHIVO CON INFORMACIÓN PROVINCIAL > DE ACA SE TOMA EL LISTADO DE VALIDACIÓN
establec_educativos_completo_original=gpd.read_file("./data/establecimientos-educativos-PBA.geojson")

establec_educativos_completo = establec_educativos_completo_original.copy()
establec_educativos_completo = establec_educativos_completo[establec_educativos_completo[VAR_PARTIDO]== FILTRO_PARTIDOS]

# LIMPIEZA Y ORDENAMIENTO DE DATOS
# Se unifican los codigos postales para evitar pérdida de información
validacion_cp = pd.read_csv('data\codigo_postales_pba.csv', encoding = 'latin1', on_bad_lines='skip', sep = ";", decimal=",")
validacion_cp = validacion_cp.dropna(how= 'all', axis=0)
validacion_cp[VAR_CP_MANUAL] =  validacion_cp[VAR_CP_MANUAL].astype(int).astype(str).replace({'0': 'S/CP'})
validacion_cp[VAR_LOCALIDAD_MANUAL] = validacion_cp[VAR_LOCALIDAD_MANUAL].str.upper()
validacion_cp = validacion_cp.rename(columns = {VAR_LOCALIDAD_MANUAL: VAR_LOCALIDAD})
validacion_cp = validacion_cp[[VAR_LOCALIDAD, VAR_CP_MANUAL]]

establec_educativos_completo = pd.merge(establec_educativos_completo, validacion_cp, on = VAR_LOCALIDAD)
establec_educativos_completo = establec_educativos_completo.drop(columns = {VAR_COD_POSTAL}).rename(columns = {VAR_CP_MANUAL: VAR_COD_POSTAL})

# Trabajamos sobre el resto de las variables
establec_educativos_completo[VAR_DIRECCION_INDEC] = establec_educativos_completo['dirección calle'] + establec_educativos_completo['dirección nro.']
establec_educativos_completo['característica telefónica'] = '(' + establec_educativos_completo['característica telefónica'].fillna(0).astype(int).astype(str) + ')'
establec_educativos_completo[VAR_TELEFONO_INDEC] = establec_educativos_completo['característica telefónica'] +' ' + establec_educativos_completo['teléfono'].astype(str)
establec_educativos_completo = establec_educativos_completo.rename(columns = {VAR_MAIL: 'mail_indec', VAR_LATITUD : 'latitud_indec', VAR_LONGITUD : 'longitud_indec', VAR_GEOMETRIA : 'geometry_indec'})

establec_educativos_completo[VAR_CODIGO_UNICO] = establec_educativos_completo[VAR_COD_POSTAL] + ' - ' +  establec_educativos_completo[VAR_CUE].astype(str) + ' - ' + establec_educativos_completo[VAR_SEDE_ANEXO_EXT]

# Base de datos actualizada manualmente
escuelas_informacion_manual = pd.read_csv('data\est_educativos_actualizacion_provincial.csv', encoding = 'latin1', on_bad_lines='skip', sep = ";", decimal=",")
escuelas_informacion_manual = escuelas_informacion_manual.dropna(how= 'all', axis=0)
escuelas_informacion_manual = escuelas_informacion_manual.dropna(how= 'all', axis=1)
escuelas_informacion_manual[VAR_CP_MANUAL] =  escuelas_informacion_manual[VAR_CP_MANUAL].astype(int).astype(str).replace({'0': 'S/CP'})
# Filtramos para solo quedarnos con las escuelas rurales. Las urbanas se incluyen dentro de las localidades.
escuelas_informacion_manual = escuelas_informacion_manual[escuelas_informacion_manual['ubicacion_manual']!= 'Urbano']


# Construimos codigo para el merge
escuelas_informacion_manual[VAR_CODIGO_UNICO] = escuelas_informacion_manual[VAR_CP_MANUAL] + ' - ' + escuelas_informacion_manual[VAR_CUE].astype(str) + ' - ' + escuelas_informacion_manual[VAR_SEDE_ANEXO_EXT]

# Construimos nombre a mostrar del establecimiento
escuelas_informacion_manual['nombre_apellido_manual'] = escuelas_informacion_manual['nombre'] + ' ' + escuelas_informacion_manual['apellido']
escuelas_informacion_manual['longitud_manual'] = escuelas_informacion_manual['longitud_manual'].astype(float)
escuelas_informacion_manual['latitud_manual'] = escuelas_informacion_manual['latitud_manual'].astype(float)

## ACHICAMOS LA BBDD A UNIR CON EL GEOJSON
VARIABLES_A_ACTUALIZAR = ['codigo_unico_pis', 'nombre establecimiento a considerar', 'direccion_manual', 'cargo', 'nombre_apellido_manual', 'telefono_manual', 'mail_manual', 'matricula_2021', 'latitud_manual', 'longitud_manual', 'nueva_existente']
escuelas_informacion_manual = escuelas_informacion_manual[VARIABLES_A_ACTUALIZAR]

## UNIMOS LAS BASES DE DATOS CON LOS DATOS DE ESCUELAS EXISTENTES EN BBDD DE INDEC

### Separamos las bbdd segun si es escuela que está en el catastro o no
escuelas_existentes_informacion_manual = escuelas_informacion_manual[escuelas_informacion_manual['nueva_existente']=='Existente'].copy()
escuelas_nuevas_informacion_manual = escuelas_informacion_manual[escuelas_informacion_manual['nueva_existente']=='Nueva'].copy()

#### Unimos GeoJson con la info de escuelas existentes
base_escuelas_actualizada = pd.merge(establec_educativos_completo , escuelas_existentes_informacion_manual, on = VAR_CODIGO_UNICO, how = 'left')
base_escuelas_actualizada = base_escuelas_actualizada.drop(columns = ['geometry_indec'])

if len(escuelas_nuevas_informacion_manual):
    base_escuelas_actualizada = pd.concat([base_escuelas_actualizada, escuelas_nuevas_informacion_manual])

base_escuelas_actualizada[VAR_NOM_ESTABLEC] = base_escuelas_actualizada['nombre establecimiento a considerar'].fillna(base_escuelas_actualizada['nombre establecimiento']).str.title()
base_escuelas_actualizada[VAR_MAIL] = base_escuelas_actualizada['mail_manual'].fillna(base_escuelas_actualizada['mail_indec']).str.lower()
base_escuelas_actualizada[VAR_TELEFONO] = base_escuelas_actualizada['telefono_manual'].fillna(base_escuelas_actualizada['telefono_indec'])
base_escuelas_actualizada[VAR_DIRECCION] = base_escuelas_actualizada['direccion_manual'].fillna(base_escuelas_actualizada['direccion_indec']).str.title()
base_escuelas_actualizada[VAR_LATITUD] = base_escuelas_actualizada['latitud_manual'].fillna(base_escuelas_actualizada['latitud_indec'])
base_escuelas_actualizada[VAR_LONGITUD] = base_escuelas_actualizada['longitud_manual'].fillna(base_escuelas_actualizada['longitud_indec'])
base_escuelas_actualizada[VAR_NUEVA_EXISTENTE] = base_escuelas_actualizada[VAR_NUEVA_EXISTENTE].fillna('Existente')


COLS_TO_SAVE = [VAR_CODIGO_UNICO, VAR_CUE, 'clave provincial', 
                VAR_PARTIDO, VAR_COD_POSTAL,  VAR_NUEVA_EXISTENTE, VAR_SEDE_ANEXO_EXT, 
                'region educativa', VAR_NIVEL, VAR_NOM_ESTABLEC, VAR_DIRECCION, VAR_TELEFONO, VAR_MAIL, 
                VAR_LATITUD, VAR_LONGITUD]

base_escuelas_actualizada = base_escuelas_actualizada[COLS_TO_SAVE]


cup_manualmente_cargados = escuelas_informacion_manual[VAR_CODIGO_UNICO].unique()
cup_finales = base_escuelas_actualizada[VAR_CODIGO_UNICO].unique()
escuelas_faltantes = [c for c in cup_manualmente_cargados if c not in cup_finales]

print(f'Al cruzar los datos se pierden {len(escuelas_faltantes)} escuelas. Por favor, corregir y volver a correr el código. Este es el listado de escuelas faltantes: {escuelas_faltantes}')

base_escuelas_actualizada_gsjon = gpd.GeoDataFrame(base_escuelas_actualizada, geometry=gpd.points_from_xy(base_escuelas_actualizada[VAR_LONGITUD], base_escuelas_actualizada[VAR_LATITUD]), crs='EPSG:4326')
base_escuelas_actualizada_gsjon.to_file('./data/escuelas_informacion_actualizada_v230420.geojson', driver='GeoJSON')









