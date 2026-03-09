# Methodology — UK Wellbeing & Health Value Factors

**Pipeline author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Conceptual Foundation: Welfare Economics and Wellbeing Valuation

### 1.1 Theoretical basis

UK government value factors are grounded in **welfare economics** — the quantification
of societal welfare change using monetary equivalents derived from stated or revealed
preferences.

| Concept | UK Wellbeing approach | Classical damage-cost (EPS, CE Delft) |
|---|---|---|
| Basis | Stated preference (WTP) + QALY/WELLBY | Damage cost (IPA) |
| Unit | GBP/QALY or GBP/WELLBY | EUR/kg (per emission unit) |
| Scope | UK-specific | EU27 or global |
| Primary metric | Subjective wellbeing (LS 0–10 scale) | Physical emission → endpoint damage |
| Reference | HM Treasury Green Book | ExternE / EEA; ReCiPe 2016 |

### 1.2 WELLBY — Wellbeing-Adjusted Life Year

The **WELLBY** is the primary unit introduced by HM Treasury (2021) for measuring
subjective wellbeing in UK public sector appraisal:

> One WELLBY = a change of one point on a 0–10 life satisfaction scale for one person
> for one year.

The central value of **£13,000/WELLBY** is derived as the midpoint between:
- A QALY-anchored estimate (£10,000): £70,000 QALY ÷ 7 LS points/QALY
- An income-anchored estimate (£16,000): £30,673 avg. earnings ÷ 1.96 log-income coefficient

### 1.3 QALY — Quality-Adjusted Life Year

The **QALY** is the established metric in health economics:
- **Green Book welfare appraisal:** £70,000/QALY (2019) — primary for SCBA
- **NICE HTA healthcare threshold:** £20,000–£30,000/QALY — health sector benchmark

The relationship `1 QALY ≈ 7 WELLBYs` (Frijters & Krekel 2021) enables partial
interoperability between the two metrics, though they are not equivalent in general.

---

## 2. Source Documents

### 2.1 HM Treasury — The Green Book (2026)
UK government framework for appraisal and evaluation of public spending decisions.
Provides Social Time Preference Rates (STPR), distributional weights, treatment of
uncertainty, and cross-references to supplementary guidance on health and wellbeing.

### 2.2 HM Treasury — Wellbeing Guidance for Appraisal (July 2021)
Supplementary Green Book guidance introducing the WELLBY (Wellbeing-Adjusted Life Year)
as the primary unit for monetising subjective wellbeing impacts in UK public policy appraisal.
Provides the standard WELLBY value (£13,000, 2019 prices), derivation methodology,
uprating formulas, and illustrative case studies.

### 2.3 OECD — The WELLBY Well-being Valuation Method in the UK (2025)
OECD documentation of the UK's adoption of the WELLBY method, confirming the standard
value and describing international applicability. Reference: 60c1396c-en.

### 2.4 Frontier Economics / DCMS — Health and Wellbeing Final Report (December 2024)
Commissioned by the UK Department for Culture, Media and Sport. Monetises the health
and wellbeing benefits of cultural and heritage engagement in England across 13 model
variants covering four age groups, two valuation frameworks (QALY and WELLBY), and
three impact dimensions (individual health, NHS savings, productivity).

### 2.5 HM Treasury / PHE — Workplace Wellbeing Tool (December 2011)
Interactive Excel calculator for quantifying the financial impact of employee health
and wellbeing on organisations. Provides standard parameters, cost category definitions,
and investment appraisal methodology using NPV, BCR, and IRR.

---

## 3. Table Group Methodologies

### Table 01 — WELLBY and QALY Unit Valuations

**WELLBY (Wellbeing-Adjusted Life Year):**
One WELLBY = one-point change in life satisfaction (0–10 scale) for one person for one year.

**Three derivation approaches:**

