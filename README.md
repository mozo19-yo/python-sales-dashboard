📊 Sales Dashboard using Python + MySQL

This project is a complete Sales Dashboard built using:

- Python
- Pandas
- MySQL
- Matplotlib
- Seaborn

It includes:

- Data extraction from MySQL
- Data cleaning and merging
- KPI calculations
- Visualizations
- Revenue analysis
- Customer analysis

---

📁 Project Structure


project/
│── dashboard.ipynb
│── requirements.txt
│── README.md
│── images/
│     ├── salesbyproduct.png
│     ├── salesbycountry.png
│     ├── monthly_sales.png
│     ├── revenuebyproduct.png
│     ├── revenuebycountry.png
│     └── top_customers.png


---

🗄 Database Structure

customers
| customer_id | name | city | country |

products
| productid | productname | category | price |

orders
| orderid | customerid | productid | quantity | orderdate |

---

📌 KPIs

- Total Sales
- Total Customers
- Total Orders
- Average Order Value

---

📈 Visualizations

- Sales by Product
- Sales by Country
- Monthly Sales
- Revenue by Product
- Revenue by Country
- Top Customers

---

🚀 How to Run


pip install -r requirements.txt
then run the notebook