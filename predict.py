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
for i in range(0,105+1):
    u=df2[df2['Номер скважины']==i]
    u['Номер скважины'].count()

    #%%
    # corr=u.corr()
    #
    # x1=corr['Дебит нефти']
    # #x1.keys() - названия cтолбцов
    #
    # x2=x1.sort_values(ascending=False) #Отсортированный


    #ТУТ РАЗДЕЛЯЕМ
    #%%
    # from sklearn.model_selection import train_test_split
    #
    # train1, test1 = train_test_split(u, test_size=0.15, shuffle=False)
    #
    #
    # print(f'Размер train таблицы {train1.shape}')
    # print(f'Размер test таблицы {test1.shape}')

    test = u[u.datetime >= '1992-01-13']
    test1 = test[test.datetime <= '1992-04-11']
    train1 = u[u.datetime < '1992-01-13']

    #%%
    #Предсказание по средней скользящей за 7 дней
    # train1['m7']=train1['Дебит нефти'].rolling( 7 ).mean()
    #
    # a=train1['m7'].describe()
    # train1 = train1.fillna(a['75%'])

    # train1['m7'].plot()
    # plt.show()

    #%%
    #train1['m7'].count()
    for i in range(0,90):
        train1 = train1.append(pd.Series(), ignore_index=True)
        #НИЖЕ ВМЕСТО ДЕБИТ НЕФТИ БЫЛО 'm7'
        train1 = train1.fillna(train1['Дебит нефти'][train1['Дебит нефти'].count()-4:train1['Дебит нефти'].count()-1].sum()/3)





    #train1=train1.drop(labels = [554])





    #%%
    # train1['m7']=train1['m7'].fillna(train1['m7'].rolling( 7 ).mean())
    #
    # #%%
    # #Предсказание по средней скользящей за 30 дней
    # train1['m30']=train1['Дебит нефти'].rolling( 30 ).mean()
    #
    # a=train1['m30'].describe()
    # train1 = train1.fillna(a['75%'])
    #
    # train1['m30'].plot()
    # plt.show()
    #
    #
    #








    #%% Тестирование


    try:
        rmse_metric = mean_squared_error(train1['Дебит нефти'][-90:],test1['Дебит нефти'][-90:],squared=False)
        print(rmse_metric)
        e1.append(rmse_metric)
    except:
        continue

print('СРЕДНЯЯ ОШИБКА ',mean(e1))
print('Минимальная ОШИБКА ',min(e1))
print(len(e1))
    # train1['Дебит нефти'].plot()
    # plt.show()

