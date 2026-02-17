import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# read data set
data=pd.read_csv('WorldSustainabilityDataset.csv')
# get rows of data set that belong to specific countries in array, that meet condition that the continent is South America
data_test=data[data['Continent']=='South America']
# plots the data for the given column list in the x_axis and the column list for the y_axis, hue creates a key for each country
sns.lineplot(data_test, x='Year', y=data.iloc[:,29], hue='Country Name')
plt.show()