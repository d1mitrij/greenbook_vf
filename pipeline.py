"""
UK wellbeing and health value factors — extraction pipeline.

All 5 table groups are hard-coded from verified source documents.
Produces CSV (UTF-8, tidy/long format) and formatted Excel (.xlsx) outputs.

Usage:
    from pipeline import run_table, run_all
    run_table("wellby_valuations")
    run_all()
"""

import csv
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

import config


# ---------------------------------------------------------------------------
# Table 1: WELLBY and QALY unit valuations
# Source: HM Treasury Wellbeing Guidance (July 2021); OECD (2025)
# Price year: GBP 2019 unless noted
# ---------------------------------------------------------------------------

# Core unit values
# Columns: value_factor, variant, value, unit, price_year, derivation_method, source
_WELLBY_CORE = [
    ("WELLBY", "low",     10000,  "GBP/WELLBY", "2019",
     "QALY-based: £70,158 QALY ÷ 7 points life satisfaction",
     "HM Treasury Wellbeing Guidance (2021)"),
    ("WELLBY", "central", 13000,  "GBP/WELLBY", "2019",
     "Midpoint of low (£10,000) and high (£16,000) estimates",
     "HM Treasury Wellbeing Guidance (2021)"),
    ("WELLBY", "high",    16000,  "GBP/WELLBY", "2019",
     "Income-based: £30,673 avg earnings ÷ 1.96 log income coefficient",
     "HM Treasury Wellbeing Guidance (2021)"),
    ("QALY_GreenBook", "central", 70000, "GBP/QALY", "2019",
     "HM Treasury welfare appraisal standard; primary for SCBA/appraisal",
     "HM Treasury Green Book 2026 / Wellbeing Guidance (2021)"),
    ("QALY_GreenBook_2014prices", "central", 60000, "GBP/QALY", "2014",
     "2014 price level reference; uprate to 2019: £70,158",
     "HM Treasury Wellbeing Guidance (2021)"),
    ("QALY_HTA", "low",    20000, "GBP/QALY", "2019",
     "NICE Health Technology Assessment lower threshold",
     "NICE / Frontier Economics (2024)"),
    ("QALY_HTA", "high",   30000, "GBP/QALY", "2019",
     "NICE Health Technology Assessment upper threshold",
     "NICE / Frontier Economics (2024)"),
]

# Key parameters
# Columns: parameter, value, unit, source
_WELLBY_PARAMS = [
    ("marginal_utility_income_elasticity", 1.3,  "dimensionless",
     "HM Treasury Green Book Annex 3; used in WELLBY uprating formula"),
    ("log_income_coefficient_0to10",       1.96, "per 0-10 scale",
     "Fujiwara (2021); derived from 1.25 on 1-7 scale"),
    ("average_earnings_uk_2019",           30673, "GBP/year",
     "UK average earnings 2019; basis for WELLBY high estimate"),
    ("life_satisfaction_points_per_QALY",  7.0,  "points (0-10 scale)",
     "Frijters & Krekel (2021); one QALY ≈ 7-point LS change (8→1)"),
]

# Illustrative wellbeing event valuations from case studies
# Columns: event, value, unit, price_year, notes, source
_WELLBY_EVENTS = [
    ("Internal water flooding (per property)",  42172,  "GBP/property", "2019",
     "LS impact: -0.273, 3 months duration",
     "HM Treasury Wellbeing Guidance (2021) — flooding case study"),
    ("Internal sewer flooding (per property)",  145220, "GBP/property", "2019",
     "LS impact: -0.508, 6 months duration",
     "HM Treasury Wellbeing Guidance (2021) — flooding case study"),
    ("External sewer flooding (per property)",  16375,  "GBP/property", "2019",
     "LS impact: -0.041",
     "HM Treasury Wellbeing Guidance (2021) — flooding case study"),
    ("Wellbeing programme 1 (8 weeks, cost per WELLBY)",  3158, "GBP/WELLBY", "2019",
     "Programme cost £2,000; LS change 0.63/year",
     "HM Treasury Wellbeing Guidance (2021) — employment programme case study"),
    ("Wellbeing programme 2 (12 weeks, cost per WELLBY)", 1000, "GBP/WELLBY", "2019",
     "Programme cost £550; LS change 0.55/year",
     "HM Treasury Wellbeing Guidance (2021) — employment programme case study"),
    ("Loneliness intervention (1-point LS reduction per person)", 13500, "GBP/person", "2019",
     "Monetised using £13,500 per 1-point life satisfaction change (≈ £13,000 WELLBY)",
     "HM Treasury Wellbeing Guidance (2021) — loneliness case study"),
    ("Youth skills training benefit (annual, per person, 40% completion)", 5200, "GBP/person/year", "2019",
     "Range £4,000–£6,400; 10,000 beneficiaries total £20.8m",
     "HM Treasury Wellbeing Guidance (2021) — skills training case study"),
    ("Employment support individual annual benefit", 31074, "GBP/person/year", "2019",
     "£25,094 wage premium + £5,980 wellbeing impact; 200 people: £6.21m/year",
     "HM Treasury Wellbeing Guidance (2021) — employment support case study"),
]


