# Investment Analysis: Uzbekistan and Ireland through the lens of SDG Composite Scores

**Authors:** MDM Group 2
**Method:** Dynamic Time Warping (DTW) against Singapore (the highest-scoring benchmark from our factor analysis)
**Data:** `new_WorldSustainabilityDataset.csv`, composite indexes built in `composite_index.py`, DTW computed in `dtw_country_comparison.py` and visualised with `dtw_app.py`.

---

## 1. Framework

Our factor analysis identified **Singapore** as the country with the highest overall sustainability composite score and the most consistent upward trajectory over the last two decades. We therefore treat Singapore as the *target state* — the trajectory we would like a candidate investment country to replicate.

For each candidate country we compute the per-goal DTW distance to Singapore. The resulting distance has two useful readings:

- **Low DTW on a goal** → the candidate is already tracking Singapore closely on that SDG. The trajectory is *de-risked* — growth has been demonstrated, so a position there is a more conservative bet on continued convergence.
- **High DTW on a goal** → there is a large trajectory gap. That gap is either (a) a genuine catch-up opportunity if the underlying drivers look right, or (b) a structural weakness to avoid. These are the higher-risk / higher-return goals.

We apply this framework to two candidate countries with very different risk profiles: **Uzbekistan** (a frontier-market catch-up story) and **Ireland** (a mature-economy near-peer to Singapore).

---

## 2. Headline comparison

| Metric | Uzbekistan vs Singapore | Ireland vs Singapore |
|---|---|---|
| Avg DTW per year (across SDGs) | **0.197** | **0.049** |
| Most similar goal | Goal 2 Zero Hunger (0.026/yr) | Goal 13 Climate Action (0.009/yr) |
| Most divergent goal | Goal 16 Peace, Justice, Strong Institutions (0.56/yr) | Goal 4 Quality Education (0.164/yr) |
| Overall score level (recent) | Mid — mostly 0.5–0.8 | High — mostly 0.8–0.95, near Singapore |

Ireland is, on average, roughly **four times closer** to Singapore's trajectory than Uzbekistan is. That already tells us Ireland is the "safe" peer and Uzbekistan is the "growth" bet, and our per-goal analysis below shows the *where* and *why*.

---

## 3. Uzbekistan — frontier growth story

Uzbekistan's DTW profile vs Singapore is extremely bimodal — the goals split cleanly into "already converging" and "structurally divergent".

### 3.1 Low-DTW goals (de-risked convergence plays)

| Goal | DTW/yr | Uzbekistan recent level | Recent change |
|---|---|---|---|
| Goal 2 — Zero Hunger | **0.026** | 0.80 | **+0.24** |
| Goal 15 — Life on Land | 0.086 | 0.42 | +0.00 |
| Goal 5 — Gender Equality | 0.088 | 0.56 | +0.05 |
| Goal 7 — Affordable and Clean Energy | 0.098 | 0.81 | **+0.24** |
| Goal 11 — Sustainable Cities and Communities | 0.116 | 0.76 | +0.02 |

**Zero Hunger (Goal 2)** is the standout. Uzbekistan's recent five-year mean is 0.80 — essentially indistinguishable from Singapore's 0.83 — and it has grown by **+0.24** over the period measured. The DTW/yr of 0.026 confirms the two trajectories have tracked each other closely. This is the *most likely rate of return* play: agri-tech, food processing, and cold-chain logistics investments are underpinned by a trajectory that already demonstrably converges with a best-in-class benchmark.

**Affordable and Clean Energy (Goal 7)** is the second most attractive conservative bet. The composite jumped from ~0.55 in 2002 to 0.81 in recent years — a +0.24 swing — and the 2022 data point converges almost exactly onto Singapore's level (see the attached Singapore vs Uzbekistan Goal 7 chart). Uzbekistan's gas-to-renewables transition and grid modernisation are consistent with this signal.

### 3.2 High-DTW goals (higher-risk catch-up plays)

| Goal | DTW/yr | Uzbekistan recent level | Gap vs Singapore | Recent change |
|---|---|---|---|---|
| Goal 16 — Peace, Justice, Strong Institutions | **0.559** | 0.49 | −0.45 | +0.04 |
| Goal 9 — Industry, Innovation & Infrastructure | **0.434** | 0.26 | −0.34 | **+0.26** |
| Goal 4 — Quality Education | 0.245 | 0.49 | −0.05 | −0.37 |
| Goal 8 — Decent Work and Economic Growth | 0.210 | 0.52 | −0.23 | +0.03 |
| Goal 13 — Climate Action | 0.199 | 0.82 | −0.10 | +0.18 |

The high-DTW picks are more nuanced — DTW tells you *these trajectories differ*, not *which direction they differ in*. We separate them by looking at the level and recent trend:

- **Goal 9 — Industry, Innovation & Infrastructure** is the best high-risk/high-reward pick. Uzbekistan's level is low (0.26) but the recent change is **+0.26** — i.e. the series is more than doubling from a low base. This is exactly the profile we want for a catch-up trade: a big DTW gap *combined with* a steeply positive slope. Infrastructure, logistics, and industrial-capacity plays fit here.
- **Goal 13 — Climate Action** is similarly promising: a +0.18 recent change is bringing the score back into the 0.8+ range that Singapore has sat in for two decades.
- **Goal 16** has the biggest DTW gap but only a +0.04 recent change — institutional convergence is shallow. This is the classic emerging-market *governance risk* premium and should be priced in accordingly.
- **Goal 4 — Quality Education** has gone backwards recently (−0.37). We would avoid a thesis that relies on an education-quality turnaround until the trend reverses.

