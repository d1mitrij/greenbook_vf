# Input Files Methodology — vf_uk

**UK Wellbeing & Health Value Factor Extraction Pipeline**

**Pipeline author:** Dr Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Source Files

Five source publications are covered by this pipeline. All PDFs are stored in
the project root alongside their Markdown conversions.

### 1.1 HM Treasury — The Green Book (2026)

| Field | Value |
|---|---|
| File | `The_Green_Book_2026.pdf` |
| Markdown | `The_Green_Book_2026.md` |
| Publisher | HM Treasury, London |
| Publication year | 2026 |
| Price level | N/A (discount rates are dimensionless) |
| Pipeline tables | `discount_rates` |
| License | **Open Government Licence v3.0 (OGL v3)** |
| Commercial use | ✓ Yes |
| License URL | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

Provides the Social Time Preference Rate (STPR) schedule (Annex 6) and the
health/wellbeing discount rate. The STPR is derived from the Ramsey growth
formula: `r = ρ + ηg`, where `ρ` is the pure time preference rate, `η` is
the marginal utility of consumption elasticity, and `g` is expected long-run
per-capita consumption growth.

### 1.2 HM Treasury — Wellbeing Guidance for Appraisal (July 2021)

| Field | Value |
|---|---|
| File | `Wellbeing_guidance_for_appraisal_-_supplementary_Green_Book_guidance.pdf` |
| Markdown | `Wellbeing_guidance_for_appraisal_-_supplementary_Green_Book_guidance.md` |
| Publisher | HM Treasury, London |
| Publication year | July 2021 |
| Price level | GBP 2019 |
| Pipeline tables | `wellby_valuations` |
| License | **Open Government Licence v3.0 (OGL v3)** |
| Commercial use | ✓ Yes |
| License URL | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

Primary source for WELLBY unit values (low £10,000 / central £13,000 / high £16,000),
the three derivation approaches (QALY-based, income-based, midpoint), the uprating
formula, the Compensating Surplus formula for large changes, and all case study
event valuations (flooding, employment, loneliness, youth training).

### 1.3 OECD — The WELLBY Well-being Valuation Method in the UK (2025)

| Field | Value |
|---|---|
| File | `60c1396c-en.pdf` |
| Markdown | `60c1396c-en.md` |
| Publisher | OECD Publishing, Paris |
| Reference | 60c1396c-en |
| Publication year | 2025 |
| Price level | GBP 2019 (consistent with UK Wellbeing Guidance) |
| Pipeline tables | `wellby_valuations` (cross-reference and methodology confirmation) |
| License | **OECD Proprietary — All Rights Reserved** |
| Commercial use | ✗ No — reproduction requires OECD permission |
| License URL | https://www.oecd.org/en/about/terms-conditions.html |

Confirms and contextualises the UK WELLBY methodology in an international
framework. Provides guidance on geographic transfer of WELLBY values using
income elasticity adjustment. Used in this pipeline for cross-checking only —
no values are sourced exclusively from this document.

**OECD license note:** Short quotations with attribution are permitted for
non-commercial use; reproduction of tables or figures requires written
permission from OECD Publishing.

### 1.4 Frontier Economics / DCMS — Health and Wellbeing Final Report (December 2024)

| Field | Value |
|---|---|
| File | `rpt_-_Frontier_Health_and_Wellbeing_Final_Report_09_12_24_accessible_final.pdf` |
| Markdown | `rpt_-_Frontier_Health_and_Wellbeing_Final_Report_09_12_24_accessible_final.md` |
| Authors | Frontier Economics |
| Commissioner | UK Department for Culture, Media and Sport (DCMS) |
| Publication date | December 2024 |
| Price level | GBP 2024 |
| Pipeline tables | `culture_health_per_person`, `culture_health_societal` |
| License | **Mixed — likely OGL v3 for factual data (Crown copyright)** |
| Commercial use | Likely ✓ for factual outputs — confirm on GOV.UK publication page |
| License URL | https://www.gov.uk/government/publications/dcms-sectors-economic-estimates |

**License note:** This report was commissioned by DCMS (a UK government department).
Content produced by government contractors and published on GOV.UK typically falls
under **Crown copyright** and the **Open Government Licence v3.0**, permitting
free reuse with attribution. However, Frontier Economics retains copyright over
their proprietary methodologies and models. The extracted value factors (per-person
benefit estimates, engager counts) are factual outputs derived from publicly funded
research and are reported here with full attribution.

**Attribution required:**
> Frontier Economics (2024). *Health and Wellbeing Final Report* (December 2024).
> Prepared for the UK Department for Culture, Media and Sport.

