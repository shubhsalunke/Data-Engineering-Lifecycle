import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="deuser",
    password="depass123",
    database="data_lifecycle"
)

query = """
SELECT customer, SUM(amount) AS total_sales
FROM sales
GROUP BY customer
ORDER BY total_sales DESC;
"""

df = pd.read_sql(query, conn)
df.to_csv("customer_sales_report.csv", index=False)

print(df)
print("Report created: customer_sales_report.csv")

conn.close()
