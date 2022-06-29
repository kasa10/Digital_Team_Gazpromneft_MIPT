import pandas as pd
import matplotlib
#%%
from sklearn.model_selection import train_test_split
df=pd.read_csv('data/train.csv')
df2=pd.read_csv('data/interpolate.csv')
df3=pd.read_csv('data/pad_data.csv')

#%%
pd.isnull(df)

#%% Количество пропущенных значений
pd.isnull(df).sum()

#%%
x=0
# if df['Номер скважины'] == 41:
#     x=x+1

