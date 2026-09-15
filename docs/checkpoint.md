# Current Checkpoint

## Completed
- Raw CSV files loaded into Fabric Lakehouse
- Bronze source tables created
- Dataflow Gen2 created
- Power Query transformations completed
- Silver tables created:
  - silver_customers
  - silver_jobs
  - silver_invoices
  - silver_expenses
  - silver_targets
- Silver semantic model created
- Tables renamed:
  - DimCustomer
  - FactJobs
  - FactInvoices
  - FactExpenses
  - FactTargets
- Relationships created:
  - DimCustomer[CustomerID] 1:* FactJobs[CustomerID]
  - FactJobs[JobID] 1:* FactInvoices[JobID]
  - FactJobs[JobID] 1:* FactExpenses[JobID]
- Total Expenses measure created

## Next
- Create/verify Total Contract Value
- Create Total Invoiced
- Create Gross Margin $
- Create Job Count
- Build validation cards
- Begin dashboard

^X

