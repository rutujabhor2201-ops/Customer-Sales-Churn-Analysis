\# Customer Sales \& Churn Analysis Report



\## 1. Project Overview



This project analyzes customer sales and customer churn data using Python and Pandas. The objective is to understand sales performance, identify important sales trends, analyze customer churn patterns, and provide business recommendations based on the findings.



The project uses two datasets:



\* Sales transaction data

\* Customer churn data



Python libraries such as Pandas and Matplotlib were used for data analysis and visualization.



\---



\## 2. Project Objectives



The main objectives of this project are:



\* Analyze overall sales performance.

\* Identify the best-performing products.

\* Compare sales performance across regions.

\* Analyze product quantities sold.

\* Identify sales trends over time.

\* Calculate the overall customer churn rate.

\* Analyze churn based on contract type, payment method, tenure, paperless billing, and senior citizen status.

\* Identify important customer retention patterns.

\* Provide actionable business recommendations.



\---



\## 3. Data Sources



\### Sales Dataset



The sales dataset contains 100 sales transactions with the following columns:



\* Date

\* Product

\* Quantity

\* Price

\* Customer\_ID

\* Region

\* Total\_Sales



\### Customer Churn Dataset



The customer churn dataset contains 500 customer records with the following columns:



\* CustomerID

\* Tenure

\* MonthlyCharges

\* TotalCharges

\* Contract

\* PaymentMethod

\* PaperlessBilling

\* SeniorCitizen

\* Churn



\---



\## 4. Data Inspection and Cleaning



Both datasets were inspected before analysis.



\### Sales Dataset



\* Total records: 100

\* Total columns: 7

\* Missing values: 0

\* Duplicate records: 0



\### Customer Churn Dataset



\* Total records: 500

\* Total columns: 9

\* Missing values: 0

\* Duplicate records: 0



No major data-cleaning issues were found.



The `Date` column in the sales dataset was converted into datetime format to support time-based analysis.



\---



\# 5. Sales Analysis



\## 5.1 Overall Sales Performance



The major sales metrics are:



| Metric                        |      Value |

| ----------------------------- | ---------: |

| Total Transactions            |        100 |

| Total Quantity Sold           |        478 |

| Total Sales                   | 12,365,048 |

| Average Sales per Transaction | 123,650.48 |



The dataset generated total sales of \*\*12,365,048\*\* across 100 transactions.



\---



\## 5.2 Sales by Product



The product-wise sales performance is:



| Product    | Total Sales |

| ---------- | ----------: |

| Laptop     |   3,889,210 |

| Tablet     |   2,884,340 |

| Phone      |   2,859,394 |

| Headphones |   1,384,033 |

| Monitor    |   1,348,071 |



\### Insight



\*\*Laptop\*\* is the best-performing product, generating total sales of \*\*3,889,210\*\*.



Tablets and phones are the next strongest-performing products.



Headphones and monitors generate comparatively lower sales.



\---



\## 5.3 Quantity Sold by Product



| Product    | Quantity Sold |

| ---------- | ------------: |

| Laptop     |           136 |

| Tablet     |           127 |

| Phone      |           101 |

| Monitor    |            66 |

| Headphones |            48 |



\### Insight



Laptops also have the highest quantity sold, with \*\*136 units\*\*.



This indicates that laptops are a strong product category in both sales value and quantity.



\---



\## 5.4 Sales by Region



| Region | Total Sales |

| ------ | ----------: |

| North  |   3,983,635 |

| South  |   3,737,852 |

| East   |   2,519,639 |

| West   |   2,123,922 |



\### Insight



The \*\*North region\*\* has the highest sales with \*\*3,983,635\*\*.



The South region is the second-highest-performing region.



The West region has the lowest sales and may require additional attention.



\---



\## 5.5 Quantity Sold by Region



| Region | Quantity Sold |

| ------ | ------------: |

| North  |           147 |

| South  |           143 |

| East   |            94 |

| West   |            94 |



The North region also has the highest quantity sold, with \*\*147 units\*\*.



\---



\## 5.6 Daily Sales Trend



The highest sales recorded on a single date were:



\* \*\*Date:\*\* 16 January 2024

\* \*\*Sales:\*\* 373,932



This date represents the highest daily sales value in the provided dataset.



\---



\# 6. Customer Churn Analysis



\## 6.1 Overall Churn



The customer churn dataset contains 500 customers.



| Metric                | Value |

| --------------------- | ----: |

| Total Customers       |   500 |

| Churned Customers     |    53 |

| Non-Churned Customers |   447 |

| Overall Churn Rate    | 10.6% |



The overall churn rate is \*\*10.6%\*\*.



\---



\## 6.2 Churn by Contract Type



| Contract Type  | Churn Rate |

| -------------- | ---------: |

| Month-to-month |     20.59% |

| One year       |      4.30% |

| Two year       |      6.94% |



\### Insight



Customers with \*\*month-to-month contracts have the highest churn rate at 20.59%\*\*.



Customers with longer-term contracts have substantially lower churn.



This suggests that encouraging customers to move from month-to-month contracts to longer-term plans could improve customer retention.



\---



\## 6.3 Churn by Payment Method



| Payment Method   | Churn Rate |

| ---------------- | ---------: |

| Bank Transfer    |      6.92% |

| Credit Card      |     13.48% |

| Electronic Check |     11.04% |



\### Insight



The highest churn rate in this dataset is observed among customers using \*\*credit card payments\*\*, at approximately \*\*13.48%\*\*.



Payment method should therefore be monitored as part of customer retention analysis.



\---



\## 6.4 Churn by Paperless Billing



| Paperless Billing | Churn Rate |

