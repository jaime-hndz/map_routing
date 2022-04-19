"""Librerias necesarias"""
from sqlite3 import Row
from numpy import empty
import pandas as p
import folium
import webbrowser
from folium import plugins
from pyparsing import col
import os
import sys
sys.path.append("/")
import openstreetmap as op
"""Ejemplo:
Latitud:18.497889
Longitud:-69.860808 """

mapa =folium.Map(location=[18.497889,-69.860808], zoom_start=15,min_zoom=8,max_zoom=14)
#Entrada longuitud y latitud de ubicacion actual
def MostrarMapa():
    cls()
    print("Ingrese la latitud de donde se encuentra: ",end="")
    latitud=input()
    cls()
    print("Ingrese la longitud de donde se encuentra: ",end="")
    longitud=input()
    cls()
    print("Ingrese la latitud destino: ",end="")
    latitudDestino=input()
    cls()
    print("Ingrese la longitud destino: ",end="")
    longitudDestino=input()


    #Generando, guardando y abriendo mapa
    """Variable mapa, ademas de la localizacion con latitud y longuitud"""
    mapa =folium.Map(location=[latitud,longitud], zoom_start=15,min_zoom=8,max_zoom=14)

    #Agregando los puntos al mapa
    """Localizacion"""
    folium.Marker(location=[latitud,longitud], icon=folium.Icon(color='red', icon='location-crosshairs', prefix='fa')).add_to(mapa)
    """Destino"""
    folium.Marker(location=[latitudDestino,longitudDestino], icon=folium.Icon(color='black', icon='flag-checkered', prefix='fa')).add_to(mapa)

    #Las capas de visualizacion
    folium.TileLayer('Stamen Terrain').add_to(mapa)
    folium.TileLayer('Cartodb Positron').add_to(mapa)
    folium.TileLayer('Cartodb dark_matter').add_to(mapa)
    folium.TileLayer('Stamentoner').add_to(mapa)

    #controlador de capas
    folium.LayerControl().add_to(mapa)
    op.main()
    guardar()

def guardar():
    mapa.save('mapa.html')

    """Luego de guardar el formato de mapa, lo muestra en el navegador""" #Debe de modificarse a la ruta del html dentro de la PC de quien este probando
    webbrowser.open("file:///Users/luisalbertomarmol/Desktop/map/mapa.html")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

MostrarMapa()