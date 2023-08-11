import geopandas as gpd
import shapely
import pandas as pd
import numpy as np

import plotly.graph_objects as go

import pickle

class MapHandler:

    """

        Clase para la manipulación de mapas

        Parametros que recibe
        ----------
            municipios: list
                Municipios que quiera mostrar.
            recursos: list
                Lista de recursos que se quiera mostrar.
            vista: str
                Tipo de vista que se quiera mostrar 'open-street-map' o 'white-bg'.
                Default: 'open-street-map'.

        Atributos principales
        ----------
            TIPO_RECURSOS: dict
                Diccionario de los tipos de recursos disponibles con sus caracterizaciones.
                    [cursos_agua, cuerpos_agua, escuelas_parcelas, ...]
            MUNICIPIOS: 
                Municipios de Bs As. (Por ahora solo Mar Chiquita).
                Falta ...
            fig: go.Figure
                Figura a la que se le agregarán y quitarán capas.
        
        Métodos principales
        ----------
            .render() -> go.Figure
                Prende y apaga las capas y el tipo de vista.
                Retorna el mapa entero.
            
    """

    DEFAULT_FOLDER = 'data'

    TIPO_RECURSOS = {
        'reservas': {
            'title': 'Reservas',
            'color': None,
            'pkl': 'reservas_geojson.pkl',
            'parquet': 'reservas.parquet',
            'graph': 'choroplet',
            'opacity': 0.3,
            'line_width': 1.2,
            'customdata_attrs': ["Name", "color"],
            'hover': '<b>Nombre</b>: %{customdata[0]}<br>'+'<extra></extra>'
        },          
        'total_amort_geojson': {
            'title': 'Zonas de Amortiguamiento',
            'color': None,
            'pkl': 'total_amort_geojson.pkl',
            'parquet': 'total_amort.parquet',
            'graph': 'choroplet',
            'opacity': 0.3,
            'line_width': 1.2,
            'customdata_attrs': [],
            'hover': '<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
        },        
        'total_excl': {
            'title': 'Zonas de Exclusión',
            'color': None,
            'pkl': 'total_excl_geojson.pkl',
            'parquet': 'total_excl.parquet',
            'graph': 'choroplet',
            'opacity': 0.5,
            'line_width': 1.2,
            'customdata_attrs': [],
            'hover': '<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
        },                       
        'cuerpos_agua': {
            'title': 'Cuerpos de agua',
            'color': 0,
            'pkl': 'cuerpos_geojson.pkl',
            'parquet': 'cuerpos.parquet',
            'graph': 'choroplet',
            'opacity': 0.7,
            'line_width': 0.5,
            'customdata_attrs': ["NOMBRE", "TIPO"],
            'hover': '<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Tipo</b>: %{customdata[1]}<br>'+'<extra></extra>'
        },
        'cursos_agua': {
            'title': 'Rios',
            'color': 'rgb(30, 115, 199)',
            'pkl': 'nombres_rios.npy',
            'lats': 'latitudes_rios.npy',
            'lons': 'longitudes_rios.npy',
            'graph': 'scatter',
            'line_width': 12,
            'hover': '<b>Nombre</b>: %{customdata[0]}<br>'+'<extra></extra>'

        },        
        'localidades_parajes': {
            'title': 'Localidades y parajes',
            'color': 0,
            'pkl': 'localidades_parajes_geojson.pkl',
            'parquet': 'localidades_parajes.parquet',
            'graph': 'choroplet',
            'opacity': 0.7,
            'line_width': 1.2,
            'customdata_attrs': ["Name","Habitantes"],
            'hover': '<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Población</b>:  %{customdata[1]}<br>'+'<extra></extra>'
        },        
        'escuelas_parcelas': {
            'title': 'Escuelas',
            'color': 1,
            'pkl': 'escuelas_parcelas_geojson.pkl',
            'parquet': 'escuelas_parcelas.parquet',
            'graph': 'choroplet',
            'opacity': 0.7,
            'line_width': 1.2,
            'customdata_attrs': ["nombre.establecimiento", "nivel", "Tel", "email"],
            'hover': '<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Nivel</b>: %{customdata[1]}<br>'+'<b>Teléfono</b>: %{customdata[2]}<br>'+'<b>Email</b>: %{customdata[3]}'+'<extra></extra>'

        },

    }

    MUNICIPIOS = ['Mar Chiquita']
    # SCALE = [[0, 'rgb(17, 56, 173)'], [1,'rgb(199, 30, 30)' ]]
    SCALE=[[0, 'rgb(17, 56, 173)'], [0.5,'rgb(199, 30, 30)' ],[1,'rgb(35, 161, 31)' ]]
