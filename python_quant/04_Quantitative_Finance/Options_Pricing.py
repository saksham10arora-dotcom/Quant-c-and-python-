"""
Topic: Black-Scholes Options Pricing & Greeks
"""
import numpy as np
from scipy.stats import norm

class EuropeanOption:
    def __init__(self, S, K, T, r, sigma, option_type='call'):
        self.S = S  # Underlying price
        self.K = K  # Strike price
        self.T = T  # Time to maturity (years)
        self.r = r  # Risk-free rate
        self.sigma = sigma  # Volatility
        self.type = option_type.lower()
        
        self.d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        self.d2 = self.d1 - sigma * np.sqrt(T)

    def price(self):
        if self.type == 'call':
            return self.S * norm.cdf(self.d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2)
        else:
            return self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d1)

    def delta(self):
        if self.type == 'call':
            return norm.cdf(self.d1)
        else:
            return norm.cdf(self.d1) - 1

    def gamma(self):
        return norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.T))

if __name__ == "__main__":
    call = EuropeanOption(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    print(f"Call Price: ${call.price():.2f}")
    print(f"Delta: {call.delta():.4f}")
    print(f"Gamma: {call.gamma():.4f}")






















