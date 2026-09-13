import pandas as pd

customers_df = pd.read_csv("data/raw/customers.csv")
expenses_df = pd.read_csv("data/raw/expenses.csv")
invoices_df = pd.read_csv("data/raw/invoices.csv")
jobs_df = pd.read_csv("data/raw/jobs.csv")
targets_df = pd.read_csv("data/raw/targets.csv")

datasets = {
    "customers": customers_df,
    "expenses": expenses_df,
    "invoices": invoices_df,
    "jobs": jobs_df,
    "targets": targets_df,
}

def validate_key(df, key_column, label):
    key_values = df[key_column]

    missing_count = key_values.isna().sum()
    duplicate_count = key_values.duplicated().sum()

    print(f"\n{label}")
    print(f"Missing {key_column}s:", missing_count)
    print(f"Duplicate {key_column}s:", duplicate_count)

    if missing_count > 0:
        missing_rows = df[key_values.isna()]
        print(f"\nRows with missing {key_column}:")
        print(missing_rows)

    if duplicate_count > 0:
        duplicate_rows = df[key_values.duplicated(keep=False)]
        print(f"\nRows with duplicate {key_column}:")
        print(duplicate_rows)

for name, df in datasets.items():
    print(f"\n{name}")
    print("shape:", df.shape)
    print("Columns:", list(df.columns))

validate_key(customers_df, "CustomerID", "Customer Validation")
validate_key(expenses_df, "ExpenseID", "Expense Validation")
validate_key(invoices_df, "InvoiceID", "Invoice Validation")
validate_key(jobs_df, "JobID", "Job Validation")

duplicate_targets = targets_df.duplicated(
    subset=["Month", "Region"]
).sum()

print("\nTarget Validation")
print("Duplicate Month + Region combinations:", duplicate_targets)

if duplicate_targets > 0:
    duplicate_target_rows = targets_df[
        targets_df.duplicated(
            subset=["Month", "Region"],
            keep=False
        )
    ]

print("\nDuplicate target rows:")
print(duplicate_target_rows)