### 3.3 Uzbekistan recommendation

A barbell works well here. **Allocate the safe leg to the low-DTW goals with positive slopes** — Zero Hunger and Clean Energy — where Uzbekistan is already tracking Singapore. **Allocate the growth leg to Goal 9 (Industry, Innovation & Infrastructure)**, where the DTW gap is large but the recent trajectory is the steepest of any goal. Avoid theses that rely on Goal 4 or Goal 16 moving sharply in the near term.

---

## 4. Ireland — mature peer play

Ireland's profile is the opposite of Uzbekistan's: almost every goal is close to Singapore in both level and trajectory, so the conversation shifts from *catch-up* to *quality of peer alignment*.

### 4.1 Near-identical trajectories

| Goal | DTW/yr | Ireland recent level |
|---|---|---|
| Goal 13 — Climate Action | **0.009** | 0.94 |
| Goal 7 — Affordable and Clean Energy | 0.021 | 0.87 |
| Goal 3 — Good Health and Well-being | 0.027 | 0.91 |
| Goal 5 — Gender Equality | 0.029 | 0.73 |
| Goal 8 — Decent Work and Economic Growth | 0.032 | 0.77 |
| Goal 11 — Sustainable Cities | 0.034 | 0.80 |

Ireland's Climate Action trajectory is the most Singapore-like of any goal we tested — a DTW/yr of 0.009 is essentially noise. Goals 3, 5, 7, 8 and 11 are all under 0.035, meaning Ireland's delivery on health, clean energy, labour markets and urban sustainability has been effectively a carbon copy of Singapore's trajectory over the last 22 years. For a conservative investor these are yield plays — not high-growth bets, but convergence is already done.

### 4.2 The interesting gaps

| Goal | DTW/yr | Ireland level | Singapore level | What it tells us |
|---|---|---|---|---|
| Goal 9 — Industry, Innovation & Infrastructure | 0.056 | 0.59 | 0.59 | Same level, noisy paths (see chart) |
| Goal 6 — Clean water and sanitation | 0.075 | 0.94 | 1.00 | Small absolute gap, Ireland below ceiling |
| Goal 15 — Life on Land | 0.085 | 0.39 | 0.46 | Both low and drifting down |
| Goal 4 — Quality Education | **0.164** | 0.56 | 0.54 | Largest DTW but similar levels — trajectory shape differs |

**Goal 9 (Industry, Innovation & Infrastructure)** is interesting because Ireland and Singapore end the period at essentially the same level (~0.59) but the year-by-year paths differ enough to generate a 0.056 DTW/yr. The attached chart shows Ireland *converging upward onto* Singapore (+0.246 recent change) while Singapore oscillates around a plateau. Ireland's multinational-led innovation ecosystem is catching up and in 2022 actually exceeds Singapore. This is a credible growth-within-a-peer thesis — exposure to Irish industrial R&D is buying continued convergence to the Singapore frontier, not just matching it.

**Goal 4 (Quality Education)** is Ireland's largest DTW (0.164/yr) despite levels being almost identical (0.56 vs 0.54). The divergence is in *shape*: Ireland's index dipped −0.19 recently while Singapore jumped +0.28. For an investor this flags a potential relative-value trade — Singapore is executing education reforms that Ireland is not, and human-capital quality may diverge going forward.

### 4.3 Ireland recommendation

Ireland is a **defensive, diversified SDG allocation**: every goal either matches Singapore's trajectory closely or ends the window at a similar level. Overweight Ireland if the investment brief is capital preservation with broad ESG alignment. The one active position worth considering is an overweight on **Goal 9 themes** (industrial innovation, data-centre infrastructure, advanced manufacturing), where Ireland is still closing the gap upward. Be cautious about assuming parity on **Goal 4** — the education-trajectory divergence is the one meaningful warning in the data.

---

## 5. Side-by-side recommendation

| Profile | Uzbekistan | Ireland |
|---|---|---|
| Best "likely return" play (low DTW, positive slope) | **Goal 2 Zero Hunger**, Goal 7 Clean Energy | **Goal 13 Climate Action**, Goal 7 Clean Energy |
| Best "high return" play (high DTW, strong slope) | **Goal 9 Industry, Innovation & Infrastructure** (+0.26 recent change, low base) | Goal 9 — but as a near-peer convergence, not a catch-up |
| Main risk factor (high DTW, flat/falling slope) | Goal 16 Institutions, Goal 4 Education (declining) | Goal 4 Education (declining), Goal 15 Life on Land |
| Overall role in portfolio | **Growth allocation** — barbell of Zero Hunger (safe) and Industry/Infrastructure (growth) | **Core allocation** — broad SDG peer to Singapore with a tilt toward industrial innovation |

### Final read

Using Singapore as the benchmark and DTW as the trajectory-distance metric produces an actionable split: **Uzbekistan earns its place in a portfolio on the strength of Zero Hunger convergence and a steeply rising Industry/Innovation trajectory**, while **Ireland earns its place as a near-peer whose sustainability trajectory mirrors Singapore's on climate, energy, health and labour**. The DTW-per-year metric gives us a repeatable way to rank future candidates against the same benchmark.

---

*All numbers in this report are reproducible from the repository: run `streamlit run dtw_app.py` and select Singapore as the base country with Uzbekistan or Ireland as the comparison. The "All goals" tab returns the full per-SDG DTW table used above.*
