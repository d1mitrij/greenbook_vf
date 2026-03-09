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
| License URL | https://www.oecd.org/en/about/terms-conditions.html |

Confirms and contextualises the UK WELLBY methodology in an international
framework. Provides guidance on geographic transfer of WELLBY values using
income elasticity adjustment. Used in this pipeline for cross-checking only —
no values are sourced exclusively from this document.

**OECD license note:** OECD publications are copyright OECD. Short quotations
with attribution are permitted for non-commercial use; reproduction of tables
or figures requires written permission from OECD Publishing.

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
| License | **Mixed — see note below** |
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
| License URL | https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ |

Interactive Excel calculator providing standard parameters (working days/year,
non-wage cost factor), five cost category definitions (sickness absence,
presenteeism, labour turnover, accidents, other), and investment appraisal
methodology (NPV, BCR, IRR). Values are manually transcribed from the example
worksheets (sheets 1c and 2c).

---

## 2. External Methodology Sources Embedded in Source Documents

The following external data sources and methodological references underlie the
values extracted by this pipeline. They are inputs to the source document authors,
not direct inputs to this pipeline.

| Source | Role | Used by | License |
|---|---|---|---|
| **Frijters & Krekel (2021)** | `1 QALY ≈ 7 WELLBYs` relationship | WBG 2021 §3 | Academic — CC-BY (journal-specific) |
| **Fujiwara (2021)** | Log-income coefficient (1.96 on 0–10 scale) for WELLBY high estimate | WBG 2021 §2.2 | Academic publication |
| **NICE Health Technology Assessment thresholds** | £20,000–£30,000/QALY HTA benchmark | Frontier 2024 | OGL v3 (NICE is UK NDPB) |
| **Taking Part Survey (DCMS)** | Cultural engagement participation rates; engager count basis | Frontier 2024, Table 12 | OGL v3 |
| **English Longitudinal Study of Ageing (ELSA)** | Mental health and dementia evidence base | Frontier 2024 | Open access (IFS/NatCen) |
| **ONS National Accounts / labour data** | GDP deflator, GDP per capita, average earnings | WBG 2021 | OGL v3 |
| **WHO HRAPIE / clinical literature** | Depression and dementia treatment cost estimates (NHS savings) | Frontier 2024 | WHO terms / CC-BY (journals) |

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

### 5.1 Summary by source

| Source | License | Commercial use | Redistribution | Attribution |
|---|---|---|---|---|
| Green Book 2026 | OGL v3 | ✓ Yes | ✓ Free | Required |
| Wellbeing Guidance 2021 | OGL v3 | ✓ Yes | ✓ Free | Required |
| OECD WELLBY 2025 | OECD Proprietary | ✗ No | ✗ Restricted | Required |
| Frontier / DCMS 2024 | Mixed (likely OGL v3 for factual data) | Unclear | With attribution | Required |
| Workplace Wellbeing Tool 2011 | OGL v3 | ✓ Yes | ✓ Free | Required |

### 5.2 OGL v3 standard attribution

For all OGL v3 sources, use:
> Contains public sector information licensed under the Open Government Licence v3.0.
> Source: HM Treasury / [publication title] / [year].

### 5.3 This pipeline's outputs

The extracted value factor tables (CSV/Excel) derive primarily from OGL v3
UK government publications. The outputs are therefore made available under
**OGL v3**, consistent with the most restrictive applicable license in the set.

However, the OECD WELLBY document (cross-reference only) and the Frontier
Economics report introduce uncertainty. Users wishing to use these outputs in
commercial applications should:
1. Confirm that the Frontier Economics report is published under OGL v3 on GOV.UK.
2. Note that OECD methodology is referenced but no OECD-proprietary values are
   reproduced in the pipeline outputs.

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

*Document Version 2.0 | Last Updated 2026-03-09 | Maintained by Greenings | dimitrij.euler@greenings.org*
*Value factors: HM Treasury / Frontier Economics / OECD | Scripts: Dr Dimitrij Euler with support of Claude Code (Anthropic)*
