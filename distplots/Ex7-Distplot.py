#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff 
import pandas as pd 

# create a DataFrame from the .csv file:
df = pd.read_csv('iris.csv')

# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
x1 = df[df['class']=='Iris-setosa']['petal_length']
x2 = df[df['class']=='Iris-versicolor']['petal_length']
x3 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
data = [x1, x2, x3]
group_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(data, group_labels)

pyo.plot(fig)
fig.write_html("Petal Lengths Distplots.html")