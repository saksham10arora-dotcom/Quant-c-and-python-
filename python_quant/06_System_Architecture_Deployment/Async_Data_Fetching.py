"""
Topic: Asynchronous Data Fetching
"""
import asyncio
import time
# import aiohttp # requires pip install aiohttp

async def fetch_price(symbol: str) -> float:
    """Simulates an asynchronous network call to a market data API."""
    print(f"Fetching {symbol}...")
    await asyncio.sleep(1.5)  # Simulate network latency
    price = 100.0 + (len(symbol) * 10)
    print(f"Received {symbol}: ${price}")
    return price

async def fetch_all_symbols(symbols: list):
    """Fetches multiple symbols concurrently."""
    tasks = [fetch_price(sym) for sym in symbols]
    results = await asyncio.gather(*tasks)
    return dict(zip(symbols, results))

if __name__ == "__main__":
    symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
    
    start = time.time()
    # Python 3.7+ async run
    results = asyncio.run(fetch_all_symbols(symbols))
    end = time.time()
    
    print(f"\nFetched {len(symbols)} symbols in {end - start:.2f} seconds.")
    print("Note: Sequential fetching would have taken ~7.5 seconds.")
    print(results)






















