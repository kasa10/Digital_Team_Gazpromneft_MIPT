import pandas as pd

import matplotlib.pyplot as plt
#%%
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/train.csv')
df2=pd.read_csv('data/interpolate.csv')
df3=pd.read_csv('data/pad_data.csv')


#%%


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


#ТУТ РАЗДЕЛЯЕМ
#%%
from sklearn.model_selection import train_test_split

train1, test1 = train_test_split(u, test_size=0.25, shuffle=False)


print(f'Размер train таблицы {train1.shape}')
print(f'Размер test таблицы {test1.shape}')

#%%
#Предсказание по средней скользящей за 7 дней
train1['m7']=train1['Дебит нефти'].rolling( 7 ).mean()

a=train1['m7'].describe()
train1 = train1.fillna(a['75%'])

train1['m7'].plot()
plt.show()

#%%
train1['m7'].count()
for i in range(0,90):
    train1 = train1.append(pd.Series(), ignore_index=True)







#%%
#Предсказание по средней скользящей за 30 дней
train1['m30']=train1['Дебит нефти'].rolling( 30 ).mean()

a=train1['m30'].describe()
train1 = train1.fillna(a['75%'])

train1['m30'].plot()
plt.show()







#%%


