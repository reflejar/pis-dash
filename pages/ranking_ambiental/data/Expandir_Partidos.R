library(sf)
library(leaflet)

data=st_read("C:/Users/simon/Downloads/limite_partidos.geojson")
st_crs(data) <- 4326  # Set the coordinate reference system to WGS84



i=2

partidos <- c("Almirante Brown", "Avellaneda", "Berazategui", "Esteban Echeverría", "Ezeiza", "Florencio Varela","General San Martín" ,"Hurlingham", "Ituzaingó", "José C. Paz", "La Matanza", "Lanús", "Lomas de Zamora", "Malvinas Argentinas", "Merlo", "Moreno", "Morón", "Presidente Perón", "Quilmes", "San Fernando", "San Isidro", "San Miguel", "Tigre", "Tres de Febrero", "Vicente López")

sum(partidos %in% data$nam)

leaflet()%>%addPolygons(data=data[data$nam %in% partidos,])%>%addTiles()


gba=data[data$nam %in% partidos,]
provincia=data[!data$nam %in% partidos,]


bbox_provincia <- st_as_sfc(st_bbox(provincia))
bbox_provincia <- st_cast(bbox_provincia, "POLYGON")


bbox_gba <- st_as_sfc(st_bbox(gba))
bbox_gba <- st_cast(bbox_gba, "POLYGON")

leaflet()%>%addPolygons(data=bbox_provincia)%>%addTiles()
leaflet()%>%addPolygons(data=bbox_gba)%>%addTiles()

centroide_provincia=st_centroid(bbox_provincia)

centroide_provincia=st_coordinates(centroide_provincia)

centroide_gba=st_centroid(bbox_gba)

centroide_gba=st_coordinates(centroide_gba)

# Define the fixed point's coordinates
fixed_point <- c(centroide_gba[1], centroide_gba[2])

bbox_gba[[1]][[1]][,1]

altura_bbox_gba=abs(max(bbox_gba[[1]][[1]][,2])-
                    min(bbox_gba[[1]][[1]][,2]))

ancho_bbox_gba=abs(max(bbox_gba[[1]][[1]][,1])-
                      min(bbox_gba[[1]][[1]][,1]))

altura_bbox_provincia=abs(max(bbox_provincia[[1]][[1]][,2])-
                      min(bbox_provincia[[1]][[1]][,2]))

ancho_bbox_provincia=abs(max(bbox_provincia[[1]][[1]][,1])-
                            min(bbox_provincia[[1]][[1]][,1]))

factor_expansion_altura=altura_bbox_provincia/altura_bbox_gba
factor_expansion_ancho=ancho_bbox_provincia/ancho_bbox_gba

factor_expansion=min(factor_expansion_altura,factor_expansion_ancho)

for(i in 1:nrow(gba)){
  
  print(i)
  
  
  # Convert the polygon's coordinates to an sf object
  # polygon_sf <- st_sfc(st_polygon(list(polygon_coords)))
  polygon_sf=st_sfc(gba$geometry[i])
  
  polygon_sf <- st_cast(polygon_sf, "POLYGON")
  
  for(j in 1:length(polygon_sf)){
    polygon_coords=st_coordinates(polygon_sf[[j]])
    polygon_coords=polygon_coords[,c("X","Y")]
    
    # st_crs(polygon_sf[[j]]) <- 4326  # Set the coordinate reference system to WGS84
    
    # leaflet()%>%addPolygons(data=polygon_sf)%>%addTiles()
    
    
    
    # Calculate the distances from each node to the fixed point
    distances <- sqrt((polygon_coords[, 1] - fixed_point[1])^2 + (polygon_coords[, 2] - fixed_point[2])^2)
    
    
    distancesx=polygon_coords[, 1] - fixed_point[1]
    distancesy=polygon_coords[, 2] - fixed_point[2]
    
    matrix <- cbind(distancesx, distancesy)
    
    
    # Create the transformation matrix
    # transformation_matrix <- diag(scaling_factor, nrow = 2)
    transformation_matrix=matrix*factor_expansion
    
    
    # Multiply the vertex matrix by the transformation matrix
    # transformed_coords <- polygon_coords %*% transformation_matrix
    transformed_coords <- polygon_coords + transformation_matrix
    
    # Convert the transformed coordinates to an sf object
    transformed_sf <- st_sfc(st_polygon(list(transformed_coords)))
    st_crs(transformed_sf) <- 4326  # Set the coordinate reference system to WGS84
    # leaflet()%>%addPolygons(data=transformed_sf)%>%addTiles()
    
    
    if(j==1){
      transformed_sf_total=transformed_sf  
    }else{
      transformed_sf_total= append(transformed_sf_total, transformed_sf)
    }
    
  }
  transformed_sf_total <- st_combine(transformed_sf_total)
  
  transformed_sf_total<- st_cast(transformed_sf_total, "MULTIPOLYGON")

  transformed_sf_total=st_as_sf(transformed_sf_total)

  if(nrow(transformed_sf_total)>1){
    print(paste0("Esta observacion ",i, " tiene mas"))
  }
  

  if(i ==1){
    total=transformed_sf_total
  }else{
    total=rbind(total, transformed_sf_total)
  }
  
}

st_geometry(gba)=total$x

leaflet()%>%addPolygons(data=gba)%>%addTiles()


bbox_gba_expandido <- st_as_sfc(st_bbox(gba))
bbox_gba_expandido <- st_cast(bbox_gba_expandido, "POLYGON")

centroide_gba_expandido=st_centroid(bbox_gba_expandido)

centroide_gba_expandido=st_coordinates(centroide_gba_expandido)

