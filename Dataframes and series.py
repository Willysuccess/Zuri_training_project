#Pandas is a python library used for data manipulation , analysis and cleaning
#It is used for tabular data, unlabelled data.

#Dataframes are two-dimensional.Their sizes are mutable. It is also called heterogenous tabular data
#Series is a one-dimensional label array capable of holding data of any type(int,str,float, python object). It's
#axis label is called index . It is likened to a column in an excel sheet.

import pandas as pd  # alias is pd
import numpy as np
'''
s = pd.Series([1, 2, 3, 4, 5, 6, np.nan, 8, 9, 10])
print(s)

d = pd.date_range("20220601", periods=10)
print(d)

df = pd.DataFrame(np.random.randn(10, 5), index=d, columns=["A", "B", "C", "D", "E"])
print(df)

df = pd.DataFrame({"A": [1,2,3,4],"B": pd.Timestamp("20220601"),"C":pd.Seriesj})

arr = [0,1,2,3,4]
order = [1,2,3,4,5]
s2 = pd.Series(arr, index=order)
print(s2)
n=np.random.randn(5)
print(n)

index = ["a","b","c","d","e"]
s2 = pd.Series(n, index=index)
print(s2)

d = {'a':1,'b':2,'c':3}
e = pd.Series(d)
print(e)

#modify a series
s2.index = ["A","B","C","D","E"]
print(s2)
print(s2[:3])

#SERIES OPERATION
arr1 = [0,1,2,3,4,5,7]
arr2 = [6,7,8,9,5]
s4 = pd.Series(arr1)
s5 = pd.Series(arr2)
s6 = s5.add(s4)              #add s5 to s4
print(s6)
s6 = s4.sub(s5)              #substract s5 from s4
print(s6)
s6 = s5.mul(s4)
print(s6)
s6 = s5.div(s4)
print(s6)
print("Median is", s5.median())
print("Maximum is",s5.max())
print("Minimum is", s5.min())

#CREATING DATAFRAME
dates = pd.date_range('today',periods=6)    #Define time sequence as index
print(dates)
num_arr = np.random.randn(6, 4)             #Import numpy random array. ROW IS 6. COLUMN IS 4
print(num_arr)
columns = ['A','B','C','D']
print(columns)
df1 = pd.DataFrame(num_arr,index=dates,columns=columns)     #using dates as index, and columns A,B,C,D as colummns
print(df1)
'''
#CREATE DATAFRAME WITH DICTIONARY ARRAY

data = {'animal': ['cat','dog','snake','cat','snake','dog','cat','dog','snake','dog'],
        'age': [2.5,3,3.5,np.nan,5,2,4.5,np.nan,7,3],
        'visits': [1,2,3,2,3,1,1,2,3,2],
        'priority': ['yes','no','yes','no','yes','no','yes','no','yes','no']}

labels = ['a','b','c','d','e','f','g','h','i','j']

df2 = pd.DataFrame(data, index=labels)
print(df2)
print(df2.dtypes)
print(df2.head)

print(df2.tail())
print(df2.index)
print(df2.values)
print(df2.columns)

a = df2.describe()      #see statistical data of dataframe
print(a)
b = df2.T
print(b)
c = df2.sort_values(by='priority')
print(c)
#slicing Dataframe
d = df2[1:3]
print(d)

#Query Dataframe by Tag

e = df2[['age','priority']]
print(e)

df2.isnull()    #looking for null values

f =df2.sum()
print(f)

#Operation for Dataframe missing values

df4 = df2.copy()
print(df4)
df4.fillna(4)   #fill all null value with 4
z = df4.dropna(how='any')
print(z)


#Visualization In Pandas

#Series and Dataframe line chart
import numpy as np


ts = pd.Series(np.random.randn(50), index = pd.date_range('today', periods=50))
ts = ts.cumsum()
a = ts.plot
print(a)
df = pd.DataFrame(np.random.randn(50,4), index = ts.index, columns = ['A','B','C','D'])
df = df.cumsum()
v=df.plot
print(v)

#Remove repeated data using pandas

df = pd.DataFrame({'A': [1,2,2,3,4,5,6,7,7,6,8]})
n = df.loc[ df['A'].shift() != df['A']]
print(n)
'''