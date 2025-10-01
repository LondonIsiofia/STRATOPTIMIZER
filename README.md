# STRATOPTIMIZER
✅ Features implemented:

Grid Search Optimizer:

Iterates over parameter combinations (ema_fast, ema_slow, ATR, RSI, etc.)

Runs backtests automatically with Backtrader.

Result Logging:

Portfolio final value, trade count, and Sharpe Ratio logged.

Results exported to optimization_results.csv.

Indicators Supported:

EMA (fast/slow)

ATR (with toggle & multiplier)

RSI

Profit target %

Confidence threshold

Trend EMA

Sharpe Ratio Analyzer:

Annualized Sharpe ratio computed per run.

Logged and saved to CSV.

Top 3 Results printed after each run for quick insights.

🔧 Planned Updates / Improvements
Near-Term (Next Iterations):

✅ Add max drawdown & win rate analyzers.

✅ Add indicator toggles for MACD, Bollinger Bands, CCI, ADX, Stochastic.

✅ Create shortened parameter lists for progressive optimization (reduce runtime).

✅ Improve logging: entry/exit logs, stop-loss/profit target triggers.

Medium-Term:

✅ Visualization:

Best vs worst parameter set equity curves.

Trade markers (buy/sell).

✅ Ranking optimizer results by Sharpe Ratio or custom metric (Value × Sharpe).

✅ Hyperparameter search with TensorFlow neural network instead of brute force grid search.

Long-Term (ML/AI Integration):

✅ Train TensorFlow model:

Input: strategy parameters.

Output: expected portfolio value & Sharpe ratio.

✅ Use ML to predict promising parameter combinations before testing them in Backtrader.

✅ Potential reinforcement learning reward system:

Reward = High Sharpe + High Value + Low Drawdown.

# KEY STRATEGY FEATURES

✅ Trend filter → EMA trend (200 default) ensures long-only trades in uptrends.
✅ Confidence system → Combines EMA cross, RSI, and trend.
✅ Dynamic stop-loss → ATR-based, adjustable multiplier.
✅ Profit target → Based on percentage (default: 5%).
✅ Position sizing → Risk ~10% of cash per trade.
✅ Logging → Clear console logs for debugging.
✅ Optimizer-ready → Parameters exactly match those in your optimizer grid.
