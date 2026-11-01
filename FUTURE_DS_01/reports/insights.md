# Task 1: Business Sales Performance Analytics

## 1. Project Overview

This project analyzes Superstore sales data to evaluate revenue, profitability, product category performance, regional performance, and monthly sales trends.

The objective is to identify business strengths, areas of low profitability, and opportunities for improvement using Python and Power BI.

## 2. Tools and Technologies

- Python
- Pandas
- Power BI Desktop
- CSV dataset
- Visual analytics and KPI reporting

## 3. Dataset Overview

- Total records: 9,994
- Total columns: 21
- Missing values detected: 0
- Duplicate rows detected: 0
- Unique orders: 5,009
- Unique customers: 793

## 4. Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Profit Margin | 12.47% |
| Unique Orders | 5,009 |
| Unique Customers | 793 |
| Units Sold | 37,873 |

## 5. Category Performance Analysis

### Technology
- Sales: $836,154.03
- Profit: $145,454.95
- Technology generated the highest sales and profit among the three categories.

### Furniture
- Sales: $741,999.80
- Profit: $18,451.27
- Furniture generated substantial sales but comparatively low profit.

### Office Supplies
- Sales: $719,047.03
- Profit: $122,490.80
- Office Supplies generated the second-highest profit despite having the lowest sales of the three categories.

## 6. Regional Performance Analysis

| Region | Sales | Profit |
|---|---:|---:|
| West | $725,457.82 | $108,418.45 |
| East | $678,781.24 | $91,522.78 |
| Central | $501,239.89 | $39,706.36 |
| South | $391,721.90 | $46,749.43 |

The West region generated the highest sales and profit. The Central region generated less profit than the other regions despite having higher sales than the South.

## 7. Sub-Category Profitability

### Lowest-profit sub-categories

| Sub-Category | Sales | Profit |
|---|---:|---:|
| Tables | $206,965.53 | -$17,725.48 |
| Bookcases | $114,880.00 | -$3,472.56 |
| Supplies | $46,673.54 | -$1,189.10 |

Tables recorded the largest loss among the analyzed sub-categories, followed by Bookcases and Supplies.

### Highest-profit sub-categories

| Sub-Category | Sales | Profit |
|---|---:|---:|
| Copiers | $149,528.03 | $55,617.82 |
| Phones | $330,007.05 | $44,515.73 |
| Accessories | $167,380.32 | $41,936.64 |
| Paper | $78,479.21 | $34,053.57 |
| Binders | $203,412.73 | $30,221.76 |

Copiers generated the highest profit among the listed sub-categories.

## 8. Monthly Sales Trends

Monthly sales and profit were calculated using order dates. The Power BI line chart displays changes in sales over time.

The data shows that sales fluctuate across months. Further investigation of seasonal patterns and year-over-year growth can help the business plan inventory and marketing activities.

## 9. Business Recommendations

1. **Review Tables pricing and discounts:** Investigate the causes of losses and evaluate whether pricing, discounting, or product costs need adjustment.
2. **Improve Furniture profitability:** Review product-level margins, shipping costs, and discount practices before increasing sales in this category.
3. **Learn from the West region:** Investigate its product mix, customer demand, and sales practices to identify approaches that may work in other regions.
4. **Maintain strong-performing products:** Examine the factors behind Copiers, Phones, and Accessories profitability to identify opportunities for sustainable growth.
5. **Monitor performance regularly:** Track sales, profit, and profit margin through the Power BI dashboard.

These recommendations are based on observed results. Product-level costs, discount patterns, and other contributing factors should be investigated before making operational changes.

## 10. Conclusion

The analysis identified differences in category and regional profitability, as well as three sub-categories with negative total profit. Technology and the West region were the strongest performers in their respective comparisons, while Tables was the largest loss-making sub-category.

The Power BI dashboard provides an accessible view of key performance indicators and trends to support data-informed business decisions.

## 11. Deliverables

- Python analysis script: `sales_analysis.py`
- Cleaned dataset and summary files
- Sub-category profitability analysis: `reports/subcategory_profit.csv`
- Power BI dashboard: `reports/Sales_Performance_Dashboard.pbix`
- Business insights report: `reports/insights.md`