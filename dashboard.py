import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mozomaza0909#$',
    database='store'
)

customers_df = pd.read_sql("SELECT * FROM customers", conn)
products_df = pd.read_sql("SELECT * FROM products", conn)
orders_df = pd.read_sql("SELECT * FROM orders", conn)

conn.close()

sales_df = orders_df.merge(customers_df, on='customer_id').merge(products_df, on='product_id')

sales_df['Total_price'] = sales_df['quantity'] * sales_df['price']

Total_sales = sales_df['Total_price'].sum()
Total_customers = sales_df['customer_id'].nunique()
Total_orders = sales_df['order_id'].nunique()
avg_order_value = sales_df['Total_price'].mean()

print("Total Sales:", Total_sales)
print("Total Customers:", Total_customers)
print("Total Orders:", Total_orders)
print("Average Order Value:", avg_order_value)


product_sales = sales_df.groupby('product_name')['quantity'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x='product_name', y='quantity', data=product_sales)
plt.title('Sales by Product')
plt.savefig("images/sales_by_product.png")
plt.show()

sales_by_country = sales_df.groupby('country')['quantity'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=sales_by_country, x='country', y='quantity')
plt.title('Sales by Country')
plt.savefig("images/sales_by_Country.png")
plt.show()
sales_df['order_date']=pd.to_datetime(sales_df['order_date'])
monthly_sales=sales_df.groupby(sales_df['order_date'].dt.to_period('M'))['quantity'].sum()
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line',marker='o',color='purple')
plt.title('Mothly sales')
plt.grid(True)
plt.savefig("images/Monthly_Sales.png")
plt.show()
revenue_by_product=sales_df.groupby('product_name')['Total_price'].sum().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(data=revenue_by_product,x='product_name',y='Total_price',palette='magma')
plt.title('Revenue by Product')
plt.savefig("images/Revenue_by_Product.png")
plt.show()
revenue_by_country=sales_df.groupby('country')['Total_price'].sum().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(data=revenue_by_country,x='country',y='Total_price',palette='coolwarm')
plt.title('Revenue by Country')
plt.savefig("images/Revenue_by_Country.png")
plt.show()
Top_customers=sales_df.groupby('name')['Total_price'].sum().reset_index().sort_values(by='Total_price',ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(data=Top_customers,x='name',y='Total_price',palette='viridis')
plt.title('Top Customers')
plt.savefig("images/Top_Customers.png")
plt.show()