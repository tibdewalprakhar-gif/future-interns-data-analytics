# FUTURE_DS_03 – Marketing Campaign Performance Analysis

## Project Overview

This project focuses on analyzing bank marketing campaign data to understand customer responses and identify factors associated with successful term-deposit subscriptions.

The analysis compares campaign outcomes across different job categories and contact methods. Python is used for data cleaning and analysis, while Power BI is used to create an interactive dashboard.

## Objective

- Analyze marketing campaign outcomes.
- Calculate the overall subscription rate.
- Compare subscription rates across job categories.
- Evaluate campaign performance by contact method.
- Identify patterns in customer responses.
- Provide data-based recommendations for improving campaign performance.

## Dataset

**Dataset:** UCI Bank Marketing Dataset (`bank-full.csv`)

The dataset contains information about bank marketing campaigns and whether customers subscribed to a term deposit.

**Dataset size:** 45,211 records and 17 columns.

**Important note:** This dataset represents marketing campaign contacts and subscription outcomes. It does not contain a complete digital marketing funnel such as website visitors, leads, and checkout conversions.

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Power BI Desktop
- Microsoft Excel / CSV
- GitHub

## Key Performance Metrics

| Metric | Result |
|---|---:|
| Total Campaign Records | 45,211 |
| Successful Subscriptions | 5,289 |
| Unsuccessful Outcomes | 39,922 |
| Overall Subscription Rate | 11.70% |

## Key Findings

### 1. Overall Campaign Performance

- 5,289 customers subscribed to a term deposit.
- 39,922 customers did not subscribe.
- The overall subscription rate was approximately 11.70%.

### 2. Performance by Contact Method

| Contact Method | Subscription Rate |
|---|---:|
| Cellular | 14.92% |
| Telephone | 13.42% |
| Unknown | 4.07% |

Cellular contact recorded the highest subscription rate among the listed contact methods.

### 3. Performance by Job Category

| Job Category | Subscription Rate |
|---|---:|
| Student | 28.68% |
| Retired | 22.79% |
| Unemployed | 15.50% |
| Management | 13.76% |
| Admin | 12.20% |
| Blue-collar | 7.27% |

Student and retired customer groups showed comparatively higher subscription rates in this dataset.

## Recommendations

1. Study the campaign approaches used for customer groups with higher subscription rates.
2. Review cellular and telephone contact strategies to understand their comparatively stronger performance.
3. Explore customer preferences and campaign timing to improve engagement.
4. Investigate reasons for lower subscription rates in certain job categories.
5. Track campaign outcomes regularly and use the findings to improve future marketing strategies.

These recommendations are based on observed patterns and do not establish that a particular contact method or job category causes higher subscriptions.

## Project Workflow

1. Load and inspect the original dataset.
2. Check data quality and clean the dataset.
3. Perform exploratory data analysis using Python.
4. Calculate subscription rates across customer segments.
5. Export cleaned data and summary reports.
6. Create visualizations using Matplotlib.
7. Develop an interactive Power BI dashboard.
8. Document findings and recommendations.

## Project Structure

```text
FUTURE_DS_03/
│
├── data/
│   ├── raw/
│   │   └── bank-full.csv
│   └── cleaned/
│       └── bank_marketing_cleaned.csv
│
├── reports/
│   ├── charts/
│   │   ├── conversion_by_contact.png
│   │   ├── conversion_by_job.png
│   │   └── subscription_outcomes.png
│   │
│   ├── conversion_by_contact_method.csv
│   ├── conversion_by_job.csv
│   ├── insights.md
│   └── Marketing_Campaign_Dashboard.pbix
│
├── marketing_analysis.py
└── README.md
```

## How to Run the Project

1. Clone or download this repository.
2. Install the required Python libraries:

```bash
pip install pandas matplotlib
```

3. Navigate to the project directory:

```bash
cd FUTURE_DS_03
```

4. Run the Python analysis:

```bash
python marketing_analysis.py
```

5. Open `Marketing_Campaign_Dashboard.pbix` using Power BI Desktop to explore the dashboard.

## Dashboard

The Power BI dashboard presents:

- Total campaign records
- Successful subscriptions
- Unsuccessful outcomes
- Overall subscription rate
- Subscription outcomes
- Performance by job category
- Performance by contact method

## Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning and preprocessing
- Exploratory data analysis
- Working with real-world datasets
- Calculating and comparing conversion rates
- Data visualization using Python
- Building dashboards in Power BI
- Communicating analytical findings and recommendations

## Conclusion

This project provided practical experience in analyzing marketing campaign data and understanding customer subscription patterns. It demonstrates how Python and Power BI can be used together to transform raw data into meaningful insights that support data-driven decision-making.

---

**Project:** Future Interns – Data Science & Analytics Internship  
**Task:** FUTURE_DS_03 – Marketing Campaign Performance Analysis
