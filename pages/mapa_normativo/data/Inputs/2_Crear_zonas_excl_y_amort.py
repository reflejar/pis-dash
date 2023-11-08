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

SAVE_FOLDER = 'pages/mapa_normativo/data/'

#Definir parametros de zonas de exclusion y amortiguamiento
local_excl=150
local_amort=500
par_excl=50
par_amort=500
esc_excl=200
esc_amort=500
sup_agua_excl=25

## Funcion para Transformar la proyeccion que se usa

#TEST PARA GUARDAR JSONS COMO PARQUET
# from pyarrow import json
# import pyarrow.parquet as pq

# table = json.read_json('C:/python/json_teste') 
# pq.write_table(table, 'C:/python/result.parquet')  # save json/table as parquet


#### Localidades y parajes #####

#Leemos input y los transformamos a la proyeccion que usamos
localidades=gpd.read_file(f"{SAVE_FOLDER}Inputs/Localidad_Poblacion.geojson")
localidades = localidades.to_crs("epsg:4326")

#Creamos las zonas de excl y amort haciendo un buffer (borde) al rededor de las geometrias. Cambiamos la proyeccion para que el buffer se mida en metros
localidades_excl=localidades.copy()
localidades_excl = localidades_excl.to_crs("epsg:22183")
localidades_excl.geometry = localidades_excl.geometry.buffer(local_excl, 10) #El numero final indica que tan preciso queremos que sea el buffer
localidades_excl= localidades_excl.to_crs('epsg:4326')  

localidades_amort=localidades.copy()
localidades_amort = localidades_amort.to_crs("epsg:22183")
localidades_amort.geometry = localidades_amort.geometry.buffer(local_excl+local_amort, 10)
localidades_amort= localidades_amort.to_crs('epsg:4326')  

#Sacar overlap entre los poligonos y sus zonas de exclusion y amort
localidades_amort = localidades_amort.overlay(localidades_excl, how='difference')
localidades_excl = localidades_excl.overlay(localidades, how='difference')

localidades_excl.to_parquet(f"{SAVE_FOLDER}localidades_excl.parquet")
localidades_amort.to_parquet(f"{SAVE_FOLDER}localidades_amort.parquet")


#PARAJES
parajes=gpd.read_file(f"{SAVE_FOLDER}Inputs/Parajes_Poblacion.geojson")
parajes=parajes.reset_index()

parajes = parajes.to_crs("epsg:4326")
parajes_excl=parajes.copy()
parajes_excl = parajes_excl.to_crs("epsg:22183")
parajes_excl.geometry = parajes_excl.geometry.buffer(par_excl, 10)
parajes_excl= parajes_excl.to_crs('epsg:4326')  

parajes_amort=parajes.copy()
parajes_amort = parajes_amort.to_crs("epsg:22183")
parajes_amort.geometry = parajes_amort.geometry.buffer(par_excl+par_amort, 10)
parajes_amort= parajes_amort.to_crs('epsg:4326')  

#Sacar overlap entre los poligonos
parajes_amort = parajes_amort.overlay(parajes_excl, how='difference')
parajes_excl = parajes_excl.overlay(parajes, how='difference')

# Guardar parquet de parajes excl y amor
parajes_excl.to_parquet(f"{SAVE_FOLDER}parajes_excl.parquet")
parajes_amort.to_parquet(f"{SAVE_FOLDER}parajes_amort.parquet")


#Unir y guardar localidades y parajes
localidades_parajes=pd.concat([localidades,parajes],ignore_index=True)
localidades_parajes=localidades_parajes.drop(["index"],axis=1)
localidades_parajes=localidades_parajes.reset_index()
localidades_parajes.to_parquet(f"{SAVE_FOLDER}localidades_parajes.parquet")

#Transformar a json (para mapa) y guardar
localidades_parajes_geojson=json.loads(localidades_parajes.to_json(na="keep"))
with open(f'{SAVE_FOLDER}localidades_parajes_geojson.pkl', 'wb') as f:
    pickle.dump(localidades_parajes_geojson, f, protocol=pickle.HIGHEST_PROTOCOL)

