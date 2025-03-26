"""
Topic: Principal Component Analysis (PCA) for Factor Modeling
"""
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def extract_risk_factors(returns: pd.DataFrame, n_components: int = 3):
    """Uses PCA to extract statistical risk factors from asset returns."""
    scaler = StandardScaler()
    scaled_returns = scaler.fit_transform(returns.fillna(0))
    
    pca = PCA(n_components=n_components)
    factors = pca.fit_transform(scaled_returns)
    
    explained_variance = pca.explained_variance_ratio_
    
    return pd.DataFrame(factors, index=returns.index), explained_variance

if __name__ == "__main__":
    dates = pd.date_range("2023-01-01", periods=252)
    returns = pd.DataFrame(np.random.normal(0, 0.01, (252, 10)), index=dates)
    
    # Introduce a common market factor
    market = np.random.normal(0, 0.02, 252)
    for col in returns.columns:
        returns[col] += market * np.random.uniform(0.5, 1.5)
        
    factors, var_explained = extract_risk_factors(returns)
    
    print("Variance explained by top 3 factors:")
    for i, var in enumerate(var_explained):
        print(f"Factor {i+1}: {var:.2%}")


































