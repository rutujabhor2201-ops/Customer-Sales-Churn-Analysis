import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visualizations folder
os.makedirs("visualizations", exist_ok=True)


# ============================================================
# SALES ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("SALES ANALYSIS")
print("=" * 60)

# Load sales data
sales_data = pd.read_csv("data/sales_data.csv")

# Convert Date column to datetime
sales_data["Date"] = pd.to_datetime(sales_data["Date"])

# Basic sales metrics
total_sales = sales_data["Total_Sales"].sum()
average_sales = sales_data["Total_Sales"].mean()
total_quantity = sales_data["Quantity"].sum()
total_transactions = len(sales_data)

print("\nOverall Sales Metrics")
print("-" * 40)

print("Total Transactions:", total_transactions)
print("Total Quantity Sold:", total_quantity)
print("Total Sales:", total_sales)
print("Average Sales per Transaction:", round(average_sales, 2))


# ============================================================
# SALES BY PRODUCT
# ============================================================

product_sales = sales_data.groupby("Product")["Total_Sales"].sum().sort_values(
    ascending=False
)

print("\n")
print("Sales by Product")
print("-" * 40)
print(product_sales)

top_product = product_sales.idxmax()

print("\nTop Product:", top_product)
print("Top Product Sales:", product_sales.max())


# ============================================================
# QUANTITY BY PRODUCT
# ============================================================

product_quantity = sales_data.groupby("Product")["Quantity"].sum().sort_values(
    ascending=False
)

print("\n")
print("Quantity Sold by Product")
print("-" * 40)
print(product_quantity)


# ============================================================
# SALES BY REGION
# ============================================================

region_sales = sales_data.groupby("Region")["Total_Sales"].sum().sort_values(
    ascending=False
)

print("\n")
print("Sales by Region")
print("-" * 40)
print(region_sales)

top_region = region_sales.idxmax()

print("\nTop Region:", top_region)
print("Top Region Sales:", region_sales.max())


# ============================================================
# QUANTITY BY REGION
# ============================================================

region_quantity = sales_data.groupby("Region")["Quantity"].sum().sort_values(
    ascending=False
)

print("\n")
print("Quantity Sold by Region")
print("-" * 40)
print(region_quantity)


# ============================================================
# HIGHEST SALES DATE
# ============================================================

daily_sales = sales_data.groupby("Date")["Total_Sales"].sum()

highest_sales_date = daily_sales.idxmax()
highest_daily_sales = daily_sales.max()

print("\n")
print("Highest Sales Date")
print("-" * 40)
print("Date:", highest_sales_date.strftime("%Y-%m-%d"))
print("Sales:", highest_daily_sales)


# ============================================================
# SALES VISUALIZATION 1 - SALES BY PRODUCT
# ============================================================

plt.figure(figsize=(9, 6))
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/sales_by_product.png")
plt.close()


# ============================================================
# SALES VISUALIZATION 2 - SALES BY REGION
# ============================================================

plt.figure(figsize=(9, 6))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/sales_by_region.png")
plt.close()


# ============================================================
# SALES VISUALIZATION 3 - QUANTITY BY PRODUCT
# ============================================================

plt.figure(figsize=(9, 6))
product_quantity.plot(kind="bar")

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/quantity_by_product.png")
plt.close()


# ============================================================
# SALES VISUALIZATION 4 - QUANTITY BY REGION
# ============================================================

plt.figure(figsize=(9, 6))
region_quantity.plot(kind="bar")

plt.title("Quantity Sold by Region")
plt.xlabel("Region")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/quantity_by_region.png")
plt.close()


# ============================================================
# SALES VISUALIZATION 5 - DAILY SALES TREND
# ============================================================

plt.figure(figsize=(12, 6))
daily_sales.plot(kind="line")

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/daily_sales_trend.png")
plt.close()


print("\nSales visualizations created successfully.")


# ============================================================
# CUSTOMER CHURN ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("CUSTOMER CHURN ANALYSIS")
print("=" * 60)

# Load churn data
churn_data = pd.read_csv("data/customer_churn.csv")


# ============================================================
# BASIC CHURN METRICS
# ============================================================

total_customers = len(churn_data)

churned_customers = (churn_data["Churn"] == 1).sum()
non_churned_customers = (churn_data["Churn"] == 0).sum()

churn_rate = (churned_customers / total_customers) * 100

print("\nOverall Customer Metrics")
print("-" * 40)

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Non-Churned Customers:", non_churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")


# ============================================================
# CHURN BY CONTRACT
# ============================================================

contract_churn = pd.crosstab(
    churn_data["Contract"],
    churn_data["Churn"],
    normalize="index"
) * 100

print("\n")
print("Churn Percentage by Contract")
print("-" * 40)
print(contract_churn)


