import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

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
    "Goal17": "Partnerships for the Goals",
    "Index": "Sustainable Composite Index",
}
# normalise columns

# list of goals and the metrics used for them
goal_metrics_labels = {
    # No Poverty
    "Goal1":  ["Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)",
    "Poverty gap at $5.50 a day (2011 PPP) (% of population)",
    "Poverty headcount ratio at societal poverty line (% of population) [SI.POV.SOPO]",
    "Adequacy of social protection and labor programs (% of total welfare of beneficiary households)",
    "Poverty gap at $1.90 a day (2011 PPP) (%)"
    ],
    # Zero Hunger 
    "Goal2":  ["Prevalence of undernourishment (% of population)",
    "Prevalence of moderate or severe food insecurity in the population (%) [SN.ITK.MSFI.ZS]",
    "Prevalence of stunting, height for age (modeled estimate, % of children under 5) [SH.STA.STNT.ME.ZS]",
    "Crop production index (2004-2006 = 100) [AG.PRD.CROP.XD]",
    "Food production index (2004-2006 = 100)"
    ],
    # Good Health
    "Goal3":  ["Mortality rate, under-5 (per 1,000 live births)",
    "Life expectancy at birth, total (years)",
    "Lifetime risk of maternal death (%) [SH.MMR.RISK.ZS]",
    "Incidence of tuberculosis (per 100,000 people)",
    "Current health expenditure (% of GDP)"
    ],
    # Quality Education 
    "Goal4":  ["School enrollment, primary (gross), gender parity index (GPI) [SE.ENR.PRIM.FM.ZS]",
    "Progression to secondary school (%) [SE.SEC.PROG.ZS]",
    "Net intake rate in grade 1 (% of official school-age population) [SE.PRM.NINT.ZS]",
    "Government expenditure on education, total (% of GDP) [SE.XPD.TOTL.GD.ZS]",
    "Pupil-teacher ratio, primary [SE.PRM.ENRL.TC.ZS]"
    
    ],
    # Gender equality 
    "Goal5":  ["Proportion of seats held by women in national parliaments (%)",
    "Ratio of female to male labor force participation rate (%) (modeled ILO estimate)",
    "Women Business and the Law Index Score (scale 1-100) [SG.LAW.INDX]",
    "Unemployment, female (% of female labor force) (modeled ILO estimate) [SL.UEM.TOTL.FE.ZS]",
    "Employment to population ratio, 15+, female (%) (modeled ILO estimate) [SL.EMP.TOTL.SP.FE.ZS]"
    ],
    # Clean water
    "Goal6":  ["People using basic drinking water services (% of population)",
    "People using basic sanitation services (% of population)",
    "People using safely managed drinking water services (% of population) [SH.H2O.SMDW.ZS]",
    "People practicing open defecation (% of population)",
    "People with basic handwashing facilities including soap and water (% of populartion) [SH.STA.HYGN.ZS]"
    ],
    # Clean Energy
    "Goal7":  ["Access to electricity (% of population)",
    "Renewable energy consumption (% of total final energy consumption)",
    "Energy intensity level of primary energy (MJ/$2011 PPP GDP)",
    "Adjusted savings: energy depletion (% of GNI) [NY.ADJ.DNGY.GN.ZS]",
    "Carbon dioxide (CO2) emissions from Power Industry (Energy) (Mt CO2e)"
    ],
    # Decent Work and Economic Growth
    "Goal8":  ["GDP growth (annual %)",
    "Unemployment, total (% of total labor force) (modeled ILO estimate)",
    "GDP per person employed (constant 2011 PPP $)",
    "Vulnerable employment, total (% of total employment) [SL.EMP.VULN.ZS]",
    "Labor force participation rate, total (% of total population ages 15-64) (modeled ILO estimate)"
    ],
    # Industry,Innovation and Infrastructure
    "Goal9":  ["Fixed broadband subscriptions (per 100 people)",
    "High-technology exports (% of manufactured exports) [TX.VAL.TECH.MF.ZS]",
    "Manufacturing, value added (% of GDP)",
    "Logistics performance index: Overall (1=low to 5=high)",
    "Patent applications, residents"
    ],
    # Requced Inequalities 
    "Goal10": ["GINI index (World Bank estimate)",
    "Income share held by lowest 20%",
    "Income share held by highest 20% [SI.DST.05TH.20]",
    "Poverty gap at $1.90 a day (2011 PPP) (%)",
    "Proportion of people living below 50 percent of median income (%) [SI.DST.50MD]"
    ],
    # Sustainable cities
    "Goal11":["PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)",
    "People using safely managed drinking water services, urban (% of urban population)",
    "Urban population growth (annual %) [SP.URB.GROW]",
    "Population living in slums (% of urban population) [EN.POP.SLUM.UR.ZS]",
    "Mortality caused by road traffic injury (per 100,000 people) [SH.STA.TRAF.P5]"
    ],
    # Climate Action 
    "Goal13": ["Adjusted savings: net forest depletion (% of GNI) [NY.ADJ.DFOR.GN.ZS]",
    "Carbon dioxide (CO2) emissions excluding LULUCF per capita (t CO2e/capita)",
    "Adjusted savings: carbon dioxide damage (% of GNI)",
    "Carbon intensity of GDP (kg CO2e per constant 2015 US$ of GDP)",
    "Total greenhouse gas emissions excluding LULUCF per capita (t CO2e/capita) [EN.GHG.ALL.PC.CE.AR5]"
    ],
    # Life on Land
    "Goal15":["Forest area (% of land area)",
    "Terrestrial and marine protected areas (% of total territorial area)",
    "Terrestrial protected areas (% of total land area) [ER.LND.PTLD.ZS]",
    "Mammal species, threatened",
    "Adjusted savings: net forest depletion (% of GNI) [NY.ADJ.DFOR.GN.ZS]"
    ],
    # peace, justice
    "Goal16":["Battle-related deaths (number of people)",
    "Intentional homicides (per 100,000 people)",
    "Statistical performance indicators (SPI): Overall score (scale 0-100)",
    "Rule of Law: Estimate",
    "Control of Corruption: Estimate"
    ],
    # paternships for goals 
    'Goal17':["Individuals using the Internet (% of population) [IT.NET.USER.ZS]",
    "Tariff rate, applied, simple mean, all products (%)",
    "Personal remittances, received (% of GDP)",
    "Tax revenue (% of GDP) [GC.TAX.TOTL.GD.ZS]",
    "Debt service (PPG and IMF only, % of exports of goods, services and primary income) [DT.TDS.DPPF.XP.ZS]"
    ],
}
metrics_lower_values_good=["Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)",
    "Poverty gap at $5.50 a day (2011 PPP) (% of population)",
    "Poverty headcount ratio at societal poverty line (% of population) [SI.POV.SOPO]",
    "Poverty gap at $1.90 a day (2011 PPP) (%)",
    "Prevalence of undernourishment (% of population)",
    "Prevalence of stunting, height for age (modeled estimate, % of children under 5) [SH.STA.STNT.ME.ZS]",
    "Prevalence of moderate or severe food insecurity in the population (%) [SN.ITK.MSFI.ZS]",
    "Mortality rate, under-5 (per 1,000 live births)",
    "Lifetime risk of maternal death (%) [SH.MMR.RISK.ZS]",
    "Incidence of tuberculosis (per 100,000 people)",
    "Pupil-teacher ratio, primary [SE.PRM.ENRL.TC.ZS]",
    "Unemployment, female (% of female labor force) (modeled ILO estimate) [SL.UEM.TOTL.FE.ZS]",
    "Adjusted savings: energy depletion (% of GNI) [NY.ADJ.DNGY.GN.ZS]",
    "People practicing open defecation (% of population)",
    "Energy intensity level of primary energy (MJ/$2011 PPP GDP)",
    "Carbon dioxide (CO2) emissions from Power Industry (Energy) (Mt CO2e)",
    "Unemployment, total (% of total labor force) (modeled ILO estimate)",
    "Vulnerable employment, total (% of total employment) [SL.EMP.VULN.ZS]",
    "Income share held by highest 20% [SI.DST.05TH.20]",
    "Proportion of people living below 50 percent of median income (%) [SI.DST.50MD]",
    "GINI index (World Bank estimate)",
    "Poverty gap at $1.90 a day (2011 PPP) (%)",
    "Population living in slums (% of urban population) [EN.POP.SLUM.UR.ZS]",
    "Mortality caused by road traffic injury (per 100,000 people) [SH.STA.TRAF.P5]",
    "Carbon dioxide (CO2) emissions (total) excluding LULUCF (Mt CO2e)",
    "Carbon dioxide (CO2) emissions excluding LULUCF per capita (t CO2e/capita)",
    "Adjusted savings: carbon dioxide damage (% of GNI)",
    "Carbon intensity of GDP (kg CO2e per constant 2015 US$ of GDP)",
    "Total greenhouse gas emissions excluding LULUCF per capita (t CO2e/capita) [EN.GHG.ALL.PC.CE.AR5]",
    "Terrestrial protected areas (% of total land area) [ER.LND.PTLD.ZS]",
    "PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)",
    "Mammal species, threatened",
    "Adjusted savings: net forest depletion (% of GNI) [NY.ADJ.DFOR.GN.ZS]",
    "Battle-related deaths (number of people)",
    "Intentional homicides (per 100,000 people)",
    "Tariff rate, applied, simple mean, all products (%)",
    "Debt service (PPG and IMF only, % of exports of goods, services and primary income) [DT.TDS.DPPF.XP.ZS]"
    ]
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
    years=range(2002,2024)
    # loop through each metric
    for metric in metrics:
        # loop through each year calculating normalised value for each country for metric and updating the dataframe
        for year in years:
            year_values=(df[df['Year']==int(year)][metric])
            # get min and max values of metric
            min_value=np.nanmin(year_values)
            max_value=np.nanmax(year_values)
            norm_score=(year_values-min_value)/(max_value-min_value)
            # if lower value is better change the normilisation score
            if metric in metrics_lower_values_good:
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
        # only plot data between these years
        df_filtered = df[(df['Year'] >= 2003) & (df['Year'] <= 2021)]
        sns.lineplot(country_metric(country,composite_index,df_filtered), x='Year',y=composite_index, label=country)
        #plt.ylim(0.25,0.75)
        plt.title('Sustainable Composite Index over time')
        plt.legend(loc='upper left')
        plt.xlim(2002,2022)
    plt.show()
