"""
Topic: Modern Portfolio Theory & Efficient Frontier
"""
import numpy as np
import pandas as pd
from scipy import optimize

def get_tangency_portfolio(mu, cov):
    n_assets = len(mu)
    def neg_sharpe(w):
        ret = w @ mu
        vol = np.sqrt(w @ cov @ w)
        return -(ret / vol)

    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
    bounds = [(0, 1)] * n_assets   # Long-only

    result = optimize.minimize(
        neg_sharpe, 
        x0=np.ones(n_assets)/n_assets,
        method='SLSQP', 
        bounds=bounds, 
        constraints=constraints
    )
    return result.x

def main():
    # Mock data
    mu = np.array([0.12, 0.10, 0.14])
    cov = np.array([
        [0.04, 0.02, 0.01],
        [0.02, 0.05, 0.02],
        [0.01, 0.02, 0.06]
    ])
    
    w_tangency = get_tangency_portfolio(mu, cov)
    print(f"Tangency Portfolio Weights: {np.round(w_tangency, 4)}")

if __name__ == "__main__":
    main()









































































































































