################################################### ESCUELAS ###########################################

escuelas_en_parcelas = gpd.read_file(f"{SAVE_FOLDER}Inputs/escuelas_en_parcelas.geojson")
# escuelas_en_parcelas['característica.telefónica']=escuelas_en_parcelas['característica.telefónica'].astype(str).replace('\.0', '', regex=True)
# escuelas_en_parcelas['teléfono']=escuelas_en_parcelas['teléfono'].astype(str).replace('\.0', '', regex=True)
# escuelas_en_parcelas.reset_index(inplace=True)
# escuelas_en_parcelas["Tel"]="("+escuelas_en_parcelas["característica.telefónica"]+") "+escuelas_en_parcelas['teléfono']
# escuelas_en_parcelas["Tel"][escuelas_en_parcelas["Tel"].str.contains('one')] = "-"
# escuelas_en_parcelas = escuelas_en_parcelas[escuelas_en_parcelas['ubicación'].str.contains('Rural')]

#Remplazar NA por - en todas las columnas de nivel. email, etc
for idx in [i for i, c in enumerate(escuelas_en_parcelas.columns) if c.startswith("nivel")]:
    escuelas_en_parcelas.iloc[:, idx] = escuelas_en_parcelas.iloc[:, idx].fillna("-")
for idx in [i for i, c in enumerate(escuelas_en_parcelas.columns) if c.startswith("email")]:
    escuelas_en_parcelas.iloc[:, idx] = escuelas_en_parcelas.iloc[:, idx].fillna("-")
for idx in [i for i, c in enumerate(escuelas_en_parcelas.columns) if c.startswith("Tel")]:
    escuelas_en_parcelas.iloc[:, idx] = escuelas_en_parcelas.iloc[:, idx].fillna("-")
for idx in [i for i, c in enumerate(escuelas_en_parcelas.columns) if c.startswith("nombre.establecimiento")]:
    escuelas_en_parcelas.iloc[:, idx] = escuelas_en_parcelas.iloc[:, idx].fillna("-")
for idx in [i for i, c in enumerate(escuelas_en_parcelas.columns) if c.startswith("direccion")]:
    escuelas_en_parcelas.iloc[:, idx] = escuelas_en_parcelas.iloc[:, idx].fillna("-")    

escuelas_en_parcelas.to_parquet(f"{SAVE_FOLDER}escuelas_parcelas.parquet")


#Transformar a json (para mapa) y guardar
escuelas_en_parcelas_geojson=json.loads(escuelas_en_parcelas.to_json(na="keep"))
with open(f'{SAVE_FOLDER}escuelas_parcelas_geojson.pkl', 'wb') as f:
    pickle.dump(escuelas_en_parcelas_geojson, f, protocol=pickle.HIGHEST_PROTOCOL)

escuelas_en_parcelas = escuelas_en_parcelas.to_crs("epsg:4326")

escuelas_excl=escuelas_en_parcelas.copy()
escuelas_excl = escuelas_excl.to_crs("epsg:22183")
escuelas_excl.geometry = escuelas_excl.geometry.buffer(esc_excl, 10)
escuelas_excl= escuelas_excl.to_crs('epsg:4326')  


escuelas_amort=escuelas_en_parcelas.copy()
escuelas_amort = escuelas_amort.to_crs("epsg:22183")
escuelas_amort.geometry = escuelas_amort.geometry.buffer(esc_excl+esc_amort,10)
escuelas_amort= escuelas_amort.to_crs('epsg:4326') 


#Sacar overlap entre los poligonos
escuelas_amort = escuelas_amort.overlay(escuelas_excl, how='difference')
escuelas_excl = escuelas_excl.overlay(escuelas_en_parcelas, how='difference')

escuelas_excl.to_parquet(f"{SAVE_FOLDER}escuelas_parcelas_excl.parquet")
escuelas_amort.to_parquet(f"{SAVE_FOLDER}escuelas_parcelas_amort.parquet")