def fit_linear_regmodel(years,composite_indexes):
    '''
    fit a linear regression model to x and y and returns first coefficient of model
    '''
    lr = LinearRegression()
    lr.fit(years,composite_indexes)
    return lr.coef_[0],lr.intercept_
def add_slope_of_composite_index(df, df_composite_index, composite_index):
    '''
    gets countries with the biggest positive and negatives changes in the overall composite index between 2005 and 2022

    param df: dataframe
    param df_composite_index: new dataframe
    param composite index: goal or overall composite index
    '''
    # get countries with biggest change between 2005 and 2021, this because there is less data near the edges so values aren't as accurate
    list_countries=np.array(list(dict.fromkeys(df['Country Name'].to_numpy())))
    slopes=np.zeros(len(list_countries))
    for i,country in enumerate(list_countries):
        
        # for nan values remove data point form model
        df_filtered=df[df['Country Name']==country]
        
        # get only in specified years
        nans=np.isnan(df_filtered[composite_index][4:-1].to_numpy())==False
        # only find slope if there are values if not slope is nan, maybe add only if there if certain amount of data as well
        if len(np.arange(2005,2022)[nans].reshape(-1,1))>0:
            slopes[i],intercept=fit_linear_regmodel(np.arange(2005,2022)[nans].reshape(-1,1), df_filtered[composite_index][4:-1].to_numpy()[nans].ravel())
        else:
            slopes[i]=np.nan
    df_composite_index['Slope']=pd.Series(slopes)
    return df_composite_index
