#!/usr/bin/env python
# coding: utf-8

# In[1]:


from geoband.API import *
GetCompasData('SBJ_2308_003', '8', '8.완주군_시간대별_유동인구.csv')


# In[2]:


import pandas as pd


# In[3]:


df_sPeople = pd.read_csv('8.완주군_시간대별_유동인구.csv')
df_sPeople.shape


# In[4]:


df_sPeople.head(10000000)


# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 가상의 데이터프레임 df 생성. 
df = pd.read_csv('8.완주군_시간대별_유동인구.csv')

# 데이터 프레임의 일부를 선택. 예를 들어, 2020년 1월 데이터만을 선택
df_202001 = df[df['STD_YM'] == 202001]

# 시간대별 유동인구의 평균을 계산
heatmap_data = df_202001.drop(['STD_YM', 'lon', 'lat'], axis=1).mean().reset_index()
heatmap_data.columns = ['Time', 'Avg_Pop']

# 데이터를 2차원 형태로 재구성
heatmap_data['Hour'] = heatmap_data['Time'].apply(lambda x: int(x.split('_')[1]))
heatmap_data = heatmap_data.pivot("Hour", "Time", "Avg_Pop")

# 히트맵 그리기
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f")
plt.title('Average Population by Time of Day (2020-01)')
plt.show()


# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 가상의 데이터프레임 df 생성. 실제 데이터를 로드하실 때는 이 부분을 적절히 수정해 주세요.
df = pd.read_csv('8.완주군_시간대별_유동인구.csv')

# 시간대별 유동인구의 평균을 계산
heatmap_data = df.drop(['STD_YM', 'lon', 'lat'], axis=1).mean().reset_index()
heatmap_data.columns = ['Time', 'Avg_Pop']

# 데이터를 2차원 형태로 재구성
heatmap_data['Hour'] = heatmap_data['Time'].apply(lambda x: int(x.split('_')[1]))
heatmap_data = heatmap_data.pivot("Hour", "Time", "Avg_Pop")

# 히트맵 그리기
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f")
plt.title('Average Population by Time of Day (2020-2022)')
plt.show()

