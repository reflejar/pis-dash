# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 00:06:34 2022

@author: simon
"""
import plotly.io as pio
pio.renderers.default='browser'

import geopandas as gpd
import json
import plotly.graph_objects as go
import numpy as np
import shapely
from shapely.geometry import box
from shapely.geometry import Point, Polygon
import pandas as pd
import plotly.express as px
pd.options.display.float_format = '{:.0f}'.format
import pickle
from itertools import combinations

#Definir parametros de zonas de exclusion y amortiguamiento
local_excl=150
local_amort=500
par_excl=50
par_amort=500
esc_excl=200
esc_amort=500
sup_agua_excl=25

# #### Localidades y parajes #####

# #Leemos input y los transformamos a la proyeccion que usamos
localidades=gpd.read_file("pages/mapa_normativo/data/Inputs/Localidades.geojson")
localidades=localidades.reset_index()
localidades = localidades.to_crs("epsg:4326")
#Lista de localidades para chequear
localidades['Tipo'] = 'Localidad'
localidades['Name'] = localidades['Name'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')
listado_localidades = localidades['Name'].unique()

# #Parajes
parajes=gpd.read_file("pages/mapa_normativo/data/Inputs/Parajes.geojson")
parajes=parajes.reset_index()
parajes = parajes.to_crs("epsg:4326")
#Lista de parajes para chequear
parajes['Tipo'] = 'Paraje'
parajes['Name'] = parajes['Name'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')
listado_parajes = parajes['Name'].unique()

##Unir localidades y parajes
localidades_parajes=pd.concat([localidades,parajes],ignore_index=True)
#Lista de localidades y parajes para chequear
listado_localidades_parajes = localidades_parajes['Name'].unique()


# Chequeo de parajes y localdiades - Revision de repetidos
poblados_repetidos = [c for c in listado_parajes if c in listado_localidades]
cantidad_poblados_repetidos = len(poblados_repetidos)
mensaje_repetidos = f'Al comparar la lista de parajes con la lista de localidades, encontramos {cantidad_poblados_repetidos} poblados repetidos, que son los siguientes: {poblados_repetidos}'
print(mensaje_repetidos)

#Agregar otros datos a las localidades y parajes
poblacion=pd.read_excel("pages\mapa_normativo\data\Inputs\Base de Datos - Mar Chiquita.xlsx")
poblacion['Name'] = poblacion['Nombre'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.strip()
poblacion = poblacion[poblacion['Name'].isin(listado_localidades_parajes)]
listado_poblados = poblacion['Name'].unique()

# Chequeo de parajes y localdiades - Revision de localidades y parajes perdidos
poblados_perdidos = [c for c in listado_poblados   if c not in listado_localidades_parajes]
cantidad_poblados_perdidos = len(poblados_perdidos)
mensaje_perdidos = f'Al comparar la lista original localidades y parajes con la lista luego de poblaciones, encontramos {cantidad_poblados_perdidos} poblados perdidos. {poblados_perdidos}'
#print(mensaje_perdidos)

#Unimos poblados con localdiades y parajes
base_localidades_parajes = pd.merge(localidades_parajes, poblacion, on = 'Name', how='left')
base_localidades_parajes['Nombre'] = base_localidades_parajes['Nombre'].fillna(base_localidades_parajes['Name'])
base_localidades_parajes['Nombre'] = base_localidades_parajes['Nombre'] + ", " + base_localidades_parajes['Partido']
base_localidades_parajes = base_localidades_parajes.drop(columns = ['Ubicación', 'Polígono', 'index'])
base_localidades_parajes["Habitantes"]=base_localidades_parajes["Habitantes"].fillna("-")
base_localidades_parajes["Habitantes"] = base_localidades_parajes["Habitantes"].astype(str).replace('\.0', '', regex=True)
base_localidades_parajes["Habitantes"] = base_localidades_parajes["Habitantes"] + ' ('+  base_localidades_parajes["Censo"] +')'

# Dividimos segun paraje o localidad

base_final_paraje = base_localidades_parajes[base_localidades_parajes['Tipo']=='Paraje']

base_final_paraje.to_file('pages/mapa_normativo/data/Inputs/Parajes_Poblacion.geojson', driver = 'GeoJSON')

base_final_localidad = base_localidades_parajes[base_localidades_parajes['Tipo']=='Localidad']

base_final_localidad.to_file('pages/mapa_normativo/data/Inputs/Localidad_Poblacion.geojson', driver = 'GeoJSON')












# localidades_parajes=localidades_parajes.drop(["index"],axis=1)
# localidades_parajes=localidades_parajes.reset_index()