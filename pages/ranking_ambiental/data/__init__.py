import pandas as pd
import geopandas as gpd
import numpy as np
import math

# Leer archivo geojson y cargar datos.
bsas = gpd.read_file('pages/ranking_ambiental/data/limite_partidos_expandido.geojson', encoding="ASCI")
#bsas.columns=["cca", "cde", "Municipios", "gna", "nam","sag", "ara3", "arl", "geometry"]
bsas["Municipios"]=bsas["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))





# Leer archivo csv y cargar datos de escuelas.
escuelas=pd.read_csv('pages/ranking_ambiental/data/escuelas_normativa.csv', sep=";",encoding="latin" )
escuelas["Ordenanza"] = escuelas["Ordenanza"].fillna("").apply(lambda x: "Ord. " + str(x) if x!="" else "Sin ordenanza")
escuelas["Fecha"] = escuelas["Fecha"].fillna("-")

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
bsas=pd.merge(bsas, escuelas[['Municipios', 'Puntaje']], on='Municipios', how='left')

#Se crea variable con el nombre de la columna que contiene el listado de puntuación que hace al ranking
VAR_PUNTAJE="Puntaje"

# Crear valores medios y clases.
bsas[VAR_PUNTAJE]=bsas[VAR_PUNTAJE].fillna(0).apply(lambda x: math.sqrt(x) )
min_value = bsas[VAR_PUNTAJE].min()
max_value = bsas[VAR_PUNTAJE].max()
middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
classes = list(middle_values)