def add_composite_index_recent(df,df_composite_index, composite_index):
    '''
    calcualtes mean of the each countries composite index between 2017 and 2021 and store in a new dataframe

    param df: dataframe
    param df_composite_index: new dataframe
    param composite index: goal index or overall index string
    '''
    df_recent=df[df['Year'].between(2017,2022)]
    recent_indexes=np.array(df_recent[composite_index]).reshape(193,6)
    recent_mean_index=recent_indexes.mean(axis=1)
    df_composite_index['Recent Mean Index']=pd.Series(recent_mean_index)
    return df_composite_index

def plot_slope_and_recent_index_for_list_countries(df,best_countries,composite_index):
    '''
    plot slope and recent mean composite index for all countriess

    param df: dataframe
    param country: name of country, string
    '''
    # plot once for all of the not best countries
    df_without_best=df.drop(df[df['Country'].isin(best_countries)].index)
    sns.scatterplot(df_without_best,x='Slope',y='Recent Mean Index', marker='x', color='0')
    # then plot the best countries with a legend to highlight them
    df_best=df[df['Country'].isin(best_countries)]
    sns.scatterplot(df_best,x='Slope',y='Recent Mean Index', hue=df_best['Country'])
    plt.title(f'{goal_labels[composite_index[-6:].replace(" ","")]} over time ')
    plt.ylabel('Recent Composite Index')
    plt.xlabel('Slope of composite index over time')
    plt.legend(loc='lower left')
    plt.show()
