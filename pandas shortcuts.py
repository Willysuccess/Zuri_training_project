import pandas as pd

column = ['Mariya','Batman','Spongebob']

titled_columns = {'Name': column,
                 'Height(m)': [1.67,1.9,0.25],
                 'Weight(kg)': [54,100,1]}
data = pd.DataFrame(titled_columns)
'''print(data)
selected_column = data['Weight(kg)'][1]         #for column you call the column name before the index
selected_row =data.iloc[1]        #for row you use "iloc". put the index before calling the column name
print(selected_row)
print(selected_column)
'''
#Manipulate Dataframe values

bmi = []        #body mass index
#weight/(height ** 2)

for i in range(len(data)):
    bmi_score = data['Weight(kg)'][i]/(data['Height(m)'][i] ** 2)
    bmi.append(bmi_score)

data['bmi'] = bmi

print(data)

#save dataframe to a file

data.to_csv("bmi.csv", index=False, sep="\t")