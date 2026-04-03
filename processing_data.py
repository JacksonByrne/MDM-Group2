import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# read data set
data=pd.read_csv('WorldSustainabilityDataset.csv')
# get list of countries
list_of_countries=list(set(data['Country Name']))
def country_metric(country, metric,df):
    '''
    Returns the column of metric for the specific country
    :param country: name of country, string
    :param metric: name of metric, string
    '''
    country_data=df[df['Country Name']==country]
    return (country_data[['Year',metric]])
def plot_country_metric(country, metric,df, goal_labels):
    '''
    Produces a line plot for a metric for a country over the years
    
    :param country: name of country, string
    :param metric: name of metric, string
    '''
    sns.lineplot(country_metric(country, metric,df), x='Year',y=metric, label=goal_labels[metric[-6:].replace(" ","")])  
def metric_plot():
    '''
    For each metric plots each the number of NaN values they have as a bar chart
    '''
    figs, axes=plt.subplots(1,1)
    axes.bar(x=range(0,len(data.isnull().sum())),height=data.isnull().sum())
    axes.set_xlabel('Metric Index')
    axes.set_ylabel('Count')
    axes.set_title('Number of NaN for each metric')

def norm_columns(df, data):
    # Creates a new updated dataframe where the values have been normalised, i.e put the values between 0 and 1 bases on means and standard deviations
    # add list of metrics here only ones with numerical values, that can be normalised
    metrics=data.columns.values[3:43]
    metrics=np.append(metrics,data.columns.values[44])
    metrics=np.append(metrics,data.columns.values[46:49])
    metrics=np.append(metrics,data.columns.values[50:53])
    # create array of indexs showing if a metric is good to be low or high, needs to be updated 
    lower_values_good=[3,4,5,6,9,21,24,32,33,37,38,39,40]
    years=np.linspace(2000,2018,19)
    # loop through each metric
    for i,metric in enumerate(metrics):
        # get min and max values of metric
        min=np.nanmin(df[metric])
        max=np.nanmax(df[metric])
        # loop through each year calculating normalised value for each country for metric and updating the dataframe
        for year in years:
            year_values=(df[df['Year']==int(year)][metric])
            # normalise values 
            norm_score=(year_values-min)/(max-min)
            # if lower value is better change the normilisation score
            if i in lower_values_good:
                norm_score=1-norm_score
            # update dataframe with normalised value
            new_df=pd.DataFrame({metric:norm_score})
            df.update(new_df)
# copy dataframe to keep imported dataframe
df=data.copy()
# list of goals
goal_labels = {
    "Goal1":  "No Poverty",
    "Goal2":  "Zero Hunger",
    "Goal3":  "Good Health and Well-being",
    "Goal4":  "Quality Education",
    "Goal5":  "Gender Equality",
    "Goal6":  "Clean water and sanitation",
    "Goal7":  "Affordable and Clean Energy",
    "Goal8":  "Decent Work and Economic Growth",
    "Goal9":  "Industry, Innovation & Infrastructure",
    "Goal10": "Reduced Inequalities",
    "Goal13": "Climate Action",
}
# normalise columns
norm_columns(df,data)

