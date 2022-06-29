import pandas as pd
import matplotlib
#%%
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/train.csv')
test=pd.read_csv('baseline/baseline_forecast.csv')

corr=df.corr()

#%%
x1=corr['Дебит нефти']
#x1.keys() - названия cтолбцов
#