def _build_wellby_valuations_rows() -> list[dict]:
    rows = []
    # Core unit values
    for vf, variant, value, unit, py, method, source in _WELLBY_CORE:
        rows.append({
            "source_doc": source,
            "category": "unit_value",
            "value_factor": vf,
            "variant": variant,
            "value": value,
            "unit": unit,
            "price_year": py,
            "derivation_method": method,
            "notes": "",
        })
    # Parameters
    for param, value, unit, notes in _WELLBY_PARAMS:
        rows.append({
            "source_doc": "HM Treasury Wellbeing Guidance (2021)",
            "category": "parameter",
            "value_factor": param,
            "variant": "central",
            "value": value,
            "unit": unit,
            "price_year": "N/A",
            "derivation_method": "",
            "notes": notes,
        })
    # Event valuations
    for event, value, unit, py, notes, source in _WELLBY_EVENTS:
        rows.append({
            "source_doc": source,
            "category": "event_valuation",
            "value_factor": event,
            "variant": "central",
            "value": value,
            "unit": unit,
            "price_year": py,
            "derivation_method": "WELLBY × £13,000",
            "notes": notes,
        })
    return rows


# ---------------------------------------------------------------------------
# Table 2: Discount rates
# Source: HM Treasury Green Book 2026, Wellbeing Guidance 2021
# ---------------------------------------------------------------------------

# Columns: rate_type, period_description, years_from, years_to, rate_pct, notes, source
_DISCOUNT_RATES = [
    ("STPR_standard",          "Years 1–30",    1,    30,   3.50,
     "Social Time Preference Rate for standard public sector appraisal",
     "HM Treasury Green Book 2026 Annex 6"),
    ("STPR_standard",          "Years 31–75",   31,   75,   3.00,
     "Declining schedule for long-term appraisal",
     "HM Treasury Green Book 2026 Annex 6"),
    ("STPR_standard",          "Year 76+",      76,   999,  2.50,
     "Very long-term declining schedule",
     "HM Treasury Green Book 2026 Annex 6"),
    ("STPR_health_wellbeing",  "Years 0–30",    0,    30,   1.50,
     "Lower rate for QALYs, WELLBYs, life years — preserves intergenerational equity",
     "HM Treasury Green Book 2026 / Wellbeing Guidance 2021"),
    ("STPR_health_wellbeing",  "Years 31–75",   31,   75,   1.29,
     "Declining health discount rate (approx.)",
     "HM Treasury Wellbeing Guidance 2021"),
    ("STPR_health_wellbeing",  "Year 76+",      76,   999,  1.07,
     "Declining health discount rate (approx.)",
     "HM Treasury Wellbeing Guidance 2021"),
    ("private_sector_nominal", "All years",     0,    999,  7.00,
     "Nominal rate used in Workplace Wellbeing Tool (private sector reference)",
     "HM Treasury / PHE Workplace Wellbeing Tool (2011)"),
    ("public_sector_real",     "All years",     0,    999,  3.50,
     "Real rate mentioned in Workplace Wellbeing Tool for public sector",
     "HM Treasury / PHE Workplace Wellbeing Tool (2011)"),
]


