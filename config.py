"""
Configuration for UK wellbeing and health value factors pipeline.

Sources:
  - HM Treasury: The Green Book (2026)
  - HM Treasury: Wellbeing Guidance for Appraisal — supplementary Green Book guidance (July 2021)
  - OECD: The WELLBY Well-being Valuation Method in the United Kingdom (2025)
  - Frontier Economics / DCMS: Health and Wellbeing Final Report (December 2024)
  - HM Treasury / Public Health England: Workplace Wellbeing Tool (2011)
"""

from pathlib import Path

_ROOT = Path(__file__).parent
_OUTPUT_DIR = _ROOT / "output"

TABLE_GROUPS = {
    "wellby_valuations": {
        "id": "01",
        "title": "WELLBY and QALY unit valuations",
        "source_table": "Wellbeing Guidance Tables 1–3; OECD 2025",
        "chapter": "HM Treasury Wellbeing Guidance §3–4",
        "description": (
            "Core monetary unit values for wellbeing and health appraisal in UK policy. "
            "Covers WELLBYs (Wellbeing-Adjusted Life Years), QALYs (Quality-Adjusted Life "
            "Years), key wellbeing parameters (income elasticity, log income coefficient), "
            "and illustrative monetised wellbeing impacts from case studies (flooding, "
            "employment programmes, loneliness). All values in GBP 2019 unless stated."
        ),
        "unit": "GBP_2019/unit",
        "source": "HM Treasury Wellbeing Guidance for Appraisal (July 2021); OECD (2025)",
        "notes": (
            "WELLBY central value is recommended for UK public policy appraisal. "
            "QALY Green Book value (£70,000) is for welfare appraisal; "
            "QALY HTA value (£20,000) is the NICE healthcare benchmark. "
            "Values must be uprated to current prices using GDP deflator × per-capita GDP growth^1.3."
        ),
    },
    "discount_rates": {
        "id": "02",
        "title": "Social Time Preference Rates and health discount rates",
        "source_table": "Green Book 2026 Annex 6; Wellbeing Guidance §5",
        "chapter": "HM Treasury Green Book 2026 Annex 6",
        "description": (
            "Social Time Preference Rates (STPR) for use in UK public sector appraisal, "
            "as set out in the Green Book 2026. Covers standard STPR declining schedule "
            "and the lower health/wellbeing discount rate applicable to impacts on human "
            "health, life years, and wellbeing (QALYs, WELLBYs)."
        ),
        "unit": "percent_real",
        "source": "HM Treasury Green Book 2026",
        "notes": (
            "Health/wellbeing impacts use a separate lower discount rate (1.5% for years 0–30) "
            "to preserve intergenerational equity in valuations of life and health. "
            "Private sector reference rate (7% nominal) from Workplace Wellbeing Tool (2011) "
            "is included for comparison."
        ),
    },
    "culture_health_per_person": {
        "id": "03",
        "title": "Per-person annual health and wellbeing benefits from cultural engagement",
        "source_table": "Frontier Economics Tables 3 and 12",
        "chapter": "Frontier Economics / DCMS (2024) §4–6",
        "description": (
            "Monetised per-person annual health and wellbeing benefits from cultural and "
            "heritage engagement, covering 13 model variants across four impact components: "
            "individual health gains (QALYs or WELLBYs), NHS/social care savings, and "
            "productivity impacts (paid + unpaid work). All values in GBP 2024. "
            "Models cover age groups 10–14, 18–29, 30–49, 50+, and 65+."
        ),
        "unit": "GBP_2024/person/year",
        "source": (
            "Frontier Economics / UK Department for Culture, Media and Sport (DCMS): "
            "Health and Wellbeing Final Report (December 2024)"
        ),
        "notes": (
            "Models marked WELLBY use WELLBYs × £13,000 (not directly comparable to "
            "QALY-based models). Models marked QALY use Green Book valuation £70,000/QALY "
            "or HTA valuation £20,000/QALY. NHS/social care savings modelled only for "
            "depression and dementia outcomes (Models 8–10). Productivity impacts not "
            "modelled for children (Models 3, 4a, 4b). Models are not additive."
        ),
    },
    "culture_health_societal": {
        "id": "04",
        "title": "Society-wide annual health and wellbeing benefits from cultural engagement",
        "source_table": "Frontier Economics Table 12",
        "chapter": "Frontier Economics / DCMS (2024) §7",
        "description": (
            "Estimated society-wide annual monetised health and wellbeing benefits from "
            "cultural engagement in England, derived by multiplying per-person benefits "
            "by estimated number of engagers. Values in GBP 2024."
        ),
        "unit": "GBP_2024/year",
        "source": (
            "Frontier Economics / UK Department for Culture, Media and Sport (DCMS): "
            "Health and Wellbeing Final Report (December 2024)"
        ),
        "notes": (
            "Society-wide totals are not additive across models (different populations, "
            "methodologies, and some overlap). Engager estimates from Taking Part Survey "
            "and English Longitudinal Study of Ageing."
        ),
    },
    "workplace_wellbeing": {
        "id": "05",
        "title": "Workplace wellbeing cost parameters and benchmarks",
        "source_table": "Workplace Wellbeing Tool sheets 1a, 2a, Guide",
        "chapter": "HM Treasury / PHE Workplace Wellbeing Tool (2011)",
        "description": (
            "Standard parameters and benchmarks for workplace health and wellbeing cost "
            "calculations, as embedded in the UK Workplace Wellbeing Tool. Covers five "
            "cost dimensions: sickness absence, presenteeism, labour turnover, "
            "accidents/injuries, and other wellbeing costs. Reference year 2011."
        ),
        "unit": "GBP_2011/unit or dimensionless",
        "source": "HM Treasury / Public Health England: Workplace Wellbeing Tool (2011)",
        "notes": (
            "Values reflect 2011 UK economic conditions. Wages should be updated to "
            "current prices. Discount rate of 3.5% (real) recommended for public sector "
            "appraisal per Green Book; 7% (nominal) is the private sector default in the tool."
        ),
    },
}

