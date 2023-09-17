#!/usr/bin/env python
# coding: utf-8

# In[9]:


from geoband.API import *
GetCompasData('SBJ_2308_003', '3', '3.완주군_버스정류장현황.csv')


# In[10]:


from geoband.API import *
GetCompasData('SBJ_2308_003', '5', '5.완주군_버스정류장별_승차이력.csv')


# In[18]:


import pandas as pd
import folium

bus_station_df = pd.read_csv('3.완주군_버스정류장현황.csv')
bus_riding_df = pd.read_csv('5.완주군_버스정류장별_승차이력.csv')

merged_df = pd.merge(bus_riding_df, bus_station_df, on='bis_id')  # bis_id를 기준으로 조인

grouped_df = merged_df.groupby('bis_id').agg({'total_cnt': 'sum'}).reset_index()

m = folium.Map(location=[35.83375079, 127.1185573], zoom_start=13)  # 초기 위치와 확대 정도 설정

for idx, row in grouped_df.iterrows():
    lat = bus_station_df.loc[bus_station_df['bis_id'] == row['bis_id'], 'lat'].iloc[0]
    lon = bus_station_df.loc[bus_station_df['bis_id'] == row['bis_id'], 'lon'].iloc[0]
    cnt = row['total_cnt']
    
    color = 'green'
    if cnt > 10000:
        color = 'red'
        
    radius_value = min(cnt / 10, 3)
        
    folium.CircleMarker(
        location=[lat, lon],
        radius=radius_value,  
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6  
    ).add_to(m)


m.save('bus_stations_bis_id.html')  

