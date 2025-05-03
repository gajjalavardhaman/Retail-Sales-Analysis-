
-- Total Sales by Region
SELECT Region, SUM(Total_Sales) AS TotalRevenue
FROM retail_sales
GROUP BY Region
ORDER BY TotalRevenue DESC;

-- Top 5 Selling Products
SELECT Product, SUM(Quantity) AS TotalUnits
FROM retail_sales
GROUP BY Product
ORDER BY TotalUnits DESC
LIMIT 5;

-- Monthly Revenue
SELECT strftime('%Y-%m', Date) AS Month, SUM(Total_Sales) AS Revenue
FROM retail_sales
GROUP BY Month
ORDER BY Month;

-- Sales by Category
SELECT Category, SUM(Total_Sales) AS TotalRevenue
FROM retail_sales
GROUP BY Category;