### 1.5 HM Treasury / Public Health England — Workplace Wellbeing Tool (December 2011)

| Field | Value |
|---|---|
| File | `Workplace_wellbeing_tool.xlsx` |
| Author | Barry Griffiths |
| Publisher | HM Treasury / Public Health England (PHE) |
| Publication date | December 2011 |
| Price level | GBP 2011 |
| Pipeline tables | `workplace_wellbeing` |
| License | **Open Government Licence v3.0 (OGL v3)** |
| Commercial use | ✓ Yes |
| License URL | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

Interactive Excel calculator providing standard parameters (working days/year,
non-wage cost factor), five cost category definitions (sickness absence,
presenteeism, labour turnover, accidents, other), and investment appraisal
methodology (NPV, BCR, IRR). Values are manually transcribed from the example
worksheets (sheets 1c and 2c).

---

## 2. External Methodology Sources

The values extracted by this pipeline rest on a chain of methodological inputs
that the source document authors themselves drew upon. These are not direct
inputs to this pipeline, but their licenses constrain downstream use.

### 2.1 Frijters & Krekel (2021) — QALY–WELLBY Ratio

| Attribute | Detail |
|---|---|
| **Used for** | Establishing the `1 QALY ≈ 7 WELLBYs` equivalence used in the QALY-based derivation of the WELLBY unit value (WBG 2021 §3) |
| **Full citation** | Frijters, P. and Krekel, C. (2021). *A Handbook for Wellbeing Policy-Making: History, Theory, Measurement, Implementation, and Examples*. Oxford: Oxford University Press. |
| **License** | **CC BY-NC-ND 4.0** (Open Access on OAPEN / Oxford Academic) |
| **Commercial use** | ✗ Non-commercial only |
| **Derivatives** | ✗ No derivatives permitted |
| **Attribution required** | Yes — cite Frijters & Krekel 2021 |
| **Redistribution** | Redistribution of the work as-is permitted non-commercially |
| **License URL** | https://library.oapen.org/handle/20.500.12657/60760; https://creativecommons.org/licenses/by-nc-nd/4.0/ |

---

### 2.2 Fujiwara (2021) — Log-Income Coefficient for WELLBY High Estimate

| Attribute | Detail |
|---|---|
| **Used for** | Log-income coefficient of 1.96 (income-based approach, 0–10 scale) used to derive the £16,000 high bound WELLBY value (WBG 2021 §2.2) |
| **Full citation** | Fujiwara, D. and Dass, D. (2021). *Incorporating Life Satisfaction into Discrete Choice Experiments to Estimate Wellbeing Values for Non-Market Goods*. Simetrica-Jacobs Research Paper, July 2021. |
| **License** | **Proprietary — Simetrica-Jacobs copyright** (company research report, not a journal publication) |
| **Commercial use** | ✗ Not specified; academic citation freely permitted |
| **Attribution required** | Yes — cite Fujiwara & Dass 2021, Simetrica-Jacobs |
| **Redistribution** | ✗ Restricted |
| **Note** | This is an industry research report, not an open-access publication. The coefficient value itself is a factual statistical finding and is cited by HM Treasury in published guidance. |
| **License URL** | https://simetrica-jacobs.com |

---

### 2.3 NICE Health Technology Assessment Thresholds

| Attribute | Detail |
|---|---|
| **Used for** | £20,000–£30,000/QALY HTA benchmark used to contextualise the QALY-based WELLBY derivation (Frontier 2024) |
| **Full citation** | National Institute for Health and Care Excellence (NICE). *Guide to the methods of technology appraisal 2013*. NICE Process and Methods Guides. London: NICE, 2013. |
| **License** | **NICE UK Open Content Licence** |
| **Commercial use** | ✓ Free within UK (commercial and non-commercial); international commercial use requires fee and licensing agreement |
| **Attribution required** | Yes — "© NICE [year]. All rights reserved. Content may be used within the UK without any further permission from NICE." |
| **Redistribution** | ✓ Permitted in UK under NICE UK Open Content Licence |
| **Note** | NICE is a UK Non-Departmental Public Body (NDPB); its guidance is under the NICE UK Open Content Licence, which is distinct from OGL v3. Outside the UK, reproduction of tables requires a licence fee. |
| **License URL** | https://www.nice.org.uk/re-using-our-content; https://www.nice.org.uk/terms-and-conditions |

---

### 2.4 Taking Part Survey (DCMS)

