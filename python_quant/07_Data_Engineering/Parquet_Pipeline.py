"""
Topic: High-Performance Data Engineering Pipeline (Parquet & Polars)
"""
import pandas as pd
import numpy as np
import time

def generate_large_dataset(rows: int = 1_000_000):
    """Generates a large synthetic trade dataset."""
    print(f"Generating {rows} rows of trade data...")
    dates = pd.date_range("2023-01-01", periods=rows, freq="S")
    symbols = np.random.choice(["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"], rows)
    prices = np.random.uniform(100, 500, rows)
    volumes = np.random.randint(1, 1000, rows)
    
    df = pd.DataFrame({
        "timestamp": dates,
        "symbol": symbols,
        "price": prices,
        "volume": volumes
    })
    return df

def save_and_compare(df: pd.DataFrame):
    """Saves data to CSV and Parquet, comparing file sizes and write times."""
    # CSV
    start = time.time()
    df.to_csv("trades_dump.csv", index=False)
    csv_time = time.time() - start
    
    # Parquet
    start = time.time()
    df.to_parquet("trades_dump.parquet", engine="pyarrow", compression="snappy")
    parquet_time = time.time() - start
    
    print(f"CSV Write Time: {csv_time:.2f}s")
    print(f"Parquet Write Time: {parquet_time:.2f}s")
    
    import os
    csv_size = os.path.getsize("trades_dump.csv") / (1024 * 1024)
    parquet_size = os.path.getsize("trades_dump.parquet") / (1024 * 1024)
    
    print(f"CSV Size: {csv_size:.2f} MB")
    print(f"Parquet Size: {parquet_size:.2f} MB")
    
    # Clean up
    os.remove("trades_dump.csv")
    os.remove("trades_dump.parquet")

if __name__ == "__main__":
    df = generate_large_dataset(500_000)
    save_and_compare(df)

