| Approach | Method | Value (2019) |
|----------|--------|-------------|
| **Low** | QALY-based: £70,158 QALY ÷ 7 LS points/QALY | £10,000 |
| **High** | Income-based: £30,673 avg earnings ÷ 1.96 (log income coefficient) | £16,000 |
| **Central** | Midpoint of low and high | £13,000 |

**Uprating formula for different price years:**
```
WELLBY(t) = WELLBY(2019) × [GDP_deflator(t) / GDP_deflator(2019)] × [GDP_per_capita(t) / GDP_per_capita(2019)]^1.3
```
where 1.3 is the marginal utility of income elasticity (HM Treasury Green Book Annex 3).

**Large wellbeing changes (>0.5 points):**
Use Compensating Surplus rather than linear multiplication:
```
CS = M × [1 - exp(-βQ × ΔQ / βY)]
```
where M = average net personal income, βY = 1.96, βQ × ΔQ = total LS effect per person per year.

**QALY (Quality-Adjusted Life Year):**
- Green Book welfare appraisal: £70,000/QALY (2019 prices) — primary for SCBA
- NICE HTA healthcare threshold: £20,000–£30,000/QALY — health sector benchmark
- Relationship to WELLBY: 1 QALY ≈ 7 WELLBYs (one QALY corresponds to roughly
  a 7-point change in life satisfaction, e.g., from 8 to 1 on the 0–10 scale)

### Table 02 — Discount Rates

**Social Time Preference Rate (STPR):**
Declining schedule reflecting the expectation that future generations will be wealthier
(pure time preference + expected consumption growth). Applies to standard economic costs
and benefits.

**Health/wellbeing discount rate:**
Lower rate (1.5% for years 0–30) applied to QALYs, WELLBYs, and life years to avoid
embedding excessive discounting of future health impacts and to preserve intergenerational
equity in valuations of human welfare.

| Rate type | Period | Rate |
|-----------|--------|------|
| STPR standard | Years 1–30 | 3.50% |
| STPR standard | Years 31–75 | 3.00% |
| STPR standard | Year 76+ | 2.50% |
| Health/wellbeing | Years 0–30 | 1.50% |
| Health/wellbeing | Years 31–75 | ~1.29% |
| Health/wellbeing | Year 76+ | ~1.07% |

### Table 03 — Culture Health Benefits Per Person

**Framework:** Impact Pathway Approach applied to cultural engagement evidence:

```
Cultural engagement → Health/wellbeing outcome change → Monetised value
```

**Three impact components per model:**
1. **Individual impacts** — change in health/wellbeing quality of life, monetised via:
   - QALY models: ΔQALY × £70,000 (Green Book) or ΔQALY × £20,000 (HTA)
   - WELLBY models: ΔWELLBY × £13,000
2. **NHS/social care savings** — avoided treatment costs for depression or dementia
3. **Productivity impacts** — paid and unpaid work gains from improved health

**Evidence base:** Observational studies using UK surveys (Taking Part Survey, English
Longitudinal Study of Ageing), supplemented by literature-derived effect sizes and
NICE clinical guidelines for condition management costs.

**13 model variants** covering:
- Age groups: 10–14 (children), 18–29 (young adults), 30–49 (adults), 50+ (midlife+), 65+ (older adults)
- Health outcomes: general health, mental health functioning, emotional regulation/ADHD,
  self-esteem, depression incidence, dementia incidence, quality of life in cancer patients
- Engagement types: attendance, participation, organised activities, clinical art therapy

### Table 04 — Culture Health Benefits Societal

Society-wide estimates derived from: per-person benefit × estimated number of UK engagers.

Engager counts from national survey data (Taking Part Survey, ELSA). Models are **not
additive** as they cover different sub-populations and some overlap exists.

### Table 05 — Workplace Wellbeing Parameters

Standard UK workplace health and wellbeing cost calculation parameters:
- **Working days:** 228/year (5 days/week × 52 weeks − 32 days leave)
- **Non-wage cost factor:** 1.30 (wages × 1.3 ≈ total employment cost)
- **Five cost categories:** sickness absence, presenteeism, labour turnover,
  accidents/injuries, other (customisable)
