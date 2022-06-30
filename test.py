import pandas as pd
from sklearn.metrics import mean_squared_error
from statistics import mean

import matplotlib.pyplot as plt
#%%
from sklearn.model_selection import train_test_split
r=pd.read_csv('result.csv')
prim=pd.read_csv('baseline/baseline_forecast.csv')
