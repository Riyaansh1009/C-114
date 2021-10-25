import pandas as pd 
import plotly.express as pl
data = pd.read_csv('main.csv')
height = data['GRE Score'].tolist()
weight = data['Chance of Admit '].tolist()

import numpy as np
height_array = np.array(height)
weight_array = np.array(weight)

m1,c1 = np.polyfit(height_array,weight_array,1)

y1=[]
for x in height:
    y_value = m1*x + c1
    y1.append(y_value)

figure1 = pl.scatter(x=height_array, y=weight_array)
figure1.update_layout(shapes=[dict(type="line",y0=min(y1),y1=max(y1),x0=min(height_array),x1=max(height_array))])
figure1.show()

user_height = input("What is your GRE score?")
user_height = int(user_height)
predicted_weight = m1*user_height+c1
print("Predicted chance is", predicted_weight)

