import pandas as pd

import matplotlib.pyplot as plt
#%%
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/train.csv')
df2=pd.read_csv('data/interpolate.csv')
df3=pd.read_csv('data/pad_data.csv')


#%%
p=[]

u=df2[df2['Номер скважины']==1]
u['Номер скважины'].count()

#%%
corr=u.corr()

x1=corr['Дебит нефти']
#x1.keys() - названия cтолбцов

x2=x1.sort_values(ascending=False) #Отсортированный


#%%
u['Дебит нефти'].plot()
plt.show()

#%%
#Предсказание по средней скользящей за 7 дней
u['m7']=u['Дебит нефти'].rolling( 7 ).mean()

u['m7'].plot()
u['Дебит нефти'].plot()
plt.show()