def _build_discount_rates_rows() -> list[dict]:
    rows = []
    for rate_type, period, yr_from, yr_to, rate, notes, source in _DISCOUNT_RATES:
        rows.append({
            "source_doc": source,
            "rate_type": rate_type,
            "period_description": period,
            "years_from": yr_from,
            "years_to": yr_to if yr_to != 999 else "open",
            "rate_pct": rate,
            "unit": "percent_real_unless_noted",
            "notes": notes,
        })
    return rows


# ---------------------------------------------------------------------------
# Table 3: Culture health — per person (Frontier Economics / DCMS, 2024)
# Price year: GBP 2024
# Columns: model_id, model_name, engagement_type, health_outcome, age_group,
#          valuation_method, individual_impacts, nhs_social_care, productivity, total,
#          unit, price_year, notes
# ---------------------------------------------------------------------------

_CULTURE_PER_PERSON = [
    # (model_id, model_name, engagement_type, health_outcome, age_group,
    #  val_method, individual, nhs, productivity, total, notes)
    ("1",   "General engagement and general health",
     "Museum, gallery, heritage, cinema, theatre, concert",
     "General health", "30–49", "QALY (Green Book)",
     854,  0,   138, 992,
     ""),
    ("2a",  "General attendance and mental health",
     "General cultural attendance",
     "Mental health functioning", "30–49", "QALY (Green Book)",
     559,  0,   91,  649,
     ""),
    ("2b",  "General participation and mental health",
     "Arts & culture participation",
     "Mental health functioning", "30–49", "QALY (Green Book)",
     386,  0,   63,  448,
     ""),
    ("3",   "Extracurricular activities and externalising behaviour",
     "Dance, music, art, performing arts classes",
     "Emotional regulation / ADHD", "10–14", "QALY (Green Book)",
     122,  0,   0,   122,
     "Productivity not modelled for children"),
    ("4a",  "Art and self-esteem in children",
     "Drawing, painting, making things",
     "Mental health functioning", "10–14", "WELLBY",
     134,  0,   0,   134,
     "WELLBY-based; not directly comparable to QALY models. Productivity not modelled for children"),
    ("4b",  "Music and self-esteem in children",
     "Music listening / playing",
     "Mental health functioning", "10–14", "WELLBY",
     68,   0,   0,   68,
     "WELLBY-based; not directly comparable to QALY models. Productivity not modelled for children"),
    ("5a",  "Weekly organised arts and mental health",
     "Art, music, theatre activities (participatory or attendance), once/week",
     "Mental health functioning", "18–29", "WELLBY",
     663,  0,   86,  748,
     "WELLBY-based; not directly comparable to QALY models"),
    ("5b",  "Daily organised arts and mental health",
     "Art, music, theatre activities, almost daily",
     "Mental health functioning", "18–29", "WELLBY",
     1098, 0,   142, 1240,
     "WELLBY-based; not directly comparable to QALY models"),
    ("6",   "Arts-based museum activities and general health",
     "Arts activity at museum, weekly × 12 weeks",
     "General health", "65+", "QALY (Green Book)",
     1164, 0,   146, 1310,
     ""),
    ("7",   "Choirs and general health",
     "Choir participation, weekly × 14 weeks",
     "General health", "65+", "QALY (Green Book)",
     481,  0,   71,  553,
     ""),
    ("8",   "Cultural venues and depression",
     "Theatre, concert, cinema, gallery, museum, every few months+",
     "Depression incidence", "50+", "QALY (Green Book)",
     232,  26,  56,  314,
     "NHS/social care savings modelled via avoided depression treatment"),
    ("9",   "Cultural venues and dementia",
     "Theatre, concert, gallery, museum, every few months+",
     "Dementia incidence", "50+", "QALY (Green Book)",
     66,   75,  7,   148,
     "NHS/social care savings modelled via avoided dementia treatment"),
    ("10",  "Museums and dementia",
     "Museums, galleries, exhibitions, every few months+",
     "Dementia incidence", "50+", "QALY (Green Book)",
     159,  189, 21,  369,
     "NHS/social care savings modelled via avoided dementia treatment"),
    ("11a", "Visual art therapy — breast cancer",
     "Visual art therapy in clinical setting (drawing, painting, bookmaking, mindfulness)",
     "Quality of life", "18+ (cancer patients)", "WELLBY / QoL",
     1200, 0,   0,   1200,
     "Green Book valuation. HTA valuation: £730/person/year. Clinical intervention, 5–12 weeks"),
    ("11b", "Visual art therapy — all other cancers",
     "Visual art therapy in clinical setting",
     "Quality of life", "18+ (cancer patients)", "WELLBY / QoL",
     1600, 0,   0,   1600,
     "Green Book valuation. HTA valuation: £450/person/year. Clinical intervention, 5–12 weeks"),
]


