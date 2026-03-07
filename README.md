# UK Wellbeing & Health Value Factors Pipeline

## Data Sources & Attribution

> **This pipeline extracts and structures value factors from five UK government and research publications:**
>
> 1. **HM Treasury — The Green Book (2026)**
>    Central Government Guidance on Appraisal and Evaluation
>
> 2. **HM Treasury — Wellbeing Guidance for Appraisal (July 2021)**
>    Supplementary Green Book guidance on WELLBY valuation
>
> 3. **OECD — The WELLBY Well-being Valuation Method in the United Kingdom (2025)**
>    Reference: 60c1396c-en
>
> 4. **Frontier Economics / DCMS — Health and Wellbeing Final Report (December 2024)**
>    Prepared for the UK Department for Culture, Media and Sport
>
> 5. **HM Treasury / Public Health England — Workplace Wellbeing Tool (December 2011)**
>    Author: Barry Griffiths

All value factors, monetary estimates, and methodological content remain the intellectual
property of their respective publishers. This pipeline is a structured extraction tool only.
When citing these values in research or policy work, always cite the original source publications.

---

## Script Authorship

**Extraction pipeline developed by:**
Dimitrij Euler (Greenings) — dimitrij.euler@greenings.org

**With the support of:** Claude Code (Anthropic)

---

## Overview

This pipeline converts five UK government and research documents into machine-readable,
analysis-ready CSV and Excel files. It covers **72 value factor rows** across **5 table groups**,
spanning WELLBY/QALY unit values, discount rates, culture and health benefits, and workplace
wellbeing cost parameters.

All values are hard-coded from verified source documents — no PDF parsing at runtime.

---

## Quick Start

```bash
python extract_uk_values.py                              # all 5 groups
python extract_uk_values.py --only wellby_valuations     # one group
python extract_uk_values.py --list                       # list groups
python tables/01_wellby_valuations.py                    # single table
```

---

## Table Groups

| ID | Key | Source | Description | Rows | Unit |
|----|-----|--------|-------------|------|------|
| 01 | `wellby_valuations` | Wellbeing Guidance 2021; OECD 2025 | WELLBY, QALY unit values + case study event valuations | 19 | GBP 2019/unit |
| 02 | `discount_rates` | Green Book 2026 | STPR by time period + health discount rate | 8 | % real |
| 03 | `culture_health_per_person` | Frontier / DCMS 2024 | Per-person annual benefits from cultural engagement (15 model-variants) | 15 | GBP 2024/person/year |
| 04 | `culture_health_societal` | Frontier / DCMS 2024 | Society-wide annual benefits + engager numbers (13 models) | 13 | GBP 2024/year |
| 05 | `workplace_wellbeing` | Workplace Wellbeing Tool 2011 | Standard parameters, cost benchmarks, appraisal example results | 17 | GBP 2011/unit |

**Total: 72 value factor rows**

---

## Repository Structure

```
vf_uk/
├── config.py                       # Table group definitions and publication metadata
├── pipeline.py                     # Hard-coded data, builder functions, Excel writer
├── extract_uk_values.py            # Orchestrator (CLI: --only, --list)
├── tables/
│   ├── _template.py
│   ├── 01_wellby_valuations.py
│   ├── 02_discount_rates.py
│   ├── 03_culture_health_per_person.py
│   ├── 04_culture_health_societal.py
│   └── 05_workplace_wellbeing.py
├── output/
│   ├── 01_uk_wellby_valuations.{csv,xlsx}
│   ├── 02_uk_discount_rates.{csv,xlsx}
│   ├── 03_uk_culture_health_per_person.{csv,xlsx}
│   ├── 04_uk_culture_health_societal.{csv,xlsx}
│   └── 05_uk_workplace_wellbeing.{csv,xlsx}
├── The_Green_Book_2026.{pdf,md}
├── Wellbeing_guidance_for_appraisal_*.{pdf,md}
├── 60c1396c-en.{pdf,md}
├── rpt_-_Frontier_Health_and_Wellbeing_Final_Report_*.{pdf,md}
├── Levelling Up the United Kingdom_*.{pdf,md}
├── Executive_Summary (1).{pdf,md}
├── Workplace_wellbeing_tool.xlsx
├── README.md
├── METHODOLOGY.md
├── ARCHITECTURE_DECISIONS.md
└── VALIDATION_REPORT.md
```

---

## Key Values at a Glance

**WELLBY unit values (GBP 2019):**

| Variant | Value |
|---------|-------|
| Low | £10,000/WELLBY |
| **Central** | **£13,000/WELLBY** |
| High | £16,000/WELLBY |

**QALY values:**

| Application | Value |
|-------------|-------|
| Green Book (welfare appraisal) | £70,000/QALY (2019) |
| NICE HTA (healthcare) | £20,000–£30,000/QALY |

**Social Time Preference Rates (real):**

| Period | STPR | Health rate |
|--------|------|-------------|
| Years 1–30 | 3.50% | 1.50% |
| Years 31–75 | 3.00% | ~1.29% |
| Year 76+ | 2.50% | ~1.07% |

**Per-person annual benefits from cultural engagement (GBP 2024, central):**

| Model | Benefit |
|-------|---------|
| Arts-based museum activities (65+) | £1,310/person/year |
| Daily organised arts (18–29) | £1,240/person/year |
| General engagement & health (30–49) | £992/person/year |
| Museums and dementia (50+) | £369/person/year |

---

## Dependencies

```bash
pip install openpyxl
```

---

## Integration

Follows the same structural pattern as sibling projects:

| Project | Source | Pattern |
|---------|--------|---------|
| `steen-vf1` | EPS 2015d.1 | `config + pipeline + indicators/` |
| `uba1` | UBA Handbook MC 4.0 | `config + pipeline + tables/` |
| `vf_cedelft` | CE Delft Handbook 2024 | `config + pipeline + tables/` |
| `vf_valuingimpact` | eQALY (Valuing Impact) | `config + pipeline + indicators/` |
| **`vf_uk`** | **HM Treasury / Frontier / OECD** | **`config + pipeline + tables/`** |
