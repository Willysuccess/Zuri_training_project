import pandas as pd

data = pd.read_csv(r"C:\Users\user\Downloads\archive\Stores.csv")
'''
print(data)
print(data.head())
print(data.dtypes)
print(data.index)
print(data.info())
'''
#QUESTIONS
#1.'''Find all the number of unique "Store_sales" values(number of values present) in the data'''

print(data.head(2))
a = data["Store_Sales"].nunique() #Number of values
print(a)

#2. '''Find the number of times when a value occurs'''
'''It can be solved by either value_counts or filtering'''
#value_counts()
print(data.head(3))
b = data.Store_Area.value_counts()          #Frequency of each value in the specified column
print(b)

#Filtering

c = data[data.Store_Area == 1439]
print(c)

#3. '''Find the number of times when store area was 1387
m = data[data.Store_Area == 1387]
print(m)

#4. '''Find the number of values that are null

e = data.isnull().sum()         #There is no null value in any column
print(e)

f = data.notnull().sum()        #No NULL VALUE ALSO
print(f)

#5. '''Rename a column'''

g = data.rename(columns= {'Items_Available' : 'Available Items'})
print(g)
print(data)

#6. '''What is the mean of Store_Sales?'''

h = data.Store_Sales.mean()
print(h)

#7. '''What is the standard Deviation of Daily_Customer_count?'''

i = data.Daily_Customer_Count.std()
print(i)


#8. '''What is the variance of Store_Area?'''

j = data.Store_Area.var()
print(j)

#9. '''Find all instances when 1299 was recorded'''

k = data[data.Store_Area == 1299]
print(k)
l = data[data['Store_Area'] == 1299]
print(l)

#10. '''Find all the instance when store ID is above 200 and Daily Customer Count is 300'''

#n = data[(data['Store ID'] > 200) & (data['Daily_Customer_Count'] == 300)]
#print(n)

#11. '''What is the mean value of each column against each 'Items_Available' '''

print(data.mean())

#12. Min and Max of each column

print(print(data.Store_Area.min()) & print(data.Store_Area.max()))


