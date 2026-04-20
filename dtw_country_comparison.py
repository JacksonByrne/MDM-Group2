"""
dtw_country_comparison.py

Use Dynamic Time Warping (DTW) to compare sustainability goal score trajectories
across countries.

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

This file only *reads* from the existing project (processing_data.df,
timewarping.dtw_between_countries, composite_index.goal_labels) and does not
modify any of the existing code.
"""

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reuse the cleaned, composite-indexed dataframe and the DTW helper that
# already exist in the repo. These modules are not modified here.
from processing_data import df as _df, country_goal_data
from timewarping import dtw_between_countries
from composite_index import goal_labels


# --------------------------------------------------------------------------- #
# Core DTW utilities
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

    Parameters
    ----------
    countries : list[str]
        Country names as they appear in the 'Country Name' column.
    goal : str
        Goal key like "Goal1", "Goal7", "Goal13" ...
    df : pandas.DataFrame
        Dataset containing the composite indexes (defaults to the project df).

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
            dist, years, _, _ = dtw_between_countries(c1, c2, goal)
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
    dist, years, s1, s2 = dtw_between_countries(country1, country2, goal)

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