# escuelas=gpd.read_file("./Inputs/escuelas.geojson")
# escuelas=escuelas.reset_index()
# escuelas["color"]=0.5
# escuelas = escuelas.to_crs("epsg:4326")

# escuelas_excl=escuelas.copy()
# escuelas_excl = escuelas_excl.to_crs("epsg:22183")
# escuelas_excl.geometry = escuelas_excl.geometry.buffer(esc_excl, 10)
# escuelas_excl= escuelas_excl.to_crs('epsg:4326')  


# escuelas_amort=escuelas.copy()
# escuelas_amort = escuelas_amort.to_crs("epsg:22183")
# escuelas_amort.geometry = escuelas_amort.geometry.buffer(esc_excl+esc_amort, 10)
# escuelas_amort= escuelas_amort.to_crs('epsg:4326') 

#Sacar overlap entre los poligonos
# escuelas_amort = escuelas_amort.overlay(escuelas_excl, how='difference')
# escuelas_excl = escuelas_excl.overlay(escuelas, how='difference')

# escuelas_excl.to_parquet("./Inputs/escuelas_excl.parquet")
# escuelas_amort.to_parquet("./Inputs/escuelas_amort.parquet")


################################################### AGUAS ###########################################
cuerpos=gpd.read_file(f"{SAVE_FOLDER}Inputs/cuerpos.geojson",encoding="ASCI")
cuerpos=cuerpos.reset_index()

cuerpos.to_parquet(f"{SAVE_FOLDER}cuerpos.parquet")


#Transformar a json (para mapa) y guardar
cuerpos_geojson=json.loads(cuerpos.to_json(na="keep"))
with open(f'{SAVE_FOLDER}cuerpos_geojson.pkl', 'wb') as f:
    pickle.dump(cuerpos_geojson, f, protocol=pickle.HIGHEST_PROTOCOL)

cuerpos = cuerpos.to_crs("epsg:4326")

cuerpos_excl=cuerpos.copy()
cuerpos_excl = cuerpos_excl.to_crs("epsg:22183")
cuerpos_excl.geometry = cuerpos_excl.geometry.buffer(sup_agua_excl, 10)
cuerpos_excl= cuerpos_excl.to_crs('epsg:4326')  


cursos=gpd.read_file(f"{SAVE_FOLDER}Inputs/cursos_agua.geojson")
cursos=cursos.reset_index()
cursos = cursos.to_crs("epsg:4326")

cursos_excl=cursos.copy()
cursos_excl = cursos_excl.to_crs("epsg:22183")
cursos_excl.geometry = cursos_excl.geometry.buffer(sup_agua_excl, 10)
cursos_excl= cursos_excl.to_crs('epsg:4326')  


#Sacar overlap entre los poligonos
cuerpos_excl = cuerpos_excl.overlay(cuerpos, how='difference')
cursos_excl = cursos_excl.overlay(cursos, how='difference')

cuerpos_excl.to_parquet(f"{SAVE_FOLDER}cuerpos_excl.parquet")
cursos_excl.to_parquet(f"{SAVE_FOLDER}cursos_excl.parquet")


###### Generar areas de exclusion y amortiguamiento totales

localidades_excl=gpd.read_parquet(f"{SAVE_FOLDER}localidades_excl.parquet")
localidades_amort=gpd.read_parquet(f"{SAVE_FOLDER}localidades_amort.parquet")
parajes_excl=gpd.read_parquet(f"{SAVE_FOLDER}parajes_excl.parquet")
parajes_amort=gpd.read_parquet(f"{SAVE_FOLDER}parajes_amort.parquet")
escuelas_parcelas_excl=gpd.read_parquet(f"{SAVE_FOLDER}escuelas_parcelas_excl.parquet")
escuelas_parcelas_amort=gpd.read_parquet(f"{SAVE_FOLDER}escuelas_parcelas_amort.parquet")
cuerpos_excl=gpd.read_parquet(f"{SAVE_FOLDER}cuerpos_excl.parquet")
cursos_excl=gpd.read_parquet(f"{SAVE_FOLDER}cursos_excl.parquet")

