!pip install pandas folium
!pip install pandas folium numpy

import pandas as pd
import folium
import numpy as np
from folium import FeatureGroup, LayerControl

file_path = r"C:\Users\gmkim\Desktop\khuthon\output_1.csv"

data = pd.read_csv(file_path, encoding='utf-8')

def add_jitter(series, stdev=0.001):
    return series + np.random.randn(len(series)) * stdev

data['Latitude'] = add_jitter(data['Latitude'])
data['Longitude'] = add_jitter(data['Longitude'])

map_ = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=12)

colors = {
    'bundle of ropes': 'blue',
    'circular fish trap': 'green',
    'pet': 'red',
    'fish net': 'purple',
    'plastic': 'orange',
    'rope': 'darkblue',
    'Styrofoam': 'lightgreen',
    'tire': 'pink',
    'wood': 'gray'
}

object_types = data['Object Name'].unique()
for obj in object_types:
    group = FeatureGroup(name=obj, show=False)

    obj_data = data[data['Object Name'] == obj]
    for _, row in obj_data.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            color=colors[obj],
            fill=True,
            fill_color=colors[obj],
            fill_opacity=0.5
        ).add_to(group)
    group.add_to(map_)

LayerControl().add_to(map_)

map_.save('interactive_map_west.html')
