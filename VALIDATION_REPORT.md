# Validation Report — vf_uk

**Pipeline author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## Known-Good Reference Values

### Table 01 — WELLBY and QALY Valuations (GBP 2019)

| Value factor | Variant | Value | Verified against |
|-------------|---------|-------|-----------------|
| WELLBY | low | £10,000 | Wellbeing Guidance Table 1; OECD 60c1396c-en |
| WELLBY | central | £13,000 | Wellbeing Guidance Table 1; OECD 60c1396c-en |
| WELLBY | high | £16,000 | Wellbeing Guidance Table 1; OECD 60c1396c-en |
| QALY Green Book | central | £70,000 | Wellbeing Guidance §3; Frontier report Table 1 |
| QALY Green Book 2014 | central | £60,000 | Wellbeing Guidance §3 (noted as base) |
| QALY HTA | low | £20,000 | Frontier report Table 1; NICE standard |
| Log income coefficient (0-10) | central | 1.96 | Wellbeing Guidance §4; Fujiwara (2021) |
| Marginal utility of income elasticity | central | 1.3 | Green Book Annex 3 |
| Flooding — internal water | central | £42,172 | Wellbeing Guidance flooding case study |
| Flooding — internal sewer | central | £145,220 | Wellbeing Guidance flooding case study |
| Flooding — external sewer | central | £16,375 | Wellbeing Guidance flooding case study |

### Table 02 — Discount Rates

| Rate type | Period | Rate | Verified against |
|-----------|--------|------|-----------------|
| STPR standard | Years 1–30 | 3.50% | Green Book 2026 Annex 6 |
| STPR standard | Years 31–75 | 3.00% | Green Book 2026 Annex 6 |
| STPR standard | Year 76+ | 2.50% | Green Book 2026 Annex 6 |
| Health/wellbeing | Years 0–30 | 1.50% | Wellbeing Guidance §5; Green Book 2026 |

### Table 03 — Culture Health Per Person (GBP 2024)

| Model | Total (central) | Verified against |
|-------|----------------|-----------------|
| 1 — General engagement (30–49) | £992 | Frontier Table 3 and Table 12 |
| 2a — General attendance (30–49) | £649 | Frontier Table 3 and Table 12 |
| 6 — Arts museum activities (65+) | £1,310 | Frontier Table 3 and Table 12 |
| 8 — Cultural venues & depression (50+) | £314 | Frontier Table 3 and Table 12 |
| 10 — Museums & dementia (50+) | £369 | Frontier Table 3 and Table 12 |
| 11a — Visual art therapy, breast cancer | £1,200 | Frontier visual art therapy section |
| 11b — Visual art therapy, other cancers | £1,600 | Frontier visual art therapy section |

### Table 04 — Culture Health Societal (GBP 2024)

| Model | Engagers | Society-wide total | Verified against |
|-------|----------|--------------------|-----------------|
| 1 — General engagement (30–49) | 8,103,000 | £8.04 billion | Frontier Table 12 |
| 8 — Cultural venues & depression (50+) | 9,646,000 | £3.03 billion | Frontier Table 12 |
| 10 — Museums & dementia (50+) | 4,077,000 | £1.50 billion | Frontier Table 12 |

### Table 05 — Workplace Wellbeing (GBP 2011)

| Parameter | Value | Verified against |
|-----------|-------|-----------------|
| Standard working days/year | 228 | Tool Guide; Example sheet 1c |
| Non-wage cost factor | 1.30 | Tool Guide |
| Labour turnover cost per departure | £12,500 | Example sheet 1c |
| NPV (5-year example) | £13,175.80 | Example sheet 2c |
| BCR (5-year example) | 3.85 | Example sheet 2c |

---

## Successful Extraction Log (Reference Run)

```
UK Wellbeing & Health Value Factors — extraction run
Started: 2026-03-07 18:28:41

  [OK]  01_wellby_valuations                19 rows  0.10s  -> 01_uk_wellby_valuations.csv
  [OK]  02_discount_rates                    8 rows  0.04s  -> 02_uk_discount_rates.csv
  [OK]  03_culture_health_per_person        15 rows  0.05s  -> 03_uk_culture_health_per_person.csv
  [OK]  04_culture_health_societal          13 rows  0.05s  -> 04_uk_culture_health_societal.csv
  [OK]  05_workplace_wellbeing              17 rows  0.05s  -> 05_uk_workplace_wellbeing.csv

Done. 5/5 groups extracted, 72 total rows, 0 failed.
```

---

## Known Limitations and Exclusions

| Item | Status | Reason |
|------|--------|--------|
| VPF (Value of Prevented Fatality) | Not included | Green Book references DfT TAG data book; not in source docs |
| VOLY (Value of Statistical Life Year) | Not included | Green Book references supplementary guidance; value not stated in sources |
| HTA Model 2 culture benefits | Not included | Only Green Book valuation extracted for main models |
| Full Levelling Up funding table | Not included | Policy investments, not unit value factors |
| Country-specific values (Scotland, Wales, NI) | Not included | Sources provide England/UK averages |
| Sector-differentiated workplace costs | Not included | Tool provides sector-agnostic parameters only |
| Workplace tool post-2011 updates | Not applicable | Tool not updated since December 2011 |