# list of goals and the metrics used for them
goal_metrics_labels = {
    # No Poverty
    "Goal1":  ["Proportion of population below international poverty line (%) - SI_POV_DAY1 - 1.1.1"],
    # Zero Hunger 
    "Goal2":  ["Prevalence of undernourishment (%) - SN_ITK_DEFC - 2.1.1"],
    # Good Health
    "Goal3":  ["Life expectancy at birth, total (years) - SP.DYN.LE00.IN"],
    # Quality Education 
    "Goal4":  ["Children out of school (% of primary school age) - SE.PRM.UNER.ZS",
    "Compulsory education, duration (years) - SE.COM.DURS",
    "Primary completion rate, total (% of relevant age group) - SE.PRM.CMPT.ZS",
    "School enrollment, preprimary (% gross) - SE.PRE.ENRR",
    "School enrollment, primary (% gross) - SE.PRM.ENRR",
    "School enrollment, secondary (% gross) - SE.SEC.ENRR",
    "Pupil-teacher ratio, primary - SE.PRM.ENRL.TC.ZS"],
    # Gender equality 
    "Goal5":  ["Proportion of seats held by women in national parliaments (%) - SG.GEN.PARL.ZS",
    "Women Business and the Law Index Score (scale 1-100) - SG.LAW.INDX"],
    # Clean water
    "Goal6":  ["Proportion of population using basic drinking water services (%) - SP_ACS_BSRVH2O - 1.4.1"],
    # Clean Energy
    "Goal7":  ["Access to electricity (% of population) - EG.ELC.ACCS.ZS",
    "Renewable electricity output (% of total electricity output) - EG.ELC.RNEW.ZS",
    "Renewable energy consumption (% of total final energy consumption) - EG.FEC.RNEW.ZS"],
    # Decent Work and Economic Growth
    "Goal8":  ["Adjusted net national income per capita (annual % growth) - NY.ADJ.NNTY.PC.KD.ZG",
    "Inflation, consumer prices (annual %) - FP.CPI.TOTL.ZG",
    "Unemployment rate, male (%) - SL_TLF_UEM - 8.5.2",
    "Unemployment rate, women (%) - SL_TLF_UEM - 8.5.2"],
    # Industry,Innovation and Infrastructure
    "Goal9":  ["Automated teller machines (ATMs) (per 100,000 adults) - FB.ATM.TOTL.P5",
    "Individuals using the Internet (% of population) - IT.NET.USER.ZS",
    "Proportion of population covered by at least a 2G mobile network (%) - IT_MOB_2GNTWK - 9.c.1",
    "Proportion of population covered by at least a 3G mobile network (%) - IT_MOB_3GNTWK - 9.c.1"],
    # Requced Inequalities 
    "Goal10": ["Gini index (World Bank estimate) - SI.POV.GINI"],
    # Climate Action 
    "Goal13": ["Adjusted net savings, excluding particulate emission damage (% of GNI) - NY.ADJ.SVNX.GN.ZS",
    "Adjusted savings: carbon dioxide damage (% of GNI) - NY.ADJ.DCO2.GN.ZS",
    "Adjusted savings: natural resources depletion (% of GNI) - NY.ADJ.DRES.GN.ZS",
    "Adjusted savings: net forest depletion (% of GNI) - NY.ADJ.DFOR.GN.ZS",
    "Adjusted savings: particulate emission damage (% of GNI) - NY.ADJ.DPEM.GN.ZS"],
}
# loop through each goal and caluclate a mean for all of the metrics to get a composite index for each country for each year for that goal
goals=goal_metrics_labels.keys()
for goal in goals:
    metrics_for_goal=goal_metrics_labels[goal]
    # creates a new mean which is the composite index of the two goals
    # decide how to combine metrics? For now just used standard mean. Could use median, have weight for specific goals
    # add column to dataframe for each composite index
    df[f'Composite Index {goal}'] = df[metrics_for_goal].mean(axis=1)


# different plots to just show what the data now looks like
# plot each goal for a specific country
'''country='United Kingdom'
for goal in goals:
    plot_country_metric(country, f'Composite Index {goal}',df, goal_labels)
plt.ylabel('Composite Index')
plt.title(f'Goals for {country} over time')
plt.legend(loc='upper left')
plt.show()
# plot a specific goal for multiple countries
countries=[list_of_countries[:10]]
goal='Goal7'
for country in countries[0]:
    sns.lineplot(country_metric(country, f'Composite Index {goal}',df), x='Year',y=f'Composite Index {goal}', label=country)
    plt.ylim(0,1)
    plt.title(f'{goal_labels[goal]} over time')
plt.show()'''

def country_goal_data(country, goal, df):
    '''
    country : 'United Kingdom'
    goal    : 'Goal1', 'Goal7'
    '''
    metric = f'Composite Index {goal}'
    country_df = df[df['Country Name'] == country]
    return country_df[['Year', metric]]
'''
Added a function to call for dynamic time warping for me!
Can be called through importing
'''