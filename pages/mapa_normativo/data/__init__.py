import os
import geopandas as gpd
import json
import pandas as pd
from itertools import combinations
from ..data.Inputs.constantes_mapa_normativo import *

MUNICIPIOS = ['Mar Chiquita']



FOLDER = os.path.dirname(os.path.abspath(__file__))

###### Se importan las bases de los objetos representados en el mapa ##############
cuerpos=gpd.read_parquet(f"{FOLDER}/cuerpos.parquet")
localidades_parajes=gpd.read_parquet(f"{FOLDER}/localidades_parajes.parquet")
escuelas_parcelas=gpd.read_parquet(f"{FOLDER}/escuelas_parcelas.parquet")
reservas=gpd.read_parquet(f"{FOLDER}/reservas.parquet")
cursos=gpd.read_parquet(f"{FOLDER}/cursos_agua.parquet")

###### Se importan las bases de las zonas de exclusion y amortiguamiento de cada objeto ############
cuerpos_excl=gpd.read_parquet(f"{FOLDER}/cuerpos_excl.parquet")
cursos_excl=gpd.read_parquet(f"{FOLDER}/cursos_excl.parquet")
localidades_excl=gpd.read_parquet(f"{FOLDER}/localidades_excl.parquet")
parajes_excl=gpd.read_parquet(f"{FOLDER}/parajes_excl.parquet")
escuelas_parcelas_excl=gpd.read_parquet(f"{FOLDER}/escuelas_parcelas_excl.parquet")
localidades_amort=gpd.read_parquet(f"{FOLDER}/localidades_amort.parquet")
parajes_amort=gpd.read_parquet(f"{FOLDER}/parajes_amort.parquet")
escuelas_parcelas_amort=gpd.read_parquet(f"{FOLDER}/escuelas_parcelas_amort.parquet")

################ Se crea una columna llamada "tooltip" que luego sirve como etiqueta en el mapa #############
cursos["tooltip"]="<b>Nombre</b>: "+cursos["NOMBRE"]+'<extra></extra>'
cursos["popup"]=cursos["tooltip"]

concat_cols = lambda row: '<b>Nombre</b>: '+ row['nombre.establecimiento']+'<br>'+'<b>Nivel</b>: ' + row['nivel'] + '<br>'+'<b>Teléfono</b>: '+row["Tel"]+'<br>'+'<b>Email</b>: '+row["email"]+ ("<hr>"+ '<b>Nombre</b>: '+ row['nombre.establecimiento1']+'<br>'+'<b>Nivel</b>: ' + row['nivel1']+ '<br>'+'<b>Teléfono</b>: '+row["Tel1"]+'<br>'+'<b>Email</b>: '+row["email1"] if row['nombre.establecimiento1']!="-" or row['nivel1']!="-" else '')

escuelas_parcelas['tooltip'] = escuelas_parcelas.apply(concat_cols, axis=1)
escuelas_parcelas['count'] = escuelas_parcelas['tooltip'].apply(lambda x: x.count("<b>Nivel</b>"))
escuelas_parcelas['tooltip'] = escuelas_parcelas.apply(lambda row: "<b>Edificio Escolar Compartido</b><br><br>"  + row['tooltip'] if row['count'] > 1 else row['tooltip'], axis=1)

#escuelas_parcelas["tooltip"]='<b>Nombre</b>: '+escuelas_parcelas["nombre.establecimiento"]+'<br>'+'<b>Nivel</b>: '+escuelas_parcelas["nivel"]+ '<br>'+'<b>Teléfono</b>: '+escuelas_parcelas["Tel"]+'<br>'+'<b>Email</b>: '+escuelas_parcelas["email"]+'<extra></extra>'
escuelas_parcelas["popup"]=escuelas_parcelas["tooltip"]

cuerpos["tooltip"]='<b>Nombre</b>: '+cuerpos["NOMBRE"]+'<br>'+'<b>Tipo</b>: '+cuerpos['TIPO']+'<extra></extra>'
cuerpos["popup"]=cuerpos["tooltip"]

reservas["tooltip"]="<b>Nombre</b>: "+reservas["Name"]
reservas["popup"]="<b>Nombre</b>: "+reservas["Name"]

localidades_parajes["tooltip"]='<b>Nombre</b>: '+localidades_parajes[VAR_NOMBRE_HOVER]+'<br>'+'<b>Habitantes</b>: '+localidades_parajes[VAR_HABITANTES_HOVER]+'<br>'+ '<b>Categoría</b>: '+localidades_parajes[VAR_CATEGORIA_INDEC] + '<extra></extra>'
localidades_parajes["popup"]=localidades_parajes["tooltip"]


################ se pasan las tablas a json #################################################################

cursos_geojson = json.loads(cursos.to_json(na="keep"))
cuerpos_geojson = json.loads(cuerpos.to_json(na="keep"))
localidades_parajes_geojson=json.loads(localidades_parajes.to_json(na="keep"))
escuelas_parcelas_geojson = json.loads(escuelas_parcelas.to_json(na="keep"))
reservas_geojson = json.loads(reservas.to_json(na="keep"))

amortiguacion=gpd.read_parquet(f"{FOLDER}/amortiguacion.parquet")
exclusion=gpd.read_parquet(f"{FOLDER}/exclusion.parquet")
