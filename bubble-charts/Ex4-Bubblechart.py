#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go 
import pandas as pd 

# create a DataFrame from the .csv file:
df = pd.read_csv('mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data =[go.Scatter(x=df['acceleration'],	y=df['mpg'], text=df['name'], mode='markers',
					marker=dict(size=1.2*df['cylinders']))]

# create a layout with a title and axis labels
layout = go.Layout(title='Bubble Chart', hovermode='closest', 
	xaxis_title="Acceleration", yaxis_title="MPG")

# create a fig from data & layout, and plot the fig
fig=go.Figure(data=data, layout=layout)

pyo.plot(fig)
fig.write_html("Acceleration_vs_MPG.html")