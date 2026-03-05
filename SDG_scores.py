import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/WorldSustainabilityDataset.csv")
def clip01(x):
    return x.clip(lower=0, upper=1)
def score_higher_better(x, L, U):
    return clip01((x - L) / (U - L))
def score_lower_better(x, L, U):
    return clip01((U - x) / (U - L))


rename_map = {
    # Goal 10
    "Gini index (World Bank estimate) - SI.POV.GINI": "SI.POV.GINI",
    "Adjusted net national income per capita (annual % growth) - NY.ADJ.NNTY.PC.KD.ZG":
        "NY.ADJ.NNTY.PC.KD.ZG",

    # Goal 3
    "Life expectancy at birth, total (years) - SP.DYN.LE00.IN": "SP.DYN.LE00.IN",

    # Goal 13
    "Adjusted net savings, excluding particulate emission damage (% of GNI) - NY.ADJ.SVNX.GN.ZS":
        "NY.ADJ.SVNX.GN.ZS",
    "Adjusted savings: carbon dioxide damage (% of GNI) - NY.ADJ.DCO2.GN.ZS":
        "NY.ADJ.DCO2.GN.ZS",
    "Adjusted savings: natural resources depletion (% of GNI) - NY.ADJ.DRES.GN.ZS":
        "NY.ADJ.DRES.GN.ZS",
    "Adjusted savings: net forest depletion (% of GNI) - NY.ADJ.DFOR.GN.ZS":
        "NY.ADJ.DFOR.GN.ZS",
    "Adjusted savings: particulate emission damage (% of GNI) - NY.ADJ.DPEM.GN.ZS":
        "NY.ADJ.DPEM.GN.ZS",

    # Goal 4
    "Children out of school (% of primary school age) - SE.PRM.UNER.ZS": "SE.PRM.UNER.ZS",
    "Compulsory education, duration (years) - SE.COM.DURS": "SE.COM.DURS",
    "Primary completion rate, total (% of relevant age group) - SE.PRM.CMPT.ZS": "SE.PRM.CMPT.ZS",
    "School enrollment, preprimary (% gross) - SE.PRE.ENRR": "SE.PRE.ENRR",
    "School enrollment, primary (% gross) - SE.PRM.ENRR": "SE.PRM.ENRR",
    "School enrollment, secondary (% gross) - SE.SEC.ENRR": "SE.SEC.ENRR",
    "Pupil-teacher ratio, primary - SE.PRM.ENRL.TC.ZS": "SE.PRM.ENRL.TC.ZS",

    # Goal 5
    "Proportion of seats held by women in national parliaments (%) - SG.GEN.PARL.ZS":
        "SG.GEN.PARL.ZS",
    "Women Business and the Law Index Score (scale 1-100) - SG.LAW.INDX": "SG.LAW.INDX",

    # Goal 7
    "Renewable electricity output (% of total electricity output) - EG.ELC.RNEW.ZS":
        "EG.ELC.RNEW.ZS",
    "Renewable energy consumption (% of total final energy consumption) - EG.FEC.RNEW.ZS":
        "EG.FEC.RNEW.ZS",

    # Goal 2
    "Prevalence of undernourishment (%) - SN_ITK_DEFC - 2.1.1":
        "SN_ITK_DEFC - 2.1.1",

    # Goal 1
    "Proportion of population using basic drinking water services (%) - SP_ACS_BSRVH2O - 1.4.1":
        "SP_ACS_BSRVH2O - 1.4.1",
    "Proportion of population below international poverty line (%) - SI_POV_DAY1 - 1.1.1":
        "SI_POV_DAY1 - 1.1.1",

    # Goal 8
    "Unemployment rate, male (%) - SL_TLF_UEM - 8.5.2": "SL_TLF_UEM_male",
    "Unemployment rate, women (%) - SL_TLF_UEM - 8.5.2": "SL_TLF_UEM_female",

    # Goal 9
    "Proportion of population covered by at least a 2G mobile network (%) - IT_MOB_2GNTWK - 9.c.1":
        "IT_MOB_2GNTWK - 9.c.1",
    "Proportion of population covered by at least a 3G mobile network (%) - IT_MOB_3GNTWK - 9.c.1":
        "IT_MOB_3GNTWK - 9.c.1",

    # Electricity access / ATMs / startup cost
    "Access to electricity (% of population) - EG.ELC.ACCS.ZS": "EG.ELC.ACCS.ZS",
    "Automated teller machines (ATMs) (per 100,000 adults) - FB.ATM.TOTL.P5": "FB.ATM.TOTL.P5",
    "Cost of business start-up procedures, female (% of GNI per capita) - IC.REG.COST.PC.FE.ZS":
        "IC.REG.COST.PC.FE.ZS",
    "Cost of business start-up procedures, male (% of GNI per capita) - IC.REG.COST.PC.MA.ZS":
        "IC.REG.COST.PC.MA.ZS",
}