| Attribute | Detail |
|---|---|
| **Used for** | Cultural engagement participation rates and engager count basis (Frontier 2024, Table 12) |
| **Full citation** | Department for Culture, Media and Sport (DCMS) (2024). *Taking Part: Adult and Child Survey* (annual publication). London: DCMS. |
| **License** | **Open Government Licence v3.0 (OGL v3)** |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Contains public sector information licensed under the Open Government Licence v3.0." |
| **Redistribution** | ✓ Free |
| **License URL** | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

---

### 2.5 English Longitudinal Study of Ageing (ELSA)

| Attribute | Detail |
|---|---|
| **Used for** | Mental health and dementia evidence base for cultural engagement benefit estimates (Frontier 2024) |
| **Full citation** | Banks, J., Batty, G.D., Breedvelt, J., Coughlin, K., Crawford, R., Marmot, M. et al. (2024). *English Longitudinal Study of Ageing: Waves 0–11, 1998–2024* (SN 5050). UK Data Service. |
| **License** | **UK Data Service End User Licence (EUL)** — non-commercial academic and policy research |
| **Commercial use** | ✗ Non-commercial research use only under EUL; some waves require Special Licence |
| **Attribution required** | Yes — cite ELSA and UK Data Service (SN 5050) |
| **Redistribution** | ✗ Raw data may not be redistributed; derived aggregated findings may be published |
| **Registration** | Access via UK Data Service registration |
| **License URL** | https://www.elsa-project.ac.uk/accessing-elsa-data; https://datacatalogue.ukdataservice.ac.uk/series/series/200011 |

---

### 2.6 ONS National Accounts and Labour Market Statistics

| Attribute | Detail |
|---|---|
| **Used for** | GDP deflator, GDP per capita, and average earnings — used in WELLBY temporal uprating formula and derivation parameters (WBG 2021 §4) |
| **Full citation** | Office for National Statistics (ONS). *Consumer Price Indices / UK National Accounts / Labour Market Statistics* (annual series). Newport: ONS. https://www.ons.gov.uk |
| **License** | **Open Government Licence v3.0 (OGL v3)** |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Source: Office for National Statistics licensed under the Open Government Licence v3.0" |
| **Redistribution** | ✓ Free |
| **License URL** | https://www.ons.gov.uk/help/termsandconditions |

---

### 2.7 WHO / Clinical Literature — NHS Cost Estimates

| Attribute | Detail |
|---|---|
| **Used for** | Depression and dementia treatment cost estimates (NHS savings); mortality concentration-response functions used indirectly in DCMS/Frontier modelling (Frontier 2024) |
| **Full citation** | WHO Regional Office for Europe (2013). *HRAPIE: Health Risks of Air Pollution in Europe*. Copenhagen: WHO Europe. (Plus various clinical literature cited in Frontier 2024 footnotes.) |
| **License** | **© WHO 2013 All Rights Reserved** (pre-2016 WHO publications); clinical journal articles: journal-specific (typically CC BY for recent open-access papers) |
| **Commercial use** | ✗ WHO 2013 reports: permission required; post-2016 WHO: CC BY-NC-SA 3.0 IGO (non-commercial) |
| **Attribution required** | Yes — cite WHO HRAPIE 2013 and original clinical papers |
| **Note** | WHO changed to a CC BY-NC-SA 3.0 IGO open-access policy in November 2016. Publications before this date carry full copyright. |
| **License URL** | https://www.who.int/about/policies/publishing/open-access |

---

## 3. Table Mapping — Source to Pipeline

| `pipeline.py` variable | Source document | Source location | Content |
|------------------------|----------------|-----------------|---------|
| `_WELLBY_CORE` | Wellbeing Guidance 2021 | Table 1 + §2 | WELLBY unit values (low/central/high) + QALY values |
| `_WELLBY_PARAMS` | Wellbeing Guidance 2021 | §4 + Annex | Derivation parameters (elasticity, income coefficient) |
| `_WELLBY_EVENTS` | Wellbeing Guidance 2021 | Case studies §5–9 | Event-level valuations (flooding, employment, loneliness, training) |
| `_DISCOUNT_RATES` | Green Book 2026 | Annex 6 | STPR schedule (years 1–30, 31–75, 76+) + health rate |
| `_CULTURE_PER_PERSON` | Frontier 2024 | Tables 3, 12 | Per-person annual benefits, 15 model-variants (11a, 11b as additional) |
| `_CULTURE_SOCIETAL` | Frontier 2024 | Table 12 | Society-wide totals (GBP) + estimated engager counts |
| `_WORKPLACE_PARAMS` | Workplace Wellbeing Tool 2011 | Sheets 1c, 2c | Standard parameters, cost benchmarks, appraisal example results |

