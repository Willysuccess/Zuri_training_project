import pandas as pd
from matplotlib import style

style.use("fivethirtyeight")
xyz_web = {'Day': [1,2,3,4,5,6], 'visitors': [1000,7000,6000,1000,400,350], 'Bounce_Data': [20,20,23,15,10,34]}

df = pd.DataFrame(xyz_web)
df.plot
plt.show




print(df)