df = df.rename(columns=rename_map)

# 4. Scoring function
def add_goal_scores(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Goal 10
    if {'SI.POV.GINI', 'NY.ADJ.NNTY.PC.KD.ZG'} <= set(out.columns):
        gini_score = score_lower_better(out['SI.POV.GINI'], L=20, U=60)
        inc_score = score_higher_better(out['NY.ADJ.NNTY.PC.KD.ZG'], L=-5, U=5)
        out['Goal10_score'] = pd.concat([gini_score, inc_score], axis=1).mean(axis=1)

    # Goal 3
    if 'SP.DYN.LE00.IN' in out.columns:
        out['Goal3_score'] = score_higher_better(out['SP.DYN.LE00.IN'], L=50, U=85)

    # Goal 13
    if 'NY.ADJ.SVNX.GN.ZS' in out.columns:
        out['Goal13_AdjSavings_score'] = score_higher_better(out['NY.ADJ.SVNX.GN.ZS'],
            L=-10, U=20)
    for c in ['NY.ADJ.DCO2.GN.ZS', 'NY.ADJ.DRES.GN.ZS',
            'NY.ADJ.DPEM.GN.ZS', 'NY.ADJ.DFOR.GN.ZS']:
        if c in out.columns:
            out[f'Goal13_{c}_score'] = score_lower_better(out[c], L=0, U=10)
    goal13_subs = [c for c in out.columns if c.startswith('Goal13_') and c.endswith('_score')]
    if goal13_subs:
        out['Goal13_score'] = out[goal13_subs].mean(axis=1)

    # Goal 4
    if 'SE.PRM.UNER.ZS' in out.columns:
        out['Goal4_OutOfSchool_score'] = score_lower_better(out['SE.PRM.UNER.ZS'], 0, 30)
    if 'SE.COM.DURS' in out.columns:
        out['Goal4_CompYears_score'] = score_higher_better(out['SE.COM.DURS'], 4, 12)
    if 'SE.PRM.CMPT.ZS' in out.columns:
        out['Goal4_PrimCompletion_score'] = score_higher_better(out['SE.PRM.CMPT.ZS'], 50, 100)
    for c in ['SE.PRE.ENRR', 'SE.PRM.ENRR', 'SE.SEC.ENRR']:
        if c in out.columns:
            out[f'Goal4_{c}_score'] = score_higher_better(out[c], 60, 110)
    if 'SE.PRM.ENRL.TC.ZS' in out.columns:
        out['Goal4_PTR_score'] = score_lower_better(out['SE.PRM.ENRL.TC.ZS'], 15, 40)
    goal4_subs = [c for c in out.columns if c.startswith('Goal4_') and c.endswith('_score')]
    if goal4_subs:
        out['Goal4_score'] = out[goal4_subs].mean(axis=1)

    # Goal 5
    if 'SG.GEN.PARL.ZS' in out.columns:
        out['Goal5_ParliamentWomen_score'] = score_higher_better(out['SG.GEN.PARL.ZS'], 0, 50)
    if 'SG.LAW.INDX' in out.columns:
        out['Goal5_WBL_score'] = clip01(out['SG.LAW.INDX'] / 100.0)
    goal5_subs = [c for c in out.columns if c.startswith('Goal5_') and c.endswith('_score')]
    if goal5_subs:
        out['Goal5_score'] = out[goal5_subs].mean(axis=1)

    # Goal 7
    if 'EG.FEC.RNEW.ZS' in out.columns:
        out['Goal7_RenFinal_score'] = score_higher_better(out['EG.FEC.RNEW.ZS'], 0, 80)
    if 'EG.ELC.RNEW.ZS' in out.columns:
        out['Goal7_RenElec_score'] = clip01(out['EG.ELC.RNEW.ZS'] / 100.0)
    goal7_subs = [c for c in out.columns if c.startswith('Goal7_') and c.endswith('_score')]
    if goal7_subs:
        out['Goal7_score'] = out[goal7_subs].mean(axis=1)

    # Goal 2
    if 'SN_ITK_DEFC - 2.1.1' in out.columns:
        out['Goal2_score'] = score_lower_better(out['SN_ITK_DEFC - 2.1.1'], 0, 30)

    # Goal 1
    if 'SP_ACS_BSRVH2O - 1.4.1' in out.columns:
        out['Goal1_Water_score'] = score_higher_better(out['SP_ACS_BSRVH2O - 1.4.1'], 50, 100)
    if 'SI_POV_DAY1 - 1.1.1' in out.columns:
        out['Goal1_Poverty_score'] = score_lower_better(out['SI_POV_DAY1 - 1.1.1'], 0, 40)
    goal1_subs = [c for c in out.columns if c.startswith('Goal1_') and c.endswith('_score')]
    if goal1_subs:
        out['Goal1_score'] = out[goal1_subs].mean(axis=1)

    # Goal 8
    if {'SL_TLF_UEM_male', 'SL_TLF_UEM_female'} <= set(out.columns):
        u_avg = (out['SL_TLF_UEM_male'] + out['SL_TLF_UEM_female']) / 2.0
        out['Goal8_score'] = score_lower_better(u_avg, 0, 20)

    # Goal 9
    if 'IT_MOB_2GNTWK - 9.c.1' in out.columns:
        out['Goal9_2G_score'] = clip01(out['IT_MOB_2GNTWK - 9.c.1'] / 100.0)
    if 'IT_MOB_3GNTWK - 9.c.1' in out.columns:
        out['Goal9_3G_score'] = clip01(out['IT_MOB_3GNTWK - 9.c.1'] / 100.0)
    goal9_subs = [c for c in out.columns if c.startswith('Goal9_') and c.endswith('_score')]
    if goal9_subs:
        out['Goal9_score'] = out[goal9_subs].mean(axis=1)

    return out
'''
Only added easily quantifiable goals (1, 2, 3, 4, 5, 7, 8, 9, 10) 
since they have more data and are more comparable across countries. 
Missing data for some goals from the spreadsheet, so have to find ourselves.
'''

df_scored = add_goal_scores(df)
goal_labels = {
    "Goal1":  "No Poverty",
    "Goal2":  "Zero Hunger",
    "Goal3":  "Good Health",
    "Goal4":  "Quality Education",
    "Goal5":  "Gender Equality",
    "Goal7":  "Clean Energy",
    "Goal8":  "Decent Work",
    "Goal9":  "Industry & Infra",
    "Goal10": "Reduced Inequalities",
    "Goal13": "Climate Action",
}


def plot_country_score_single(country, year):
    row = df_scored[
        (df_scored["Country Name"] == country) &
        (df_scored["Year"] == year)
    ].iloc[0]

    goal_cols = [
        "Goal1_score", "Goal2_score", "Goal3_score",
        "Goal4_score", "Goal5_score", "Goal7_score",
        "Goal8_score", "Goal9_score", "Goal10_score",
    ]

    labels = [goal_labels[c.replace("_score", "")] for c in goal_cols]
    values = row[goal_cols].values

    plt.figure()
    plt.bar(labels, values)
    plt.ylabel("Score (0–1)")
    plt.xlabel("SDG goal")
    plt.title(f"SDG scores for {country} ({year})")
    plt.ylim(0, 1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_country_scores_over_time(country, start, end, goal):
    mask = (
    (df_scored["Country Name"] == country) &
    (df_scored["Year"] >= start) &
    (df_scored["Year"] <= end)
    )

    sub = df_scored.loc[mask, ["Year", goal]].sort_values("Year")

    plt.figure()
    plt.plot(sub["Year"], sub[goal], marker="o")
    plt.xlabel("Year")
    goal_code = goal.replace("_score", "")          # e.g. "Goal5"
    goal_name = goal_labels.get(goal_code, goal_code)

    plt.ylabel(f"{goal_name} score (0–1)")
    plt.title(f"{goal_name} score over time: {country} ({start}–{end})")
    plt.ylim(0, 1)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_all_countries_2004_2015_lines(df, goal):
    """
    Plot Goal scores for all countries over 2004–2015 as lines.
    Countries with no Goal scores in this period are excluded.
    """
    df_scored = add_goal_scores(df)

    # Filter year range and keep only rows with the specified goal score
    d = df_scored[
        (df_scored["Year"] >= 2004) &
        (df_scored["Year"] <= 2015)
    ].dropna(subset=[goal])

    countries = d["Country Name"].unique()

    plt.figure(figsize=(10, 6))

    for c in countries:
        sub = d[d["Country Name"] == c].sort_values("Year")
        plt.plot(
            sub["Year"],
            sub[goal],
            marker="o",
            linewidth=1,
            alpha=0.5,
            label=c
        )

    plt.xlabel("Year")
    goal_code = goal.replace("_score", "")
    goal_name = goal_labels.get(goal_code, goal_code)

    plt.ylabel(f"{goal_name} score (0–1)")
    plt.title(f"{goal_name} scores by country (2004–2015)")
    plt.ylim(0, 1)
    plt.grid(True, alpha=0.3)

    # If too many countries, legend can be huge; optionally comment this out
    plt.legend(fontsize=6, ncol=2, bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.show()


def main():
    country = "United Arab Emirates"
    year = 2015
    start_year = 2000
    end_year = 2018
    goal = 'Goal3_score'
    (1, 2, 3, 4, 5, 7, 8, 9, 10, 13) 

    '''plot_country_score_single(country, year)'''
    plot_country_scores_over_time(country, start_year, end_year, goal)
    plot_all_countries_2004_2015_lines(df, goal)

main()