def _build_culture_health_per_person_rows() -> list[dict]:
    rows = []
    for (mid, name, eng, outcome, age, val_method,
         individual, nhs, productivity, total, notes) in _CULTURE_PER_PERSON:
        rows.append({
            "source_doc": "Frontier Economics / DCMS: Health and Wellbeing Final Report (December 2024)",
            "model_id": mid,
            "model_name": name,
            "engagement_type": eng,
            "health_outcome": outcome,
            "age_group": age,
            "valuation_method": val_method,
            "individual_impacts": individual,
            "nhs_social_care_savings": nhs,
            "productivity_impacts": productivity,
            "total_per_person": total,
            "unit": "GBP_2024/person/year",
            "price_year": "2024",
            "notes": notes,
        })
    return rows


# ---------------------------------------------------------------------------
# Table 4: Culture health — society-wide (Frontier Economics / DCMS, 2024)
# Columns: model_id, model_name, age_group, total_per_person, engagers, society_wide_total
# ---------------------------------------------------------------------------

_CULTURE_SOCIETAL = [
    ("1",   "General engagement and general health",       "30–49", 992,  8103000,  8040000000),
    ("2a",  "General attendance and mental health",        "30–49", 649,  3201000,  2080000000),
    ("2b",  "General participation and mental health",     "30–49", 448,  9855000,  4420000000),
    ("3",   "Extracurricular activities",                  "10–14", 122,  1911000,   230000000),
    ("4a",  "Art and self-esteem in children",             "10–14", 134,   911000,   120000000),
    ("4b",  "Music and self-esteem in children",           "10–14",  68,  2380000,   160000000),
    ("5a",  "Weekly organised arts and mental health",     "18–29", 748,  1074000,   800000000),
    ("5b",  "Daily organised arts and mental health",      "18–29", 1240,  586000,   730000000),
    ("6",   "Arts-based museum activities",                "65+",   1310,   14000,    20000000),
    ("7",   "Choirs and general health",                   "65+",    553,  307000,   170000000),
    ("8",   "Cultural venues and depression",              "50+",    314, 9646000,  3030000000),
    ("9",   "Cultural venues and dementia",                "50+",    148, 5018000,   740000000),
    ("10",  "Museums and dementia",                        "50+",    369, 4077000,  1500000000),
]


def _build_culture_health_societal_rows() -> list[dict]:
    rows = []
    for mid, name, age, per_person, engagers, society_wide in _CULTURE_SOCIETAL:
        rows.append({
            "source_doc": "Frontier Economics / DCMS: Health and Wellbeing Final Report (December 2024)",
            "model_id": mid,
            "model_name": name,
            "age_group": age,
            "total_per_person_GBP2024": per_person,
            "estimated_engagers": engagers,
            "society_wide_total_GBP2024": society_wide,
            "unit_per_person": "GBP_2024/person/year",
            "unit_societal": "GBP_2024/year",
            "price_year": "2024",
            "notes": "Society-wide totals not additive across models (different populations/methods)",
        })
    return rows


# ---------------------------------------------------------------------------
# Table 5: Workplace wellbeing parameters (Workplace Wellbeing Tool, 2011)
# ---------------------------------------------------------------------------