cuerpos=gpd.read_parquet(f"{SAVE_FOLDER}cuerpos.parquet")
localidades_parajes=gpd.read_parquet(f"{SAVE_FOLDER}localidades_parajes.parquet")
escuelas_parcelas=gpd.read_parquet(f"{SAVE_FOLDER}escuelas_parcelas.parquet")
reservas=gpd.read_parquet(f"{SAVE_FOLDER}reservas.parquet")

# puntos_interes=pd.concat([cuerpos,localidades_parajes,escuelas_parcelas,reservas])
puntos_interes=pd.concat([cuerpos,localidades_parajes,escuelas_parcelas])

loc_excl=localidades_excl[["geometry"]]
loc_amort=localidades_amort[["geometry"]]
par_excl=parajes_excl[["geometry"]]
par_amort=parajes_amort[["geometry"]]
esc_par_excl=escuelas_parcelas_excl[["geometry"]]
esc_par_amort=escuelas_parcelas_amort[["geometry"]]
cuerp_excl=cuerpos_excl[["geometry"]]
curs_excl=cursos_excl[["geometry"]]

total_excl=pd.concat([loc_excl,par_excl,esc_par_excl,cuerp_excl,curs_excl])
total_amort=pd.concat([loc_amort,par_amort,esc_par_amort])

total_amort = total_amort.overlay(pd.concat([total_excl,puntos_interes]), how='difference')
total_excl = total_excl.overlay(puntos_interes, how='difference')

total_excl = total_excl.dissolve().explode(ignore_index=True,index_parts=False)
total_amort = total_amort.dissolve().explode(ignore_index=True,index_parts=False)

total_excl.reset_index(inplace=True)
total_amort.reset_index(inplace=True)

total_excl.to_parquet(f"{SAVE_FOLDER}total_excl.parquet")
total_amort.to_parquet(f"{SAVE_FOLDER}total_amort.parquet")

total_excl_geojson=json.loads(total_excl.to_json(na="keep"))
total_amort_geojson=json.loads(total_amort.to_json(na="keep"))

