
import pandas as pd
from pathlib import Path

# Load the Superstore dataset
file_path = Path("data/raw/Superstore.csv")

print("Loading sales dataset...")


df = pd.read_csv(file_path, encoding="cp1252")

print("\nDATASET LOADED SUCCESSFULLY!")
print("-" * 40)

# Dataset size
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Display first five records
print("\nFirst five rows:")
print(df.head())

# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check duplicate records
print("\nNumber of duplicate rows:", df.duplicated().sum())


# ==========================================
# BUSINESS SALES PERFORMANCE ANALYSIS
# ==========================================

print("\n" + "=" * 45)
print("BUSINESS SALES PERFORMANCE ANALYSIS")
print("=" * 45)

# Convert order dates into datetime format
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

# Calculate key business KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Unique Orders: {total_orders:,}")
print(f"Unique Customers: {total_customers:,}")
print(f"Units Sold: {total_quantity:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

# Sales and profit by category
print("\n--- CATEGORY PERFORMANCE ---")

category_summary = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)

print(category_summary.round(2))

# Sales and profit by region
print("\n--- REGIONAL PERFORMANCE ---")

region_summary = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Sales", ascending=False)

print(region_summary.round(2))

# Monthly sales trend
df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("YearMonth", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

print("\n--- FIRST 12 MONTHLY RESULTS ---")
print(monthly_sales.head(12).round(2))

# Export analysis results for Power BI
output_folder = Path("data/cleaned")
output_folder.mkdir(parents=True, exist_ok=True)

df.to_csv(
    output_folder / "sales_cleaned.csv",
    index=False,
    encoding="utf-8-sig"
)

category_summary.to_csv(
    output_folder / "category_summary.csv",
    encoding="utf-8-sig"
)

region_summary.to_csv(
    output_folder / "region_summary.csv",
    encoding="utf-8-sig"
)

monthly_sales.to_csv(
    output_folder / "monthly_sales.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nAnalysis completed successfully!")
print("Cleaned data and summaries saved in data/cleaned/")


# TASK 1: Sub-category Profitability Analysis

from pathlib import Path

print("\n" + "=" * 50)
print("SUB-CATEGORY PROFITABILITY ANALYSIS")
print("=" * 50)

# Calculate total sales and profit for each sub-category
subcategory_profit = (
    df.groupby("Sub-Category", as_index=False)
      .agg(
          Total_Sales=("Sales", "sum"),
          Total_Profit=("Profit", "sum")
      )
      .sort_values("Total_Profit")
)

# Display the five lowest-profit sub-categories
print("\n5 LOWEST-PROFIT SUB-CATEGORIES:")
print(subcategory_profit.head(5).to_string(index=False))

# Display the five highest-profit sub-categories
print("\n5 HIGHEST-PROFIT SUB-CATEGORIES:")
print(
    subcategory_profit.tail(5)
    .sort_values("Total_Profit", ascending=False)
    .to_string(index=False)
)

# Save the results inside the reports folder
output_folder = Path("reports")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "subcategory_profit.csv"
subcategory_profit.to_csv(output_file, index=False)

print(f"\nAnalysis saved successfully: {output_file}")
