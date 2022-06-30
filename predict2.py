import pandas as pd
from sklearn.metrics import mean_squared_error
from statistics import mean

import matplotlib.pyplot as plt
##%%
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/train.csv')
df2=pd.read_csv('data/interpolate.csv')
#df3=pd.read_csv('data/pad_data.csv')
prim=pd.read_csv('baseline/baseline_forecast.csv')
prim2=pd.read_csv('baseline/baseline_forecast.csv')

#%%
x=[]
e1=[]
for i in range(0,105+1):
    u=df2[df2['Номер скважины']==i]
    u['Номер скважины'].count()

    train1 = u[u.datetime < '1992-04-11']

    #%%

    for j in range(0,90):
        train1 = train1.append(pd.Series(), ignore_index=True)
        #Средняя скользящая за 3 дня
        train1 = train1.fillna(train1['Дебит нефти'][train1['Дебит нефти'].count()-4:train1['Дебит нефти'].count()-1].sum()/3)

    y = train1['Дебит нефти'][-90:].tolist()
    for l in y:
        x.append(l)
        #prim['forecast'].loc[j*i] = train1['Дебит нефти'][-1:].values

    #%%

for t in range(0,9540):
    prim['forecast'].loc[t] = x[t]

    #prim.replace(prim['forecast'][prim['Номер скважины'] == 0][0] , 2 )

    #['forecast'][prim['Номер скважины']==0]
    #dframe = pd.DataFrame(lst)
    #prim(prim['forecast'][prim['Номер скважины']==0],train1['Дебит нефти'][-90:])







     #%%
    prim.to_csv('result.csv',index=False)

     #%%
    # prim['forecast'][prim['Номер скважины']==2].plot()
    # plt.show()


