- **Investment appraisal:** NPV, BCR, IRR over 2–10 year horizon

---

## 4. Value Transfer Mechanism

### 4.1 Temporal transfer — WELLBY uprating

The WELLBY central value (£13,000) and QALY reference value (£70,000) are expressed
at **2019 GBP price levels**. Applying these to other time periods requires an
income-adjusted temporal value transfer:

```
WELLBY(t) = WELLBY(2019) × [GDP_deflator(t) / GDP_deflator(2019)]
                          × [GDP_per_capita(t) / GDP_per_capita(2019)]^1.3
```

The exponent 1.3 is the **marginal utility of income elasticity** (HM Treasury Green
Book Annex 3). The GDP-per-capita term accounts for real income growth — society
is richer in future years, so a WELLBY is worth more in nominal terms.

| Parameter | Value | Source |
|---|---|---|
| Income elasticity ε | 1.3 | HM Treasury Green Book Annex 3 |
| GDP deflator data | ONS GDP deflator series (OGL v3) | HM Treasury |
| GDP per capita data | ONS National Accounts (OGL v3) | ONS |

For large wellbeing changes (>0.5 life-satisfaction points), a Compensating Surplus
formula replaces linear scaling to avoid overestimation of non-marginal changes.

### 4.2 Geographic transfer (OECD guidance)

The OECD (2025) document 60c1396c-en provides guidance for transferring WELLBY values
to other countries using:

```
WELLBY_country = WELLBY_UK × (GDP_per_capita_country / GDP_per_capita_UK)^ε
```

This is not implemented in this pipeline — the extracted values are the **UK reference
values** intended to serve as the unit transfer value for subsequent applications.

### 4.3 No transfer between QALYs and WELLBYs

The stated relationship `1 QALY ≈ 7 WELLBYs` is a calibration based on welfare
research (Frijters & Krekel 2021), not a direct transfer. The Green Book uses QALY
(£70,000) and WELLBY (£13,000) as two parallel but distinct metrics — they should
not be freely substituted without methodological justification.

---

## 4.4 External Sources for Value Transfer — License Detail

Each source that enables or calibrates the value transfer mechanisms above is
documented here with its precise license terms.

### 4.4.1 HM Treasury Green Book — Income Elasticity and STPR

| Attribute | Detail |
|---|---|
| **Used for** | Marginal utility of income elasticity ε = 1.3 (temporal WELLBY uprating, Annex 3); Ramsey STPR formula and schedule (Annex 6); Compensating Surplus formula |
| **Full citation** | HM Treasury (2026). *The Green Book: Central Government Guidance on Appraisal and Evaluation*. London: HM Treasury. |
| **License** | **Open Government Licence v3.0 (OGL v3)** |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Contains public sector information licensed under the Open Government Licence v3.0. Source: HM Treasury, The Green Book, 2026." |
| **Redistribution** | ✓ Free |
| **License URL** | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

---

### 4.4.2 ONS — GDP Deflator and GDP per Capita

| Attribute | Detail |
|---|---|
| **Used for** | GDP deflator time series and GDP per capita (both required for WELLBY temporal uprating formula); average earnings for WELLBY high estimate (Wellbeing Guidance §2.2) |
| **Full citation** | Office for National Statistics (ONS). *Consumer Price Indices; UK National Accounts (GDP per head); Annual Survey of Hours and Earnings (ASHE)*. Newport: ONS. https://www.ons.gov.uk |
| **License** | **Open Government Licence v3.0 (OGL v3)** |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Source: Office for National Statistics licensed under the Open Government Licence v3.0" |
| **Redistribution** | ✓ Free |
| **License URL** | https://www.ons.gov.uk/help/termsandconditions |

---

### 4.4.3 OECD — Geographic Transfer Guidance (60c1396c-en)

