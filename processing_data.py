import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# read data set
data=pd.read_csv('WorldSustainabilityDataset.csv')
# get list of countries
list_of_countries=list(set(data['Country Name']))
def country_metric(country, metric):
    '''
    Returns the column of metric for the specific country
    :param country: name of country, string
    :param metric: name of metric, string
    '''
    country_data=data[data['Country Name']==country]
    return (country_data[['Year',metric]])
def plot_country_metric(country, metric):
    '''
    Produces a line plot for a metric for a country over the years
    
    :param country: name of country, string
    :param metric: name of metric, string
    '''
    sns.lineplot(country_metric(country, metric), x='Year',y=metric)  
def metric_plot():
    '''
    For each metric plots each the number of NaN values they have as a bar chart
    '''
    figs, axes=plt.subplots(1,1)
    axes.bar(x=range(0,len(data.isnull().sum())),height=data.isnull().sum())
    axes.set_xlabel('Metric Index')
    axes.set_ylabel('Count')
    axes.set_title('Number of NaN for each metric')
metric_plot()



plt.show()