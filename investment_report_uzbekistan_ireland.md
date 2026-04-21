# Investment Analysis: Uzbekistan and Ireland through the lens of SDG Composite Scores

**Authors:** MDM Group 2
**Method:** Dynamic Time Warping (DTW) against Singapore (the highest-scoring benchmark from our factor analysis) + triangulation with external macro, sector and SDG sources
**Data:** `new_WorldSustainabilityDataset.csv`, composite indexes built in `composite_index.py`, DTW computed in `dtw_country_comparison.py` and visualised in `dtw_app.py`.

---

## 1. Framework

Factor analysis identified **Singapore** as the country with the highest overall sustainability composite score and the most consistent upward trajectory over the last two decades. We therefore treat Singapore as the *target state* and measure how closely a candidate country's per-goal trajectory tracks it using DTW distance.

DTW distance has two useful readings:

- **Low DTW** → the candidate has already tracked Singapore closely. The trajectory is *de-risked* — the convergence pattern has been demonstrated, so a position there is a more conservative bet on continued alignment.
- **High DTW** → a large trajectory gap, which can be either (a) a genuine catch-up opportunity if the drivers look right, or (b) a structural weakness to avoid. We disambiguate using the recent level and the recent slope.

We then cross-reference each DTW signal against external sources (IMF, World Bank, EBRD, IDA Ireland, OECD, Central Bank of Ireland, Ireland's Climate Action Plan, Sustainable Development Report, PISA, etc.) to see whether the SDG-index signal is supported by on-the-ground dynamics.

---

## 2. Headline comparison

| Metric | Uzbekistan vs Singapore | Ireland vs Singapore |
|---|---|---|
| Avg DTW per year (across SDGs) | **0.197** | **0.049** |
| Most similar goal | Goal 2 Zero Hunger (0.026/yr) | Goal 13 Climate Action (0.009/yr) |
| Most divergent goal | Goal 16 Peace/Justice/Institutions (0.56/yr) | Goal 4 Quality Education (0.164/yr) |
| Recent level profile | Mid — 0.25–0.90 range | High — mostly 0.8–0.95, near Singapore |
| 2025 real GDP growth | **7.7%** ([IMF via Times of Central Asia](https://timesca.com/uzbekistans-economy-to-remain-strong-in-2026-imf-forecasts-6-8-growth/)) | **4.9% MDD / 10.7% headline GDP** ([Central Bank of Ireland](https://www.centralbank.ie/publication/quarterly-bulletins/quarterly-bulletin-q1-2026), [European Commission](https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages/ireland/economic-forecast-ireland_en)) |
| SDG Index rank (2025) | Mid-tier, improving | **31 / 167**, Score 78.59 ([Sarah S. summary of SDR 2025](https://www.linkedin.com/posts/sarah-s-308ab4101_sdg-sdgreport2025-sdgireland-activity-7343617824688402432-cbzr)) |

Ireland is, on average, ~4× closer to Singapore's trajectory than Uzbekistan — a pattern that matches their economic profiles: Ireland is a mature high-income EU peer, Uzbekistan is a frontier market mid-way through a reform-driven transformation.

---

## 3. Uzbekistan — frontier growth story

### 3.1 Macro backdrop

Uzbekistan's DTW story is credible precisely because its macro trajectory is accelerating rather than stalling:

- Real GDP grew **7.7% in 2025**, with the IMF forecasting **6.8% in 2026** and inflation projected to return to the 5% target by 2027 ([IMF via Times of Central Asia](https://timesca.com/uzbekistans-economy-to-remain-strong-in-2026-imf-forecasts-6-8-growth/), [Caspian Post](https://caspianpost.com/uzbekistan/why-imf-raised-uzbekistan-s-growth-forecast)).
- The [World Bank](https://www.linkedin.com/posts/farkhodjon-israilov-66b363151_uzbekistan-worldbank-economicgrowth-activity-7382948479586799616-gKEn) lifted its 2025 Uzbekistan growth forecast to 6.2%, flagging chemicals, IT and agriculture as priority expansion sectors.
- Unemployment fell to 4.8% in 2025, and the IMF's 2026 policy recommendations focus on privatising state-owned banks, strengthening financial oversight, and improving governance — signalling that the reform agenda that began in 2016 is still active.

### 3.2 Low-DTW goals (de-risked convergence plays)

| Goal | DTW/yr | UZ recent level | Recent change | External reading |
|---|---|---|---|---|
| Goal 2 — Zero Hunger | **0.026** | 0.80 | **+0.24** | Cotton-to-textile cluster reform, end of state procurement, ILO-verified end of systemic forced labour in cotton, mechanisation to 50%+ of harvest by 2025 ([World Bank feature](https://www.worldbank.org/en/news/feature/2025/05/27/weaving-a-new-future-in-uzbekistan-s-cotton-sector), [EconStor food-security study](https://www.econstor.eu/bitstream/10419/318075/1/Food-Security-in-Uzbekistan.pdf)) |
| Goal 15 — Life on Land | 0.086 | 0.42 | +0.00 | Limited policy momentum; low external signal |
| Goal 5 — Gender Equality | 0.088 | 0.56 | +0.05 | EBRD's Women in Business programme active in Uzbekistan; 60 advisory projects, 80k entrepreneurs reached ([EBRD](https://kun.uz/en/news/2025/01/17/ebrd-breaks-investment-records-in-uzbekistan-with-938-million-in-2024)) |
| Goal 7 — Affordable & Clean Energy | 0.098 | 0.81 | **+0.24** | Solar + wind generation more than **doubled in 2025** to 10.5 bn kWh; renewables share reached 30% in 2025 with government target of 54% by 2030 ([Renewables.az](https://renewables.az/en/news/uzbekistan-doubles-solar-and-wind-power-generation-in-2025), [Times of Central Asia](https://timesca.com/uzbekistans-green-energy-output-hits-9-billion-kwh-in-2025/), [Facebook/Oilprice news](https://www.facebook.com/oilpricenews/posts/uzbekistan-targets-26-renewables-by-2025-with-16-solarwind-projects-35-gw-presid/1039332358208427/)) |
| Goal 11 — Sustainable Cities | 0.116 | 0.76 | +0.02 | EBRD green cities, water efficiency and cleaner energy are central to the 2024–29 country strategy ([EBRD](https://www.ebrd.com/home/news-and-events/news/2024/ebrd-approves-new-country-strategy-for-uzbekistan.html)) |

**Zero Hunger (Goal 2)** is the standout conservative play. The DTW signal (+0.24 rise, recent level 0.80 vs Singapore's 0.83) is fully supported by external evidence: cotton-textile value-chain reform has lifted employment in the textile industry from ~188k to ~600k workers; Uzbekistan can now convert 100% of raw cotton into yarn domestically; mechanisation has cut forced-labour risk; and the ILO formally certified the sector as free of systemic forced labour in 2022 ([World Bank](https://www.worldbank.org/en/news/feature/2025/05/27/weaving-a-new-future-in-uzbekistan-s-cotton-sector)). Investable themes: agri-tech, food processing, cold-chain logistics, textile clusters.

**Affordable and Clean Energy (Goal 7)** is the second most attractive conservative bet and arguably the highest-conviction idea in the whole analysis. DTW/yr is 0.098 and the composite jumped +0.24. External data is unambiguously bullish: solar and wind generation rose from 434 m kWh in 2022 to 10.5 bn kWh in 2025 — a **24× increase in four years** ([QazaqGreen](https://qazaqgreen.com/en/news/central-asia/3273/)). The government declared 2025 the "year of the green economy" and has 3.5 GW of new solar/wind under construction ([Oilprice news summary](https://www.facebook.com/oilpricenews/posts/1039332358208427/)). Investable themes: utility-scale solar, wind, grid modernisation, battery storage.

### 3.3 High-DTW goals (higher-risk catch-up plays)

| Goal | DTW/yr | UZ recent level | Gap vs SG | Recent change | External reading |
|---|---|---|---|---|---|
| Goal 16 — Peace, Justice, Strong Institutions | **0.559** | 0.49 | −0.45 | +0.04 | Reform agenda active since 2016 (judicial reform, SNB curtailment, constitutional changes) but results are slow ([ISDP](https://www.isdp.eu/publication/political-reform-mirziyoyevs-uzbekistan/), [OSW](https://www.osw.waw.pl/en/publikacje/osw-commentary/2018-07-17/thaw-uzbekistan-reforms-president-mirziyoyev-0)); IMF flags governance as a key 2026 priority |
| Goal 9 — Industry, Innovation & Infrastructure | **0.434** | 0.26 | −0.34 | **+0.26** | EBRD's €938 m 2024 commitment was a **record** for Central Asia; EBRD has deployed €3.4 bn across 115 operations since 2018 ([Kun.uz](https://kun.uz/en/news/2025/01/17/ebrd-breaks-investment-records-in-uzbekistan-with-938-million-in-2024)); major infra financings include a US$238 m upgrade of the 4R156 road and Amu Darya bridge ([EBRD](https://www.ebrd.com/home/news-and-events/news/2024/ebrd-finances-upgrade-of-key-road-in-uzbekistan.html)) |
| Goal 4 — Quality Education | 0.245 | 0.49 | −0.05 | **−0.37** | PISA 2022 maths score = 364 (OECD avg 472); education overhaul announced in 2025 to move to a 12-year system and create a Unified State Exam ([Kun.uz](https://kun.uz/en/news/2024/02/06/2022-pisa-resuls-show-urgent-need-for-educational-reforms-in-uzbekistan-president-mirziyoyev), [NACES](https://naces.org/uzbekistan-just-overhauled-its-entire-education-system-heres-what-changed/), [AACRAO](https://www.aacrao.org/edge/emergent-news/uzbekistan-to-transition-to-12-year-school-system)) |
| Goal 8 — Decent Work & Economic Growth | 0.210 | 0.52 | −0.23 | +0.03 | Strong GDP growth (7.7% in 2025) + falling unemployment (4.8%) create runway, but wage/quality-of-job convergence still lags |
| Goal 13 — Climate Action | 0.199 | 0.82 | −0.10 | +0.18 | Renewables ramp is the main lever; government is targeting carbon neutrality and an expanding renewables share ([Times of Central Asia](https://timesca.com/uzbekistans-green-energy-output-hits-9-billion-kwh-in-2025/)) |

High-DTW ≠ bad. What matters is the *direction*:

- **Goal 9 — Industry, Innovation & Infrastructure** is the strongest high-risk/high-reward pick. Uzbekistan's recent level is 0.26 but the recent change is **+0.26** — i.e. the index has roughly doubled from a low base. External money agrees: EBRD's 2024 Uzbekistan commitment of €938 m was a record for Central Asia and focuses on infrastructure, digital transition and private-sector development ([EBRD news](https://www.ebrd.com/home/news-and-events/news/2024/ebrd-approves-new-country-strategy-for-uzbekistan.html)). Investable themes: transport infrastructure, logistics corridors (Trans-Caspian), digital connectivity, industrial clusters.
- **Goal 13** is also attractive — its high DTW is a *legacy* signal, and the +0.18 recent change is being driven by the same green-economy push that's powering Goal 7.
- **Goal 16** is the classic emerging-market governance risk. Reform direction is positive but slow; price this as an ongoing discount, not a near-term catalyst.
- **Goal 4 Quality Education** has a red-flag slope (−0.37). The 2025 reform programme (12-year schooling, unified exam, PISA-aligned curricula, target of top-30 PISA by 2030) is *ambitious* but too new to price in — wait for measurable reversal before leaning in ([Kun.uz](https://kun.uz/en/news/2024/02/06/2022-pisa-resuls-show-urgent-need-for-educational-reforms-in-uzbekistan-president-mirziyoyev), [NACES](https://naces.org/uzbekistan-just-overhauled-its-entire-education-system-heres-what-changed/)).

### 3.4 Uzbekistan recommendation

A **barbell**: *safe leg* in the low-DTW positive-slope goals (Zero Hunger agri/textile value-chain, Clean Energy renewables buildout), *growth leg* in Goal 9 (infrastructure, industrial capacity, logistics) where EBRD capital and macro momentum align with a steeply rising SDG trajectory. Avoid theses that rely on Goal 4 turning in the next 2–3 years, and apply a governance-risk discount for any position tied to Goal 16 outcomes.

---

## 4. Ireland — mature peer play

### 4.1 Macro backdrop

- Real GDP grew ~10.7% in 2025 (distorted by pharma front-loading) with **Modified Domestic Demand up 4.9%** — the cleaner signal — and the Central Bank forecasting ~2.8% MDD growth averaged 2026–28 ([Central Bank of Ireland](https://www.centralbank.ie/publication/quarterly-bulletins/quarterly-bulletin-q1-2026), [European Commission](https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages/ireland/economic-forecast-ireland_en)).
- **IDA Ireland secured a record 323 FDI investments in 2025** (+38% YoY), with €2.5 bn of R&D client expenditure and 15,300+ new jobs expected ([PwC](https://www.pwc.ie/publications/2026/fdi-investing-in-ireland-issue-65.pdf), [Kelmer Group](https://kelmer.com/invest-in-ireland-fdi-record-2025/)).
- Pharmaceuticals are now **54% of all goods exports** (€139 bn in 2025) ([IPHA/Goodbody](https://www.ipha.ie/wp-content/uploads/2026/03/Pharma-in-Ireland-Goodbody-Report-for-IPHA-2026-1.pdf)).
- Ireland's 2025 SDG Index score is 78.59 (rank 31/167 globally), strong on SDG 1 (96.4) and SDG 3 (93.1), but weak on SDG 13 (50.9) due to agricultural emissions and low forest cover ([SDR 2025 summary](https://www.linkedin.com/posts/sarah-s-308ab4101_sdg-sdgreport2025-sdgireland-activity-7343617824688402432-cbzr)).

### 4.2 Near-identical trajectories (DTW/yr < 0.04)

| Goal | DTW/yr | IE recent level | External reading |
|---|---|---|---|
| Goal 13 — Climate Action | **0.009** | 0.94 | Signal is composite-level; reality is mixed — SDR 2025 puts Ireland's SDG 13 sub-score at only 50.9/100 because per-capita emissions remain high. CAP 2025 warns Ireland is **not on track** for its 51%-by-2030 target ([EY](https://www.ey.com/en_ie/insights/sustainability/irelands-climate-plan-2025-business-impacts), [Mason Hayes Curran](https://www.mhc.ie/latest/insights/review-of-climate-action-plan-2025)) |
| Goal 7 — Affordable & Clean Energy | 0.021 | 0.87 | Government targets **80% renewable electricity by 2030**, 5 GW offshore wind by 2030, 37 GW total offshore renewable capacity by 2050 ([EnergyIreland](https://www.energyireland.ie/post-2030-vision-for-offshore-renewable-energy/), [DETE](https://enterprise.gov.ie/en/what-we-do/the-business-environment/offshore-wind-energy/)); H1 2024 electricity-sector emissions fell 17% ([Mason Hayes Curran](https://www.mhc.ie/latest/insights/review-of-climate-action-plan-2025)) |
| Goal 3 — Good Health and Well-being | 0.027 | 0.91 | Top-tier (SDR 2025 sub-score 93.1); public health + biologics manufacturing are symbiotic |
| Goal 5 — Gender Equality | 0.029 | 0.73 | — |
| Goal 8 — Decent Work & Economic Growth | 0.032 | 0.77 | Unemployment 4.6–4.7% through 2027 ([EU forecast](https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages/ireland/economic-forecast-ireland_en)) |
| Goal 11 — Sustainable Cities | 0.034 | 0.80 | SDR 2025 and OECD both flag housing as the weak link — home prices rose 75% and rents 90% between 2012 and 2022 vs wages +27% ([OECD PCS](https://www.oecd.org/en/publications/oecd-policy-coherence-scan-of-ireland_23b0a0f4-en/full-report/in-focus-localising-the-sdgs-in-ireland_cd971c07.html)) |

These six goals are effectively "done" — Ireland tracks Singapore so tightly that a broad-based allocation is getting convergence that has already happened. The forward-looking signal is more nuanced because SDR 2025 shows the composite index masks genuine weaknesses (especially climate + housing).

### 4.3 The interesting gaps

| Goal | DTW/yr | IE level | SG level | What it tells us |
|---|---|---|---|---|
| Goal 9 — Industry, Innovation & Infrastructure | 0.056 | 0.59 | 0.59 | Same level, different paths — Ireland *converging upward* (+0.246 recent change) onto Singapore's plateau |
| Goal 6 — Clean water and sanitation | 0.075 | 0.94 | 1.00 | Small gap; Ireland has grown (+0.062) while Singapore is capped at 1.0 |
| Goal 15 — Life on Land | 0.085 | 0.39 | 0.46 | Both low; 11.5% forest cover in Ireland is 2nd-lowest in EU ([SDR 2025](https://www.linkedin.com/posts/sarah-s-308ab4101_sdg-sdgreport2025-sdgireland-activity-7343617824688402432-cbzr)) |
| Goal 4 — Quality Education | **0.164** | 0.56 | 0.54 | Same level, very different shapes — Ireland's recent index fell −0.19 while Singapore's surged +0.28 |

**Goal 9** is the single most actionable overweight. Levels converge but Ireland's trajectory is steeper, underpinned by two structural tailwinds: (a) the 2025 **Silicon Island** semiconductor strategy aligned with the €3.3 bn European Chips Act ([DETE/Silicon Island PDF](https://enterprise.gov.ie/en/publications/publication-files/silicon-island-a-national-semiconductor-strategy.pdf)), and (b) record-breaking FDI with 323 projects in 2025, €2.5 bn R&D client expenditure and the R&D tax credit raised to 35% in Budget 2026 ([PwC](https://www.pwc.ie/publications/2026/fdi-investing-in-ireland-issue-65.pdf), [IPHA](https://www.ipha.ie/wp-content/uploads/2026/03/Pharma-in-Ireland-Goodbody-Report-for-IPHA-2026-1.pdf)). Sector picks: semiconductors, advanced biologics/GLP-1 manufacturing, med-tech (Galway), cybersecurity (Cork), data-centre infrastructure (Dublin, which already absorbs 48% of the city's electricity).

**Goal 7 + Goal 13** look aligned on the DTW surface but the external picture is less bullish: 2030 offshore wind targets **cannot be met by existing port infrastructure** and require €2–3 bn of investment in ports alone ([DCU policy brief](https://www.dcu.ie/engineeringandcomputing/news/2025/oct/2030-offshore-wind-energy-targets-cannot-be-met-existing-port)); CAP 2025 flags the country is off its 51% emissions-reduction trajectory ([EY](https://www.ey.com/en_ie/insights/sustainability/irelands-climate-plan-2025-business-impacts)). That is actually an investable bottleneck — port capacity, grid reinforcement, and long-duration storage are the exact areas where policy will push capital.

**Goal 4 Quality Education** is Ireland's largest DTW and the clearest warning. PISA 2022 showed Ireland's maths score fall from 499.6 (2018) to 491.6, with the Educational Research Centre flagging a need for ongoing monitoring of maths decline ([ERC](https://www.erc.ie/wp-content/uploads/2024/09/B23617-Education-in-a-Dynamic-World-Report-rev3.pdf), [NALA/PISA presentation](https://www.nala.ie/wp-content/uploads/2025/10/National-Skills-Conversation-Dr-Lorraine-Gilleece-PISA_Educational-Research-Centre.pdf), [TheGlobalEconomy](https://www.theglobaleconomy.com/Ireland/pisa_math_scores/)). Singapore's opposite trajectory suggests human-capital quality may diverge — relevant for long-horizon plays dependent on STEM pipeline (semiconductors, pharma R&D).

**Goal 11 Sustainable Cities** also deserves a caveat. Ireland's DTW is low (0.034) but the **housing crisis** is well-documented: demand hugely outpacing supply, apartments at only 14% of stock vs OECD average 40%, and constitutional-level policy debate about a right to housing ([OECD PCS](https://www.oecd.org/en/publications/oecd-policy-coherence-scan-of-ireland_23b0a0f4-en/full-report/in-focus-localising-the-sdgs-in-ireland_cd971c07.html), [IHREC](https://www.ihrec.ie/downloads/Ireland-and-the-Sustainable-Development-Goals.pdf)). The DTW signal is lagged; the forward-looking risk is real.

### 4.4 Ireland recommendation

Ireland is a **core / defensive SDG allocation** with two active tilts:

1. **Overweight Goal 9 themes** — semiconductors (Silicon Island + EU Chips Act), biologics/GLP-1 manufacturing, med-tech, data-centre infrastructure. This is where DTW says "still closing the gap upward" and external evidence says "capital and policy both aligned".
2. **Overweight the Goal 7/13 bottleneck infrastructure** — port capacity for offshore wind, grid reinforcement, long-duration storage. DTW undersells the opportunity because the CAP 2025 gap is the trigger for capital deployment.

Known risks to price in: (a) Goal 4 education divergence threatening long-term STEM pipeline, (b) Goal 11 housing supply constraints that could cap domestic demand growth, and (c) pharma-export concentration risk flagged repeatedly in the IPHA/Goodbody report.

---

## 5. Side-by-side recommendation

| Profile | Uzbekistan | Ireland |
|---|---|---|
| Best "likely-return" play (low DTW, positive slope, external support) | **Goal 2 Zero Hunger** (cotton-textile value chain); **Goal 7 Clean Energy** (solar + wind +24× in 4 yrs) | **Goal 13 Climate Action** / Goal 7 (CAP 2025, offshore wind) |
| Best "high-return" play (high DTW, strong slope, external momentum) | **Goal 9 Industry & Infrastructure** (EBRD record funding, +0.26 slope, low base) | **Goal 9** (Silicon Island + IDA record FDI — but peer convergence, not catch-up) |
| Main risk factor | Goal 16 governance (slow reform), Goal 4 education (decline, reform unproven) | Goal 4 education (PISA maths decline), Goal 11 housing, pharma concentration risk |
| Macro tailwind | IMF 6.8% 2026 GDP growth, accelerating reforms | 4.9% MDD growth 2025, record FDI, R&D tax credit 35% |
| Portfolio role | **Growth allocation** — barbell of agri/energy (safe) + infra/industry (growth) | **Core allocation** — broad peer to Singapore with active tilt to Goal 9 themes |

### Final read

DTW against Singapore gives us a repeatable, trajectory-aware ranking that surfaces non-obvious investment signals. **External data confirms or qualifies each signal**: Uzbekistan's low-DTW Goals 2 and 7 are backed by textile-cluster reform and a 24× renewables ramp; its high-DTW Goal 9 is validated by record EBRD funding and steep index acceleration. Ireland's DTW-near-zero profile on Goals 3, 5, 7, 8, 11, 13 reflects mature convergence, while the one meaningful high-DTW goal (Goal 4) is corroborated by the PISA 2022 maths decline — and the most attractive active opportunity is Goal 9 themes, where DTW, IDA Ireland FDI flows, and the EU Chips Act all point the same direction.

---

### Sources

- IMF / Times of Central Asia — [Uzbekistan's Economy to Remain Strong in 2026, IMF Forecasts 6.8% Growth](https://timesca.com/uzbekistans-economy-to-remain-strong-in-2026-imf-forecasts-6-8-growth/)
- Caspian Post — [Why IMF Raised Uzbekistan's Growth Forecast](https://caspianpost.com/uzbekistan/why-imf-raised-uzbekistan-s-growth-forecast)
- World Bank — [Weaving a New Future in Uzbekistan's Cotton Sector](https://www.worldbank.org/en/news/feature/2025/05/27/weaving-a-new-future-in-uzbekistan-s-cotton-sector)
- World Bank via LinkedIn — [Growth forecast 6.2% in 2025, chemicals/IT/agriculture expansion sectors](https://www.linkedin.com/posts/farkhodjon-israilov-66b363151_uzbekistan-worldbank-economicgrowth-activity-7382948479586799616-gKEn)
- EconStor — [Fostering Resilience for Food Security in Uzbekistan](https://www.econstor.eu/bitstream/10419/318075/1/Food-Security-in-Uzbekistan.pdf)
- Renewables.az — [Uzbekistan doubles solar and wind power generation in 2025](https://renewables.az/en/news/uzbekistan-doubles-solar-and-wind-power-generation-in-2025)
- QazaqGreen — [Uzbekistan doubles solar and wind](https://qazaqgreen.com/en/news/central-asia/3273/)
- Times of Central Asia — [Uzbekistan's Green Energy Output Hits 9 Billion kWh](https://timesca.com/uzbekistans-green-energy-output-hits-9-billion-kwh-in-2025/)
- EBRD — [EBRD breaks investment records in Uzbekistan with €938 m in 2024](https://kun.uz/en/news/2025/01/17/ebrd-breaks-investment-records-in-uzbekistan-with-938-million-in-2024)
- EBRD — [EBRD approves new country strategy for Uzbekistan 2024–29](https://www.ebrd.com/home/news-and-events/news/2024/ebrd-approves-new-country-strategy-for-uzbekistan.html)
- EBRD — [US$238 m road/bridge financing](https://www.ebrd.com/home/news-and-events/news/2024/ebrd-finances-upgrade-of-key-road-in-uzbekistan.html)
- Kun.uz — [2022 PISA results show urgent need for educational reforms in Uzbekistan](https://kun.uz/en/news/2024/02/06/2022-pisa-resuls-show-urgent-need-for-educational-reforms-in-uzbekistan-president-mirziyoyev)
- NACES — [Uzbekistan Just Overhauled Its Entire Education System](https://naces.org/uzbekistan-just-overhauled-its-entire-education-system-heres-what-changed/)
- AACRAO — [Uzbekistan to Transition to 12-Year School System](https://www.aacrao.org/edge/emergent-news/uzbekistan-to-transition-to-12-year-school-system)
- ISDP — [Political Reform in Mirziyoyev's Uzbekistan](https://www.isdp.eu/publication/political-reform-mirziyoyevs-uzbekistan/)
- OSW — [Thaw in Uzbekistan: Reforms by President Mirziyoyev](https://www.osw.waw.pl/en/publikacje/osw-commentary/2018-07-17/thaw-uzbekistan-reforms-president-mirziyoyev-0)
- Central Bank of Ireland — [Quarterly Bulletin Q1 2026](https://www.centralbank.ie/publication/quarterly-bulletins/quarterly-bulletin-q1-2026)
- European Commission — [Economic forecast for Ireland](https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages/ireland/economic-forecast-ireland_en)
- PwC Ireland — [FDI Investing in Ireland Issue 65](https://www.pwc.ie/publications/2026/fdi-investing-in-ireland-issue-65.pdf)
- Kelmer Group — [Ireland FDI Record 2025](https://kelmer.com/invest-in-ireland-fdi-record-2025/)
- IPHA / Goodbody — [The Pharmaceutical Sector in Ireland 2026](https://www.ipha.ie/wp-content/uploads/2026/03/Pharma-in-Ireland-Goodbody-Report-for-IPHA-2026-1.pdf)
- DETE — [Silicon Island: Ireland's National Semiconductor Strategy](https://enterprise.gov.ie/en/publications/publication-files/silicon-island-a-national-semiconductor-strategy.pdf)
- DETE — [Offshore Wind Energy strategy](https://enterprise.gov.ie/en/what-we-do/the-business-environment/offshore-wind-energy/)
- EnergyIreland — [Post-2030 vision for offshore renewable energy](https://www.energyireland.ie/post-2030-vision-for-offshore-renewable-energy/)
- DCU — [2030 offshore wind targets cannot be met by existing port infrastructure](https://www.dcu.ie/engineeringandcomputing/news/2025/oct/2030-offshore-wind-energy-targets-cannot-be-met-existing-port)
- EY Ireland — [Climate Action Plan 2025: What It Means for Business](https://www.ey.com/en_ie/insights/sustainability/irelands-climate-plan-2025-business-impacts)
- Mason Hayes Curran — [Review of Climate Action Plan 2025](https://www.mhc.ie/latest/insights/review-of-climate-action-plan-2025)
- OECD — [Localising the SDGs in Ireland: Policy Coherence Scan](https://www.oecd.org/en/publications/oecd-policy-coherence-scan-of-ireland_23b0a0f4-en/full-report/in-focus-localising-the-sdgs-in-ireland_cd971c07.html)
- OECD — [Ireland — Student performance (PISA 2022)](https://gpseducation.oecd.org/CountryProfile?primaryCountry=IRL&treshold=10&topic=PI)
- ERC — [Education in a Dynamic World: performance of students in Ireland in PISA 2022](https://www.erc.ie/wp-content/uploads/2024/09/B23617-Education-in-a-Dynamic-World-Report-rev3.pdf)
- NALA — [PISA Educational Research Centre presentation](https://www.nala.ie/wp-content/uploads/2025/10/National-Skills-Conversation-Dr-Lorraine-Gilleece-PISA_Educational-Research-Centre.pdf)
- IHREC — [Ireland and the Sustainable Development Goals](https://www.ihrec.ie/downloads/Ireland-and-the-Sustainable-Development-Goals.pdf)
- Sustainable Development Report 2025 summary — [Ireland's 2025 SDG Index](https://www.linkedin.com/posts/sarah-s-308ab4101_sdg-sdgreport2025-sdgireland-activity-7343617824688402432-cbzr)

*All DTW numbers in this report are reproducible: run `streamlit run dtw_app.py`, choose Singapore as base and Uzbekistan or Ireland as comparison. The "All goals" tab returns the full per-SDG DTW table used above.*
