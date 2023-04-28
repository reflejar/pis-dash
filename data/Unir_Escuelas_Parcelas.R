library(sf)
library(leaflet)
escuelas=st_read("./Inputs/escuelas_informacion_actualizada.geojson")
parcelas=st_read("./Inputs/parcelas/110101.shp")

escuelas=st_transform(escuelas,st_crs(4326))
parcelas=st_transform(parcelas,st_crs(escuelas))

join=st_join(parcelas,escuelas)

save=join[!is.na(join$cue),]

no_match=escuelas[!escuelas$cue %in% join$cue,]

st_write(save,"./Inputs/escuelas_en_parcelas.geojson",append=F)

sum(!is.na(join$cue))

sum(!is.na(escuelas$cue))


map <- leaflet() %>%
  # Base groups
  addProviderTiles(providers$Esri.WorldImagery) %>%
  addPolygons(data = parcelas,
              fill = T,fillOpacity = 0.2, weight = 2, color = "#19a82c", group = "Parcelas") %>%
  # Overlay groups
  addCircleMarkers(data=escuelas,fillOpacity = 0.5,radius=5, group = "Escuelas",color="#19a82c",label=~as.character(nombre.establecimiento),
                   # highlight = highlightOptions(
                   #   weight = 3,
                   #   fillOpacity = 0.9,
                   #   color = "#19a82c",
                   #   opacity = 1,
                   #   bringToFront = TRUE,
                   #   sendToBack = TRUE)
  ) %>%
  # Layers control
  addLayersControl(
    overlayGroups = c("Escuelas", "Parcelas"),
    options = layersControlOptions(collapsed = FALSE)
  )
map

providers
