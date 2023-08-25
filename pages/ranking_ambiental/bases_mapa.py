import pandas as pd
import geopandas as gpd
import numpy as np
import math

# Leer archivo geojson y cargar datos.
bsas = gpd.read_file('pages/ranking_ambiental/limite_partidos_expandido.geojson', encoding="ASCI")
#bsas.columns=["cca", "cde", "Municipios", "gna", "nam","sag", "ara3", "arl", "geometry"]
bsas["Municipios"]=bsas["fna"].copy().apply(lambda x: str(x).replace("Partido de ", ""))

# Leer archivo csv y cargar datos de escuelas.
escuelas=pd.read_csv('pages/ranking_ambiental/escuelas_normativa.csv', sep=";",encoding="latin" )

#union de tablas para incorporar ranking 
bsas=pd.merge(bsas, escuelas[['Municipios', 'Puntaje - Escuelas rurales']], on='Municipios', how='left')

#Se crea variable con el nombre de la columna que contiene el listado de puntuación que hace al ranking
VAR_PUNTAJE="Puntaje - Escuelas rurales"

# Crear valores medios y clases.
bsas[VAR_PUNTAJE]=bsas[VAR_PUNTAJE].fillna(0).apply(lambda x: math.sqrt(int(x)))
min_value = bsas[VAR_PUNTAJE].min()
max_value = bsas[VAR_PUNTAJE].max()
middle_values = np.linspace(min_value, max_value, num=8, endpoint=True)
classes = list(middle_values)