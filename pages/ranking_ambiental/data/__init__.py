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
transparencia=pd.read_csv('pages/ranking_ambiental/data/transparencia_normativa.csv', sep=";",encoding="latin" )
agua=pd.read_csv('pages/ranking_ambiental/data/agua_normativa.csv', sep=";",encoding="latin" )
apiarios=pd.read_csv('pages/ranking_ambiental/data/apiarios_normativa.csv', sep=";",encoding="latin" )
poblaciones=pd.read_csv('pages/ranking_ambiental/data/poblaciones_normativa.csv', sep=";",encoding="latin" )
agroecologia=pd.read_csv('pages/ranking_ambiental/data/agroecologia_normativa.csv', sep=";",encoding="latin" )


def crear_link(x):
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

def preparar_base(base): 
    if 'Link - Repositorio' in base.columns:
        base.rename(columns={'Link - Repositorio': 'Link'}, inplace=True)
    elif 'LINK' in base.columns: 
        base.rename(columns={'LOCALIDAD':'Municipios','LINK': 'Link','ORDENANZA': 'Ordenanza', 'FECHA': 'Fecha' , 'Puntaje - agroeco NORMALIZADO': 'Puntaje'}, inplace=True)
    

    base["Ordenanza"] = base["Ordenanza"].fillna("Sin Ordenanza")

    base["Link"] = base["Link"].fillna("")
    base['Ordenanza'] = base[['Ordenanza','Link' ]].apply(crear_link, axis=1) 


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
    base["Puntaje"]=base["Puntaje"].fillna(0).apply(lambda x: round(math.sqrt(x), 2) )
    del base["Link"]
    return base

escuelas=preparar_base(escuelas)
transparencia=preparar_base(transparencia)
agua=preparar_base(agua)
apiarios=preparar_base(apiarios)
poblaciones=preparar_base(poblaciones)
agroecologia=preparar_base(agroecologia)

def crear_geojson(mapa, base):
    # union de tablas para incorporar ranking 
    final_mapa=pd.merge(mapa, base[['Municipios', 'Puntaje']], on='Municipios', how='left')
    # Agregar informacion de etiquetas
    final_mapa["tooltip"] = final_mapa["nam"]
    return json.loads(final_mapa.to_json(na="keep"))

def crear_classes(base):
    min_value = base["Puntaje"].min()
    max_value = base["Puntaje"].max()
    middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
    return list(middle_values)



# Preparamos datas
DATA = {
    'escuelas': {
        'data': escuelas,
        'geojson_pba': crear_geojson(pba, escuelas),
        'geojson_gba': crear_geojson(gba, escuelas),
        'classes': crear_classes(escuelas),
        'color': ROJO
    },
    'transparencia': {
        'data': transparencia,
        'geojson_pba': crear_geojson(pba, transparencia),
        'geojson_gba': crear_geojson(gba, transparencia),
        'classes': crear_classes(transparencia),
        'color': NARANJA
    },
    'agua': {
        'data': agua,
        'geojson_pba': crear_geojson(pba, agua),
        'geojson_gba': crear_geojson(gba, agua),
        'classes': crear_classes(agua),
        'color': VERDE_AGUA
    },
    'poblaciones': {
        'data': poblaciones,
        'geojson_pba': crear_geojson(pba, poblaciones),
        'geojson_gba': crear_geojson(gba, poblaciones),
        'classes': crear_classes(poblaciones),
        'color': LIMA
    },
    'apiarios': {
        'data': apiarios,
        'geojson_pba': crear_geojson(pba, apiarios),
        'geojson_gba': crear_geojson(gba, apiarios),
        'classes': crear_classes(apiarios),
        'color': LILA
    },
    'agroecologia': {
        'data': agroecologia,
        'geojson_pba': crear_geojson(pba, agroecologia),
        'geojson_gba': crear_geojson(gba, agroecologia),
        'classes': crear_classes(agroecologia),
        'color': CELESTE
    },
}
