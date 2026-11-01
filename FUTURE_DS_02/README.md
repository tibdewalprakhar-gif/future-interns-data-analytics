# Customer Retention & Churn Analysis

## Project Overview

This project analyzes customer churn patterns to understand why customers discontinue a service and identify factors associated with customer retention.

The analysis was performed using Python for data cleaning and exploratory data analysis, and Power BI for creating an interactive dashboard.

## Project Objectives

- Analyze the overall customer churn rate.
- Compare churn across different contract types.
- Understand the relationship between customer tenure and churn.
- Analyze churn patterns across internet service categories.
- Identify customer groups with higher churn rates.
- Present findings and recommendations through a Power BI dashboard.

## Tools and Technologies

- **Python** – Data analysis and processing
- **Pandas** – Data cleaning and manipulation
- **Matplotlib** – Data visualization
- **Power BI** – Interactive dashboard
- **DAX** – Measures and calculated columns

## Dataset

The project uses the Telco Customer Churn dataset.

- Total Records: 7,043 customers
- Total Columns: 21

Important dataset fields include:
- CustomerID
- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- Contract
- InternetService
- MonthlyCharges
- TotalCharges
- Churn

## Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Customers | 7,043 |
| Retained Customers | 5,174 |
| Churned Customers | 1,869 |
| Overall Churn Rate | 26.54% |
| Retention Rate | 73.46% |
| Average Monthly Charges | $64.76 |

## Key Findings

1. The overall customer churn rate is 26.54%.
2. Month-to-month contract customers have the highest churn rate at 42.71%.
3. Customers with two-year contracts have a much lower churn rate of 2.83%.
4. Fiber optic internet customers show a churn rate of 41.89%, compared with 18.96% for DSL customers.
5. Customers with 0–12 months of tenure have the highest churn rate at 47.44%.
6. Customers with 49–72 months of tenure have a lower churn rate of 9.51%.

## Project Structure

```text
FUTURE_DS_02/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   │
│   └── cleaned/
│       └── customer_churn_cleaned.csv
│
├── reports/
│   ├── charts/
│   │   ├── churn_distribution.png
│   │   ├── churn_by_contract.png
│   │   └── churn_by_tenure.png
│   │
│   ├── churn_by_contract.csv
│   ├── churn_by_internet.csv
│   ├── churn_by_tenure.csv
│   ├── Customer_Churn_Dashboard.pbix
│   └── insights.md
│
├── churn_analysis.py
└── README.md
```

## Business Recommendations

1. **Improve Early Customer Retention**
   - Evidence: Customers with 0–12 months of tenure have a churn rate of 47.44%.
   - Expected Benefit: Better onboarding and early engagement may help reduce customer losses.

2. **Encourage Long-Term Contracts**
   - Evidence: Month-to-month customers have a 42.71% churn rate, compared with 2.83% for two-year contracts.
   - Expected Benefit: Suitable long-term contract offers may improve customer retention.

3. **Investigate Fiber Optic Customer Experience**
   - Evidence: Fiber optic customers have a churn rate of 41.89%.
   - Expected Benefit: Understanding service-related issues may help improve customer satisfaction.

## How to Run

1. Clone or download this repository.
2. Install the required Python libraries:

   `pip install pandas matplotlib`

3. Run the analysis script:

   `python churn_analysis.py`

4. Open `Customer_Churn_Dashboard.pbix` using Power BI Desktop.

## Conclusion

This project provided practical experience in customer data analysis, data cleaning, churn measurement, exploratory data analysis, and dashboard development. The findings highlight the importance of customer tenure, contract type, and internet service category when studying customer churn patterns.