def find_best_countries(df):
    '''
    normalise slope column such that both values are on same scale 0-1, get average of slope and recent mean composite index then return the countries 
    with the best average

    param df: contains countries, slope and recent mean composite index, dataframe
    '''
    min_slope=np.nanmin(df['Slope'])
    max_slope=np.nanmax(df['Slope'])
    df['Slope Normalised']=(df['Slope']-min_slope)/(max_slope-min_slope)
    # favour a good recent mean composite index overall slighty, weight by 1.25
    mean_value=(df['Slope Normalised'].to_numpy()+df['Recent Mean Index'].to_numpy()*1.25)/2
    # ignore nan values and get highest values
    mean_value_without_nan=mean_value[np.isnan(mean_value)==False]
    max_indexes=np.where(np.isin(mean_value,mean_value_without_nan[np.argsort(mean_value_without_nan)[-10:]]))[0]
    countries=np.array(list(dict.fromkeys(df['Country'].to_numpy())))
    best_countries=countries[max_indexes]
    return best_countries

def find_best_countries_to_invest(df):
    '''
    calcualte slope of composite index over time and recent mean composite index, plot these metrics against each other and highlight the countries
    with the best average of the two metrics
    
    param df: contains countries, slope and recent mean composite index, dataframe
    '''
    # dataframe to store countries, recent mean composite index and slope of composite index, used to determine best countries
    df_composite_index=pd.DataFrame()
    df_composite_index['Country']=np.array(list(dict.fromkeys(df['Country Name'].to_numpy())))
    df_composite_index=add_slope_of_composite_index(df, df_composite_index, composite_index='Sustainable Composite Index')
    df_composite_index=add_composite_index_recent(df, df_composite_index, composite_index='Sustainable Composite Index')
    best_countries=find_best_countries(df_composite_index)
    plot_slope_and_recent_index_for_list_countries(df_composite_index,best_countries,composite_index='Sustainable Composite Index')
    
    return df_composite_index

def plot_best_change_goals_for_country(df,country,goals):
    '''
    plot the top 5 composite index goals with the biggest positive change over time

    param df: dataframe
    param country: name of country, string
    param goals, list of goals, list
    '''
    # only plot data between these years
    df_filtered = df[(df['Year']>2004) & (df['Year']<2022) & (df['Country Name']==country)]
    slope_goals=np.zeros(len(goals))
    # loop through each goal and fit a linear regression model and get the slope
    for i,goal in enumerate(goals):
        # if only nan values then change
        nans=np.isnan(df_filtered[f'Composite Index {goal}'].to_numpy())==False
        if len(np.arange(2005,2022)[nans].reshape(-1,1))>5:
            slope_goals[i],intercept=fit_linear_regmodel(np.arange(2005,2022)[nans].reshape(-1,1), df_filtered[f'Composite Index {goal}'].to_numpy()[nans].ravel())
        else:
            slope_goals[i]=np.nan
    # get top 5 goals
    # ignore nan values and get highest values
    slope_goals_without_nan=slope_goals[np.isnan(slope_goals)==False]
    max_indexes=np.where(np.isin(slope_goals,slope_goals_without_nan[np.argsort(slope_goals_without_nan)[-5:]]))[0]
    best_slope_goals=np.array(goals)[max_indexes]
    # loop through and plot the top 5 goals for change over time
    for goal in best_slope_goals:
        plot_country_metric(country, f'Composite Index {goal}',df[df['Country Name']==country], goal_labels)
    plt.ylabel('Recent Composite Index')
    plt.title(f'Goals for {country} over time')
    plt.legend(loc='upper left')
    plt.xlim(2001,2024)
    plt.show()
def plot_index_for_countries(df, composite_index):
    '''
    calcualte slope of a composite index over time and recent mean composite index, plot these metrics against each other and highlight the countries
    with the best average of the two metrics
    
    param df: contains countries, slope and recent mean composite index, dataframe
    param composite_index: goal or overall index
    '''
    # dataframe to store countries, recent mean composite index and slope of composite index, used to determine best countries
    df_composite_index=pd.DataFrame()
    df_composite_index['Country']=np.array(list(dict.fromkeys(df['Country Name'].to_numpy())))
    df_composite_index=add_slope_of_composite_index(df, df_composite_index, composite_index)
    df_composite_index=add_composite_index_recent(df, df_composite_index, composite_index)
    best_countries=find_best_countries(df_composite_index)
    plot_slope_and_recent_index_for_list_countries(df_composite_index,best_countries,composite_index)
    plt.show()
# read data set
data=pd.read_csv('new_WorldSustainabilityDataset.csv')
# copy dataframe to keep imported dataframe
df=data.copy()
normalise_columns(df,data)
add_composite_indexes_to_dataframe(df)
find_best_countries_to_invest(df)
goals=[f'Composite Index {goal}' for goal in goal_labels.keys()][:-1]
# display plots of countries for all goals
#for goal in goals:
    #plot_index_for_countries(df, composite_index=goal)

plot_best_change_goals_for_country(df,'China',list(goal_labels.keys())[:-1])



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
