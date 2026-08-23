**1. Which source would be easiest to integrate into a future pipeline, and why?**

The `products.parquet` file would be the easiest source to integrate. Because Parquet is a strictly typed columnar format, the data types (such as `int32` for stock quantities and `float64` for prices) are inherently enforced upon ingestion. Our profiling also confirmed it is incredibly clean, containing zero null values and zero duplicated rows. This eliminates the need for complex, manual type casting and heavy data cleaning transformations before loading it into a data warehouse.

**2. Which source presents the greatest schema or data-quality risk, and what evidence supports your answer?**

The `orders.json` file and the External REST API present the greatest schema risks. Our profiling of `orders.json` revealed nested dictionary structures within the `shipping` column. If the source system adds new, unexpected keys inside that nested structure, a rigidly defined pipeline will fail to parse it. Similarly, external APIs pose a high risk because the schema owner is a third party; endpoints can be deprecated or payload structures can change without warning, instantly breaking the acquisition method. 

**3. What could go wrong if a pipeline is built before the source schema and contract are understood?**

Building a pipeline blindly leads to catastrophic pipeline failures and compromised data integrity. If the schema is misunderstood, operations like deduplication might fail (as seen when Pandas crashed attempting to hash the nested dictionaries in our `orders.json` file). If a contract does not identify duplicated primary keys, like the 2 duplicated rows in our `customers.csv`, the pipeline will attempt to insert them into a relational database, triggering primary key constraint violations and halting the entire ingestion process.

**4. How do Git, virtual environments, containers, and documentation improve reproducibility for a data-engineering team?**

These tools eliminate the "it works on my machine" problem. Git provides a strict version history, allowing a team to track exactly when and why code changed. Virtual environments isolate Python dependencies, ensuring that every engineer uses the exact same package versions (like Pandas and SQLAlchemy). Docker containers standardize the infrastructure, guaranteeing that the PostgreSQL database runs identically regardless of the host operating system. Finally, comprehensive documentation acts as the blueprint, explicitly telling teammates exactly how to orchestrate these tools to rebuild the entire ecosystem from scratch.