with open(f'{SAVE_FOLDER}total_excl_geojson.pkl', 'wb') as f:
    pickle.dump(total_excl_geojson, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(f'{SAVE_FOLDER}total_amort_geojson.pkl', 'wb') as f:
    pickle.dump(total_amort_geojson, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    
total_excl = total_excl.to_crs("epsg:22183")
total_excl_area=total_excl.area
    
total_excl_area=total_excl_area/10000


total_amort = total_amort.to_crs("epsg:22183")
total_amort_area=total_amort.area 
total_amort_area=total_amort_area/10000


sum(total_amort_area) #En Ha
sum(total_excl_area)

sum(total_amort_area)/100 #En Km2
sum(total_excl_area)/100



#################  Preprocesar archivos geoespaciales  ##################


################################################### RESERVAS ###########################################


reservas=gpd.read_file(f"{SAVE_FOLDER}Inputs/Reservas.geojson")
reservas=reservas.reset_index()

#Agregar la palabra "Reserva" al nombre si no esta 
reservas.loc[~reservas['Name'].str.contains("reserva", case=False),"Name"] = "Reserva "+reservas.loc[~reservas['Name'].str.contains("reserva", case=False),"Name"]
reservas.to_parquet(f"{SAVE_FOLDER}reservas.parquet")

#Transformar a json (para mapa) y guardar
reservas_geojson=json.loads(reservas.to_json(na="keep"))
with open(f'{SAVE_FOLDER}reservas_geojson.pkl', 'wb') as f:
    pickle.dump(reservas_geojson, f, protocol=pickle.HIGHEST_PROTOCOL)

################################################### CURSOS ###########################################

cursos=gpd.read_file(f"{SAVE_FOLDER}Inputs/cursos_agua.geojson")
cursos.to_parquet(f"{SAVE_FOLDER}cursos_agua.parquet")



# ######     Crear latitudes y longitudes de rios  ##########
# lats_cursos = []
# lons_cursos = []
# names = []

# for feature, name in zip(cursos.geometry, cursos.NOMBRE):
#     if isinstance(feature, shapely.geometry.linestring.LineString):
#         linestrings = [feature]
#     elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
#         linestrings = feature.geoms
#     else:
#         continue
#     for linestring in linestrings:
#         x, y = linestring.xy
#         lats_cursos = np.append(lats_cursos, y)
#         lons_cursos = np.append(lons_cursos, x)
#         names = np.append(names, [name]*len(y))
#         lats_cursos = np.append(lats_cursos, None)
#         lons_cursos = np.append(lons_cursos, None)
#         names = np.append(names, None)

# np.save("./latitudes_rios.npy",lats_cursos,allow_pickle=True)
# np.save("./longitudes_rios.npy",lons_cursos,allow_pickle=True)
# np.save("./nombres_rios.npy",names,allow_pickle=True)

excl=[localidades_excl, parajes_excl,cursos_excl, cuerpos_excl,escuelas_parcelas_excl]
combinaciones=[]
for i in range(1,len(excl)+1):
    x = combinations(excl, i)
    for j in list(x):
        combinaciones.append(j)
combinaciones
exclusion=pd.DataFrame()
for i in list(combinaciones):
    exclusion_x=pd.DataFrame()
    lista=[]
    puntos_interes=pd.DataFrame()
    for j in i:
        exclusion_x=pd.concat([exclusion_x, j[["geometry"]]])
        nombre_variable=[name for name in globals() if globals()[name] is j]
        lista.append(nombre_variable[0][0:nombre_variable[0].find("_")])
    x=""
    for z in lista:
        x=x+z

    
    if "cuerpos" in x:
        puntos_interes=pd.concat([puntos_interes, cuerpos])
    if "localidades"  in x:
        puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "parajes"  in x:
        if "localidades"  not in x:
            puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "escuelas" in x:
        puntos_interes=pd.concat([puntos_interes, escuelas_parcelas])

    exclusion_x["id"]=x
    if x!="cursos":
        exclusion_x = exclusion_x.overlay(puntos_interes, how='difference')
    exclusion_x = exclusion_x.dissolve().explode(ignore_index=True,index_parts=False)
    exclusion=pd.concat([exclusion,exclusion_x])
exclusion.reset_index(inplace=True)

###################### tabla general amortiguamiento ####################################################
   
amort=[localidades_amort, parajes_amort, escuelas_parcelas_amort ]

combinaciones=[]
for i in range(1,len(amort)+1):
    x = combinations(amort, i)
    for j in list(x):
        combinaciones.append(j)
combinaciones

amortiguacion=pd.DataFrame()
for i in list(combinaciones):
    amortiguacion_x=pd.DataFrame()
    lista=[]
    puntos_interes=pd.DataFrame()
    for j in i:
        amortiguacion_x=pd.concat([amortiguacion_x, j[["geometry"]]])
        nombre_variable=[name for name in globals() if globals()[name] is j]
        lista.append(nombre_variable[0][0:nombre_variable[0].find("_")])
    x=""
    for z in lista:
        x=x+z
    
    puntos_interes=pd.concat([puntos_interes, cuerpos])
    if "localidades"  in x:
        puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "parajes"  in x:
        if "localidades"  not in x:
            puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "escuelas" in x:
        puntos_interes=pd.concat([puntos_interes, escuelas_parcelas])

    amortiguacion_x["id"]=x
    amortiguacion_x = amortiguacion_x.overlay(pd.concat([exclusion[exclusion["id"]==x],puntos_interes]), how='difference')
    amortiguacion_x = amortiguacion_x.dissolve().explode(ignore_index=True,index_parts=False)
    amortiguacion=pd.concat([amortiguacion,amortiguacion_x])
amortiguacion.reset_index(inplace=True)

amortiguacion.to_parquet(f"{SAVE_FOLDER}amortiguacion.parquet")
exclusion.to_parquet(f"{SAVE_FOLDER}exclusion.parquet")