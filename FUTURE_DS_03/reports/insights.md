# Findings and Recommendations — Marketing Funnel and Conversion Performance Analysis

## Executive summary

This project analyzes 45,211 records from the UCI Bank Marketing dataset to evaluate marketing campaign conversion performance. Out of these records, 5,289 resulted in successful term-deposit subscriptions, giving an overall subscription rate of 11.70%. Students and retired customers showed the highest subscription rates among job categories, while cellular contacts performed better than telephone contacts. These findings can help guide customer segmentation and campaign optimization.

## Key metrics

- **Metric 1 — Total campaign contacts:** 45,211
- **Metric 2 — Successful subscriptions:** 5,289 (11.70%)
- **Metric 3 — Unsuccessful contacts:** 39,922 (88.30%)

## Findings supported by the data

1. **Overall conversion:** The subscription rate was 11.70%, with 5,289 successful subscriptions out of 45,211 campaign records.
2. **Job category:** Students had the highest subscription rate at 28.68%, followed by retired customers at 22.79%.
3. **Contact method:** Cellular contacts had a subscription rate of 14.92%, telephone contacts 13.42%, and records with an unknown contact method 4.07%.

## Recommendations

1. **Focus on customer segments with higher subscription rates.**
   - **Evidence:** Students had a 28.68% subscription rate and retired customers had a 22.79% rate.
   - **Expected business benefit:** Testing targeted campaign messages for these segments may improve subscription rates and make campaign efforts more effective.

2. **Review contact method effectiveness and data quality.**
   - **Evidence:** Cellular contacts achieved a 14.92% subscription rate, compared with 13.42% for telephone contacts and 4.07% for unknown contact methods.
   - **Expected business benefit:** Evaluating outreach performance and improving contact information quality may help improve campaign targeting and conversion outcomes.

## Limitations

- **Dataset coverage:** The dataset contains bank marketing contact records and term-deposit subscription outcomes. It does not represent a complete digital marketing funnel with website visits, leads, checkout stages, and purchases.
- **Data quality issues:** The initial analysis reported zero missing values across the 17 columns. However, some categorical values, such as `unknown`, are present and may limit interpretation.
- **Other caveats:** The results show associations, not proof that a particular job category or contact method causes higher conversion. Campaign costs and profitability were not included.

## Tools and methods

- **Python:** Pandas for data loading, cleaning, and conversion-rate analysis; Matplotlib for charts; CSV files for exporting summary reports.
- **Power BI:** KPI cards and charts for campaign outcomes, subscription rates by job category, and subscription rates by contact method. DAX measures were used to calculate total contacts, successful subscriptions, unsuccessful contacts, and subscription rate.