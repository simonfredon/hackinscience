# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:37:57 2015

@author: simonfredon
"""

import folium
import json

map_osm = folium.Map(location=[48.853056, 2.349722])

f = open("velib.json")
j = json.load(f)

for i in j:
    st = i['fields']
    lat = st['position'][0]
    long = st['position'][1]
    av_bikes = st['available_bikes']
    av_stands = st['available_bike_stands']
    name = st['name']
    tot = st['bike_stands']
    bulle = name + ('<br/>available: %i;<br/>parking: %i;\
                    <br/>total: %i' % (av_bikes, av_stands, tot))
    map_osm.simple_marker(location=[lat, long],
                          popup=bulle)
map_osm.create_map(path='osm.html')
