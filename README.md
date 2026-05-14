# vibe-kpi-demo

A beginner-friendly Applied Analytics mini project demonstrating ETL, SQLite, and SQL injection prevention.

## Project Structure
- `data/raw/` - Raw CSV data files
- `data/db/` - SQLite database files
- `src/` - Source code (ETL script, KPI calculations)
- `tests/` - Pytest test files

## Setup and Run Commands

# Install requirements (inside your activated .venv)
pip install -r requirements.txt

# Run ETL (creates SQLite DB)
python src/etl_load_sqlite.py

# Run KPI script
python src/kpi_city.py

# Run tests
python -m pytest -q