PUBLICATIONS = {
    "green_book": {
        "title": "The Green Book: Central Government Guidance on Appraisal and Evaluation",
        "edition": "2026",
        "publisher": "HM Treasury",
        "url": "https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government",
    },
    "wellbeing_guidance": {
        "title": "Wellbeing Guidance for Appraisal: supplementary Green Book guidance",
        "date": "July 2021",
        "publisher": "HM Treasury",
    },
    "oecd_wellby": {
        "title": "The WELLBY Well-being Valuation Method in the United Kingdom",
        "date": "2025",
        "publisher": "OECD",
        "reference": "60c1396c-en",
    },
    "frontier_dcms": {
        "title": "Health and Wellbeing Final Report",
        "date": "12 November 2024 (published December 2024)",
        "authors": "Frontier Economics",
        "commissioner": "UK Department for Culture, Media and Sport (DCMS)",
        "reference": "rpt_-_Frontier_Health_and_Wellbeing_Final_Report_09_12_24_accessible_final",
    },
    "workplace_tool": {
        "title": "Workplace Wellbeing Tool",
        "date": "December 2011",
        "authors": "Barry Griffiths",
        "publisher": "HM Treasury / Public Health England",
    },
}


def get_output_path(key: str) -> Path:
    _OUTPUT_DIR.mkdir(exist_ok=True)
    cfg = TABLE_GROUPS[key]
    return _OUTPUT_DIR / f"{cfg['id']}_uk_{key}.csv"


def get_excel_path(key: str) -> Path:
    _OUTPUT_DIR.mkdir(exist_ok=True)
    cfg = TABLE_GROUPS[key]
    return _OUTPUT_DIR / f"{cfg['id']}_uk_{key}.xlsx"


def get_table_config(key: str) -> dict:
    if key not in TABLE_GROUPS:
        raise KeyError(f"Unknown table group '{key}'. Available: {list(TABLE_GROUPS)}")
    return {**TABLE_GROUPS[key], "key": key}