---

## 4. What the Pipeline Does NOT Read at Runtime

- Any PDF or Markdown file
- The Workplace Wellbeing XLSX (values manually transcribed)
- Any external API or database (ONS, NICE, DCMS)

All data is embedded in `pipeline.py` as Python data structures, verified
against the source documents.

---

## 5. License Model

### 5.1 License summary by source

| Source | License | Commercial use (UK) | Commercial use (intl.) | Attribution |
|---|---|---|---|---|
| Green Book 2026 | OGL v3 | ✓ Free | ✓ Free | Required |
| Wellbeing Guidance 2021 | OGL v3 | ✓ Free | ✓ Free | Required |
| OECD WELLBY 2025 | OECD Proprietary | ✗ No | ✗ No | Required |
| Frontier / DCMS 2024 | Likely OGL v3 (Crown copyright) | ✓ Likely free | ✓ With attribution | Required |
| Workplace Wellbeing Tool 2011 | OGL v3 | ✓ Free | ✓ Free | Required |
| Frijters & Krekel 2021 | CC BY-NC-ND 4.0 | ✗ Non-commercial | ✗ Non-commercial | Required |
| Fujiwara 2021 | Simetrica-Jacobs proprietary | ✗ Restricted | ✗ Restricted | Required |
| NICE HTA thresholds | NICE UK Open Content Licence | ✓ Free | Fee required | Required |
| Taking Part Survey | OGL v3 | ✓ Free | ✓ Free | Required |
| ELSA | UK Data Service EUL | ✗ Non-commercial | ✗ Non-commercial | Required |
| ONS statistics | OGL v3 | ✓ Free | ✓ Free | Required |
| WHO clinical literature | © WHO / journal-specific | ✗ WHO: restricted | ✗ | Required |

### 5.2 OGL v3 standard attribution

For all OGL v3 sources, use:
> Contains public sector information licensed under the Open Government Licence v3.0.
> Source: HM Treasury / [publication title] / [year].

### 5.3 This pipeline's outputs

The extracted value factor tables (CSV/Excel) derive primarily from OGL v3 UK
government publications. The primary WELLBY, STPR, and workplace values are
OGL v3 and freely reusable commercially.

The Frijters & Krekel 2021 input (CC BY-NC-ND 4.0) and Fujiwara 2021
(Simetrica-Jacobs proprietary) underpin the *derivation methodology*
documented in HM Treasury guidance, not values directly extracted by this
pipeline. No values from the OECD WELLBY 2025 document are exclusively
sourced from that publication.

**Effective output license: OGL v3**, applying to the core pipeline outputs
(wellby_valuations, discount_rates, culture tables, workplace tables).

Users of `culture_health` tables derived from Frontier Economics 2024 should
confirm OGL v3 status on the GOV.UK publication page before commercial use.

---

## 6. Updating Source Files

When source publications are updated (e.g. Green Book revised, new Wellbeing Guidance):

1. Replace the PDF in the project root.
2. Regenerate the Markdown conversion.
3. Update `pipeline.py` data structures — see `DATA_UPDATES.md`.
4. Update `VALIDATION_REPORT.md` with new known-good reference values.
5. Review whether the WELLBY central value or STPR schedule has changed.

---

## 7. Source File Validation Checklist

Before a pipeline run, verify:

- [ ] `The_Green_Book_2026.pdf` present; title reads "The Green Book: Appraisal and Evaluation in Central Government"
- [ ] `Wellbeing_guidance_for_appraisal_*.pdf` present; publication date July 2021
- [ ] `60c1396c-en.pdf` present; OECD reference code 60c1396c-en confirmed
- [ ] `rpt_-_Frontier_Health_and_Wellbeing_Final_Report_*.pdf` present; date December 2024
- [ ] `Workplace_wellbeing_tool.xlsx` present; author Barry Griffiths, December 2011
- [ ] WELLBY central value in pipeline = £13,000 (Wellbeing Guidance Table 1)
- [ ] QALY Green Book value = £70,000 (Wellbeing Guidance §3.2)
- [ ] STPR years 1–30 = 3.50% (Green Book Annex 6)
- [ ] Health discount rate years 0–30 = 1.50% (Green Book / Wellbeing Guidance)

---

*Document Version 3.0 | Last Updated 2026-03-09 | Maintained by Greenings | dimitrij.euler@greenings.org*
*Value factors: HM Treasury / Frontier Economics / OECD | Scripts: Dr Dimitrij Euler with support of Claude Code (Anthropic)*
