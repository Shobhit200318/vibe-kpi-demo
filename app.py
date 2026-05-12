import sqlite3
import os

# Create folder if it doesn't exist
os.makedirs("data/db", exist_ok=True)

DB_PATH = "data/db/analytics.db"

# Create database + table + sample data
with sqlite3.connect(DB_PATH) as conn:

    conn.execute("""
    CREATE TABLE IF NOT EXISTS customers_raw (
        city TEXT,
        monthly_spend REAL,
        churned INTEGER
    )
    """)

    # Insert sample rows
    conn.execute("""
    INSERT INTO customers_raw (city, monthly_spend, churned)
    VALUES
    ('Mumbai', 1200, 0),
    ('Mumbai', 1500, 1),
    ('Delhi', 900, 0),
    ('Pune', 2000, 1)
    """)

    conn.commit()


# Safe KPI function
def city_kpi(city: str):

    sql = """
    SELECT
        city,
        COUNT(*) AS n_customers,
        ROUND(AVG(monthly_spend), 2) AS avg_spend,
        ROUND(AVG(churned), 4) AS churn_rate
    FROM customers_raw
    WHERE city = ?
    GROUP BY city;
    """

    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(sql, (city,)).fetchone()

    if row is None:
        return None

    return {
        "city": row[0],
        "n_customers": row[1],
        "avg_spend": row[2],
        "churn_rate": row[3],
    }


# Test
print(city_kpi("Mumbai"))
