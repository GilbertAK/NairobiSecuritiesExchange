# 📈 NSE AI Predictive Ticker (Nairobi Securities Exchange)

A high-frequency algorithmic trading simulator for the Kenyan market. This project integrates **Machine Learning (Linear Regression)** into a real-time data pipeline to forecast short-term price movements of Nairobi's blue-chip stocks.

## 🧠 Machine Learning Integration
Unlike simple trackers, this terminal uses a **Scikit-Learn** backend to:
1. Ingest a rolling window of the last 20 price ticks.
2. Train a linear regression model on-the-fly.
3. Extrapolate the "Next-Tick" price (T+1).

## 🚀 Technical Stack
- **Language:** Python 3.7+ (32-bit optimized)
- **ML Library:** Scikit-Learn (Linear Regression)
- **Data Handling:** NumPy, Deque (for memory efficiency)
- **UI:** Colorama (ANSI Terminal Formatting)

## 📁 Project Structure
- `main.py`: Entry point with 0.4s refresh loop.
- `ml_engine.py`: Scikit-Learn model implementation.
- `market_simulator.py`: Real-time price generation engine.
- `config.py`: Asset definitions (Safaricom, KCB, Equity Bank, etc.).

## 🔧 Installation
```bash
pip install -r requirements.txt
python main.py