# Data Source Profiles

## 1. customers.csv
* **Observation 1 (Data Quality / Duplicates):** There are 2 fully duplicated rows in the dataset. Additionally, `customer_id` only has 247 distinct values out of 250 total rows, meaning there are duplicated primary keys that must be deduplicated before loading into a database.
* **Observation 2 (Nullability):** The data contains missing values in the `email` column (3 nulls) and `city` column (2 nulls). A downstream pipeline will need rules on how to handle these (e.g., dropping the rows or filling with defaults).
* **Observation 3 (Data Types):** The `signup_date` column was imported as a standard string/object rather than a native datetime object. It will require explicit datetime parsing in the pipeline.

## 2. orders.json
* **Observation 1 (Nested Structure):** The `shipping` column contains a nested JSON dictionary (e.g., `{'region': 'Region VII', 'method': 'Standard'}`). A data pipeline will need to flatten or unpack this column into separate `shipping_region` and `shipping_method` columns to be useful in a relational database.
* **Observation 2 (Data Integrity):** This dataset is exceptionally clean regarding completeness; there are 0 null values and 0 fully duplicated rows. The `order_id` column is a perfect primary key with exactly 250 distinct values for 250 rows.
* **Observation 3 (Data Types):** Similar to the CSV, the `order_timestamp` column is stored as a string (ISO 8601 format) and will need to be cast to a datetime type during processing.

## 3. products.parquet
* **Observation 1 (Strict Typing):** Because this is a Parquet file, the data types are strictly enforced and read correctly upon ingestion (e.g., `stock_quantity` is properly cast as `int32` and `unit_price` as `float64`), which reduces the transformation workload.
* **Observation 2 (Data Quality):** The dataset is perfectly complete with 0 null values and 0 duplicated rows. 
* **Observation 3 (Keys):** The `product_id` column contains exactly 200 distinct values for 200 rows, making it a reliable primary key for downstream table joins.