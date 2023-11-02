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

# Comuna Municipios
gba["Municipios"]=gba["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))
pba["Municipios"]=pba["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))

# Leer archivo csv
escuelas=pd.read_csv('pages/ranking_ambiental/data/escuelas_normativa.csv', sep=";",encoding="latin" )
transparencia=pd.read_csv('pages/ranking_ambiental/data/transparencia_normativa.csv', sep=";",encoding="latin" )
agua=pd.read_csv('pages/ranking_ambiental/data/agua_normativa.csv', sep=";",encoding="latin" )
apiarios=pd.read_csv('pages/ranking_ambiental/data/apiarios_normativa.csv', sep=";",encoding="latin" )
poblaciones=pd.read_csv('pages/ranking_ambiental/data/poblaciones_normativa.csv', sep=";",encoding="latin" )
agroecologia=pd.read_csv('pages/ranking_ambiental/data/agroecologia_normativa.csv', sep=";",encoding="latin" )
#etuiquetas para el mapa
etiquetas=pd.read_csv('pages/ranking_ambiental/data/datos_etiquetas_mapas.csv', sep=";",encoding="latin" )

def crear_link(x):
    """
        función para limpiar el link
        y convertirlo a formato Markdown
    """
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
    """
        función para preparar la base
    """    
    if 'Link - Repositorio' in base.columns:
        base = base.rename(columns={'Link - Repositorio': 'Link'})
    elif 'LINK' in base.columns: 
        base = base.rename(columns={'LOCALIDAD':'Municipios','LINK': 'Link','ORDENANZA': 'Ordenanza', 'FECHA': 'Fecha' , 'Puntaje - agroeco NORMALIZADO': 'Puntaje'})
    

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
    base["Fecha"]=base["Fecha"].apply(lambda x: x if x!="\-" else "")
    del base["Link"]
    return base

escuelas=preparar_base(escuelas)
transparencia=preparar_base(transparencia)
agua=preparar_base(agua)
apiarios=preparar_base(apiarios)
poblaciones=preparar_base(poblaciones)
agroecologia=preparar_base(agroecologia)

def concatenar_base_mapa(mapa, base, nombre_normativa):
    """
        función para mergear las bases con la base del mapa
    """    
    a=base.copy()
    a = a.rename(columns={'Puntaje': nombre_normativa})
    # union de tablas para incorporar ranking 
    final_mapa=pd.merge(mapa, a[['Municipios', nombre_normativa]], on='Municipios', how='left')
    final_mapa[nombre_normativa]=final_mapa[nombre_normativa].fillna(0)
    return final_mapa

def agregar_etiquetas_mapa(mapa, etiquetas):
    """
        función para agregar tooltip a las bases con el geojson
    """    
    final_mapa=pd.merge(mapa, etiquetas, on='Municipios', how='left')
    # Agregar informacion de etiquetas
    final_mapa["tooltip"] = final_mapa['nam']+ '\n' + "Cantidad de habitantes: " + final_mapa['Habitantes (CENSO 2022)']
    return final_mapa

gba=agregar_etiquetas_mapa(gba, etiquetas)
pba=agregar_etiquetas_mapa(pba, etiquetas)

def crear_classes(base):
    """
        función para crear los diferentes valores de las clases
    """        
    min_value = base["Puntaje"].min()
    max_value = base["Puntaje"].max()
    middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
    return list(middle_values)

clases_escuelas=crear_classes(escuelas)
clases_transparencia=crear_classes(transparencia)
clases_agua=crear_classes(agua)
clases_poblaciones=crear_classes(poblaciones)
clases_apiarios=crear_classes(apiarios)
clases_agroecologia=crear_classes(agroecologia)

pba=concatenar_base_mapa(pba, escuelas, "escuelas")
gba=concatenar_base_mapa(gba, escuelas, "escuelas")
pba=concatenar_base_mapa(pba, transparencia, "transparencia")
gba=concatenar_base_mapa(gba, transparencia, "transparencia")
pba=concatenar_base_mapa(pba, agua, "agua")
gba=concatenar_base_mapa(gba, agua, "agua")
pba=concatenar_base_mapa(pba, poblaciones, "poblaciones")
gba=concatenar_base_mapa(gba, poblaciones, "poblaciones")
pba=concatenar_base_mapa(pba, apiarios, "apiarios")
gba=concatenar_base_mapa(gba, apiarios, "apiarios")
pba=concatenar_base_mapa(pba, agroecologia, "agroecologia")
gba=concatenar_base_mapa(gba, agroecologia, "agroecologia")

def crear_geojson (mapa, filtro):
    """
        función para crear los diferentes geojson
    """ 
    mapa=mapa[['cca', 'cde', 'fna', 'gna', 'nam', 'sag', 'ara3', 'arl', 'geometry','Municipios', 'tooltip', filtro]]
    mapa = mapa.rename(columns={filtro:'Puntaje'})
    return json.loads(mapa.to_json(na="keep"))


# Preparamos datas
DATA = {
    'escuelas': {
        'data': escuelas,
        'geojson_pba': crear_geojson(pba, "escuelas"),
        'geojson_gba': crear_geojson(gba, "escuelas"),
        'classes': clases_escuelas,
        'color': ROJO,
        'color_claro':ROJO_CLARO
    },
    'transparencia': {
        'data': transparencia,
        'geojson_pba': crear_geojson(pba, "transparencia"),
        'geojson_gba': crear_geojson(gba, "transparencia"),
        'classes': clases_transparencia,
        'color': NARANJA,
        'color_claro':NARANJA_CLARO
    },
    'agua': {
        'data': agua,
        'geojson_pba': crear_geojson(pba, "agua"),
        'geojson_gba': crear_geojson(gba, "agua"),
        'classes': clases_agua,
        'color': VERDE_AGUA,
        'color_claro':VERDE_AGUA_CLARO
    },
    'poblaciones': {
        'data': poblaciones,
        'geojson_pba': crear_geojson(pba, "poblaciones"),
        'geojson_gba': crear_geojson(gba, "poblaciones"),
        'classes': clases_poblaciones,
        'color': LIMA,
        'color_claro':LIMA_CLARO
    },
    'apiarios': {
        'data': apiarios,
        'geojson_pba': crear_geojson(pba, "apiarios"),
        'geojson_gba': crear_geojson(gba, "apiarios"),
        'classes': clases_apiarios,
        'color': LILA,
        'color_claro':LILA_CLARO
    },
    'agroecologia': {
        'data': agroecologia,
        'geojson_pba': crear_geojson(pba, "agroecologia"),
        'geojson_gba': crear_geojson(gba, "agroecologia"), 
        'classes': clases_agroecologia,
        'color': CELESTE,
        'color_claro':CELESTE_CLARO
    },
}
