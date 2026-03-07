# Architecture Decision Records — UK Wellbeing & Health Value Factors

**Pipeline:** UK Wellbeing & Health Value Factor Extraction
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)
**Data sources:** HM Treasury / Wellbeing Guidance / OECD / Frontier Economics / Workplace Tool

---

## Index

| ADR | Title | Status |
|-----|-------|--------|
| ADR-001 | Hard-code all data in pipeline.py | Accepted |
| ADR-002 | Flat tidy CSV as primary output format | Accepted |
| ADR-003 | Five table groups matching publication structure | Accepted |
| ADR-004 | Excel output with Metadata sheet and formatted header | Accepted |
| ADR-005 | Single orchestrator with --only and --list flags | Accepted |
| ADR-006 | Thin wrapper scripts under tables/ | Accepted |
| ADR-007 | Sequential processing (no parallelism) | Accepted |
| ADR-008 | GBP price years retained as a data column | Accepted |
| ADR-009 | Timestamped execution log | Accepted |
| ADR-010 | Source PDFs converted to Markdown and stored in root | Accepted |

---

## ADR-001 — Hard-code all data in pipeline.py

**Status:** Accepted
**Date:** 2026-03-07

### Context

The five source publications are static, published documents. Values were
manually verified against source text before transcription.

### Decision

All value factors are hard-coded as Python data structures (`list`, `dict`)
in `pipeline.py`. Builder functions convert these to `list[dict]` for CSV/Excel output.

### Consequences

- Zero parsing errors: each value is verified once against the source document.
- Update procedure is manual; see `DATA_UPDATES.md`.
- Data and code are co-located in `pipeline.py` — a reader can see exactly where
  each value originates.

---

## ADR-002 — Flat tidy CSV as primary output format

**Status:** Accepted
**Date:** 2026-03-07

### Context

UK value factor data is a flat list of parameters — not a country × sector matrix.
No HDF5 or multi-dimensional structure is needed.

### Decision

CSV (UTF-8, comma-delimited, `csv.DictWriter`) is the primary output. One file per
table group, one row per unique combination of dimensions.

### Consequences

- Importable into any tool (Excel, R, Python, LibreOffice).
- No dependency on PyTables or HDF5 libraries.
- Human-readable without special tooling.

---

## ADR-003 — Five table groups matching publication structure

**Status:** Accepted
**Date:** 2026-03-07

### Context

The five source publications each provide a distinct, self-contained set of parameters.
Grouping by publication preserves the methodological coherence of each source.

### Decision

| Key | Source | Description |
|-----|--------|-------------|
| `wellby_valuations` | Wellbeing Guidance 2021; OECD 2025 | WELLBY/QALY unit values |
| `discount_rates` | Green Book 2026 | STPR schedules |
| `culture_health_per_person` | Frontier / DCMS 2024 | Per-person cultural benefits |
| `culture_health_societal` | Frontier / DCMS 2024 | Society-wide totals |
| `workplace_wellbeing` | Workplace Tool 2011 | Organisational parameters |

### Consequences

- Each CSV carries a clear, single-source scope.
- Tables 03 and 04 are from the same Frontier report but differ in unit (per-person vs. aggregate).

---

## ADR-004 — Excel output with Metadata sheet and formatted header

**Status:** Accepted
**Date:** 2026-03-07

### Decision

`pipeline._write_excel()` produces an `.xlsx` alongside each CSV:
- Sheet 1 `"Value Factors"`: data with frozen header row and formatted header fill.
- Sheet 2 `"Metadata"`: publication fields, description, unit, and source citation.

### Consequences

- Both `.csv` and `.xlsx` are written on every `run_table()` call.
- Source attribution is embedded in every standalone output file.

---

## ADR-005 — Single orchestrator with --only and --list flags

**Status:** Accepted
**Date:** 2026-03-07

### Decision

`extract_uk_values.py` is the unified CLI entry point. Arguments:
- `--only <key>`: extract one table group
- `--list`: print available keys

### Consequences

- Single point of entry for full or partial extraction.
- Individual `tables/NN_*.py` scripts remain available for isolated testing.

---

## ADR-006 — Thin wrapper scripts under tables/

**Status:** Accepted
**Date:** 2026-03-07

### Decision

`tables/NN_{key}.py` scripts are four-line wrappers calling `pipeline.run_table("{key}")`.
A `_template.py` is included for adding future table groups.

### Consequences

- `python tables/01_wellby_valuations.py` and `--only wellby_valuations` produce identical output.
- No code duplication: both paths call `pipeline.run_table()`.

---

## ADR-007 — Sequential processing (no parallelism)

**Status:** Accepted
**Date:** 2026-03-07

### Decision

`extract_uk_values.py` runs all table groups sequentially. Total extraction time
is under 0.5 s — parallelism provides no benefit.

### Consequences

- Simpler code; no race conditions.
- The public `run_table()` API is unchanged if parallelism is needed in future.

---

## ADR-008 — GBP price years retained as a data column

**Status:** Accepted
**Date:** 2026-03-07

### Context

The five source publications use different price years (GBP 2011, 2019, 2024).
Merging all into one price base would require inflation assumptions not specified
in the source documents.

### Decision

Each row retains the `currency` and `price_year` as explicit fields. No uprating
is applied by the pipeline. The uprating formula is documented in `METHODOLOGY.md`.

### Consequences

- Values are auditable against source documents without reverse-engineering deflation.
- Downstream users apply their own uprating as appropriate.

---

## ADR-009 — Timestamped execution log

**Status:** Accepted
**Date:** 2026-03-07

### Decision

`extract_uk_values.py` writes `execution_log_{YYYYMMDD_HHMMSS}.txt` to the
project root at the end of each run, recording which groups succeeded and how
many rows were produced.

### Consequences

- Audit trail of extraction runs.
- Log files are excluded from git via `.gitignore`.

---

## ADR-010 — Source PDFs converted to Markdown and stored in root

**Status:** Accepted
**Date:** 2026-03-07

### Decision

All five source PDFs are stored in the project root. Markdown conversions
(via pypdf text extraction) are stored alongside them for reference and QA.

### Consequences

- Readers can cross-check pipeline values against source text in any Markdown viewer.
- The pipeline itself reads only from `pipeline.py`; Markdown files are reference only.
