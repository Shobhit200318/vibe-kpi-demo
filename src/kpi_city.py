ALLOWED_CITIES = {"Mumbai", "Delhi", "Pune"}

def city_kpi(city: str):

    if city not in ALLOWED_CITIES:
        raise ValueError("City not allowed")

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