# Define the fixed point's coordinates
puntos_centro_gba <- c(centroide_gba_expandido[1], centroide_gba_expandido[2])
puntos_centro_provincia <- c(centroide_provincia[1], centroide_provincia[2])


correccion_vertical=centroide_provincia[2]-centroide_gba_expandido[2]
correccion_horizontal=centroide_provincia[1]-centroide_gba_expandido[1]+ancho_bbox_provincia*1.5


for(i in 1:nrow(gba)){

  
  # Convert the polygon's coordinates to an sf object
  # polygon_sf <- st_sfc(st_polygon(list(polygon_coords)))
  polygon_sf=st_sfc(gba$geometry[i])
  
  polygon_sf <- st_cast(polygon_sf, "POLYGON")
  
  for(j in 1:length(polygon_sf)){
    polygon_coords=st_coordinates(polygon_sf[[j]])
    polygon_coords=polygon_coords[,c("X","Y")]
    
    
    # Multiply the vertex matrix by the transformation matrix
    # transformed_coords <- polygon_coords %*% transformation_matrix
    polygon_coords[,1]=polygon_coords[,1]+correccion_horizontal
    polygon_coords[,2]=polygon_coords[,2]+correccion_vertical
    
    transformed_coords <- polygon_coords
    
    # Convert the transformed coordinates to an sf object
    transformed_sf <- st_sfc(st_polygon(list(transformed_coords)))
    st_crs(transformed_sf) <- 4326  # Set the coordinate reference system to WGS84
    # leaflet()%>%addPolygons(data=transformed_sf)%>%addTiles()
    
    
    if(j==1){
      transformed_sf_total=transformed_sf  
    }else{
      transformed_sf_total= append(transformed_sf_total, transformed_sf)
    }
    
  }
  transformed_sf_total <- st_combine(transformed_sf_total)
  
  transformed_sf_total<- st_cast(transformed_sf_total, "MULTIPOLYGON")
  
  transformed_sf_total=st_as_sf(transformed_sf_total)
  
  if(nrow(transformed_sf_total)>1){
    print(paste0("Esta observacion ",i, " tiene mas"))
  }
  
  
  if(i ==1){
    total=transformed_sf_total
  }else{
    total=rbind(total, transformed_sf_total)
  }
  
}

st_geometry(gba)=total$x

leaflet()%>%addPolygons(data=gba,label=~as.character(gba$nam))%>%addPolygons(data=provincia,label=~as.character(provincia$nam))%>%addTiles()




provincia_total=rbind(provincia,gba)


st_write(provincia_total,"C:/Users/simon/Downloads/limite_partidos_expandido.geojson")



transformed_coords[1,]
transformed_coords[857,]

polygon_coords[1,]
polygon_coords[857,]

nrow(transformed_coords)



# Define the polygons' coordinates
polygon1_coords <- matrix(c(-122.431297, 37.773972, -122.431297, 37.774672, -122.430297, 37.774672, -122.430297, 37.773972, -122.431297, 37.773972), ncol = 2, byrow = TRUE)
polygon2_coords <- matrix(c(-122.430297, 37.773972, -122.430297, 37.774672, -122.429297, 37.774672, -122.429297, 37.773972, -122.430297, 37.773972), ncol = 2, byrow = TRUE)



library(sf)

# Convert the polygons' coordinates to sf objects with no CRS
polygon1_sf <- st_sfc(st_polygon(list(polygon1_coords)))
polygon2_sf <- st_sfc(st_polygon(list(polygon2_coords)))

# Combine the polygons into a list
polygon_list <- list(polygon1_sf, polygon2_sf)

# Combine the polygons into an sf object
polygon_sf <- st_sfc(polygon_list)
polygon_sf=rbind(polygon1_sf,polygon2_sf)
# Set the CRS of the sf object
st_crs(polygon_sf) <- 4326  # Set the coordinate reference system to WGS84

leaflet()%>%addPolygons(data=polygon1_sf)%>%addPolygons(data=polygon2_sf)%>%addTiles()

# Define the fixed point's coordinates
fixed_point <- c(-122.430297, 37.774672)

# Calculate the distances from each node to the fixed point
# distances <- sqrt((polygon_coords[, 1] - fixed_point[1])^2 + (polygon_coords[, 2] - fixed_point[2])^2)


distancesx1=polygon1_coords[, 1] - fixed_point[1]
distancesy1=polygon1_coords[, 2] - fixed_point[2]

distancesx2=polygon2_coords[, 1] - fixed_point[1]
distancesy2=polygon2_coords[, 2] - fixed_point[2]

matrix1 <- cbind(distancesx1, distancesy1)
matrix2 <- cbind(distancesx2, distancesy2)


# Define the scaling factor
scaling_factor <- 2  # Adjust this value as desired

# Create the transformation matrix
# transformation_matrix <- diag(scaling_factor, nrow = 2)
transformation_matrix1=matrix1*scaling_factor
transformation_matrix2=matrix2*scaling_factor


# Multiply the vertex matrix by the transformation matrix
# transformed_coords <- polygon_coords %*% transformation_matrix
transformed_coords1 <- polygon1_coords + transformation_matrix1
transformed_coords2 <- polygon2_coords + transformation_matrix2

# Convert the transformed coordinates to an sf object
transformed_sf1 <- st_sfc(st_polygon(list(transformed_coords1)))
transformed_sf2 <- st_sfc(st_polygon(list(transformed_coords2)))

st_crs(transformed_sf1) <- 4326  # Set the coordinate reference system to WGS84
st_crs(transformed_sf2) <- 4326  # Set the coordinate reference system to WGS84

leaflet()%>%addPolygons(data=transformed_sf1)%>%addPolygons(data=transformed_sf2)%>%addTiles()
