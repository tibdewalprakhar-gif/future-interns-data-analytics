# Findings and Recommendations — Customer Retention and Churn Analysis

## Executive summary

This project analyzes customer retention and churn using a dataset of 7,043 telecom customers. The overall churn rate is 26.54%, with 1,869 customers having discontinued the service. Month-to-month contract customers and customers with shorter tenure show notably higher churn rates. Fiber optic customers also have a higher churn rate than the other internet service groups. These findings can help the business prioritize customer retention efforts and investigate potential causes of churn.

## Key metrics

- **Metric 1 — Total customers:** 7,043
- **Metric 2 — Overall churn rate:** 26.54% (1,869 churned customers)
- **Metric 3 — Customer retention:** 73.46% (5,174 retained customers)
- **Metric 4 — Average monthly charges:** $64.76

## Findings supported by the data

1. **Contract type:** Month-to-month customers have a churn rate of 42.71%, compared with 11.27% for one-year contracts and 2.83% for two-year contracts.
2. **Internet service:** Fiber optic customers have the highest churn rate at 41.89%, compared with 18.96% for DSL customers and 7.40% for customers without internet service.
3. **Customer tenure:** Customers with 0–12 months of tenure have a churn rate of 47.44%. This rate declines to 9.51% among customers with 49–72 months of tenure.

## Recommendations

1. **Improve onboarding and early customer engagement.**
   - **Evidence:** Customers with 0–12 months of tenure have the highest churn rate at 47.44%.
   - **Expected business benefit:** Better early support and engagement may improve customer satisfaction and reduce early-stage churn.

2. **Develop retention strategies for month-to-month customers.**
   - **Evidence:** Month-to-month customers have a churn rate of 42.71%, compared with 2.83% for two-year contract customers.
   - **Expected business benefit:** Relevant loyalty benefits and suitable longer-contract offers may encourage customers to stay longer.

3. **Investigate churn among fiber optic customers.**
   - **Evidence:** The fiber optic customer group has a churn rate of 41.89%.
   - **Expected business benefit:** Investigating customer feedback, pricing, and service experiences may identify opportunities to improve retention.

## Limitations

- **Dataset coverage:** The analysis uses 7,043 customer records from the supplied telecom churn dataset. The dataset may not represent all customers, locations, or time periods.
- **Data quality issues:** The initial missing-value check reported zero missing values across the 21 columns. `TotalCharges` was converted to numeric using error coercion; any values that could not be converted should be checked separately.
- **Other caveats:** The analysis identifies associations, not causes of churn. The supplied dataset does not establish why customers left or whether the recommendations will reduce churn. The results describe this dataset and should be validated against current business data.

## Tools and methods

- **Python:** Used Pandas for data loading, inspection, churn-rate calculations, customer grouping, and CSV exports. Matplotlib was used to generate charts.
- **Power BI:** Used to build KPI cards and visualizations for overall churn, contract type, internet service, and customer tenure.
- **DAX:** Used to calculate the churn-rate measure and group customer tenure for dashboard analysis.
