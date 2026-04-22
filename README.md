MDM2-Group17 World Sustainability Dataset
Description
This project analyses the world countries and finds the best investment opportunities to invest in 
based on their sustainability trajectories. All code is done in Python.
  
Files 
composite_index.py- creates a sustainable composite index by normalising metrics and weight mean, 
uses linear regression to estimate sustainability trajectory and rank countries 

factoranalysis final (2).ipynb- runs a full factor analysis by screening metrics, choosing appropriate number of factors, producing investment leaderboard ranking countries using weighted score of current position and trajectory using the chosen factors. 

dtw_country_comparison.py- The baseline code before developing the dtw_app, uses composite index data and the new_WorldSustainabilityDataset and performs dynamic time warping.

dtw_app.py- Uses streamlit and the code from country_comparison to create a local hosted web app where you can compare two countries across one or all goals, and download the images.

DTW_plus_clustering_final.ipynb- Interprets the data and uses DTW on every pair of countries based on the sustainibility metrics followed by a clustering method. Grouping countries of similarity together.

timewarping.py- Legacy code that used the original dataset, two countries a goal to produce a flat dtw distance averaged over all the years.


Datasets
new_WorldSustainabilityDataset.csv- dataset from World Bank Group for metrics for UN's sustainable
development goals, used for composite_index.py



archive/WorldSustainabilityDataset.csv — dataset from kaggle used in factor analysis 

Dependencies, libraries used 
numpy, sklearn, pandas, seaborn, matplotlib, streamlit, scipy, factor_analyzer
 
