import pandas as pd

'''
df = pd.read_csv("bmi.csv", sep="\t")
print(df)

#CREATING A DATAFRAME  USING A TUPLE LIST(TUPLE INSIDE A LIST)

weather_data1= [('1/1/2022', 32,6,'Rain'),      #each line represent a row
                ('1/2/2022', 35,7, 'Sunny'),            #,,
                ('1/3/2022', 28,2, 'Snow')              #,,
]
data2 = pd.DataFrame(weather_data1, columns=['days', 'temperature', 'windspeed','event'])    #the columns headings must be specified

print(data2)

#CREATING A DATAFRAME USING A LIST OF DICTIONARIES
weather_data2 = [{'day': '1/1/2022', 'temperature': 32,'windspeed': 6, 'event': 'Rain'},
                {'day': '2/1/2022', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
                {'day': '3/1/2022', 'temperature': 37, 'windspeed': 8, 'event': 'Cloudy'},
                ]

data3 = pd.DataFrame(weather_data2)
print(data3)
df = pd.concat([data2, data3])
print(dft)


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
'''