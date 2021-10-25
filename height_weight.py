import pandas as pd
import plotly.express as pl 

data = pd.read_csv('data.csv')
height = data["Height"].tolist()
weight = data["Weight"].tolist()

y1 = max(height)
y0 = 28.2
x1 = max(weight)
x0=min(weight)
# m = (y1-y0)/(x1-x0)
m=0.95
print(m)
c = -93
y=[]
for x in height:
    y_value = m*x + c
    y.append(y_value)

figure = pl.scatter(x=height, y=weight)
figure.update_layout(shapes=[dict(type="line",y0=min(y),y1=max(y),x0=min(height),x1=max(height))])
figure.show()

user_height = input("What is your height in cm?")
user_height = int(user_height)
predicted_weight = 0.95*user_height-93
print("Predicted Weight is", predicted_weight, "kg")


# figure = pl.scatter(x=height, y=weight)
# figure.show()

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

user_height = input("What is your height in cm?")
user_height = int(user_height)
predicted_weight = m1*user_height+c1
print("Predicted Weight is", predicted_weight, "kg")

