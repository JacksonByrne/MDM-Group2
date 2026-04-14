import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    "Goal11": "Sustainable Cities and Communities",
    "Goal13": "Climate Action",
    "Goal15": "Life on Land",
    "Goal16": "Peace, Justice and Strong Institutions",
    "Goal17": "Partnerships for the Goals"
}
# normalise columns

# list of goals and the metrics used for them
goal_metrics_labels = {
    # No Poverty
    "Goal1":  ["Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)",
    "Poverty gap at $5.50 a day (2011 PPP) (% of population)",
    "Poverty headcount ratio at national poverty lines (% of population)",
    "Adequacy of social protection and labor programs (% of total welfare of beneficiary households)",
    "Poverty gap at $1.90 a day (2011 PPP) (%)"
    ],
    # Zero Hunger 
    "Goal2":  ["Prevalence of undernourishment (% of population)",
    "Cereal yield (kg per hectare)",
    "Prevalence of stunting, height for age (% of children under 5)",
    "Agricultural land (% of land area)",
    "Food production index (2004-2006 = 100)"
    ],
    # Good Health
    "Goal3":  ["Mortality rate, under-5 (per 1,000 live births)",
    "Life expectancy at birth, total (years)",
    "Maternal mortality ratio (modeled estimate, per 100,000 live births)",
    "Incidence of tuberculosis (per 100,000 people)",
    "Current health expenditure (% of GDP)"
    ],
    # Quality Education 
    "Goal4":  ["School enrollment, primary (% gross)",
    "Literacy rate, adult total (% of people ages 15 and above)",
    "Children out of school (% of primary school age)",
    "Government expenditure on education, total (% of GDP) [SE.XPD.TOTL.GD.ZS]",
    "Compulsory education, duration (years)"
    ],
    # Gender equality 
    "Goal5":  ["Proportion of seats held by women in national parliaments (%)",
    "Ratio of female to male labor force participation rate (%) (modeled ILO estimate)",
    "Women who were first married by age 18 (% of women ages 20-24)",
    "Proportion of women subjected to physical and/or sexual violence in the last 12 months (% of women age 15-49)",
    "School enrollment, primary (% gross)"
    ],
    # Clean water
    "Goal6":  ["People using basic drinking water services (% of population)",
    "People using basic sanitation services (% of population)",
    "Annual freshwater withdrawals, total (% of internal resources)",
    "People practicing open defecation (% of population)",
    "Water pollution, food industry (% of total BOD emissions) [EE.BOD.FOOD.ZS]"
    ],
    # Clean Energy
    "Goal7":  ["Access to electricity (% of population)",
    "Renewable energy consumption (% of total final energy consumption)",
    "Energy intensity level of primary energy (MJ/$2011 PPP GDP)",
    "Carbon dioxide (CO2) emissions from Power Industry (Energy) (Mt CO2e)",
    "Access to clean fuels and technologies for cooking  (% of population)"
    ],
    # Decent Work and Economic Growth
    "Goal8":  ["GDP growth (annual %)",
    "Unemployment, total (% of total labor force) (modeled ILO estimate)",
    "GDP per person employed (constant 2011 PPP $)",
    "Children in employment, total (% of children ages 7-14)",
    "Labor force participation rate, total (% of total population ages 15-64) (modeled ILO estimate)"
    ],
    # Industry,Innovation and Infrastructure
    "Goal9":  ["Fixed broadband subscriptions (per 100 people)",
    "Research and development expenditure (% of GDP)",
    "Manufacturing, value added (% of GDP)",
    "Logistics performance index: Overall (1=low to 5=high)",
    "Patent applications, residents"
    ],
    # Requced Inequalities 
    "Goal10": ["GINI index (World Bank estimate)",
    "Income share held by lowest 20%",
    "Poverty gap at $1.90 a day (2011 PPP) (%)"
    ],
    # Sustainable cities
    "Goal11":["PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)",
    "People using safely managed drinking water services, urban (% of urban population)",
    "Disaster risk reduction progress score (1-5 scale; 5=best)"
    ],
    # Climate Action 
    "Goal13": ["Carbon dioxide (CO2) emissions (total) excluding LULUCF (Mt CO2e)",
    "Carbon dioxide (CO2) emissions excluding LULUCF per capita (t CO2e/capita)",
    "Adjusted savings: carbon dioxide damage (% of GNI)",
    "Carbon intensity of GDP (kg CO2e per constant 2015 US$ of GDP)",
    "Total greenhouse gas emissions (kt of CO2 equivalent) [EN.ATM.GHGT.KT.CE]"
    ],
    # Life on Land
    "Goal15":["Forest area (% of land area)",
    "Terrestrial and marine protected areas (% of total territorial area)",
    "Bird species, threatened",
    "Mammal species, threatened",
    "Adjusted savings: net forest depletion (% of GNI)"
    ],
    # peace, justice
    "Goal16":["Battle-related deaths (number of people)",
    "Intentional homicides (per 100,000 people)",
    "Statistical performance indicators (SPI): Overall score (scale 0-100)",
    "Rule of Law: Estimate",
    "Control of Corruption: Estimate"
    ],
    # paternships for goals 
    'Goal17':["Net official development assistance received (current US$)",
    "Tariff rate, applied, simple mean, all products (%)",
    "Foreign direct investment, net inflows (% of GDP)",
    "Personal remittances, received (% of GDP)",
    "Net official development assistance and official aid received (current US$) [DT.ODA.ALLD.CD]"
    ],
}
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

