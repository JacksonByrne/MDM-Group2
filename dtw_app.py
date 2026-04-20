"""
dtw_app.py

Interactive Streamlit app for exploring Dynamic Time Warping (DTW)
comparisons of Sustainable Development Goal (SDG) composite scores between
countries.

How to run from VS Code
-----------------------
1. Install dependencies once (in the terminal VS Code opens):
       pip install streamlit pandas numpy matplotlib seaborn scikit-learn

2. From the repo root, run:
       streamlit run dtw_app.py

   VS Code will show a clickable http://localhost:8501 link in the terminal.
   You can also use the "Run and Debug" panel with a Python config that
   executes `streamlit run dtw_app.py`.

The app lets you pick:
  - a base country
  - a comparison country
  - a goal (SDG composite index)

and shows the aligned trajectories plus the DTW distance. An optional
"DTW ranking" section lists the countries whose trajectory is most / least
similar to the base country for the chosen goal.

This file does not modify any existing code. It reuses helpers from
`dtw_country_comparison.py`.
"""

import streamlit as st
import matplotlib.pyplot as plt

from dtw_country_comparison import (
    _df as df,
    goal_labels,
    dtw_between_countries,
    plot_aligned_series,
    most_similar_countries,
    most_dissimilar_countries,
    _available_countries_for_goal,
)


# --------------------------------------------------------------------------- #
# Page setup
# --------------------------------------------------------------------------- #
st.set_page_config(
    page_title="SDG DTW Country Comparison",
    layout="wide",
)

st.title("SDG trajectories — Dynamic Time Warping comparison")
st.caption(
    "Compare how two countries' Sustainable Development Goal composite "
    "scores evolved over time, using DTW distance on the years they share."
)


# --------------------------------------------------------------------------- #
# Build selection options
# --------------------------------------------------------------------------- #
all_countries = sorted(df['Country Name'].dropna().unique().tolist())
goal_keys = [g for g in goal_labels.keys() if g != 'Index']

# Pretty "Goal1 — No Poverty" display for the goal dropdown.
goal_display = {g: f"{g} — {goal_labels[g]}" for g in goal_keys}


# --------------------------------------------------------------------------- #
# Sidebar controls
# --------------------------------------------------------------------------- #
with st.sidebar:
    st.header("Selection")

    default_base = 'United Kingdom' if 'United Kingdom' in all_countries else all_countries[0]
    default_comp = 'Ireland' if 'Ireland' in all_countries else all_countries[1]

    base_country = st.selectbox(
        "Base country",
        options=all_countries,
        index=all_countries.index(default_base),
    )

    comp_country = st.selectbox(
        "Comparison country",
        options=all_countries,
        index=all_countries.index(default_comp),
    )

    goal = st.selectbox(
        "SDG goal",
        options=goal_keys,
        index=goal_keys.index('Goal7') if 'Goal7' in goal_keys else 0,
        format_func=lambda g: goal_display[g],
    )

    st.divider()
    st.header("Ranking (optional)")
    show_ranking = st.checkbox("Show DTW ranking vs base country", value=True)
    top_n = st.slider("Top N", min_value=3, max_value=25, value=10)
    restrict_to_available = st.checkbox(
        "Restrict candidates to countries with enough data for this goal",
        value=True,
    )


# --------------------------------------------------------------------------- #
# Main comparison
# --------------------------------------------------------------------------- #
if base_country == comp_country:
    st.warning("Base country and comparison country are the same — pick "
               "different countries to get a meaningful DTW distance.")
else:
    try:
        dist, years, s1, s2 = dtw_between_countries(base_country, comp_country,
                                                    goal, df=df)
    except Exception as e:
        st.error(f"Could not compute DTW: {e}")
        st.stop()

    if len(years) == 0:
        st.error(
            f"No overlapping years of data between **{base_country}** and "
            f"**{comp_country}** for **{goal_display[goal]}**. "
            "Try a different pair or goal."
        )
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("DTW distance", f"{dist:.3f}")
        col2.metric("Common years", f"{len(years)}")
        col3.metric("Year range", f"{int(years.min())}–{int(years.max())}")

        st.subheader(f"Aligned trajectories — {goal_display[goal]}")

        fig, ax = plt.subplots(figsize=(9, 4))
        plot_aligned_series(base_country, comp_country, goal, df=df, ax=ax)
        st.pyplot(fig, clear_figure=True)

        with st.expander("Show underlying data"):
            import pandas as pd
            table = pd.DataFrame({
                'Year': years,
                base_country: s1,
                comp_country: s2,
                'abs difference': abs(s1 - s2),
            })
            st.dataframe(table, use_container_width=True)


# --------------------------------------------------------------------------- #
# Ranking section
# --------------------------------------------------------------------------- #
if show_ranking:
    st.divider()
    st.subheader(
        f"Countries ranked vs {base_country} — {goal_display[goal]}"
    )

    if restrict_to_available:
        candidates = _available_countries_for_goal(goal, df=df)
    else:
        candidates = all_countries

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**Most similar (smallest DTW distance)**")
        similar = most_similar_countries(base_country, goal, df=df,
                                         top_n=top_n, candidates=candidates)
        st.dataframe(similar, use_container_width=True, hide_index=True)

    with col_b:
        st.markdown("**Most different (largest DTW distance)**")
        different = most_dissimilar_countries(base_country, goal, df=df,
                                              top_n=top_n,
                                              candidates=candidates)
        st.dataframe(different, use_container_width=True, hide_index=True)


# --------------------------------------------------------------------------- #
# Footer
# --------------------------------------------------------------------------- #
st.caption(
    "Data: new_WorldSustainabilityDataset.csv · Composite indexes built via "
    "`composite_index.py` · DTW computed in `dtw_country_comparison.py`."
)
