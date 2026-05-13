"""
Topic: Event-Driven Backtesting Engine
"""
import pandas as pd
import numpy as np
from enum import Enum
from dataclasses import dataclass

class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"

@dataclass
class Order:
    timestamp: pd.Timestamp
    symbol: str
    side: Side
    quantity: int

class SMACrossover:
    """Simple Moving Average crossover strategy."""
    def __init__(self, fast=10, slow=30):
        self.fast = fast
        self.slow = slow
        self.price_history = {}
    
    def generate_signals(self, timestamp, prices, portfolio_pos) -> list[Order]:
        orders = []
        for symbol, price in prices.items():
            if symbol not in self.price_history:
                self.price_history[symbol] = []
            self.price_history[symbol].append(price)
            
            history = self.price_history[symbol]
            if len(history) < self.slow:
                continue
            
            sma_fast = np.mean(history[-self.fast:])
            sma_slow = np.mean(history[-self.slow:])
            
            current_pos = portfolio_pos.get(symbol, 0)
            
            if sma_fast > sma_slow and current_pos == 0:
                orders.append(Order(timestamp, symbol, Side.BUY, 100))
            elif sma_fast < sma_slow and current_pos > 0:
                orders.append(Order(timestamp, symbol, Side.SELL, current_pos))
        return orders

if __name__ == "__main__":
    print("Backtester Engine initialized. Strategy: SMACrossover.")




















































































































