| ----------------- | ---------: |

| No                |     10.12% |

| Yes               |     11.11% |



\### Insight



The difference between the two groups is relatively small.



Therefore, paperless billing does not appear to be a major churn driver in this dataset.



\---



\## 6.5 Churn by Senior Citizen Status



| Senior Citizen Status | Churn Rate |

| --------------------- | ---------: |

| Non-Senior Citizen    |     11.16% |

| Senior Citizen        |     10.04% |



\### Insight



The churn rates are very similar between the two groups.



Therefore, senior citizen status does not appear to be a major factor influencing churn in this dataset.



\---



\## 6.6 Average Customer Tenure



| Customer Status | Average Tenure |

| --------------- | -------------: |

| Non-Churned     |   40.15 months |

| Churned         |    6.00 months |



\### Insight



Churned customers have a significantly lower average tenure than non-churned customers.



This indicates that \*\*customer retention during the early stage of the customer lifecycle is particularly important\*\*.



\---



\## 6.7 Average Monthly Charges



| Customer Status | Average Monthly Charges |

| --------------- | ----------------------: |

| Non-Churned     |                  111.72 |

| Churned         |                  129.77 |



\### Insight



Churned customers have higher average monthly charges than non-churned customers.



This suggests that customers with higher monthly costs may require additional attention, suitable pricing plans, or personalized offers.



\---



\## 6.8 Average Total Charges



| Customer Status | Average Total Charges |

| --------------- | --------------------: |

| Non-Churned     |              4,234.58 |

| Churned         |              4,265.75 |



The average total charges are relatively similar between churned and non-churned customers.



\---



\## 6.9 Churn by Tenure Group



| Tenure Group | Churn Rate |

| ------------ | ---------: |

| 0–12 months  |     63.10% |

| 13–24 months |         0% |

| 25–36 months |         0% |

| 37–48 months |         0% |

| 49–60 months |         0% |

| 61–72 months |         0% |



\### Insight



In the provided dataset, churn is heavily concentrated among customers with \*\*0–12 months of tenure\*\*.



This is a dataset-specific observation and suggests that the first year of the customer relationship is a critical period for retention.



\---



\# 7. Key Business Insights



The major findings from the analysis are:



1\. \*\*Laptops are the strongest-performing product\*\*, generating 3,889,210 in sales.

2\. \*\*The North region has the highest sales\*\*, with 3,983,635.

3\. Total sales across the dataset are \*\*12,365,048\*\*.

4\. The overall customer churn rate is \*\*10.6%\*\*.

5\. \*\*Month-to-month customers have considerably higher churn\*\* than customers on longer contracts.

6\. Churned customers have a much lower average tenure than non-churned customers.

7\. Customers with higher average monthly charges show higher churn in the provided data.

8\. Churn is strongly concentrated in the \*\*0–12 month tenure group\*\*.

9\. Paperless billing and senior citizen status show relatively small differences in churn rates.

10\. The North and South regions contribute the largest share of sales.



\---



\# 8. Business Recommendations



\## 8.1 Promote High-Performing Products



The company should continue promoting laptops because they generate the highest sales and quantity sold.



Cross-selling laptops with accessories such as headphones or monitors may also increase revenue.



\## 8.2 Improve Performance in Lower-Sales Regions



The West region has the lowest sales.



The company could investigate customer preferences, product availability, pricing, and marketing effectiveness in this region.



\## 8.3 Encourage Longer-Term Contracts



Since month-to-month customers have the highest churn rate, the company should provide incentives for customers to choose one-year or two-year contracts.



Possible strategies include:



\* Discounts for annual plans

\* Loyalty benefits

\* Contract upgrade offers

\* Special offers for long-term customers



\## 8.4 Focus on New Customers



The provided dataset shows that churn is heavily concentrated among customers with 0–12 months of tenure.



The company should strengthen early customer engagement through:



\* Welcome programs

\* Onboarding support

\* Early feedback collection

\* Personalized offers

\* Customer service follow-ups



\## 8.5 Monitor High Monthly Charges



Customers with higher monthly charges show higher churn in the provided dataset.



The company could introduce:



\* Customized plans

\* Discounts

\* Flexible packages

\* Value-added services



to improve customer satisfaction.



\## 8.6 Develop Customer Retention Programs



The company should identify customers who show potential churn risk and provide targeted retention campaigns.



These may include personalized discounts, loyalty rewards, customer support, and contract upgrade incentives.



\---



\# 9. Visualizations



The project includes the following visualizations:



\### Sales Visualizations



\* `sales\_by\_product.png`

\* `sales\_by\_region.png`

\* `quantity\_by\_product.png`

\* `quantity\_by\_region.png`

\* `daily\_sales\_trend.png`



\### Customer Churn Visualizations



\* `churn\_distribution.png`

\* `churn\_by\_contract.png`

\* `churn\_by\_payment\_method.png`

\* `churn\_by\_tenure.png`



These visualizations make it easier to understand sales performance and customer churn patterns.



\---



\# 10. Conclusion



The analysis provides useful insights into both sales performance and customer retention.



The sales analysis shows that \*\*laptops are the leading product\*\* and the \*\*North region is the strongest-performing region\*\*.



The churn analysis shows that \*\*month-to-month customers and newer customers are important groups for retention efforts\*\*. Churned customers also have considerably lower average tenure and higher average monthly charges.



Overall, the business can improve performance by focusing on high-performing products, strengthening lower-performing regions, encouraging longer-term contracts, and implementing stronger retention strategies during the early stages of the customer relationship.



The combination of sales analysis and churn analysis provides a data-driven approach for improving revenue and customer retention.



