import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import processing_data
from processing_data import df, country_goal_data

uk_goal1 = country_goal_data('United Kingdom', 'Goal1', df)
print(uk_goal1.head())