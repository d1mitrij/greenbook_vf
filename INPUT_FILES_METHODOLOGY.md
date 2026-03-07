# Input Files — vf_uk

**UK Wellbeing & Health Value Factor Extraction Pipeline**
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Source Files

Five source publications are covered by this pipeline. All PDFs are stored in
the project root alongside their Markdown conversions.

### 1.1 HM Treasury — The Green Book (2026)

| Field | Value |
|---|---|
| File | `The_Green_Book_2026.pdf` |
| Markdown | `The_Green_Book_2026.md` |
| Publisher | HM Treasury |
| Price level | N/A (discount rates are dimensionless) |
| Pipeline tables | `discount_rates` |

### 1.2 HM Treasury — Wellbeing Guidance for Appraisal (July 2021)

| Field | Value |
|---|---|
| File | `Wellbeing_guidance_for_appraisal_-_supplementary_Green_Book_guidance.pdf` |
| Markdown | `Wellbeing_guidance_for_appraisal_-_supplementary_Green_Book_guidance.md` |
| Publisher | HM Treasury |
| Price level | GBP 2019 |
| Pipeline tables | `wellby_valuations` |

### 1.3 OECD — The WELLBY Method in the UK (2025)

| Field | Value |
|---|---|
| File | `60c1396c-en.pdf` |
| Markdown | `60c1396c-en.md` |
| Publisher | OECD |
| Price level | GBP 2019 |
| Pipeline tables | `wellby_valuations` (cross-check) |

### 1.4 Frontier Economics / DCMS — Health and Wellbeing Final Report (December 2024)

| Field | Value |
|---|---|
| File | `rpt_-_Frontier_Health_and_Wellbeing_Final_Report_09_12_24_accessible_final.pdf` |
| Markdown | `rpt_-_Frontier_Health_and_Wellbeing_Final_Report_09_12_24_accessible_final.md` |
| Publisher | Frontier Economics / UK Department for Culture, Media and Sport |
| Price level | GBP 2024 |
| Pipeline tables | `culture_health_per_person`, `culture_health_societal` |

### 1.5 HM Treasury / PHE — Workplace Wellbeing Tool (December 2011)

| Field | Value |
|---|---|
| File | `Workplace_wellbeing_tool.xlsx` |
| Publisher | HM Treasury / Public Health England |
| Author | Barry Griffiths |
| Price level | GBP 2011 |
| Pipeline tables | `workplace_wellbeing` |

---

## 2. Table Mapping

| pipeline.py variable | Source | Content |
|---------------------|--------|---------|
| `_WELLBY_CORE` | Wellbeing Guidance 2021, Table 1 | WELLBY unit values (low/central/high) and QALY values |
| `_WELLBY_PARAMS` | Wellbeing Guidance 2021, §4 | Derivation parameters (elasticity, log income coeff.) |
| `_WELLBY_EVENTS` | Wellbeing Guidance 2021, case studies | Event-level valuations (flooding, employment, loneliness) |
| `_DISCOUNT_RATES` | Green Book 2026, Annex 6 | STPR schedule and health/wellbeing discount rate |
| `_CULTURE_PER_PERSON` | Frontier 2024, Tables 3 and 12 | Per-person annual benefits, 15 model-variants |
| `_CULTURE_SOCIETAL` | Frontier 2024, Table 12 | Society-wide totals and engager counts, 13 models |
| `_WORKPLACE_PARAMS` | Workplace Wellbeing Tool 2011 | Standard parameters, benchmarks, appraisal examples |

---

## 3. Markdown Conversion Process

PDFs were converted to Markdown using:

```bash
python adb_china/convert_to_md.py <filename>.pdf
```

The script uses the `pypdf` library for plain text extraction. No machine
learning or layout analysis is involved. The resulting Markdown is used for
reference and QA; the pipeline reads only from hard-coded data in `pipeline.py`.

---

## 4. What the Pipeline Does NOT Read at Runtime

- Any PDF or Markdown file
- The Workplace Wellbeing XLSX (values manually transcribed)
- Any external API or database

All data is embedded in `pipeline.py` as Python data structures, verified
against the source documents.

---

## 5. Updating Source Files

When source publications are updated:

1. Replace the PDF and regenerate the Markdown.
2. Update `pipeline.py` — see `DATA_UPDATES.md` for the procedure.
3. Update `VALIDATION_REPORT.md` with new known-good reference values.