# ============================================================
# CHURN BY PAYMENT METHOD
# ============================================================

payment_churn = pd.crosstab(
    churn_data["PaymentMethod"],
    churn_data["Churn"],
    normalize="index"
) * 100

print("\n")
print("Churn Percentage by Payment Method")
print("-" * 40)
print(payment_churn)


# ============================================================
# CHURN BY PAPERLESS BILLING
# ============================================================

paperless_churn = pd.crosstab(
    churn_data["PaperlessBilling"],
    churn_data["Churn"],
    normalize="index"
) * 100

print("\n")
print("Churn Percentage by Paperless Billing")
print("-" * 40)
print(paperless_churn)


# ============================================================
# CHURN BY SENIOR CITIZEN STATUS
# ============================================================

senior_churn = pd.crosstab(
    churn_data["SeniorCitizen"],
    churn_data["Churn"],
    normalize="index"
) * 100

print("\n")
print("Churn Percentage by Senior Citizen Status")
print("-" * 40)
print(senior_churn)


# ============================================================
# AVERAGE TENURE
# ============================================================

tenure_churn = churn_data.groupby("Churn")["Tenure"].mean()

print("\n")
print("Average Tenure")
print("-" * 40)

print(
    "Non-Churned Customers:",
    round(tenure_churn[0], 2),
    "months"
)

print(
    "Churned Customers:",
    round(tenure_churn[1], 2),
    "months"
)


# ============================================================
# AVERAGE MONTHLY CHARGES
# ============================================================

monthly_charges_churn = churn_data.groupby("Churn")["MonthlyCharges"].mean()

print("\n")
print("Average Monthly Charges")
print("-" * 40)

print(
    "Non-Churned Customers:",
    round(monthly_charges_churn[0], 2)
)

print(
    "Churned Customers:",
    round(monthly_charges_churn[1], 2)
)


# ============================================================
# AVERAGE TOTAL CHARGES
# ============================================================

total_charges_churn = churn_data.groupby("Churn")["TotalCharges"].mean()

print("\n")
print("Average Total Charges")
print("-" * 40)

print(
    "Non-Churned Customers:",
    round(total_charges_churn[0], 2)
)

print(
    "Churned Customers:",
    round(total_charges_churn[1], 2)
)


# ============================================================
# CHURN DISTRIBUTION GRAPH
# ============================================================

churn_counts = churn_data["Churn"].value_counts()

plt.figure(figsize=(8, 6))
churn_counts.plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/churn_distribution.png")
plt.close()


# ============================================================
# CHURN BY CONTRACT GRAPH
# ============================================================

contract_rates = (
    churn_data.groupby("Contract")["Churn"]
    .mean() * 100
)

plt.figure(figsize=(9, 6))
contract_rates.plot(kind="bar")

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/churn_by_contract.png")
plt.close()


# ============================================================
# CHURN BY PAYMENT METHOD GRAPH
# ============================================================

payment_rates = (
    churn_data.groupby("PaymentMethod")["Churn"]
    .mean() * 100
)

plt.figure(figsize=(10, 6))
payment_rates.plot(kind="bar")

plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=25)
plt.tight_layout()

plt.savefig("visualizations/churn_by_payment_method.png")
plt.close()


# ============================================================
# CHURN BY TENURE
# ============================================================

tenure_groups = pd.cut(
    churn_data["Tenure"],
    bins=[0, 12, 24, 36, 48, 60, 72],
    labels=[
        "0-12 months",
        "13-24 months",
        "25-36 months",
        "37-48 months",
        "49-60 months",
        "61-72 months"
    ]
)

tenure_churn_rate = (
    churn_data.groupby(
        tenure_groups,
        observed=False
    )["Churn"].mean() * 100
)

print("\n")
print("Churn Rate by Tenure Group")
print("-" * 40)
print(tenure_churn_rate)

plt.figure(figsize=(10, 6))
tenure_churn_rate.plot(kind="bar")

plt.title("Churn Rate by Tenure Group")
plt.xlabel("Tenure")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("visualizations/churn_by_tenure.png")
plt.close()


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n")
print("=" * 60)
print("COMPLETE SALES AND CHURN ANALYSIS FINISHED")
print("=" * 60)

print("\nAll visualizations have been created successfully.")

print("\nSales Visualizations:")
print("1. sales_by_product.png")
print("2. sales_by_region.png")
print("3. quantity_by_product.png")
print("4. quantity_by_region.png")
print("5. daily_sales_trend.png")

print("\nChurn Visualizations:")
print("6. churn_distribution.png")
print("7. churn_by_contract.png")
print("8. churn_by_payment_method.png")
print("9. churn_by_tenure.png")

print("\nProject analysis completed successfully!")