| Attribute | Detail |
|---|---|
| **Used for** | Guidance for cross-country WELLBY transfer using income elasticity adjustment: `WELLBY_country = WELLBY_UK × (GDPpc_country / GDPpc_UK)^ε` |
| **Full citation** | OECD (2025). *The WELLBY Well-being Valuation Method in the United Kingdom* (reference 60c1396c-en). OECD Publishing, Paris. |
| **License** | **OECD Proprietary — All Rights Reserved** |
| **Commercial use** | ✗ No — reproduction requires OECD written permission |
| **Attribution required** | Yes — cite OECD with reference code 60c1396c-en |
| **Redistribution** | ✗ Restricted; short quotation with attribution permitted for non-commercial use |
| **Note** | Used in this pipeline for cross-reference only; no values exclusive to this document are extracted. |
| **License URL** | https://www.oecd.org/en/about/terms-conditions.html |

---

### 4.4.4 Frijters & Krekel (2021) — QALY–WELLBY Calibration

| Attribute | Detail |
|---|---|
| **Used for** | `1 QALY ≈ 7 WELLBYs` calibration relationship underpinning the low WELLBY estimate (£10,000 = £70,000 QALY ÷ 7) |
| **Full citation** | Frijters, P. and Krekel, C. (2021). *A Handbook for Wellbeing Policy-Making: History, Theory, Measurement, Implementation, and Examples*. Oxford: Oxford University Press. |
| **License** | **CC BY-NC-ND 4.0** (Open Access on OAPEN / Oxford Academic) |
| **Commercial use** | ✗ Non-commercial only |
| **Derivatives** | ✗ No derivatives permitted |
| **Attribution required** | Yes — cite Frijters & Krekel 2021 |
| **Redistribution** | Non-commercial redistribution of the unmodified work permitted |
| **License URL** | https://library.oapen.org/handle/20.500.12657/60760; https://creativecommons.org/licenses/by-nc-nd/4.0/ |

---

### 4.4.5 Stern (2006) — STPR and Ramsey Formula

| Attribute | Detail |
|---|---|
| **Used for** | Theoretical foundation for the Ramsey growth formula used in STPR derivation (`r = ρ + ηg`); pure time preference rate ρ and consumption elasticity η values referenced in Green Book Annex 6 |
| **Full citation** | Stern, N. (2006). *Stern Review: The Economics of Climate Change*. Cambridge: Cambridge University Press. (Original government report: HM Treasury, October 2006.) |
| **License** | Original HM Treasury report: **OGL v3** (Crown copyright, freely available). Cambridge University Press edition: **All rights reserved** (academic book copyright; citation free, reproduction requires CUP permission). |
| **Commercial use** | OGL version: ✓ Yes. CUP edition: ✗ Restricted |
| **Attribution required** | Yes — cite Stern 2006 |
| **Redistribution** | OGL version: ✓ Free. CUP edition: ✗ Restricted |
| **Note** | The original Treasury report is freely downloadable under OGL from HM Treasury archives. Cite the Treasury version for open-use compliance. |
| **License URL** | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ (OGL); https://www.cambridge.org/core/books/economics-of-climate-change/A1E0BBF2F0ED8E2E4142A9C878052204 (CUP) |

---

### 4.4.6 NICE — QALY HTA Threshold

| Attribute | Detail |
|---|---|
| **Used for** | £20,000–£30,000/QALY NICE HTA benchmark used in culture model variants (Frontier 2024); calibrates one set of culture health benefit estimates |
| **Full citation** | National Institute for Health and Care Excellence (NICE) (2013). *Guide to the methods of technology appraisal 2013*. NICE Process and Methods Guides. London: NICE. |
| **License** | **NICE UK Open Content Licence** |
| **Commercial use** | ✓ Free within UK (commercial and non-commercial); international commercial use requires fee and licensing agreement |
| **Attribution required** | Yes — "© NICE [year]. All rights reserved. Content may be used within the UK without further permission from NICE." |
| **Redistribution** | ✓ Permitted in UK under NICE UK Open Content Licence |
| **License URL** | https://www.nice.org.uk/re-using-our-content; https://www.nice.org.uk/terms-and-conditions |

