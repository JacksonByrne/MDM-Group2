import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import processing_data
from processing_data import df, country_goal_data, goal_metric_data

df=df
cleandf = df.dropna(subset=['Composite Index Goal1'])
countries = [
    'Aruba',
    'Angola',
    'Albania',
    'United Arab Emirates',
    'Argentina',
    'Armenia',
    'Antigua and Barbuda',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Burundi',
    'Belgium',
    'Benin',
    'Burkina Faso',
    'Bangladesh',
    'Bulgaria',
    'Bahrain',
    'Bahamas, The',
    'Bosnia and Herzegovina',
    'Belarus',
    'Belize',
    'Bolivia',
    'Brazil',
    'Barbados',
    'Brunei Darussalam',
    'Bhutan',
    'Botswana',
    'Central African Republic',
    'Canada',
    'Switzerland',
    'Chile',
    'China',
    "Cote d'Ivoire",
    'Cameroon',
    'Congo, Dem. Rep.',
    'Congo, Rep.',
    'Colombia',
    'Comoros',
    'Cabo Verde',
    'Costa Rica',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Germany',
    'Dominica',
    'Denmark',
    'Dominican Republic',
    'Algeria',
    'Ecuador',
    'Egypt, Arab Rep.',
    'Eritrea',
    'Spain',
    'Estonia',
    'Ethiopia',
    'Finland',
    'Fiji',
    'France',
    'Gabon',
    'United Kingdom',
    'Georgia',
    'Ghana',
    'Gambia, The',
    'Guinea-Bissau',
    'Equatorial Guinea',
    'Greece',
    'Guatemala',
    'Guyana',
    'Hong Kong SAR, China',
    'Honduras',
    'Croatia',
    'Haiti',
    'Hungary',
    'Indonesia',
    'India',
    'Ireland',
    'Iran, Islamic Rep.',
    'Iraq',
    'Iceland',
    'Israel',
    'Italy',
    'Jamaica',
    'Jordan',
    'Japan',
    'Kazakhstan',
    'Kenya',
    'Kyrgyz Republic',
    'Cambodia',
    'Korea, Rep.',
    'Kuwait',
    'Lao PDR',
    'Lebanon',
    'Liberia',
    'St. Lucia',
    'Sri Lanka',
    'Lesotho',
    'Lithuania',
    'Luxembourg',
    'Latvia',
    'Macao SAR, China',
    'Morocco',
    'Moldova',
    'Madagascar',
    'Maldives',
    'Mexico',
    'North Macedonia',
    'Mali',
    'Malta',
    'Myanmar',
    'Montenegro',
    'Mongolia',
    'Mozambique',
    'Mauritania',
    'Mauritius',
    'Malawi',
    'Malaysia',
    'Namibia',
    'Niger',
    'Nigeria',
    'Nicaragua',
    'Netherlands',
    'Norway',
    'Nepal',
    'New Zealand',
    'Oman',
    'Pakistan',
    'Panama',
    'Peru',
    'Philippines',
    'Poland',
    "Korea, Dem. People's Rep.",
    'Portugal',
    'Paraguay',
    'West Bank and Gaza',
    'Qatar',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saudi Arabia',
    'Senegal',
    'Singapore',
    'Solomon Islands',
    'Sierra Leone',
    'El Salvador',
    'Serbia',
    'Suriname',
    'Slovak Republic',
    'Slovenia',
    'Sweden',
    'Eswatini',
    'Seychelles',
    'Syrian Arab Republic',
    'Chad',
    'Togo',
    'Thailand',
    'Tajikistan',
    'Timor-Leste',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Tanzania',
    'Uganda',
    'Ukraine',
    'Uruguay',
    'United States',
    'Uzbekistan',
    'St. Vincent and the Grenadines',
    'Venezuela, RB',
    'Vietnam',
    'Vanuatu',
    'South Africa',
    'Zambia',
    'Zimbabwe',
]

def dtw_between_countries(country1, country2, goal):
    def dtw_distance(s, t, dist_func=None):
        """
        s, t: 1D numpy arrays
        dist_func: function(x, y) -> cost, default |x - y|
        """
        if dist_func is None:
            dist_func = lambda x, y: abs(x - y)

        n, m = len(s), len(t)
        DTW = np.full((n + 1, m + 1), np.inf)
        DTW[0, 0] = 0.0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost = dist_func(s[i - 1], t[j - 1])
                DTW[i, j] = cost + min(
                    DTW[i - 1, j],     # insertion
                    DTW[i, j - 1],     # deletion
                    DTW[i - 1, j - 1]  # match
                )

        return DTW[n, m]

    def country_goal_series(country, goal, df, drop_na=True):
        sub = country_goal_data(country, goal, df).sort_values('Year')
        if drop_na:
            sub = sub.dropna()
        years = sub['Year'].to_numpy()
        values = sub[f'Composite Index {goal}'].to_numpy(dtype=float)
        return years, values

    def aligned_goal_series_two_countries(country1, country2, goal, df):
        years1, s1 = country_goal_series(country1, goal, df)
        years2, s2 = country_goal_series(country2, goal, df)

        common_years = np.intersect1d(years1, years2)
        s1_aligned = s1[np.isin(years1, common_years)]
        s2_aligned = s2[np.isin(years2, common_years)]

        return common_years, s1_aligned, s2_aligned
    
    years, s, t = aligned_goal_series_two_countries(country1, country2, goal, df)
    distance = dtw_distance(s, t)
    return distance, years, s, t



dist, years, one_vals, two_vals = dtw_between_countries(
    "Argentina",
    "United States",
    "Goal5"
    )

print("DTW distance Goal5 (UK vs US):", dist)
print("Aligned years:", years)