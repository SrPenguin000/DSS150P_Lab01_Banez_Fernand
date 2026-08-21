import os
from pathlib import Path
import pandas as pd

RAW = Path("data/raw")

try:
    customers = pd.read_csv(RAW / "customers.csv")
    orders = pd.read_json(RAW / "orders.json")
    products = pd.read_parquet(RAW / "products.parquet")
except FileNotFoundError as e:
    print(f"Error: {e}\nPlease make sure the raw data files are in the data/raw directory.")
    exit()

for name, df in {
    "customers.csv": customers,
    "orders.json": orders,
    "products.parquet": products,
}.items():
    file_path = RAW / name
    file_size_kb = os.path.getsize(file_path) / 1024
    
    print(f"\n{'='*50}")
    print(f"--- Profiling {name} ---")
    print(f"File Size: {file_size_kb:.2f} KB")
    print(f"Shape (Rows, Columns): {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nNull Values:\n{df.isna().sum()}")
    
    print(f"\nFully Duplicated Rows: {df.astype(str).duplicated().sum()}")
    print(f"\nDistinct Values per Column:\n{df.astype(str).nunique()}")
    
    print("\n--- Numeric Columns (Min/Max) ---")
    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        for col in numeric_cols:
            print(f"  {col}: Min = {df[col].min()}, Max = {df[col].max()}")
    else:
        print("  No numeric columns found.")
        
    print("\n--- Date/Time Columns (Min/Max) ---")
    datetime_cols = df.select_dtypes(include='datetime').columns
    if not datetime_cols.empty:
        for col in datetime_cols:
            print(f"  {col}: Min = {df[col].min()}, Max = {df[col].max()}")
    else:
        print("  No automatically detected datetime columns. (May require manual parsing)")
        
    print(f"\nFirst 5 Records:\n{df.head()}")
    print(f"{'='*50}\n")