# colorscale=[[0, 'rgb(17, 56, 173)'], [1,'rgb(199, 30, 30)' ]]

    def __init__(
        self,
        municipios:list=[],
        recursos:list=[],
        vista:str='open-street-map',
    ) -> None:
        if not isinstance(recursos, list):
            raise Exception("dame una lista de strings para los tipos de recurso porfis")
        self.fig = go.Figure()
        self.municipios = municipios or self.MUNICIPIOS
        self.recursos = recursos
        self.vista = vista

    def render(self):
        self.switch_vista()
        self.switch_capas()
        self.switch_municipio()
        return self.fig
        
    
    def switch_municipio(self):
        # Por ahora no hace nada mas que centrar y centra con un gdf dummy
        gdf = gpd.read_file(f"{self.DEFAULT_FOLDER}/cursos_agua.geojson").reset_index()
        self.zoom_and_center(gdf)


    def switch_vista(self):
        self.fig.update_layout(
            mapbox_style="open-street-map",
            mapbox_zoom=6, 
            uirevision=True,
            height=800,
            coloraxis_showscale=False,
            margin={"r":0,"t":0,"l":0,"b":0},
            mapbox_center={"lat": -36.26, "lon": -60.23},
        )
        if self.vista == "open-street-map":
            self.fig.update_layout(
                mapbox_style="open-street-map",
                mapbox_layers=[]
            )
        else:
            self.fig.update_layout(
                mapbox_style="white-bg",
                mapbox_layers=[
                    {
                        "below": 'traces',
                        "sourcetype": "raster",
                        "sourceattribution": 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                        "source": [
                            "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
                        ]
                        
                    }
                ]
            )                

    def switch_capas(self):
        for recurso in self.recursos:
            recurso = self.TIPO_RECURSOS[recurso]
            self.fig.add_trace(getattr(self, recurso['graph'])(recurso))
            
    def choroplet(self, recurso):
        df = gpd.read_parquet(f"{self.DEFAULT_FOLDER}/{recurso['parquet']}").reset_index()
        with open(f"{self.DEFAULT_FOLDER}/{recurso['pkl']}", 'rb') as f:
            gdf= pickle.load(f)        
        gdf['color'] = recurso['color']

        return go.Choroplethmapbox(
            geojson=gdf, 
            featureidkey="properties.index",
            locations=df['index'], 
            z=df['color'],
            colorscale=self.SCALE,
            zmax=1,
            zmin=0,
            marker_opacity=recurso['opacity'],
            marker_line_width=recurso['line_width'],
            customdata=np.stack([df[attr] for attr in recurso['customdata_attrs']], axis=-1) if recurso['customdata_attrs'] else [],
            name=recurso['parquet'],
            showscale=False,
            hovertemplate=recurso['hover'],
        )

    def scatter(self, recurso):
        #Crear latitudes y longitudes de rios
        lats=np.load(f"{self.DEFAULT_FOLDER}/{recurso['lats']}",allow_pickle=True)
        lons=np.load(f"{self.DEFAULT_FOLDER}/{recurso['lons']}",allow_pickle=True)
        nombres=np.load(f"{self.DEFAULT_FOLDER}/{recurso['pkl']}",allow_pickle=True)
        
        
        return go.Scattermapbox(
            lat = lats,
            lon = lons,
            mode = 'lines',
            marker_size=recurso['line_width'],
            marker_color=recurso['color'],
            name=recurso['pkl'],
            customdata = np.stack((nombres, nombres), axis=-1),
            hovertemplate =recurso['hover'],   

            )            

    def zoom_and_center(self, gdf):
        """Function documentation:\n
        Basic framework adopted from Krichardson under the following thread:
        https://community.plotly.com/t/dynamic-zoom-for-mapbox/32658/7

        # NOTE:
        # THIS IS A TEMPORARY SOLUTION UNTIL THE DASH TEAM IMPLEMENTS DYNAMIC ZOOM
        # in their plotly-functions associated with mapbox, such as go.Densitymapbox() etc.

        Returns the appropriate zoom-level for these plotly-mapbox-graphics along with
        the center coordinate tuple of all provided coordinate tuples.
        """

        # Check whether both latitudes and longitudes have been passed,
        x1,y1,x2,y2 = gdf['geometry'].total_bounds
        longitudes=np.array([x1,x2])
        latitudes=np.array([y1,y2])
        max_bound = max(abs(x1-x2), abs(y1-y2)) * 111
        zoom = 11.5 - np.log(max_bound)

        # or if the list lenghts don't match
        if ((latitudes is None or longitudes is None)
                or (len(latitudes) != len(longitudes))):
            # Otherwise, return the default values of 0 zoom and the coordinate origin as center point
            return 0, (0, 0)

        # Get the boundary-box 
        b_box = {} 
        b_box['height'] = latitudes.max()-latitudes.min()
        b_box['width'] = longitudes.max()-longitudes.min()
        b_box['center']= (np.mean(longitudes), np.mean(latitudes))

        # get the area of the bounding box in order to calculate a zoom-level
        area = b_box['height'] * b_box['width']

        # * 1D-linear interpolation with numpy:
        # - Pass the area as the only x-value and not as a list, in order to return a scalar as well
        # - The x-points "xp" should be in parts in comparable order of magnitude of the given area
        # - The zpom-levels are adapted to the areas, i.e. start with the smallest area possible of 0
        # which leads to the highest possible zoom value 20, and so forth decreasing with increasing areas
        # as these variables are antiproportional
        zoom = np.interp(x=area,
                        xp=[0, 5**-10, 4**-10, 3**-10, 2**-10, 1**-10, 1**-5],
                        fp=[20, 15,    14,     13,     12,     7,      5])

        # Finally, return the zoom level and the associated boundary-box center coordinates
        self.fig.update_layout(
            mapbox_zoom=zoom-1, 
            mapbox_center = {"lat": b_box['center'][1], "lon": b_box['center'][0]},
        )


    # def create_hover_info(self):
    #     hover_escuelas_parc='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Nivel</b>: %{customdata[1]}<br>'+'<b>Teléfono</b>: %{customdata[2]}'+'<extra></extra>'
    
    #     customdata_escuelas_parc = np.stack((gdf["nombre.establecimiento"], gdf['nivel'],
    #                         gdf["Tel"]), axis=-1)
    #     hover_cuerpos='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Tipo</b>: %{customdata[1]}<br>'+'<extra></extra>'
    #     customdata_cuerpos = np.stack((gdf["NOMBRE"], gdf['TIPO']), axis=-1)
    #     hover_cursos='<b>Nombre</b>: %{customdata[0]}<br>'+'<extra></extra>'
    #     customdata_cursos = np.stack((names,names), axis=-1)