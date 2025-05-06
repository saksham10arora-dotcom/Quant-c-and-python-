"""
Topic: Advanced Pandas & Time Series Analysis
"""
import pandas as pd
import numpy as np

def compute_rolling_volatility(prices: pd.Series, window: int = 20) -> pd.Series:
    """Calculates annualized rolling volatility from daily prices."""
    returns = prices.pct_change().dropna()
    rolling_std = returns.rolling(window=window).std()
    return rolling_std * np.sqrt(252)

def resample_tick_data(ticks: pd.DataFrame, freq: str = '1Min') -> pd.DataFrame:
    """Aggregates tick data into OHLCV bars."""
    bars = ticks.resample(freq).agg({
        'price': ['first', 'max', 'min', 'last'],
        'volume': 'sum'
    })
    bars.columns = ['open', 'high', 'low', 'close', 'volume']
    return bars.dropna()

if __name__ == "__main__":
    dates = pd.date_range("2023-01-01", periods=100)
    prices = pd.Series(np.random.normal(100, 2, 100).cumsum(), index=dates)
    vol = compute_rolling_volatility(prices)
    print(f"Latest rolling volatility: {vol.iloc[-1]:.4f}")























