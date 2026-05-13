"""
Topic: Cointegration & Statistical Arbitrage (Pairs Trading)
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

def test_cointegration(asset1: pd.Series, asset2: pd.Series):
    """Tests if two price series are cointegrated."""
    score, pvalue, _ = coint(asset1, asset2)
    return pvalue < 0.05, pvalue

def calculate_spread(asset1: pd.Series, asset2: pd.Series) -> pd.Series:
    """Calculates the hedge ratio and spread between two cointegrated assets."""
    # OLS regression: asset1 = beta * asset2 + alpha
    X = sm.add_constant(asset2)
    model = sm.OLS(asset1, X).fit()
    beta = model.params.iloc[1]
    
    spread = asset1 - beta * asset2
    return spread, beta

if __name__ == "__main__":
    np.random.seed(42)
    x = np.cumsum(np.random.normal(0, 1, 1000))
    y = x * 1.5 + np.random.normal(0, 0.5, 1000)
    
    is_coint, pval = test_cointegration(x, y)
    print(f"Cointegrated: {is_coint} (p-value: {pval:.4f})")
    
    if is_coint:
        spread, hedge_ratio = calculate_spread(pd.Series(y), pd.Series(x))
        print(f"Hedge Ratio: {hedge_ratio:.4f}")
        print(f"Spread Mean: {spread.mean():.4f}")




















