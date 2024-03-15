library(sf)

sf::sf_use_s2(F)

escuelas=st_read("./escuelas_informacion_actualizada.geojson")
parcelas=st_read("./Inputs/parcelas/110101.shp")

escuelas=st_transform(escuelas,st_crs(4326))
parcelas=st_transform(parcelas,st_crs(escuelas))

join=st_join(parcelas,escuelas)


no_match=escuelas[!escuelas$codigo_unico_pis %in% join$codigo_unico_pis,]

#Unir archivos de parcelas que se cargaron manualmente

archivos_escuelas_parcelas_manuales=list.files("./Inputs/parcelas/escuelas_manuales/",full.names = T)
for(archivo in archivos_escuelas_parcelas_manuales){
  data=st_read(archivo)
  if(archivo==archivos_escuelas_parcelas_manuales[1]){
    escuelas_parcelas_manuales=data  
  }else{
    escuelas_parcelas_manuales=rbind(escuelas_parcelas_manuales,data)
  }
}

escuelas_parcelas_manuales$manual=1

#Cambiar en los codigos pis los codigos postales que son 0 por S/CP para que pueda
#matchear con la base de escuelas
cambiar_cp=which(substr(escuelas_parcelas_manuales$codigo_unico_pis,1,2)=="0 ")
if(length(cambiar_cp)>0){
  escuelas_parcelas_manuales$codigo_unico_pis[cambiar_cp]=paste0("S/CP ",substr(escuelas_parcelas_manuales$codigo_unico_pis[cambiar_cp],3,nchar(escuelas_parcelas_manuales$codigo_unico_pis[cambiar_cp])))
}


#Agregar data de escuelas a las parcelas de carga manual
escuelas_parcelas_manuales=dplyr::left_join(escuelas_parcelas_manuales,st_drop_geometry(escuelas),by="codigo_unico_pis")

#Ver que parcelas de catastro tienen escuelas que fueron corregidas a mano, en ese
#caso se reemplaza la geometria de catastro por la geometria manual.
#Si hay escuelas que no eran asignadas a una parcela de catastro se agregan las 
#parcelas cargadas manualmente.

# match(save$codigo_unico_pis,escuelas_parcelas_manuales$codigo_unico_pis)
match=escuelas_parcelas_manuales$codigo_unico_pis %in% join$codigo_unico_pis
no_match=which(match==F)
match=which(match==T)
match_data=escuelas_parcelas_manuales[match,]
no_match_data=escuelas_parcelas_manuales[no_match,]

join$manual=0

if(length(match)>0){
  
  filas=match(match_data$codigo_unico_pis,join$codigo_unico_pis)
  st_geometry(join[filas,])=st_geometry(match_data)
  join$manual[filas]=1
  
}

if(length(no_match)>0){
  
  join=plyr::rbind.fill(join,no_match_data)
  join=st_as_sf(join)
}

#Sacar las parcelas que no tienen un codigo unico pis, es decir que no tienen escuelas
save=join[!is.na(join$codigo_unico_pis),]

#Carga de archivo de localidades
localidades=st_read("./Inputs/Localidades.geojson")

#Ver que escuelas estan dentro de localidades para sacarlas. No tiene sentido
# dejarlas porque las zonas de amort y excl de las localidades las cubren
contenidos=st_contains(localidades,save)

remove=unique(unlist(contenidos))

if(length(remove)>0){
  save=save[-remove,]
}


#Arreglar duplicados. Combinar las escuelas que estan en una misma parcela en una sola observacion

dup=st_intersects(save,save)
dup=as.data.frame(dup)
dup=dup[!dup$row.id==dup$col.id,]

#Sacar los duplicados de los pares de intersecciones, por ejemplo si el poligono
# 1 intersecta con el 2 mantenemos la 1 2 y sacamos la combinacion 2 1

dup$sacar=0
for(i in 1:nrow(dup)){
  if(dup$sacar[i]==0){
    valrow=dup$row.id[i]
    valcol=dup$col.id[i]
    
    sacar=which(dup$row.id==valcol & dup$col.id==valrow)
    
    if(length(sacar)>0){
      dup$sacar[sacar]=1  
    }  
  }
}
dup=dup[!dup$sacar==1,]

