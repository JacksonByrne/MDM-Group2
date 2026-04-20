"""
dtw_country_comparison.py

Use Dynamic Time Warping (DTW) to compare sustainability goal score
trajectories across countries.

For each Sustainable Development Goal (SDG) composite index, this script:
1. Builds the time series of the composite index for every country.
2. Aligns pairs of countries on the years they have in common.
3. Computes the DTW distance between each pair of countries.
4. Stores the pairwise DTW distance matrix per goal.
5. Provides helpers for:
        - Finding the most similar / most dissimilar countries to a
        reference country for a given goal.
        - Plotting the aligned series for any pair of countries + goal.
        - Plotting the pairwise DTW distance matrix as a heatmap for a
        selected subset of countries.

This file is self-contained: it loads the dataset directly and reuses the
composite-index construction helpers from `composite_index.py`. It does not
import `processing_data` and does not modify any existing code.
"""

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reuse the composite-index construction helpers and the goal labels from
# composite_index.py. Importing this module also has side effects (it runs
# some plots when executed as a script), but its helper functions are safe
# to use once imported.
from composite_index import (
    goal_labels,
    normalise_columns,
    add_composite_indexes_to_dataframe,
)


# --------------------------------------------------------------------------- #
# Data loading
# --------------------------------------------------------------------------- #
def load_sustainability_df(csv_path='new_WorldSustainabilityDataset.csv'):
    """
    Load the world sustainability dataset and attach the composite indexes
    needed for DTW comparison. This mirrors what `composite_index.py` does at
    module load time, but without the plotting side effects.
    """
    data = pd.read_csv(csv_path)
    df = data.copy()
    normalise_columns(df, data)
    add_composite_indexes_to_dataframe(df)
    return df


# Build the dataframe once at import time so the helpers below can use it
# as a default.
_df = load_sustainability_df()


def country_goal_data(country, goal, df=_df):
    """
    Return a DataFrame with 'Year' and the composite index column for a
    single country and goal.
    """
    metric = f'Composite Index {goal}'
    country_df = df[df['Country Name'] == country]
    return country_df[['Year', metric]]


# --------------------------------------------------------------------------- #
# DTW core
# --------------------------------------------------------------------------- #
def _dtw_distance(s, t, dist_func=None):
    """
    Classic dynamic time warping distance between two 1D numpy arrays.
    """
    if dist_func is None:
        dist_func = lambda x, y: abs(x - y)

    n, m = len(s), len(t)
    if n == 0 or m == 0:
        return np.nan

    DTW = np.full((n + 1, m + 1), np.inf)
    DTW[0, 0] = 0.0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = dist_func(s[i - 1], t[j - 1])
            DTW[i, j] = cost + min(
                DTW[i - 1, j],      # insertion
                DTW[i, j - 1],      # deletion
                DTW[i - 1, j - 1],  # match
            )

    return DTW[n, m]


def _country_goal_series(country, goal, df=_df, drop_na=True):
    sub = country_goal_data(country, goal, df).sort_values('Year')
    if drop_na:
        sub = sub.dropna()
    years = sub['Year'].to_numpy()
    values = sub[f'Composite Index {goal}'].to_numpy(dtype=float)
    return years, values


def _aligned_series(country1, country2, goal, df=_df):
    years1, s1 = _country_goal_series(country1, goal, df)
    years2, s2 = _country_goal_series(country2, goal, df)

    common_years = np.intersect1d(years1, years2)
    s1_aligned = s1[np.isin(years1, common_years)]
    s2_aligned = s2[np.isin(years2, common_years)]

    return common_years, s1_aligned, s2_aligned


def dtw_between_countries(country1, country2, goal, df=_df):
    """
    DTW distance between the composite-index trajectories of two countries
    for a given goal, aligned on the years they have in common.

    Returns
    -------
    distance : float
        DTW distance (NaN if no overlap).
    years : np.ndarray
        Common years used for the comparison.
    s1, s2 : np.ndarray
        The aligned series for `country1` and `country2`.
    """
    years, s, t = _aligned_series(country1, country2, goal, df)
    distance = _dtw_distance(s, t)
    return distance, years, s, t


# --------------------------------------------------------------------------- #
# Pairwise matrices
# --------------------------------------------------------------------------- #
def _available_countries_for_goal(goal, df=_df, min_points=5):
    """
    Return the list of countries that have at least `min_points` non-NaN
    composite index observations for `goal`.
    """
    metric = f'Composite Index {goal}'
    counts = (
        df.dropna(subset=[metric])
        .groupby('Country Name')[metric]
        .count()
    )
    return counts[counts >= min_points].index.tolist()


def pairwise_dtw_matrix(countries, goal, df=_df):
    """
    Compute the pairwise DTW distance matrix between `countries` for a single
    SDG composite index `goal` (e.g. "Goal7").

    Returns
    -------
    pandas.DataFrame
        Symmetric DataFrame of DTW distances indexed/columned by country.
        NaN entries indicate pairs without enough overlapping data.
    """
    n = len(countries)
    dmat = np.full((n, n), np.nan, dtype=float)

    for i, j in itertools.combinations(range(n), 2):
        c1, c2 = countries[i], countries[j]
        try:
            dist, years, _, _ = dtw_between_countries(c1, c2, goal, df=df)
            if len(years) == 0 or not np.isfinite(dist):
                continue
            dmat[i, j] = dist
            dmat[j, i] = dist
        except Exception:
            # Leave as NaN if a pair can not be compared.
            continue

    np.fill_diagonal(dmat, 0.0)
    return pd.DataFrame(dmat, index=countries, columns=countries)


