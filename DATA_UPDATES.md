# Data Updates — vf_uk

**UK Wellbeing & Health Value Factor Extraction Pipeline**
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## Overview

This document describes the procedure for updating `pipeline.py` when source
publications are revised.

### Current source versions

| Source | Version | Price level |
|--------|---------|-------------|
| HM Treasury Green Book | 2026 | N/A |
| HM Treasury Wellbeing Guidance | July 2021 | GBP 2019 |
| OECD WELLBY Method | 2025 | GBP 2019 |
| Frontier Economics / DCMS | December 2024 | GBP 2024 |
| Workplace Wellbeing Tool | December 2011 | GBP 2011 |

---

## Update Procedure

### Step 1 — Replace source files

Download the updated publication. Replace the PDF in the project root.
Regenerate the Markdown:

```bash
python adb_china/convert_to_md.py <filename>.pdf
```

### Step 2 — Identify changed values

Compare the new document against the current values in `pipeline.py`.
Common change types:
- Updated STPR schedule (Green Book revisions)
- Revised WELLBY unit value (new OECD/HMT guidance)
- New model variants in the Frontier culture-health report
- Revised workplace cost benchmarks

### Step 3 — Update pipeline.py

Each data structure in `pipeline.py` corresponds to one table group:

| Variable | Key | Update trigger |
|----------|-----|---------------|
| `_WELLBY_CORE` | `wellby_valuations` | New HMT/OECD WELLBY guidance |
| `_WELLBY_PARAMS` | `wellby_valuations` | Parameter revision |
| `_WELLBY_EVENTS` | `wellby_valuations` | New case studies in guidance |
| `_DISCOUNT_RATES` | `discount_rates` | Green Book Annex 6 revision |
| `_CULTURE_PER_PERSON` | `culture_health_per_person` | New Frontier/DCMS report |
| `_CULTURE_SOCIETAL` | `culture_health_societal` | New Frontier/DCMS report |
| `_WORKPLACE_PARAMS` | `workplace_wellbeing` | New Workplace Tool release |

If the price base year changes, update the `currency` and `price_year` fields
in the relevant data rows, and update the `PUBLICATIONS` dict in `config.py`.

### Step 4 — Update config.py

If publication metadata has changed (title, date, URL), update the `PUBLICATIONS`
dict in `config.py`.

### Step 5 — Run and verify

```bash
python extract_uk_values.py
```

Compare output CSV values against the updated source. Update `VALIDATION_REPORT.md`
with new known-good reference values from the revised document.

---

## Price Level Uprating

Values are stored at the price year of their source publication. To uprate GBP
2019 WELLBY values to a current price year, apply the formula from `METHODOLOGY.md`:

```
WELLBY(t) = WELLBY(2019)
            × [GDP_deflator(t) / GDP_deflator(2019)]
            × [GDP_per_capita(t) / GDP_per_capita(2019)]^1.3
```

This uprating is not applied by the pipeline — it is documented here for user
reference. Downstream users apply the formula at the point of use.

---

## Version History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-07 | Initial extraction from all 5 source publications | D. Euler / Claude Code |