def normalise_columns(df, data):
    '''
    Creates a new updated dataframe where the values have been normalised, i.e put the values between 0 and 1 bases on means and standard deviations

    param df: copied dataframe, pandas dataframe
    param data: original dataframe, pandas dataframe
    '''
    # add list of metrics here only ones with numerical values, that can be normalised
    metrics=data.columns.values[3:]
    # create array of indexs showing if a metric is good to be low or high
    lower_values_good=[2,4,7,9,13,17,18,22,23,26,27,30,32,37,40,42,45,46,47,48,51,52,53,54,55,60,62,63,64,65,71,72]
    years=np.linspace(2002,2023,23)
    # loop through each metric
    for i,metric in enumerate(metrics):
        # get min and max values of metric
        min=np.nanmin(df[metric])
        max=np.nanmax(df[metric])
        # loop through each year calculating normalised value for each country for metric and updating the dataframe
        for year in years:
            year_values=(df[df['Year']==int(year)][metric])
            norm_score=(year_values-min)/(max-min)
            # if lower value is better change the normilisation score
            if i in lower_values_good:
                norm_score=1-norm_score
            # update dataframe with normalised value
            new_df=pd.DataFrame({metric:norm_score})
            df.update(new_df)

def add_composite_indexes_to_dataframe(df):
    '''
    loop through each goal and caluclate a mean for all of the metrics to get a composite index for each country for each year for that goal

    param df: dataframe
    '''
    goals=goal_metrics_labels.keys()
    for goal in goals:
        metrics_for_goal=goal_metrics_labels[goal]
        # creates a new mean which is the composite index of the two goals
        # decide how to combine metrics? For now just used standard mean. Could use median, have weight for specific goals
        # add column to dataframe for each composite index
        df[f'Composite Index {goal}'] = df[metrics_for_goal].mean(axis=1)
    # then take the mean of all the goal composite indexes to get an overall composite index for each country each year
    goals_columns=[f'Composite Index {goal}' for goal in goals]
    df['Sustainable Composite Index']=df[goals_columns].mean(axis=1)

def plot_composite_index_for_list_countries(df,countries,composite_index):
    '''
    plot a composite index column for different countries over time

    param df: dataframe
    param countries: list of countries, list
    param composite_index: composite index column header, string
    '''
    for country in countries:
        # ignore countries that have a low composite index value in 2002 due to lack of data 
        countrydf=df[df['Country Name']==country]
        countrydf=countrydf[countrydf['Year']==2002]
        # only plot data between these years
        df_filtered = df[(df['Year'] >= 2005) & (df['Year'] <= 2021)]
        if list(countrydf[composite_index])[0]>0.3:
            sns.lineplot(country_metric(country,composite_index,df_filtered), x='Year',y=composite_index, label=country)
            plt.ylim(0.3,0.75)
            plt.title('Sustainable Composite Index over time')
            plt.legend(loc='upper left')
            plt.xlim(2005,2022)
    plt.show()

def get_countries_with_biggest_changes(df):
    '''
    gets countries with the biggest positive and negatives changes in the overall composite index between 2005 and 2022

    param df: dataframe
    '''
    # get countries with biggest change between 2005 and 2021, this because there is less data near the edges so values aren't as accurate
    df_start=df[df['Year']==2005]
    df_end=df[df['Year']==2021]
    # change in composite index between 2005 and 2021
    change=df_end['Sustainable Composite Index'].to_numpy()-df_start['Sustainable Composite Index'].to_numpy()
    # get 10 smallest and 10 biggest changes
    max_indexes=np.argsort(change)[-10:]
    min_indexes=np.argsort(change)[:10]
    # find these countries and plot the composite index over time
    countries=np.array(list(dict.fromkeys(df['Country Name'].to_numpy())))
    biggest_pos_change_countries=countries[max_indexes]
    biggest_neg_change_countries=countries[min_indexes]
    return (biggest_pos_change_countries,biggest_neg_change_countries)
def plot_goals_for_country(df,country,goals):
    '''
    plot specific composite indexes of goals for a country over time

    param df: dataframe
    param country: name of country, string
    param goals, list of goals, list
    '''
    # only plot data between these years
    df_filtered = df[(df['Year'] >= 2005) & (df['Year'] <= 2021)]
    # loop through plot each composite index of goal
    for goal in goals:
        plot_country_metric(country, f'Composite Index {goal}',df_filtered, goal_labels)
    plt.ylabel('Composite Index')
    plt.title(f'Goals for {country} over time')
    plt.legend(loc='upper left')
    plt.xlim(2005,2022)
    plt.show()
# read data set
data=pd.read_csv('new_WorldSustainabilityDataset.csv')
# copy dataframe to keep imported dataframe
df=data.copy()
normalise_columns(df,data)
add_composite_indexes_to_dataframe(df)
big_pos_change,big_neg_change=get_countries_with_biggest_changes(df)
plot_composite_index_for_list_countries(df, big_pos_change, 'Sustainable Composite Index')
plot_composite_index_for_list_countries(df, big_neg_change, 'Sustainable Composite Index')
goals=['Goal10','Goal11','Goal13','Goal15','Goal16','Goal17']
plot_goals_for_country(df,'Bolivia',goals)



def country_goal_data(country, goal, df):
    '''
    country : 'United Kingdom'
    goal    : 'Goal1', 'Goal7'
    '''
    metric = f'Composite Index {goal}'
    country_df = df[df['Country Name'] == country]
    return country_df[['Year', metric]]

def goal_metric_data(countries, goal, df):
    '''
    countries : list of country names
    goal    : 'Goal1', 'Goal7'
    '''
    metric = f'Composite Index {goal}'
    filtered_df = df[df['Country Name'].isin(countries)]
    return filtered_df[['Country Name', 'Year', metric]].sort_values(['Country Name', 'Year'])
'''
Added functions to call for dynamic time warping for me!
Can be called through importing
'''
