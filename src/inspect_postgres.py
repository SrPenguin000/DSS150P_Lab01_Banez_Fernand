from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("postgresql+psycopg2://dss150p:dss150p_lab@localhost:5432/dss150p_lab")

with engine.connect() as conn:
    print("=== Checking Tables ===")
    tables = pd.read_sql(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"), conn)
    print(tables)
    
    if not tables.empty:
        target_table = tables.iloc[0]['table_name']
        
        print(f"\n=== Metadata for: {target_table} ===")
        cols_query = f"""
        SELECT column_name, data_type, is_nullable 
        FROM information_schema.columns 
        WHERE table_name = '{target_table}' 
        ORDER BY ordinal_position;
        """
        print(pd.read_sql(text(cols_query), conn).to_string(index=False))
        
        count_query = f"SELECT COUNT(*) as total_rows FROM {target_table};"
        print(f"\n=== Row Count ===")
        print(pd.read_sql(text(count_query), conn).to_string(index=False))
        
        sample_query = f"SELECT * FROM {target_table} LIMIT 5;"
        print(f"\n=== Sample 5 Rows ===")
        print(pd.read_sql(text(sample_query), conn))
    else:
        print("\nNo tables found! The seed data might not have loaded correctly.")