import json
import pandas as pd
import geopandas as gpd
import numpy as np
import math
from dash import html
from pages.constantes import *

# Leer archivo geojson y cargar datos.
bsas = gpd.read_file('pages/ranking_ambiental/data/limite_partidos_expandido.geojson', encoding="ASCI")
#bsas.columns=["cca", "cde", "Municipios", "gna", "nam","sag", "ara3", "arl", "geometry"]
bsas["Municipios"]=bsas["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))

# Leer archivo csv y cargar datos de escuelas.
escuelas=pd.read_csv('pages/ranking_ambiental/data/escuelas_normativa.csv', sep=";",encoding="latin" )
transparencia=pd.read_csv('pages/ranking_ambiental/data/transparencia_normativa.csv', sep=";",encoding="latin" )
agua=pd.read_csv('pages/ranking_ambiental/data/agua_normativa.csv', sep=";",encoding="latin" )
apiarios=pd.read_csv('pages/ranking_ambiental/data/apiarios_normativa.csv', sep=";",encoding="latin" )
poblaciones=pd.read_csv('pages/ranking_ambiental/data/poblaciones_normativa.csv', sep=";",encoding="latin" )
agroecologia=pd.read_csv('pages/ranking_ambiental/data/agroecologia_normativa.csv', sep=";",encoding="latin" )


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

def crear_base(base): 
    if 'Link - Repositorio' in base.columns:
        base.rename(columns={'Link - Repositorio': 'Link'}, inplace=True)
    elif 'LINK' in base.columns: 
        base.rename(columns={'LOCALIDAD':'Municipios','LINK': 'Link','ORDENANZA': 'Ordenanza', 'FECHA': 'Fecha' , 'Puntaje - agroeco NORMALIZADO': 'Puntaje'}, inplace=True)
    

    base["Ordenanza"] = base["Ordenanza"].fillna("Sin Ordenanza")

    base["Link"] = base["Link"].fillna("")
    base['Ordenanza'] = base[['Ordenanza','Link' ]].apply(func, axis=1) 


    base["Fecha"] = base["Fecha"].fillna("\-")

    # # Reemplazar valores nulos en columnas de tipo objeto con 'NO'
    # columna_especifica = "Obligatoriedad de notificación"
    # base[columna_especifica] = base[columna_especifica].fillna('NO')

    # # Reemplazar valores nulos en la columna específica con '-'
    # columna_especifica = 'Puntaje'
    # base[columna_especifica] = base[columna_especifica].fillna(0)

    # Identificar las columnas que no son numéricas
    non_numeric_columns = base.select_dtypes(exclude=['number']).columns
    # Llenar los valores faltantes en las columnas no numéricas con una cadena vacía
    base[non_numeric_columns] = base[non_numeric_columns].fillna("NO")

    # Reemplazar valores nulos en columnas numéricas con 0
    numeric_columns = base.select_dtypes(include=['number']).columns
    base[numeric_columns] = base[numeric_columns].fillna(0)
    del base["Link"]
    return base

escuelas=crear_base(escuelas)
transparencia=crear_base(transparencia)
agua=crear_base(agua)
apiarios=crear_base(apiarios)
poblaciones=crear_base(poblaciones)
agroecologia=crear_base(agroecologia)


def crear_mapa(mapa, base, nombre_columna_puntaje):
    #union de tablas para incorporar ranking 
    mapa_1=pd.merge(mapa, base[['Municipios', 'Puntaje']], on='Municipios', how='left')
    
    # Crear valores medios y clases.
    mapa_1[nombre_columna_puntaje]=mapa_1[nombre_columna_puntaje].fillna(0).apply(lambda x: math.sqrt(x) )
    min_value = mapa_1[nombre_columna_puntaje].min()
    max_value = mapa_1[nombre_columna_puntaje].max()
    middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
    classes = list(middle_values)
    # Agregar informacion de etiquetas
    mapa_1["tooltip"] = mapa_1["nam"]

    mapa_geojson = json.loads(mapa_1.to_json(na="keep"))
    return mapa_geojson, classes

#Se crea variable con el nombre de la columna que contiene el listado de puntuación que hace al ranking
VAR_PUNTAJE="Puntaje"

mapa_escuelas, clases_escuelas=crear_mapa(bsas, escuelas, VAR_PUNTAJE)
mapa_transparencia, clases_transparencia=crear_mapa(bsas, transparencia, VAR_PUNTAJE)
mapa_agua, clases_agua=crear_mapa(bsas, agua, VAR_PUNTAJE)
mapa_apiarios, clases_apiarios=crear_mapa(bsas, apiarios, VAR_PUNTAJE)
mapa_poblaciones, clases_poblaciones=crear_mapa(bsas, poblaciones, VAR_PUNTAJE)
mapa_agroecologia, clases_agroecologia=crear_mapa(bsas, agroecologia, VAR_PUNTAJE)

# Preparamos datas
DATA = {
    'escuelas': {
        'data': escuelas,
        'geojson_bsas': mapa_escuelas,
        'geojson_caba': mapa_escuelas,
        'classes': clases_escuelas,
        'color': ROJO
    },
    'transparencia': {
        'data': transparencia,
        'geojson_bsas': mapa_transparencia,
        'geojson_caba': mapa_transparencia,
        'classes': clases_transparencia,
        'color': NARANJA
    },
    'agua': {
        'data': agua,
        'geojson_bsas': mapa_agua,
        'geojson_caba': mapa_agua,
        'classes': clases_agua,
        'color': VERDE_AGUA
    },
    'poblaciones': {
        'data': poblaciones,
        'geojson_bsas': mapa_poblaciones,
        'geojson_caba': mapa_poblaciones,
        'classes': clases_poblaciones,
        'color': LIMA
    },
    'apiarios': {
        'data': apiarios,
        'geojson_bsas': mapa_apiarios,
        'geojson_caba': mapa_apiarios,
        'classes': clases_apiarios,
        'color': LILA
    },
    'agroecologia': {
        'data': agroecologia,
        'geojson_bsas': mapa_agroecologia,
        'geojson_caba': mapa_agroecologia,
        'classes': clases_agroecologia,
        'color': CELESTE
    },
}
