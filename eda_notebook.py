
# Retail Sales Data Cleaning and EDA

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_data.csv", parse_dates=["Date"])

# Preview data
print("First 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Data types
print("\nData types:")
print(df.dtypes)

# Basic stats
print("\nSummary statistics:")
print(df.describe())

# Add Month and Year columns for trend analysis
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Sales Trend by Month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
plt.figure(figsize=(10, 5))
monthly_sales.plot(marker='o', title='Monthly Sales Trend')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values()
region_sales.plot(kind='barh', title='Sales by Region', color='skyblue')
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

# Product Category Analysis
category_sales = df.groupby('Category')['Total_Sales'].sum()
category_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Category')
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()
