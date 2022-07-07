import pandas as pd
import sqlite3

data = pd.read_csv("bmi.csv", sep="\t")
print(data)
a = data['Height(m)'].mean()
print(a)
rows , columns = data.shape
print(columns)
print(data[0:2])
print(data.columns)
print(data.bmi)
print(type(data['bmi']))
print(data[['Height(m)','bmi']])
print(data['bmi'].std())
print(data.describe())          #use describe() for quickly printing the statistic of your data
print(data[data.bmi == data.bmi.max()])
print(data.index)


