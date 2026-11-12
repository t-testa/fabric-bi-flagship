# Fabric BI Flagship

An operations-intelligence learning project covering customers, jobs, invoices, expenses and regional monthly targets in Microsoft Fabric and Power BI.

## Repository status

This repository contains five raw CSV datasets, a Python validation script and a [build checkpoint](docs/checkpoint.md). The checkpoint records work in Fabric: a Lakehouse, Bronze/Silver processing, a semantic model, a dashboard MVP and a refresh pipeline.

Those cloud assets are **not exported here**. This checkout alone cannot reproduce the Fabric pipeline or Power BI report, and the checkpoint is a progress record rather than an independently verified deployment result.

## What is included

| Path | Purpose |
|---|---|
| `data/raw/customers.csv` | Customer source data |
| `data/raw/jobs.csv` | Jobs and contract information |
| `data/raw/invoices.csv` | Invoice source data |
| `data/raw/expenses.csv` | Expense source data |
| `data/raw/targets.csv` | Monthly regional targets |
| `src/validate_raw_data.py` | Prints shapes, columns, missing/duplicate keys and duplicate target combinations |
| `docs/checkpoint.md` | Fabric and Power BI build progress |

## Local inspection

The validation script requires Python and pandas. From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas
python src/validate_raw_data.py
```

**Known script issue:** when there are no duplicate Month/Region target rows, `duplicate_target_rows` is never assigned before the final print, so the script can end with a `NameError`. Its printed diagnostics are not an automated pass/fail test suite.

## Next deliverables

- Export the semantic model, report and pipeline definitions so the build can be reviewed from Git.
- Reconcile dashboard totals against the source data and investigate blank Region/ProjectType categories.
- Add report screenshots and metric definitions.
- Consolidate the checkpoint's overlapping “Next” lists and fix the validator's no-duplicates branch.

The repository documents work in progress; it does not yet provide a complete deployable BI solution.
