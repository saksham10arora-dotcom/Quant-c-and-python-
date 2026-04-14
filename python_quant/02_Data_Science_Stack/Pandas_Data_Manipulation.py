"""
Topic: Pandas Data Manipulation & Cleaning
"""
import pandas as pd
import numpy as np

def generate_trade_report():
    df = pd.DataFrame({
        "symbol": ["AAPL", "GOOG", "MSFT", "AMZN"],
        "price": [178.52, 141.80, 415.30, 185.60],
        "volume": [50e6, 30e6, 25e6, 45e6],
        "sector": ["Tech", "Tech", "Tech", "Consumer"],
    })
    
    # Vectorized operations
    df["notional"] = df["price"] * df["volume"]
    df["tier"] = np.where(df["price"] > 200, "HIGH", "STANDARD")
    
    # Grouping
    summary = df.groupby("sector").agg(
        avg_price=("price", "mean"),
        total_notional=("notional", "sum")
    )
    
    print("Trade Summary by Sector:")
    print(summary)

if __name__ == "__main__":
    generate_trade_report()





















































































































































