# Source Data Inventory

| Field | Customers (CSV) | Orders (JSON) | Products (Parquet) | External REST API | PostgreSQL (Inventory) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Source name** | customers.csv | orders.json | products.parquet | REST API | support_tickets |
| **Source-system type** | Flat File | File (Web/App Export) | Columnar File | Web Service | Relational Database |
| **Data format** | CSV | JSON | Parquet | JSON | SQL Table |
| **Structure** | Structured | Semi-structured | Structured | Semi-structured | Structured |
| **Expected update pattern** | Batch (Daily/Weekly) | Batch or Streaming | Batch (Analytical) | On-Demand (API Call) | Transactional (Continuous) |
| **Likely acquisition method** | File drop (SFTP/Cloud) | API or File drop | Data Lake export | HTTP GET Request | SQL Query / CDC |
| **Schema location/owner** | Inferred from header | Embedded (Keys) | Embedded in file metadata | API Documentation | Database Information Schema |
| **Possible primary/business key** | customer_id | order_id | product_id | id | ticket_id |
| **Potential schema-evolution risk** | Columns added/removed, delimiter changes | Missing keys, nested structures changing | Low (Strictly typed), but types might change | High (Endpoints deprecating, payload changes) | Medium (DB migrations, altered constraints) |
| **Potential data-quality risk** | Nulls, formatting issues, encoding errors | Missing values, mismatched data types | Null values | Rate limits, timeouts, incomplete payloads | Stale data, constraint violations |

*Note: API retrieval timestamp (UTC): 2026-08-21T11:27:00+00:00*