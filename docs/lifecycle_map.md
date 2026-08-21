# Data Lifecycle Map

## Lifecycle Element Table

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Source system** | The original location or creator of the raw data. | The provided CSV, JSON, Parquet files, or a web server hosting the REST API. | File system, Web server | A file is missing or the API server is offline. |
| **Ingestion/acquisition** | The process of reading and bringing data into the working environment. | Reading a CSV file into a dataframe or fetching data via HTTP request. | Python (Pandas, Requests) | Network timeout or incorrect file path. |
| **Storage** | The structured environment where data is saved for long-term access. | Saving the final, cleaned data tables into the database. | PostgreSQL | Database connection drops or runs out of disk space. |
| **Processing/transformation** | Cleaning, filtering, or reshaping the data into a usable format. | Dropping empty rows, renaming columns, or merging tables in memory. | Python (Pandas) | Code crashes due to an unexpected data type. |
| **Data quality/validation** | Checking the data against rules to ensure it is accurate and complete. | Verifying there are no missing values in a primary key column. | Python | Data fails the schema check and is rejected. |
| **Delivery** | Providing access to the stored data for end-users. | Allowing an analyst to run SQL `SELECT` queries on the database. | PostgreSQL, SQL | User lacks permissions or the query is too slow. |
| **Consumer** | The final user or system that gains insights from the data. | A business analyst building a report or a dashboard application. | BI Tool, Analyst | The user misinterprets the final data. |

<br>

## Data Flow Diagram

Here is a box-and-arrow diagram illustrating how the raw sources move through the pipeline to the final consumer:

```text
[CSV Source] ------\
                    \
[JSON Source] -------\
                      ====> [ Pipeline/Process Box ] ====> [ Storage/Destination ] ====> [ Downstream Analyst / ]
                     /      (Python / Pandas)              (PostgreSQL Database)         [ Application Consumer ]
[Parquet Source] ---/
                   /
[REST API] -------/