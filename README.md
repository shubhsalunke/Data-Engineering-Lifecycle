# Data Engineering Lifecycle Practical

# Project Overview

This practical demonstrates a complete mini **Data Engineering Lifecycle** workflow using:

* Python
* MySQL
* CSV Data Source
* SQL Transformation
* ETL Pipeline Concepts

The activity covers:

* Data Source Creation
* Data Ingestion
* Data Storage
* Data Transformation
* Reporting & Analytics

---

# Architecture Flow

```text
CSV File
↓
Python Ingestion Script
↓
MySQL Database
↓
SQL Transformation
↓
CSV Business Report
```

---

# Server Details

| Component   | Value                      |
| ----------- | -------------------------- |
| Server IP   | SERVER_IP                  |
| OS          | Ubuntu                     |
| Database    | MySQL 8                    |
| Language    | Python 3                   |
| Environment | Python Virtual Environment |

---

# Step 1 — Connect to Server

```bash
ssh azureuser@SERVER_IP
```

---

# Step 2 — Clone Repository

```bash
git clone https://github.com/shubhsalunke/Flask-PostgreSQL-Dockerfile.git
```

```bash
cd Data-Engineering-Lifecycle
```

---

# Step 3 — Install Required Packages

```bash
sudo apt update

sudo apt install mysql-server python3 python3-pip python3-venv -y
```

---

# Step 4 — Create Python Virtual Environment

```bash
python3 -m venv venv
```

---

# Step 5 — Activate Virtual Environment

```bash
source venv/bin/activate
```

Expected Output:

```bash
(venv) azureuser@server:~/Flask-PostgreSQL-Dockerfile$
```

---

# Step 6 — Install Python Libraries

```bash
pip install pandas mysql-connector-python
```

---

# Step 7 — Open MySQL

```bash
sudo mysql
```

---

# Step 8 — Create Database & Table

```sql
CREATE DATABASE data_lifecycle;

USE data_lifecycle;

CREATE TABLE sales (
  id INT PRIMARY KEY,
  customer VARCHAR(100),
  product VARCHAR(100),
  amount INT,
  sale_date DATE
);

SHOW TABLES;
```

Expected Output:

```text
sales
```

---

# Step 9 — Create MySQL User

```sql
CREATE USER 'deuser'@'localhost' IDENTIFIED BY 'depass123';

GRANT ALL PRIVILEGES ON data_lifecycle.* TO 'deuser'@'localhost';

FLUSH PRIVILEGES;

USE data_lifecycle;

TRUNCATE TABLE sales;

EXIT;
```

---

# Step 10 — Run Data Ingestion

```bash
python3 ingest.py
```

Expected Output:

```text
Data ingestion completed successfully
```

---

# Step 11 — Verify Stored Data

```bash
sudo mysql -e "USE data_lifecycle; SELECT * FROM sales;"
```

Expected Output:

```text
+----+----------+----------+--------+------------+
| id | customer | product  | amount | sale_date  |
+----+----------+----------+--------+------------+
|  1 | Rahul    | Laptop   |  55000 | 2026-05-01 |
|  2 | Amit     | Mouse    |    500 | 2026-05-01 |
|  3 | Neha     | Keyboard |   1200 | 2026-05-02 |
|  4 | Rahul    | Monitor  |   9000 | 2026-05-03 |
|  5 | Amit     | Laptop   |  56000 | 2026-05-03 |
+----+----------+----------+--------+------------+
```

---

# Step 12 — Run Transformation

```bash
python3 transform.py
```

Expected Output:

```text
  customer  total_sales
0    Rahul      64000.0
1     Amit      56500.0
2     Neha       1200.0
```

---

# Step 13 — Verify Final Report

```bash
cat customer_sales_report.csv
```

Expected Output:

```text
customer,total_sales
Rahul,64000.0
Amit,56500.0
Neha,1200.0
```

---

# Step 14 — Check All Project Files

```bash
ls
```

Expected Output:

```text
customer_sales_report.csv
ingest.py
sales.csv
transform.py
venv
```

---

# Lifecycle Components Covered

| Lifecycle Stage     | Practical Implementation  |
| ------------------- | ------------------------- |
| Data Source         | sales.csv                 |
| Data Ingestion      | ingest.py                 |
| Data Storage        | MySQL Database            |
| Data Processing     | SQL Queries               |
| Data Transformation | transform.py              |
| Data Serving        | customer_sales_report.csv |

---

# Real Skills Covered

Data Engineering Lifecycle
ETL Pipeline Basics
Python + MySQL Integration
SQL Aggregation
Data Transformation
CSV Processing
Business Reporting
Analytics Workflow
Virtual Environment Setup
Database Connectivity

---

# Real-World Use Cases

## Banking

* Transaction analytics
* Fraud detection

## E-Commerce

* Sales analytics
* Customer insights

## Healthcare

* Patient data processing

## DevOps & Monitoring

* Log processing
* Metrics aggregation

---

# Conclusion

This practical demonstrates a complete mini Data Engineering pipeline where raw CSV data is ingested into MySQL, transformed using SQL aggregation, and exported into a final business analytics report.

The project helps understand how real-world ETL and analytics workflows operate in modern Data Engineering systems.
