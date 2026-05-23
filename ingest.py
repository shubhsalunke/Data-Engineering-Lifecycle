import pandas as pd
import mysql.connector

df = pd.read_csv("sales.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="deuser",
    password="depass123",
    database="data_lifecycle"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (id, customer, product, amount, sale_date)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row["id"],
        row["customer"],
        row["product"],
        row["amount"],
        row["date"]
    ))

conn.commit()

print("Data ingestion completed successfully")

cursor.close()
conn.close()
