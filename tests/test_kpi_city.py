import sqlite3
import os
import sys

# Add src to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from kpi_city import city_kpi, DB_PATH

def test_city_kpi_happy_path():
    """Test that city_kpi returns correct data for a valid city."""
    result = city_kpi("Mumbai")
    assert result is not None
    assert result[0] == "Mumbai"
    assert result[1] == 3  # 3 customers in Mumbai
    assert result[2] > 0  # avg_spend should be positive
    assert 0 <= result[3] <= 1  # churn_rate should be between 0 and 1

def test_city_kpi_injection_attempt():
    """Test that SQL injection attempt is rejected by city allowlist."""
    import pytest
    with pytest.raises(ValueError, match="City 'Mumbai' OR 1=1 --' not allowed"):
        city_kpi("Mumbai' OR 1=1 --")

def test_city_kpi_unknown_city():
    """Test that unknown cities are rejected."""
    import pytest
    with pytest.raises(ValueError, match="City 'Chennai' not allowed"):
        city_kpi("Chennai")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
