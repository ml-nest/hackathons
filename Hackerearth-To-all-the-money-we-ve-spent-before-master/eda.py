import pandas as pd 
import numpy as np 

df = pd.read_csv('dataset/train.csv')
print(df.columns)
print(df.info())