# Columns: parameter_category, parameter, value, unit, price_year, notes, source
_WORKPLACE_PARAMS = [
    # Standard working parameters
    ("working_time", "standard_working_days_per_year", 228, "days/year", "2011",
     "5 days/week × 52 weeks − 32 days leave (UK standard)",
     "Workplace Wellbeing Tool Guide"),
    ("working_time", "standard_working_weeks_per_year", 52, "weeks/year", "2011",
     "Standard UK full-time assumption",
     "Workplace Wellbeing Tool Guide"),
    ("costs_structure", "non_wage_cost_factor",  1.30, "ratio", "2011",
     "Non-wage costs ≈ 30% above gross wages (e.g. NI, pension, benefits)",
     "Workplace Wellbeing Tool Guide"),
    ("costs_structure", "example_average_wage",  25000, "GBP/year", "2011",
     "Example value; update to current average earnings for current appraisals",
     "Workplace Wellbeing Tool Example sheet 1c"),
    # Discount rates
    ("discount_rate", "private_sector_nominal", 7.0, "percent_nominal", "2011",
     "Default in tool for private sector business case appraisal",
     "Workplace Wellbeing Tool Guide"),
    ("discount_rate", "public_sector_real",     3.5, "percent_real", "2011",
     "HM Treasury Green Book rate mentioned as public sector alternative",
     "Workplace Wellbeing Tool Guide"),
    # Example cost benchmarks from tool examples
    ("cost_benchmark", "labour_turnover_cost_per_departure", 12500, "GBP/departure", "2011",
     "Example cost per employee turnover event (recruitment, onboarding, lost productivity)",
     "Workplace Wellbeing Tool Example sheet 1c"),
    ("cost_benchmark", "accident_claim_average_cost",  200, "GBP/claim", "2011",
     "Example average cost per accident/injury insurance claim",
     "Workplace Wellbeing Tool Example sheet 1c"),
    # Investment appraisal example results
    ("appraisal_example", "net_present_value_5yr",     13175.80, "GBP", "2011",
     "Example 5-year NPV from sickness absence management project (10 employees)",
     "Workplace Wellbeing Tool Example sheet 2c"),
    ("appraisal_example", "benefit_to_cost_ratio",     3.85, "ratio", "2011",
     "BCR = discounted benefits ÷ discounted costs for example project",
     "Workplace Wellbeing Tool Example sheet 2c"),
    ("appraisal_example", "payback_period",            0.77, "years", "2011",
     "Approx. 9 months payback for example sickness absence management project",
     "Workplace Wellbeing Tool Example sheet 2c"),
    ("appraisal_example", "internal_rate_of_return",   139.26, "percent", "2011",
     "IRR for example project",
     "Workplace Wellbeing Tool Example sheet 2c"),
    # Cost category definitions (dimensionless flags/descriptions)
    ("cost_category", "sickness_absence", 1, "category", "2011",
     "Working days lost to employee absence due to sickness or ill health",
     "Workplace Wellbeing Tool Guide"),
    ("cost_category", "presenteeism", 1, "category", "2011",
     "Lost output when employees are at work but functioning below full capacity",
     "Workplace Wellbeing Tool Guide"),
    ("cost_category", "labour_turnover", 1, "category", "2011",
     "Employee departures and associated recruitment/onboarding costs",
     "Workplace Wellbeing Tool Guide"),
    ("cost_category", "accidents_injuries", 1, "category", "2011",
     "Workplace accidents, injuries and associated insurance/legal costs",
     "Workplace Wellbeing Tool Guide"),
    ("cost_category", "other_costs", 1, "category", "2011",
     "Customisable: ill-health retirement, private health insurance, grievances, etc.",
     "Workplace Wellbeing Tool Guide"),
]


def _build_workplace_wellbeing_rows() -> list[dict]:
    rows = []
    for (cat, param, value, unit, py, notes, source) in _WORKPLACE_PARAMS:
        rows.append({
            "source_doc": source,
            "parameter_category": cat,
            "parameter": param,
            "value": value,
            "unit": unit,
            "price_year": py,
            "notes": notes,
        })
    return rows


# ---------------------------------------------------------------------------
# Dispatch table
# ---------------------------------------------------------------------------

