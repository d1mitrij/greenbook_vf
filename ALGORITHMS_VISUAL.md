# Algorithms — vf_uk

**UK Wellbeing & Health Value Factor Extraction Pipeline**
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Overall Data Flow

```
pipeline.py
  _WELLBY_CORE    (list of dicts)   ─┐
  _WELLBY_PARAMS  (list of dicts)    │  _build_wellby_valuations_rows()
  _WELLBY_EVENTS  (list of dicts)    │
  _DISCOUNT_RATES (list of dicts)   ─┼──────────────────────────────→ list[dict]
  _CULTURE_PER_PERSON               ─┤  builder functions (one per table group)
  _CULTURE_SOCIETAL                  │
  _WORKPLACE_PARAMS (list of dicts) ─┘
            │
            ▼
       run_table(key)
            │
            ├──→ CSV  (output/NN_uk_*.csv)
            └──→ XLSX (output/NN_uk_*.xlsx)
                        │
                        ├── Sheet: "Value Factors"   (formatted data)
                        └── Sheet: "Metadata"        (source attribution)
```

---

## 2. Builder Functions

| Function | Key | Source | Output columns |
|----------|-----|--------|----------------|
| `_build_wellby_valuations_rows()` | `wellby_valuations` | Wellbeing Guidance 2021 | row_type, metric, variant, value_gbp, price_year, notes |
| `_build_discount_rates_rows()` | `discount_rates` | Green Book 2026 | rate_type, period, period_start_yr, period_end_yr, rate_pct, notes |
| `_build_culture_per_person_rows()` | `culture_health_per_person` | Frontier 2024 | model_id, model_name, age_group, valuation_method, component, variant, value_gbp, price_year |
| `_build_culture_societal_rows()` | `culture_health_societal` | Frontier 2024 | model_id, model_name, age_group, metric, value, unit, price_year, notes |
| `_build_workplace_wellbeing_rows()` | `workplace_wellbeing` | Workplace Tool 2011 | parameter, category, value, unit, price_year, notes |

---

## 3. run_table() Algorithm

```
run_table(key):
  1. Look up (builder_fn, fieldnames) from _BUILDERS[key]
  2. Call builder_fn() → rows: list[dict]
  3. Look up output paths from config.TABLE_GROUPS[key]
  4. Create output/ directory if needed
  5. Write CSV:
       DictWriter(fieldnames, extrasaction="ignore")
  6. Write XLSX (_write_excel()):
       ws_data: "Value Factors" — dark header, freeze A2
       ws_meta: "Metadata" — publication and table group fields
  7. Return output_csv path
```

---

## 4. WELLBY Data Structure

The `wellby_valuations` table group contains three types of rows, distinguished
by the `row_type` field:

```
row_type = "unit_value"   → core WELLBY/QALY monetary values
row_type = "parameter"    → derivation parameters (elasticity, log income coeff.)
row_type = "event"        → case study event valuations (flooding, employment, etc.)
```

This allows a single CSV to carry all WELLBY-related data while remaining filterable.

---

## 5. Culture Health Model Structure

The `culture_health_per_person` table has 15 model-variants covering:

- 5 age groups: 10–14, 18–29, 30–49, 50+, 65+
- 2 valuation frameworks: QALY (Green Book £70k and HTA £20k) and WELLBY
- 3 impact components per model: individual health, NHS/care savings, productivity

Each row is one component × one model × one variant (low/central/high).

The `culture_health_societal` table provides aggregate totals and engager counts
for the 13 models where Frontier reports society-wide estimates.

---

## 6. Dispatch Table

```python
_BUILDERS = {
    "wellby_valuations":        (_build_wellby_valuations_rows,   WELLBY_FIELDS),
    "discount_rates":           (_build_discount_rates_rows,      DISCOUNT_FIELDS),
    "culture_health_per_person":(_build_culture_per_person_rows,  CULTURE_PP_FIELDS),
    "culture_health_societal":  (_build_culture_societal_rows,    CULTURE_SOC_FIELDS),
    "workplace_wellbeing":      (_build_workplace_wellbeing_rows, WORKPLACE_FIELDS),
}
```

---

## 7. Orchestrator Flow

```
extract_uk_values.py:

  parse args (--only KEY | --list | default: all)

  if --list:
    print available keys → exit

  keys = [only_key] or list(_BUILDERS.keys())

  for key in keys:
    t0 = time.time()
    result = pipeline.run_table(key)
    n_rows = row_count(result)
    elapsed = time.time() - t0
    print(f"  [OK]  {key:35s} {n_rows:4d} rows  {elapsed:.2f}s")

  write execution_log_{datetime}.txt
```

---

## 8. Discount Rate Representation

The STPR schedule is represented as period-based rows:

| rate_type | period_start_yr | period_end_yr | rate_pct |
|-----------|----------------|---------------|----------|
| STPR standard | 1 | 30 | 3.50 |
| STPR standard | 31 | 75 | 3.00 |
| STPR standard | 76 | ∞ | 2.50 |
| Health/wellbeing | 0 | 30 | 1.50 |
| ... | | | |

This format is directly usable for computing discount factors over any horizon.
