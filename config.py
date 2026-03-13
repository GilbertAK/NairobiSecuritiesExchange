# List of blue-chip stocks on the Nairobi Securities Exchange
STOCKS = {
    "SCOM": {"name": "Safaricom PLC", "base_price": 17.50, "volatility": 0.05},
    "EQTY": {"name": "Equity Group", "base_price": 42.10, "volatility": 0.12},
    "KCB":  {"name": "KCB Group", "base_price": 29.35, "volatility": 0.10},
    "EABL": {"name": "East African Breweries", "base_price": 150.00, "volatility": 0.25},
    "ABSA": {"name": "ABSA Bank Kenya", "base_price": 12.80, "volatility": 0.04}
}

REFRESH_RATE = 0.4  # Your requested 0.4s refresh rate
WINDOW_SIZE = 20    # Number of data points for the ML model to learn from
