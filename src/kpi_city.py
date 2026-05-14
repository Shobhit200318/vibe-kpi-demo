import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'db', 'analytics.db')
ALLOWED_CITIES = {"Mumbai", "Delhi", "Pune", "Bangalore"}

def city_kpi(city: str):
    """Calculate KPIs for a given city using parameterized SQL to prevent injection."""
    if city not in ALLOWED_CITIES:
        raise ValueError(f"City '{city}' not allowed. Allowed cities: {ALLOWED_CITIES}")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

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

    cursor.execute(sql, (city,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print(f"City: {result[0]}, Customers: {result[1]}, Avg Spend: {result[2]}, Churn Rate: {result[3]}")
        return result
    else:
        print(f"No data found for city: {city}")
        return None

if __name__ == "__main__":
    print("=== Normal Query ===")
    city_kpi("Mumbai")

    print("\n=== SQL Injection Attempt (should fail or return no data) ===")
    city_kpi("Mumbai' OR 1=1 --")