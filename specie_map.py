import pandas as pd
# INSTRUCCION
# Es necesario instalar el paquete folium desde Anaconda Navigator
import folium

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# que se llame specie con pd.read_csv

#Eleccion de dos especies, Aurelia aurita y Pelagia noctiluca
specie = pd.read_csv('Aurelia_aurita.csv')

specie2 = pd.read_csv('Pelagia_noctiluca.csv')

# Lectura de latitud y longitud de las observaciones
lon, lat, lon2, lat2 = specie['decimalLongitude'], specie['decimalLatitude'], 
specie2 ['decimalLongitude'], specie2 ['decimalLatitude']

# MODIFICABLE
# Lectura de datos adicionales (se deben convertir a cadena para visualizarlos)

#Especies elegidas para ser incorporadas como informacion al conjunto de datos
Aureliaaurita = specie ['scientificName'].astype('str')

Pelagianoctiluca = specie2 ['scientificName'].astype('str')
 

# MODIFICABLE
# Opciones de visualizacion de la especie
# Debeis ajustar las coordenadas y el zoom del mapa a la localizacion de la especie
# Muchas mas en: http://python-visualization.github.io/folium/docs-v0.5.0/modules.html

m = folium.Map(location=[40, 20], zoom_start=2,tiles='Stamen Terrain', 
               control_scale = True, prefer_canvas = True)

# Creacion del conjunto de puntos
feature_group = folium.FeatureGroup('Ocurrences', overlay=True, control = True)

# MODIFICABLE

#Conjunto de puntos de Aurelia aurita
for lon, lat, Aureliaaurita in zip(lon,lat, Aureliaaurita): 
    feature_group.add_child(folium.RegularPolygonMarker(location= [lat, lon], popup= Aureliaaurita, 
                                                        fill_color='#31cccc', number_of_sides=5,
                                                        radius=10))
 
#Conjunto de puntos de Pelagia noctiluca    
for lon2, lat2, Pelagianoctiluca in zip(lon2,lat2, Pelagianoctiluca): 
    feature_group.add_child(folium.RegularPolygonMarker(location= [lat2, lon2], popup= Pelagianoctiluca, 
                                                        fill_color='#ed9e21', number_of_sides=6,
                                                        radius=10))

# Se incorporan los puntos al mapa

m.add_child(feature_group)

# Se guarda el mapa como una pagina web
m.save('Especiesporcolor.html')
