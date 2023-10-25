import json
import pandas as pd
import geopandas as gpd
import numpy as np
import math
from dash import html
from pages.constantes import *

# Leer archivo geojson y cargar datos.
gba = gpd.read_file('pages/ranking_ambiental/data/gba_limite_partidos_expandido.geojson', encoding="ASCI")

pba = gpd.read_file('pages/ranking_ambiental/data/bsas_provincia.geojson', encoding="ASCI")
#gba.columns=["cca", "cde", "Municipios", "gna", "nam","sag", "ara3", "arl", "geometry"]
gba["Municipios"]=gba["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))
pba["Municipios"]=pba["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))





# Leer archivo csv y cargar datos de escuelas.
escuelas=pd.read_csv('pages/ranking_ambiental/data/escuelas_normativa.csv', sep=";",encoding="latin" )



def func(x):
    if " y " in x[0] or "--y--" in x[1]:
        a=x[0].split("y")
        b=x[1].split("--y--")
        c=""
        for i,j in zip(a,b):
            c=c + "\n" + "[" +"Ord. " + i.strip()+ "]" + '(' + j.strip() + ')'
        rdo=c
    elif " y " in x[1]:
        a=x[0].strip()
        b=x[1].split("y")
        rdo= "[" +"Ord. "+ a+ "]" + '(' + b[0].strip() + ')'
    elif x[0]=="" or x[0]=="Sin Ordenanza":
        rdo="Sin Ordenanza"
    else:
        rdo="[" + "Ord. " + x[0].strip()+ "]" + '(' + x[1].strip() + ')'
    return rdo

escuelas["Ordenanza"] = escuelas["Ordenanza"].fillna("Sin Ordenanza")
escuelas["Link"] = escuelas["Link"].fillna("")
escuelas['Ordenanza'] = escuelas[['Ordenanza','Link' ]].apply(func, axis=1) 


escuelas["Fecha"] = escuelas["Fecha"].fillna("\-")

# Reemplazar valores nulos en columnas de tipo objeto con 'NO'
columna_especifica = "Obligatoriedad de notificación"
escuelas[columna_especifica] = escuelas[columna_especifica].fillna('NO')

# Reemplazar valores nulos en la columna específica con '-'
columna_especifica = 'Puntaje'
escuelas[columna_especifica] = escuelas[columna_especifica].fillna('-')

# Reemplazar valores nulos en columnas numéricas con 0
numeric_columns = escuelas.select_dtypes(include=['number']).columns
escuelas[numeric_columns] = escuelas[numeric_columns].fillna(0)
del escuelas["Link"]





#union de tablas para incorporar ranking 
gba=pd.merge(gba, escuelas[['Municipios', 'Puntaje']], on='Municipios', how='left')
pba=pd.merge(pba, escuelas[['Municipios', 'Puntaje']], on='Municipios', how='left')

#Se crea variable con el nombre de la columna que contiene el listado de puntuación que hace al ranking
VAR_PUNTAJE="Puntaje"

# Crear valores medios y clases.
gba[VAR_PUNTAJE]=gba[VAR_PUNTAJE].fillna(0).apply(lambda x: math.sqrt(x) )
min_value = gba[VAR_PUNTAJE].min()
max_value = gba[VAR_PUNTAJE].max()
middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
classes = list(middle_values)
# Crear valores medios y clases.
pba[VAR_PUNTAJE]=pba[VAR_PUNTAJE].fillna(0).apply(lambda x: math.sqrt(x) )
min_value = pba[VAR_PUNTAJE].min()
max_value = pba[VAR_PUNTAJE].max()
middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
classes = list(middle_values)

# Agregar informacion de etiquetas
gba["tooltip"] = gba["nam"]
pba["tooltip"] = pba["nam"]

gba_geojson = json.loads(gba.to_json(na="keep"))
pba_geojson = json.loads(pba.to_json(na="keep"))

# Preparamos datas
DATA = {
    'escuelas': {
        'data': escuelas,
        'geojson_pba': pba_geojson,
        'geojson_gba': gba_geojson,
        'color': ROJO
    },
    'transparencia': {
        'data': escuelas,
        'geojson_pba': gba_geojson,
        'geojson_gba': gba_geojson,
        'color': NARANJA
    },
    'agua': {
        'data': escuelas,
        'geojson_pba': gba_geojson,
        'geojson_gba': gba_geojson,
        'color': VERDE_AGUA
    },
    'poblaciones': {
        'data': escuelas,
        'geojson_pba': gba_geojson,
        'geojson_gba': gba_geojson,
        'color': LIMA
    },
    'apiarios': {
        'data': escuelas,
        'geojson_pba': gba_geojson,
        'geojson_gba': gba_geojson,
        'color': LILA
    },
    'agroecologia': {
        'data': escuelas,
        'geojson_pba': gba_geojson,
        'geojson_gba': gba_geojson,
        'color': CELESTE
    },
}