#Ver cual es la cantidad maxima de poligonos que intersectan (para ver cuantas
#columnas agregar)

n_nuevas_col=max(table(dup$row.id))

for(i in 1:n_nuevas_col){
  
  save[,paste0("nivel",i)]=NA
  save[,paste0("nombre.establecimiento",i)]=NA
  save[,paste0("Tel",i)]=NA
  save[,paste0("email",i)]=NA
  save[,paste0("direccion",i)]=NA
  
  
}


save$index=1:nrow(save)
save$sacar=NA

for(i in unique(dup$row.id)){
  
  # rows=which(dup$row.id==i)
  
  #Poligonos con los que intersecta
  intersecta=unique(dup$col.id[dup$row.id==i])
  
  data=save[c(i,intersecta),]
  
  #Ver cual de todos los poligonos que intersectan son manuales (para mantener
  #estos y eliminar los otros)
  mantener=which(data$manual==1)
  
  if(length(mantener)>0){
    #Me quedo con el primer valor en caso de que haya varios
    mantener=mantener[1]
  }else{
    #Si no hay parcela cargada manual nos quedamos con la primera
    mantener=1
  }

  
  
  #Indice de el que guardamos
  index_mantener=data$index[mantener]
  
  #Filas que vamos a sacar
  sacar=1:nrow(data)
  sacar=sacar[-which(sacar==mantener)]
  
  #Data que vamos a sacar
  sacar=data[sacar,]
  
  #Para cada fila que hay que sacar la marcamos y copiamos la data a las columnas
  #de la fila que guardamos
  
  
  for(j in 1:nrow(sacar)){
    
    #Marcar esta fila para eliminarla mas tarde
    index_sacar=sacar$index[j]
    save$sacar[which(save$index==index_sacar)]=1
    
    #Copiar la data de las filas que se van a eliminar a la que se va a mantener
    save[which(save$index==index_mantener),paste0("nivel",j)]=sacar$nivel[j]
    save[which(save$index==index_mantener),paste0("nombre.establecimiento",j)]=sacar$nombre.establecimiento[j]
    save[which(save$index==index_mantener),paste0("Tel",j)]=sacar$Tel[j]
    save[which(save$index==index_mantener),paste0("email",j)]=sacar$email[j]
    save[which(save$index==index_mantener),paste0("direccion",j)]=sacar$direccion[j]
    
    
  }


  
  
}


save=save[-which(save$sacar==1),]


if(file.exists("./Inputs/escuelas_en_parcelas.geojson")){
  file.remove("./Inputs/escuelas_en_parcelas.geojson")
  st_write(save,"./Inputs/escuelas_en_parcelas.geojson")
  
}else{
  st_write(save,"./Inputs/escuelas_en_parcelas.geojson")
  
}






sum(!is.na(join$cue))

sum(!is.na(escuelas$cue))

# leaflet(save) %>%addPolygons(label=~nombre.establecimiento)%>%addTiles()

# leaflet() %>%addCircleMarkers(data=no_match,label=~nombre.establecimiento)%>%addTiles()


# t=st_read("./Inputs/escuelas_en_parcelas.geojson")


# map <- leaflet() %>%
#   # Base groups
#   addProviderTiles(providers$Esri.WorldImagery) %>%
#   addPolygons(data = parcelas,
#               fill = T,fillOpacity = 0.2, weight = 2, color = "#19a82c", group = "Parcelas") %>%
#   # Overlay groups
#   addCircleMarkers(data=escuelas,fillOpacity = 0.5,radius=5, group = "Escuelas",color="#19a82c",label=~as.character(nombre.establecimiento),
#                    # highlight = highlightOptions(
#                    #   weight = 3,
#                    #   fillOpacity = 0.9,
#                    #   color = "#19a82c",
#                    #   opacity = 1,
#                    #   bringToFront = TRUE,
#                    #   sendToBack = TRUE)
#   ) %>%
#   # Layers control
#   addLayersControl(
#     overlayGroups = c("Escuelas", "Parcelas"),
#     options = layersControlOptions(collapsed = FALSE)
#   )
# map

# providers
