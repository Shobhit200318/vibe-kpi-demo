import sqlite3
import pandas as pd
import os

# Paths
CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'customers_raw.csv')
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'db', 'analytics.db')

# Create database directory if it doesn't exist
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Load CSV into DataFrame
df = pd.read_csv(CSV_PATH)

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Drop table if exists to ensure clean schema
cursor.execute('DROP TABLE IF EXISTS customers_raw')

# Create table
cursor.execute('''
    CREATE TABLE customers_raw (
        customer_id INTEGER,
        city TEXT,
        monthly_spend REAL,
        churned INTEGER
    )
''')

# Insert data from CSV
df.to_sql('customers_raw', conn, if_exists='append', index=False)

# Commit and close
conn.commit()
conn.close()

print(f"ETL complete: Loaded {len(df)} rows from {CSV_PATH} into {DB_PATH}")