---

### 4.4.7 Taking Part Survey (DCMS) and ONS Population Data

| Attribute | Detail |
|---|---|
| **Used for** | Cultural engagement participation rates (engager count basis) for societal-level culture health estimates; ONS population denominators |
| **Full citation** | DCMS (2024). *Taking Part Adult and Child Survey* (annual). London: DCMS. — ONS (annual). *Population Estimates for the UK*. Newport: ONS. |
| **License** | **Open Government Licence v3.0 (OGL v3)** (both DCMS and ONS) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Contains public sector information licensed under the Open Government Licence v3.0." |
| **Redistribution** | ✓ Free |
| **License URL** | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

---

### 4.4.8 ELSA — English Longitudinal Study of Ageing

| Attribute | Detail |
|---|---|
| **Used for** | Epidemiological evidence base for mental health, depression, and dementia benefit estimates in culture models (regression inputs to Frontier 2024 model) |
| **Full citation** | Banks, J. et al. (2024). *English Longitudinal Study of Ageing: Waves 0–11, 1998–2024* (SN 5050). UK Data Service. https://doi.org/10.5255/UKDA-SN-5050-22 |
| **License** | **UK Data Service End User Licence (EUL)** — non-commercial academic and policy research |
| **Commercial use** | ✗ Non-commercial research use only under EUL; some waves under Special Licence |
| **Attribution required** | Yes — cite ELSA and UK Data Service (SN 5050) |
| **Redistribution** | ✗ Raw data may not be redistributed; derived aggregated findings may be published |
| **License URL** | https://www.elsa-project.ac.uk/accessing-elsa-data |

---

## 5. Relationship Between Value Factors

```
WELLBY (£13,000) ←── derived from ──→ QALY (£70,000)
                                              │
                   1 QALY ≈ 7 WELLBYs       │
                   £70,000 ÷ 7 ≈ £10,000    │
                   (→ low WELLBY estimate)   │
                                              ↓
Culture models (Table 03):          ΔQALY × £70,000 OR ΔWELLBY × £13,000
Workplace tool (Table 05):          Cost per day absent = wage/228
```

---

## 6. Price Levels and Currency

| Table group | Currency | Price year | Notes |
|-------------|----------|------------|-------|
| `wellby_valuations` | GBP | 2019 | Must uprate using GDP deflator + per-capita GDP^1.3 |
| `discount_rates` | N/A | N/A | Rates are dimensionless |
| `culture_health_per_person` | GBP | 2024 | Latest available; Frontier Economics 2024 |
| `culture_health_societal` | GBP | 2024 | Same as above |
| `workplace_wellbeing` | GBP | 2011 | Update wages to current prices for new appraisals |

---

## 7. Citation

When using these value factors in research or policy analysis, cite the original sources:

**WELLBY values:**
> HM Treasury (2021). *Wellbeing Guidance for Appraisal: supplementary Green Book guidance*. London: HM Treasury.

**Discount rates:**
> HM Treasury (2026). *The Green Book: Central Government Guidance on Appraisal and Evaluation*. London: HM Treasury.

**Culture and health benefits:**
> Frontier Economics (2024). *Health and Wellbeing Final Report* (December 2024). Prepared for the UK Department for Culture, Media and Sport.

**WELLBY methodology (international):**
> OECD (2025). *The WELLBY Well-being Valuation Method in the United Kingdom* (60c1396c-en). OECD.

**For the extraction pipeline:**
> Euler, D. (2026). *UK Wellbeing & Health Value Factor Pipeline* (vf_uk). Developed with the support of Claude Code (Anthropic). Greenings.
