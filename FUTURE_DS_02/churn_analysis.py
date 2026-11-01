
import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from pathlib import Path

# Dataset location
file_path = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Load dataset
df = pd.read_csv(file_path)

# Basic dataset overview
print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nCHURN COUNTS")
print(df["Churn"].value_counts())

print("\nCHURN PERCENTAGE")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))


# -----------------------------
# CUSTOMER CHURN ANALYSIS
# -----------------------------

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Save cleaned dataset
from pathlib import Path

cleaned_folder = Path("data/cleaned")
cleaned_folder.mkdir(parents=True, exist_ok=True)

df.to_csv(
    cleaned_folder / "customer_churn_cleaned.csv",
    index=False
)

# Overall business metrics
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()
churn_rate = df["Churn"].eq("Yes").mean() * 100
avg_monthly_charges = df["MonthlyCharges"].mean()

print("\n--- BUSINESS METRICS ---")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Average Monthly Charges: ${avg_monthly_charges:.2f}")

# Churn by contract type
contract_churn = (
    df.groupby("Contract", observed=True)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
)

print("\n--- CHURN RATE BY CONTRACT (%) ---")
print(contract_churn)

# Churn by internet service
internet_churn = (
    df.groupby("InternetService", observed=True)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
)

print("\n--- CHURN RATE BY INTERNET SERVICE (%) ---")
print(internet_churn)

# Churn by tenure group
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 months", "13-24 months",
            "25-48 months", "49-72 months"]
)

tenure_churn = (
    df.groupby("TenureGroup", observed=True)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
)

print("\n--- CHURN RATE BY TENURE (%) ---")
print(tenure_churn)

# Save analysis summaries
reports_folder = Path("reports")
reports_folder.mkdir(parents=True, exist_ok=True)

contract_churn.to_csv(reports_folder / "churn_by_contract.csv")
internet_churn.to_csv(reports_folder / "churn_by_internet.csv")
tenure_churn.to_csv(reports_folder / "churn_by_tenure.csv")

print("\nAnalysis complete! CSV reports saved.")

import matplotlib.pyplot as plt

# Create chart output folder
chart_folder = Path("reports/charts")
chart_folder.mkdir(parents=True, exist_ok=True)

# Chart 1: Churn distribution
churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(7, 5))
churn_counts.plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(chart_folder / "churn_distribution.png", dpi=150)
plt.close()

# Chart 2: Churn by contract type
plt.figure(figsize=(8, 5))
contract_churn.sort_values().plot(kind="barh")
plt.title("Churn Rate by Contract Type")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Contract Type")
plt.tight_layout()
plt.savefig(chart_folder / "churn_by_contract.png", dpi=150)
plt.close()

# Chart 3: Churn by tenure group
plt.figure(figsize=(8, 5))
tenure_churn.plot(kind="bar")
plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(chart_folder / "churn_by_tenure.png", dpi=150)
plt.close()

print("Charts saved in reports/charts/")
