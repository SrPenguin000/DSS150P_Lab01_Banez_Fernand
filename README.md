# DSS150P Lab 01: Data Engineering Foundations
**Name:** Fernand Benedict Bañez
**Student Number:** 2024110121

## Purpose of the Laboratory
To establish a foundational data engineering environment using Python, Git, and Docker, and to practice profiling, documenting, and validating various raw data sources.

## Software Requirements
* Python 3.10+
* Git
* Docker Desktop
* Visual Studio Code

## Exact Steps to Reproduce the Environment
1. Clone the repository to your local machine.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.\.venv\Scripts\Activate.ps1` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Exact Commands to Start and Stop PostgreSQL
* **Start PostgreSQL:** `docker-compose up -d`
* **Stop PostgreSQL:** `docker-compose down`

## How to Run Each Python Script
* **Profile Sources:** `python src/profile_sources.py`
* **Inspect API:** `python src/inspect_api.py`
* **Inspect PostgreSQL:** `python src/inspect_postgres.py`

## Description of Each Source
* `customers.csv`: A flat file containing customer demographic data.
* `orders.json`: A semi-structured file containing e-commerce transaction records.
* `products.parquet`: A strongly typed columnar file containing the product catalog.
* `REST API`: An external web service providing JSON payload records on demand.
* `support_tickets`: A PostgreSQL relational table containing customer service logs.

## Known Limitations or Unresolved Questions
* The `orders.json` file contains nested JSON structures (shipping details) that require flattening before relational ingestion.
* Duplicates exist in `customers.csv` that require a strict deduplication strategy before loading into the final database tables.