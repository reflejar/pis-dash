import json
import pandas as pd
import geopandas as gpd
import numpy as np
import math
from dash import html
from pages.constantes import *

# Leer archivo geojson y cargar datos.
gba = gpd.read_parquet('pages/ranking_ambiental/data/gba_limite_partidos_expandido.parquet')
pba = gpd.read_parquet('pages/ranking_ambiental/data/bsas_provincia.parquet')

# Comuna Municipios
gba["Municipios"]=gba["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))
pba["Municipios"]=pba["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))

# # Leer archivo csv
# escuelas=pd.read_csv('pages/ranking_ambiental/data/escuelas_normativa.csv', sep=";",encoding="latin" )
# transparencia=pd.read_csv('pages/ranking_ambiental/data/transparencia_normativa.csv', sep=";",encoding="latin" )
# agua=pd.read_csv('pages/ranking_ambiental/data/agua_normativa.csv', sep=";",encoding="latin" )
# apiarios=pd.read_csv('pages/ranking_ambiental/data/apiarios_normativa.csv', sep=";",encoding="latin" )
# poblaciones=pd.read_csv('pages/ranking_ambiental/data/poblaciones_normativa.csv', sep=";",encoding="latin" )
# agroecologia=pd.read_csv('pages/ranking_ambiental/data/agroecologia_normativa.csv', sep=";",encoding="latin" )
# #etuiquetas para el mapa
# etiquetas=pd.read_csv('pages/ranking_ambiental/data/datos_etiquetas_mapas.csv', sep=";",encoding="latin" )

# Leer diccionario de municipios 
dicc=pd.read_csv("C:\Reflejar\data pis\dicc_municipios.csv",encoding="latin"  )
diccionario_municipios = dicc.set_index('Municipio2')['Municipio1'].to_dict()

# Leer archivo parquet
escuelas=pd.read_parquet('pages/ranking_ambiental/data/escuelas_normativa.parquet')
transparencia=pd.read_parquet('pages/ranking_ambiental/data/transparencia_normativa.parquet')
agua=pd.read_parquet('pages/ranking_ambiental/data/agua_normativa.parquet')
apiarios=pd.read_parquet('pages/ranking_ambiental/data/apiarios_normativa.parquet')
poblaciones=pd.read_parquet('pages/ranking_ambiental/data/poblaciones_normativa.parquet')
agroecologia=pd.read_parquet('pages/ranking_ambiental/data/agroecologia_normativa.parquet')
#etuiquetas para el mapa
etiquetas=pd.read_parquet('pages/ranking_ambiental/data/datos_etiquetas_mapas.parquet')

#Crear columnas para unir que tengan los nombres sin acento, para evitar problemas si estan escritos distinto
etiquetas["Municipios_nombre_original"]=etiquetas["Municipios"]
pba["Municipios_nombre_original"]=pba["Municipios"]
gba["Municipios_nombre_original"]=gba["Municipios"]

etiquetas["Municipios"]=etiquetas["Municipios"].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.strip()
pba["Municipios"]=pba["Municipios"].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.strip()
gba["Municipios"]=gba["Municipios"].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.strip()


etiquetas["Municipios"]=etiquetas["Municipios"].str.replace(" - Pigue","")

etiquetas=etiquetas.fillna("-")


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
            c=c + "\n" + "["  + i.strip()+ "]" + '(' + j.strip() + ')'
        rdo=c
    elif " y " in x[1]:
        a=x[0].strip()
        b=x[1].split("y")
        rdo= "[" + a+ "]" + '(' + b[0].strip() + ')'
    elif x[0]=="" or x[0]=="Sin Ordenanza":
        rdo="Sin Ordenanza"
    else:
        rdo="["  + x[0].strip()+ "]" + '(' + x[1].strip() + ')'
    return rdo

def preparar_base(base): 
    """
        función para preparar la base
    """    
    if 'Link - Repositorio' in base.columns:
        base = base.rename(columns={'Link - Repositorio': 'Link'})
    elif 'LINK' in base.columns: 
        base = base.rename(columns={'LOCALIDAD':'Municipios','LINK': 'Link','ORDENANZA': 'Ordenanza', 'FECHA': 'Fecha' , 'Puntaje - agroeco NORMALIZADO': 'Puntaje'})

    base["Municipios"] = base["Municipios"].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.strip()
    base["Ordenanza"] = base["Ordenanza"].fillna("Sin Ordenanza")

    base["Link"] = base["Link"].fillna("")
    base['Ordenanza'] = base['Ordenanza'].apply(lambda x: x if ("N°" in x) or (x=="") or (x=="Sin Ordenanza") or (x=="S/N") or ("N° " in x) else "N°"+x) 
    base['Ordenanza'] = base[['Ordenanza','Link' ]].apply(crear_link, axis=1) 


    base["Fecha"] = base["Fecha"].fillna("\-").apply(lambda x: x[-4:] if len(x)>=4 else x)

    base["Puntaje"]=base["Puntaje"].fillna(0).apply(lambda x:  round(float(x.replace(',', '.')), 2) if isinstance(x, str) else round(x, 2))
    # Identificar las columnas que no son numéricas
    non_numeric_columns = base.select_dtypes(exclude=['number']).columns
    # Llenar los valores faltantes en las columnas no numéricas con una cadena vacía
    base[non_numeric_columns] = base[non_numeric_columns].fillna("NO")

    # Reemplazar valores nulos en columnas numéricas con 0
    numeric_columns = base.select_dtypes(include=['number']).columns
    base[numeric_columns] = base[numeric_columns].fillna(0)
    # base["Puntaje"]=base["Puntaje"].fillna(0).apply(lambda x: round(math.sqrt(x), 2) )
    
    base["Fecha"]=base["Fecha"].apply(lambda x: x if x!="\-" else "")
    base = base.rename(columns={"Fecha": "Año"})
    del base["Link"]
    return base

escuelas=preparar_base(escuelas)
transparencia=preparar_base(transparencia)
agua=preparar_base(agua)
apiarios=preparar_base(apiarios)
poblaciones=preparar_base(poblaciones)
agroecologia=preparar_base(agroecologia)

def concatenar_base_mapa(mapa, base):
    """
        función para mergear las bases con la base del mapa
    """    
    a=base.copy()
    final_mapa=pd.merge(mapa, a[['Municipios', "Puntaje"]], on='Municipios', how='left')
    final_mapa["Puntaje"]=final_mapa["Puntaje"].fillna(0)
    return final_mapa

def agregar_etiquetas_mapa(mapa, etiquetas):
    """
        función para agregar tooltip a las bases con el geojson
    """    
    final_mapa=pd.merge(mapa, etiquetas, on='Municipios', how='left')
    #Volver a poner los nombres originales y descartar la columna adicional
    final_mapa["Municipios"]=final_mapa["Municipios_nombre_original_y"]
    final_mapa=final_mapa.drop(columns=["Municipios_nombre_original_x","Municipios_nombre_original_y"])
    puntaje=final_mapa["Puntaje"].apply(lambda x: str(x))
    # Agregar informacion de etiquetas
    final_mapa["tooltip"] = '<b>Partido</b>: '+ final_mapa["nam"] + '<br>'+'<b>Puntaje</b>: '  + puntaje+ '<br>'+'<b>Habitantes</b>: '+final_mapa["Habitantes (CENSO 2022)"].apply(lambda x: str(x).split(".")[0]) + '<br>'+'<b>Intendente</b>: '+final_mapa["INTENDENTE"] + '<br>'+'<b>Afiliación política</b>: '+final_mapa["AFILIACIÓN POLÍTICA"] 
    final_mapa["popup"] = final_mapa["tooltip"]
    return final_mapa

def crear_classes(base):
    """
        función para crear los diferentes valores de las clases
    """        
    min_value = base["Puntaje"].min() 
    max_value = base["Puntaje"].max()
    middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
    return list(middle_values)

def reemplazar_municipios(base):
    base["Municipios"]=base["Municipios"].replace(diccionario_municipios)
    return base

clases_escuelas=crear_classes(escuelas)
clases_transparencia=crear_classes(transparencia)
clases_agua=crear_classes(agua)
clases_poblaciones=crear_classes(poblaciones)
clases_apiarios=crear_classes(apiarios)
clases_agroecologia=crear_classes(agroecologia)


def crear_geojson (map, tabla_puntaje, etiquetas ):
    """
        función para crear el geojson
    """ 
    mapa=concatenar_base_mapa(map, tabla_puntaje) 
    mapa=agregar_etiquetas_mapa(mapa, etiquetas)

    return json.loads(mapa.to_json(na="keep"))


# Preparamos datas
DATA = {
    'escuelas': {
        'geojson_pba': crear_geojson(pba,escuelas, etiquetas),
        'geojson_gba': crear_geojson(gba, escuelas, etiquetas),
        'data': reemplazar_municipios(escuelas),
        'classes': clases_escuelas,
        'color': ROJO,
        'color_claro':ROJO_CLARO
    },
    'transparencia': {
        'geojson_pba': crear_geojson(pba,transparencia, etiquetas),
        'geojson_gba': crear_geojson(gba,transparencia,  etiquetas),
        'data': reemplazar_municipios(transparencia),
        'classes': clases_transparencia,
        'color': LILA,
        'color_claro':LILA_CLARO
    },
    'agua': {
        'geojson_pba': crear_geojson(pba, agua, etiquetas),
        'geojson_gba': crear_geojson(gba, agua,etiquetas),
        'data': reemplazar_municipios(agua),
        'classes': clases_agua,
        'color': VERDE_AGUA,
        'color_claro':VERDE_AGUA_CLARO
    },
    'poblaciones': {
        'geojson_pba': crear_geojson(pba, poblaciones, etiquetas),
        'geojson_gba': crear_geojson(gba, poblaciones,etiquetas),
        'data': reemplazar_municipios(poblaciones),
        'classes': clases_poblaciones,
        'color': LIMA,
        'color_claro':LIMA_CLARO
    },
    'apiarios': {
        'geojson_pba': crear_geojson(pba, apiarios, etiquetas),
        'geojson_gba': crear_geojson(gba,apiarios,  etiquetas),
        'data': reemplazar_municipios(apiarios),
        'classes': clases_apiarios,
        'color': NARANJA,
        'color_claro':NARANJA_CLARO
    },
    'agroecologia': {
        'data': agroecologia,
        'geojson_pba': crear_geojson(pba, agroecologia,  etiquetas),
        'geojson_gba': crear_geojson(gba, agroecologia,  etiquetas), 
        'data': reemplazar_municipios(agroecologia),
        'classes': clases_agroecologia,
        'color': CELESTE,
        'color_claro':CELESTE_CLARO
    },
}
etiquetas['Municipios'].str.contains('Rojas').sum()
pba['Municipios'].str.contains('Rojas').sum()

(etiquetas['Municipios']=='Rojas').sum()
(pba['Municipios']=='Rojas').sum()
