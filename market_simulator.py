import random
from collections import deque
from config import STOCKS, WINDOW_SIZE

class MarketSimulator:
    """Generates synthetic live market data with price memory."""
    
    def __init__(self):
        self.data_streams = {
            symbol: deque([info['base_price']], maxlen=WINDOW_SIZE) 
            for symbol, info in STOCKS.items()
        }

    def update_market(self):
        """Simulates one tick of market movement."""
        updates = {}
        for symbol, info in STOCKS.items():
            current_price = self.data_streams[symbol][-1]
            # Gaussian random walk
            change = random.gauss(0, info['volatility'])
            new_price = max(0.01, round(current_price + change, 2))
            
            self.data_streams[symbol].append(new_price)
            
            # Calculate daily change %
            pc_change = ((new_price - info['base_price']) / info['base_price']) * 100
            updates[symbol] = {
                "price": new_price,
                "history": list(self.data_streams[symbol]),
                "pc_change": pc_change
            }
        return updates