def dtw_matrix_all_goals(countries, goals=None, df=_df):
    """
    Compute pairwise DTW distance matrices for every goal in `goals` and
    return them in a dict keyed by goal.
    """
    if goals is None:
        goals = [g for g in goal_labels.keys() if g != "Index"]

    return {g: pairwise_dtw_matrix(countries, g, df=df) for g in goals}


# --------------------------------------------------------------------------- #
# Ranking helpers
# --------------------------------------------------------------------------- #
def most_similar_countries(reference_country, goal, df=_df, top_n=10,
                        candidates=None):
    """
    For a given reference country and goal, return the `top_n` countries whose
    composite index trajectory is most similar (smallest DTW distance).
    """
    if candidates is None:
        candidates = _available_countries_for_goal(goal, df=df)

    results = []
    for other in candidates:
        if other == reference_country:
            continue
        try:
            dist, years, _, _ = dtw_between_countries(reference_country, other,
                                                    goal)
            if len(years) == 0 or not np.isfinite(dist):
                continue
            results.append((other, dist, len(years)))
        except Exception:
            continue

    ranked = pd.DataFrame(results,
                        columns=['Country', 'DTW_distance', 'n_years'])
    ranked = ranked.sort_values('DTW_distance').reset_index(drop=True)
    return ranked.head(top_n)


def most_dissimilar_countries(reference_country, goal, df=_df, top_n=10,
                            candidates=None):
    """
    Same as `most_similar_countries` but returns the `top_n` countries whose
    trajectory is *most different* from the reference country.
    """
    if candidates is None:
        candidates = _available_countries_for_goal(goal, df=df)

    ranked = most_similar_countries(reference_country, goal, df=df,
                                    top_n=len(candidates),
                                    candidates=candidates)
    return ranked.sort_values('DTW_distance',
                            ascending=False).head(top_n).reset_index(drop=True)


# --------------------------------------------------------------------------- #
# Plotting
# --------------------------------------------------------------------------- #
def plot_aligned_series(country1, country2, goal, df=_df, ax=None):
    """
    Plot the aligned composite index series for two countries and annotate
    with the DTW distance.
    """
    dist, years, s1, s2 = dtw_between_countries(country1, country2, goal, df=df)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(years, s1, marker='o', label=country1)
    ax.plot(years, s2, marker='s', label=country2)
    ax.set_xlabel('Year')
    ax.set_ylabel(f'Composite Index {goal}')
    ax.set_title(
        f'{goal_labels.get(goal, goal)}: {country1} vs {country2}\n'
        f'DTW distance = {dist:.3f} over {len(years)} common years'
    )
    ax.legend()
    ax.grid(True, alpha=0.3)
    return dist, years, s1, s2


def plot_dtw_heatmap(countries, goal, df=_df, cmap='viridis_r',
                    annotate=False, ax=None):
    """
    Plot the pairwise DTW distance matrix as a heatmap for the given
    countries and goal.
    """
    dmat = pairwise_dtw_matrix(countries, goal, df=df)

    if ax is None:
        fig, ax = plt.subplots(figsize=(max(6, 0.6 * len(countries)),
                                        max(5, 0.55 * len(countries))))

    sns.heatmap(dmat, cmap=cmap, annot=annotate, fmt='.2f',
                square=True, ax=ax,
                cbar_kws={'label': 'DTW distance'})
    ax.set_title(f'Pairwise DTW distance - {goal_labels.get(goal, goal)}')
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    return dmat


# --------------------------------------------------------------------------- #
# Example / demonstration run
# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    # Small, geographically diverse sample of countries that have good coverage.
    sample_countries = [
        'United Kingdom', 'Ireland', 'Germany', 'France', 'Sweden',
        'United States', 'Canada', 'Brazil', 'Argentina',
        'China', 'India', 'Vietnam', 'Japan', 'Australia',
        'South Africa', 'Kenya', 'Nigeria',
    ]
    reference = 'United Kingdom'

    # 1) Rank the sample countries by similarity to the reference country
    #    for each goal.
    print(f"\nMost similar countries to {reference} per goal "
        f"(by DTW distance):\n")
    goals = [g for g in goal_labels.keys() if g != 'Index']
    for goal in goals:
        ranked = most_similar_countries(reference, goal,
                                        top_n=5,
                                        candidates=sample_countries)
        if ranked.empty:
            continue
        print(f"--- {goal} : {goal_labels[goal]} ---")
        print(ranked.to_string(index=False))
        print()

    # 2) Plot aligned series for an interesting pair on Goal 7
    #    (Affordable and Clean Energy).
    fig, ax = plt.subplots(figsize=(9, 4))
    plot_aligned_series('Vietnam', 'China', 'Goal7', ax=ax)
    plt.tight_layout()
    plt.show()

    # 3) Plot pairwise DTW heatmap across the sample on a few headline goals.
    for goal in ['Goal3', 'Goal7', 'Goal13']:
        fig, ax = plt.subplots(figsize=(9, 7))
        plot_dtw_heatmap(sample_countries, goal, ax=ax, annotate=True)
        plt.tight_layout()
        plt.show()
