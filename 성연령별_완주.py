#!/usr/bin/env python
# coding: utf-8

# In[30]:


from geoband.API import *
GetCompasData('SBJ_2308_003', '7', '7.완주군_성연령별_유동인구.csv')


# In[31]:


import pandas as pd


# In[32]:


df_sPeople = pd.read_csv('7.완주군_성연령별_유동인구.csv')
df_sPeople.shape


# In[33]:


df_sPeople.head(10000000)


# In[34]:


df_sPeople.columns


# In[39]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('7.완주군_성연령별_유동인구.csv')

# 성별 합치기
age_cols_men = ['m_10g_pop', 'm_20g_pop', 'm_30g_pop', 'm_40g_pop', 'm_50g_pop', 'm_60g_pop']
age_cols_women = ['w_10g_pop', 'w_20g_pop', 'w_30g_pop', 'w_40g_pop', 'w_50g_pop', 'w_60g_pop']
age_cols = ['10', '20', '30', '40', '50', '60']

# 성별 데이터를 합쳐서 새로운 컬럼 생성
for men_col, women_col, age_col in zip(age_cols_men, age_cols_women, age_cols):
    df[age_col] = df[men_col] + df[women_col]

# 년월과 연령대만 선택하여 새로운 데이터프레임 생성
df_heatmap = df.groupby('STD_YM')[age_cols].mean().reset_index()

# 히트맵 그리기
plt.figure(figsize=(12, 8))
sns.heatmap(df_heatmap.set_index('STD_YM'), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('People_Count')
plt.xlabel('Age')
plt.ylabel('Year_m')
plt.show()


# In[40]:


import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('7.완주군_성연령별_유동인구.csv')

# 성별 합치기
age_cols_men = ['m_10g_pop', 'm_20g_pop', 'm_30g_pop', 'm_40g_pop', 'm_50g_pop', 'm_60g_pop']
age_cols_women = ['w_10g_pop', 'w_20g_pop', 'w_30g_pop', 'w_40g_pop', 'w_50g_pop', 'w_60g_pop']
age_cols = ['10', '20', '30', '40', '50', '60']

# 성별 데이터를 합쳐서 새로운 컬럼 생성
for men_col, women_col, age_col in zip(age_cols_men, age_cols_women, age_cols):
    df[age_col] = df[men_col] + df[women_col]

# 년월과 연령대별로 그룹화하고 평균을 계산
df_grouped = df.groupby('STD_YM')[age_cols].mean().reset_index()

# 라인 차트 그리기
plt.figure(figsize=(12, 8))

for age_col in age_cols:
    plt.plot(df_grouped['STD_YM'], df_grouped[age_col], label=age_col)

plt.title('PeopleCount')
plt.xlabel('Year_M')
plt.ylabel('people')
plt.legend()
plt.grid(True)
plt.show()


# In[41]:


import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('7.완주군_성연령별_유동인구.csv')

# 성별 합치기
age_cols_men = ['m_10g_pop', 'm_20g_pop', 'm_30g_pop', 'm_40g_pop', 'm_50g_pop', 'm_60g_pop']
age_cols_women = ['w_10g_pop', 'w_20g_pop', 'w_30g_pop', 'w_40g_pop', 'w_50g_pop', 'w_60g_pop']
age_cols = ['10대', '20대', '30대', '40대', '50대', '60대']

# 성별 데이터를 합쳐서 새로운 컬럼 생성
for men_col, women_col, age_col in zip(age_cols_men, age_cols_women, age_cols):
    df[age_col] = df[men_col] + df[women_col]

# 일부 특정 시간대만 선택 (예: 202001)
df_202001 = df[df['STD_YM'] == 202001]

# 라인 차트 그리기
plt.figure(figsize=(12, 8))

for age_col in age_cols:
    plt.plot(df_202001.index, df_202001[age_col], label=age_col)

plt.title('2020년 1월 성연령별 유동인구 라인 차트')
plt.xlabel('Index')
plt.ylabel('유동인구')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