_BUILDERS = {
    "wellby_valuations": (
        _build_wellby_valuations_rows,
        ["source_doc", "category", "value_factor", "variant", "value",
         "unit", "price_year", "derivation_method", "notes"],
    ),
    "discount_rates": (
        _build_discount_rates_rows,
        ["source_doc", "rate_type", "period_description", "years_from", "years_to",
         "rate_pct", "unit", "notes"],
    ),
    "culture_health_per_person": (
        _build_culture_health_per_person_rows,
        ["source_doc", "model_id", "model_name", "engagement_type", "health_outcome",
         "age_group", "valuation_method", "individual_impacts", "nhs_social_care_savings",
         "productivity_impacts", "total_per_person", "unit", "price_year", "notes"],
    ),
    "culture_health_societal": (
        _build_culture_health_societal_rows,
        ["source_doc", "model_id", "model_name", "age_group",
         "total_per_person_GBP2024", "estimated_engagers", "society_wide_total_GBP2024",
         "unit_per_person", "unit_societal", "price_year", "notes"],
    ),
    "workplace_wellbeing": (
        _build_workplace_wellbeing_rows,
        ["source_doc", "parameter_category", "parameter", "value",
         "unit", "price_year", "notes"],
    ),
}


# ---------------------------------------------------------------------------
# Excel writer
# ---------------------------------------------------------------------------
_HEADER_FILL = PatternFill(fill_type="solid", fgColor="1F3864")
_HEADER_FONT = Font(bold=True, color="FFFFFF")
_HEADER_ALIGN = Alignment(horizontal="center", vertical="center", wrap_text=True)


def _write_excel(key: str, rows: list[dict], fieldnames: list[str], out_path: Path) -> None:
    cfg = config.get_table_config(key)
    wb = openpyxl.Workbook()

    # Sheet 1: Value Factors
    ws = wb.active
    ws.title = "Value Factors"
    ws.append(fieldnames)
    for cell in ws[1]:
        cell.fill = _HEADER_FILL
        cell.font = _HEADER_FONT
        cell.alignment = _HEADER_ALIGN
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = "A2"
    for row in rows:
        ws.append([row.get(f, "") for f in fieldnames])
    for col in ws.columns:
        max_len = max((len(str(cell.value or "")) for cell in col), default=8)
        ws.column_dimensions[col[0].column_letter].width = min(max_len + 2, 60)

    # Sheet 2: Metadata
    ms = wb.create_sheet("Metadata")
    meta_rows = [
        ("Field", "Value"),
        ("Table group", cfg["title"]),
        ("Source", cfg.get("source", "")),
        ("Source table/section", cfg["source_table"]),
        ("Chapter/Section", cfg["chapter"]),
        ("Unit", cfg["unit"]),
        ("Description", cfg["description"]),
        ("Notes", cfg["notes"]),
        ("", ""),
        ("Key publications", ""),
        ("HM Treasury Green Book", "2026"),
        ("HM Treasury Wellbeing Guidance", "July 2021"),
        ("OECD WELLBY document", "2025 (ref: 60c1396c-en)"),
        ("Frontier Economics / DCMS", "Health and Wellbeing Final Report, December 2024"),
        ("Workplace Wellbeing Tool", "HM Treasury / PHE, December 2011"),
        ("", ""),
        ("Pipeline author", "Dimitrij Euler (Greenings) — dimitrij.euler@greenings.org"),
        ("Pipeline support", "Claude Code (Anthropic)"),
    ]
    for r in meta_rows:
        ms.append(r)
    for cell in ms[1]:
        cell.fill = _HEADER_FILL
        cell.font = _HEADER_FONT
    ms.column_dimensions["A"].width = 28
    ms.column_dimensions["B"].width = 80

    wb.save(out_path)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def run_table(key: str) -> Path:
    if key not in _BUILDERS:
        raise KeyError(f"Unknown table group '{key}'. Available: {list(_BUILDERS)}")
    builder, fieldnames = _BUILDERS[key]
    rows = builder()

    csv_path = config.get_output_path(key)
    excel_path = config.get_excel_path(key)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _write_excel(key, rows, fieldnames, excel_path)
    return csv_path


def run_all() -> dict[str, Path]:
    return {key: run_table(key) for key in _BUILDERS}
