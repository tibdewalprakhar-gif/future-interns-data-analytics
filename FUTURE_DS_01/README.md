# Business Sales Performance Analytics

## Project Overview
This project focuses on analyzing business sales data to understand sales performance, profitability, product categories, and regional trends. Python was used for data cleaning and analysis, while Power BI was used to build an interactive dashboard.

## Objectives
- Analyze overall sales and profit performance.
- Compare sales across product categories and regions.
- Identify profitable and loss-making subcategories.
- Understand monthly sales trends.
- Present key business insights through a Power BI dashboard.

## Tools and Technologies
- **Python** – Data analysis and processing
- **Pandas** – Data cleaning and manipulation
- **Matplotlib** – Data visualization
- **Power BI** – Interactive dashboard
- **DAX** – Measures and calculations

## Dataset
The project uses the Superstore sales dataset containing 9,994 records and 21 columns.

Key fields include:
- Order Date
- Sales
- Profit
- Quantity
- Category
- Sub-Category
- Region
- Customer Information

## Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Unique Customers | 793 |
| Units Sold | 37,873 |
| Profit Margin | 12.47% |

## Key Findings
1. Technology generated the highest sales, approximately $836,154.
2. Technology also recorded the highest category profit, approximately $145,455.
3. The West region recorded the highest sales, approximately $725,458.
4. Tables, Bookcases, and Supplies were identified as loss-making subcategories.
5. Copiers recorded the highest subcategory profit, approximately $55,618.

## Project Structure
```text
FUTURE_DS_01/
│
├── data/
│   ├── raw/
│   │   └── Superstore.csv
│   └── cleaned/
│       ├── category_summary.csv
│       ├── monthly_sales.csv
│       ├── region_summary.csv
│       └── sales_cleaned.csv
│
├── reports/
│   ├── Sales_Performance_Dashboard.pbix
│   ├── insights.md
│   └── subcategory_profit.csv
│
├── sales_analysis.py
└── README.md
```

## Business Recommendations
- Review pricing and discount strategies for loss-making subcategories.
- Continue monitoring Technology category performance.
- Study the sales strategies contributing to strong West region performance.
- Use monthly sales trends to support inventory and business planning.

## How to Run
1. Clone or download this repository.
2. Install the required Python libraries:
   `pip install pandas matplotlib`
3. Run the analysis script:
   `python sales_analysis.py`
4. Open the Power BI dashboard file using Power BI Desktop.

## Conclusion
This project provided practical experience in data cleaning, exploratory data analysis, business performance measurement, and dashboard development using Python and Power BI.
