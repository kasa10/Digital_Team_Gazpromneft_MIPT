import pandas as pd
from sklearn.metrics import mean_squared_error
from statistics import mean

import matplotlib.pyplot as plt
#%%
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/train.csv')
df2=pd.read_csv('data/interpolate.csv')
#df3=pd.read_csv('data/pad_data.csv')
prim=pd.read_csv('baseline/baseline_forecast.csv')


#%%
e1=[]

u=df2[df2['Номер скважины']==1]
u['Номер скважины'].count()

train1 = u[u.datetime < '1992-04-11']

#%%

for i in range(0,90):
    train1 = train1.append(pd.Series(), ignore_index=True)
    #Средняя скользящая за 3 дня
    train1 = train1.fillna(train1['Дебит нефти'][train1['Дебит нефти'].count()-4:train1['Дебит нефти'].count()-1].sum()/3)



#%%
prim['forecast'][prim['Номер скважины']==1][] = train1['Дебит нефти'][-90:]


#%%
prim['forecast'][prim['Номер скважины']==1].plot()
plt.show()


















