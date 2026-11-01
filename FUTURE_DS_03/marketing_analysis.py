
import pandas as pd
from pathlib import Path

# Dataset path
file_path = Path("data/raw/bank-full.csv")

# Load the semicolon-separated dataset
df = pd.read_csv(file_path, sep=";")

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nMISSING VALUES")
print(df.isnull().sum())

# Campaign response counts
print("\nCAMPAIGN RESPONSE COUNTS")
print(df["y"].value_counts())

print("\nCAMPAIGN RESPONSE PERCENTAGE")
print(
    (df["y"].value_counts(normalize=True) * 100).round(2)
)

# Basic marketing performance
total_contacts = len(df)
subscriptions = (df["y"] == "yes").sum()
non_subscriptions = (df["y"] == "no").sum()
conversion_rate = (subscriptions / total_contacts) * 100

print("\n--- MARKETING PERFORMANCE ---")
print("Total Campaign Contacts:", total_contacts)
print("Successful Subscriptions:", subscriptions)
print("Unsuccessful Subscriptions:", non_subscriptions)
print(f"Subscription Rate: {conversion_rate:.2f}%")

# Conversion rate by contact channel and campaign outcome
conversion_by_job = (
    df.groupby("job")["y"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print("\n--- SUBSCRIPTION RATE BY JOB (%) ---")
print(conversion_by_job)

conversion_by_contact = (
    df.groupby("contact")["y"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .round(2)
)

print("\n--- SUBSCRIPTION RATE BY CONTACT METHOD (%) ---")
print(conversion_by_contact)

# Save cleaned data and reports
cleaned_folder = Path("data/cleaned")
reports_folder = Path("reports")

cleaned_folder.mkdir(parents=True, exist_ok=True)
reports_folder.mkdir(parents=True, exist_ok=True)

df.to_csv(
    cleaned_folder / "bank_marketing_cleaned.csv",
    index=False
)

conversion_by_job.to_csv(
    reports_folder / "conversion_by_job.csv"
)

conversion_by_contact.to_csv(
    reports_folder / "conversion_by_contact_method.csv"
)

print("\nAnalysis complete! CSV reports saved.")


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Save charts in reports/charts
chart_folder = Path("reports/charts")
chart_folder.mkdir(parents=True, exist_ok=True)

# Chart 1: Subscription outcomes
response_counts = df["y"].value_counts().reindex(
    ["yes", "no"], fill_value=0
)

plt.figure(figsize=(7, 5))
response_counts.plot(kind="bar")
plt.title("Marketing Campaign Subscription Outcomes")
plt.xlabel("Subscription Outcome")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(chart_folder / "subscription_outcomes.png", dpi=150)
plt.close()

# Chart 2: Subscription rate by job
plt.figure(figsize=(9, 6))
conversion_by_job.sort_values().plot(kind="barh")
plt.title("Subscription Rate by Job")
plt.xlabel("Subscription Rate (%)")
plt.ylabel("Job")
plt.tight_layout()
plt.savefig(chart_folder / "conversion_by_job.png", dpi=150)
plt.close()

# Chart 3: Subscription rate by contact method
plt.figure(figsize=(7, 5))
conversion_by_contact.sort_values().plot(kind="bar")
plt.title("Subscription Rate by Contact Method")
plt.xlabel("Contact Method")
plt.ylabel("Subscription Rate (%)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(chart_folder / "conversion_by_contact.png", dpi=150)
plt.close()

print("Charts saved in reports/charts/")
