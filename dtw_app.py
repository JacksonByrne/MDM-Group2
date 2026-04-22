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

The app has two tabs:
- "Single goal"  : pick a base country, comparison country, and one SDG
                    goal; see aligned trajectories + DTW distance and an
                    optional ranking of other countries.
- "All goals"    : pick two countries and see their DTW similarity across
                    every SDG at once (bar chart, summary table, and small
                    multiples of every goal's trajectories).

This file does not modify any existing code. It reuses helpers from
`dtw_country_comparison.py`.
"""

import numpy as np
import pandas as pd
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
    dtw_all_goals_between,
    plot_dtw_all_goals_bar,
    plot_all_goals_trajectories,
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
goal_display = {g: f"{g} — {goal_labels[g]}" for g in goal_keys}


# --------------------------------------------------------------------------- #
# Sidebar: country pickers shared across tabs
# --------------------------------------------------------------------------- #
with st.sidebar:
    st.header("Countries")

    default_base = ('United Kingdom' if 'United Kingdom' in all_countries
                    else all_countries[0])
    default_comp = ('Ireland' if 'Ireland' in all_countries
                    else all_countries[1])

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

    st.caption("These selections apply to both tabs.")


# --------------------------------------------------------------------------- #
# Tabs
# --------------------------------------------------------------------------- #
tab_single, tab_all = st.tabs(["Single goal", "All goals"])


# =========================================================================== #
# Tab 1 — Single-goal comparison
# =========================================================================== #
with tab_single:
    st.subheader("Single-goal comparison")

    col_left, col_right = st.columns([1, 2])
    with col_left:
        goal = st.selectbox(
            "SDG goal",
            options=goal_keys,
            index=goal_keys.index('Goal7') if 'Goal7' in goal_keys else 0,
            format_func=lambda g: goal_display[g],
            key="single_goal",
        )

        st.markdown("**Ranking (optional)**")
        show_ranking = st.checkbox("Show DTW ranking vs base country",
                                value=True, key="single_show_rank")
        top_n = st.slider("Top N", min_value=3, max_value=25, value=10,
                        key="single_top_n")
        restrict_to_available = st.checkbox(
            "Restrict candidates to countries with enough data for this goal",
            value=True, key="single_restrict",
        )

    with col_right:
        if base_country == comp_country:
            st.warning("Base country and comparison country are the same — "
                    "pick different countries to get a meaningful DTW "
                    "distance.")
        else:
            try:
                dist, years, s1, s2 = dtw_between_countries(
                    base_country, comp_country, goal, df=df)
            except Exception as e:
                st.error(f"Could not compute DTW: {e}")
                st.stop()

            if len(years) == 0:
                st.error(
                    f"No overlapping years of data between **{base_country}** "
                    f"and **{comp_country}** for **{goal_display[goal]}**."
                )
            else:
                c1, c2, c3 = st.columns(3)
                c1.metric("DTW distance", f"{dist:.3f}")
                c2.metric("Common years", f"{len(years)}")
                c3.metric("Year range",
                        f"{int(years.min())}–{int(years.max())}")

                fig, ax = plt.subplots(figsize=(9, 4))
                plot_aligned_series(base_country, comp_country, goal,
                                    df=df, ax=ax)
                st.pyplot(fig, clear_figure=True)

                with st.expander("Show underlying data"):
                    table = pd.DataFrame({
                        'Year': years,
                        base_country: s1,
                        comp_country: s2,
                        'abs difference': abs(s1 - s2),
                    })
                    st.dataframe(table, use_container_width=True)

    if show_ranking:
        st.divider()
        st.markdown(
            f"### Countries ranked vs {base_country} — {goal_display[goal]}"
        )

        if restrict_to_available:
            candidates = _available_countries_for_goal(goal, df=df)
        else:
            candidates = all_countries

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Most similar (smallest DTW distance)**")
            similar = most_similar_countries(base_country, goal, df=df,
                                            top_n=top_n,
                                            candidates=candidates)
            st.dataframe(similar, use_container_width=True, hide_index=True)
        with col_b:
            st.markdown("**Most different (largest DTW distance)**")
            different = most_dissimilar_countries(base_country, goal, df=df,
                                                top_n=top_n,
                                                candidates=candidates)
            st.dataframe(different, use_container_width=True, hide_index=True)


# =========================================================================== #
# Tab 2 — All-goals comparison
# =========================================================================== #
with tab_all:
    st.subheader("All-goals comparison")
    st.caption(
        "Computes the DTW distance between the two selected countries for "
        "every SDG composite index and summarises the results in one view."
    )

    if base_country == comp_country:
        st.warning("Base country and comparison country are the same — pick "
                "different countries to compare.")
    else:
        metric_choice = st.radio(
            "Ranking metric",
            options=[
                ('DTW_per_yr', 'DTW per common year (recommended)'),
                ('DTW', 'Raw DTW distance'),
                ('mean_abs', 'Mean absolute difference'),
            ],
            format_func=lambda x: x[1],
            horizontal=True,
            key="all_metric",
        )
        metric_key = metric_choice[0]

        summary = dtw_all_goals_between(base_country, comp_country, df=df)
        summary_valid = summary.dropna(subset=[metric_key]).copy()

        if summary_valid.empty:
            st.error(
                f"No overlapping data for **{base_country}** and "
                f"**{comp_country}** on any goal."
            )
        else:
            # Headline metrics
            avg_per_yr = summary_valid['DTW_per_yr'].mean()
            best_row = summary_valid.sort_values(metric_key).iloc[0]
            worst_row = summary_valid.sort_values(metric_key).iloc[-1]

            c1, c2, c3 = st.columns(3)
            c1.metric(
                "Avg DTW per year (all goals)",
                f"{avg_per_yr:.3f}",
            )
            c2.metric(
                "Most similar goal",
                f"{best_row['Goal']}",
                delta=f"{best_row[metric_key]:.3f}",
                delta_color="off",
            )
            c3.metric(
                "Least similar goal",
                f"{worst_row['Goal']}",
                delta=f"{worst_row[metric_key]:.3f}",
                delta_color="off",
            )

            # Bar chart of all goals
            st.markdown(
                f"#### DTW across all SDGs — {base_country} vs {comp_country}"
            )
            fig, ax = plt.subplots(
                figsize=(9, max(4, 0.45 * len(summary_valid))))
            plot_dtw_all_goals_bar(base_country, comp_country, df=df,
                                metric=metric_key, ax=ax)
            st.pyplot(fig, clear_figure=True)

            # Summary table
            st.markdown("#### Summary table")
            display = summary.copy()
            # Round numeric columns for display.
            for col in ['DTW', 'mean_abs', 'DTW_per_yr']:
                display[col] = display[col].round(4)
            st.dataframe(
                display.sort_values(metric_key, na_position='last'),
                use_container_width=True,
                hide_index=True,
            )

            # Small multiples for every goal
            with st.expander("Show trajectory plots for every goal",
                            expanded=False):
                fig_all = plot_all_goals_trajectories(
                    base_country, comp_country, df=df, ncols=3)
                st.pyplot(fig_all, clear_figure=True)

            # CSV download
            csv = summary.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download summary as CSV",
                data=csv,
                file_name=(
                    f"dtw_all_goals_{base_country.replace(' ', '_')}"
                    f"_vs_{comp_country.replace(' ', '_')}.csv"
                ),
                mime='text/csv',
            )


# --------------------------------------------------------------------------- #
# Footer
# --------------------------------------------------------------------------- #
st.caption(
    "Data: new_WorldSustainabilityDataset.csv · Composite indexes built via "
    "`composite_index.py` · DTW computed in `dtw_country_comparison.py`."
)
