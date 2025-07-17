"""
Topic: NumPy Core & Advanced Operations
"""
import numpy as np

def compute_portfolio_stats():
    # Generate realistic asset returns
    rng = np.random.default_rng(42)
    n_days = 252
    n_assets = 5

    # Simulated correlated returns via Cholesky
    annual_vols = np.array([0.25, 0.28, 0.22, 0.32, 0.18])
    annual_returns = np.array([0.12, 0.10, 0.14, 0.08, 0.07])
    
    daily_vols = annual_vols / np.sqrt(252)
    daily_mus = annual_returns / 252
    
    # Assume Identity correlation for simplicity in this script
    target_corr = np.eye(n_assets)
    cov_daily = np.outer(daily_vols, daily_vols) * target_corr
    
    L = np.linalg.cholesky(cov_daily)
    Z = rng.normal(0, 1, (n_days, n_assets))
    returns = Z @ L.T + daily_mus
    
    # Calculate Sharpe
    weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    portfolio_returns = returns @ weights
    sharpe = np.mean(portfolio_returns) / np.std(portfolio_returns) * np.sqrt(252)
    
    print(f"Portfolio Sharpe: {sharpe:.2f}")

if __name__ == "__main__":
    compute_portfolio_stats()








































































































































































