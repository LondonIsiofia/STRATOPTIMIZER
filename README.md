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

# 📈 Optimizer Progress Log
🎯 Project Goal

Develop a strategy optimizer that consistently achieves 10%+ profit over the past 5 years.

Base: Converted Pine Script strategy into a Backtrader-compatible strategy (LondonTradeV1).

Dataset: SPY (S&P 500 ETF) from 2006-02-10 → 2025-05-02, imported as CSV.

✅ Current Workflow

Strategy built in Pine Script → converted to Backtrader Python class.

Imported SPY historical data.

All parameters from the Pine Script strategy were exposed for tuning:

ema_fast, ema_slow, ema_trend

rsi_length

atr_length, atr_mult

profit_target_pct

confidence_threshold

Created a grid search optimizer:

Each parameter tested with ~3 values.

Explores every possible combination.

Records: Final Portfolio Value, Trades, Sharpe Ratio.

Exports results → optimization_results.csv.

📊 Key Results (Highlights)
Long-Term Backtest (2006 → 2025)

Best configurations generated ~$12,000 final value from $10,000 starting balance.

Example top performers:

Value ≈ 12079 | Trades: 138 | ema_fast=5 | ema_slow=30 | confidence=60 | atr_mult=4.0 | TP=6% | atr_len=21 | trend=100 | rsi=10
Value ≈ 12076 | Trades: 140 | ema_fast=5 | ema_slow=25 | confidence=60 | atr_mult=4.0 | TP=6% | atr_len=21 | trend=100 | rsi=10
Value ≈ 12065 | Trades: 138 | ema_fast=9 | ema_slow=25 | confidence=60 | atr_mult=4.0 | TP=6% | atr_len=21 | trend=100 | rsi=10

Mid-Term Backtest (2020 → 2025)

Top results achieved ~5.79% – 6.94% growth.

Lower ATR multipliers increased trade frequency (≈2–3 per month).

Highlights:

Value ≈ 10618 | Trades: 44 | ema_fast=5 | ema_slow=25 | confidence=40 | atr_mult=4.0 | TP=6.5% | atr_len=7 | trend=100 | rsi=8
Value ≈ 10690 | Trades: 44 | ema_fast=5 | ema_slow=15 | confidence=35 | atr_mult=4.0 | TP=6.5% | atr_len=28 | trend=100 | rsi=8
Value ≈ 10694 | Trades: 47 | ema_fast=5 | ema_slow=15 | confidence=32 | atr_mult=3.8 | TP=6.5% | atr_len=28 | trend=100 | rsi=8

Short-Term Backtest (2022 → 2025)

Performance slightly weaker, ~4–6% growth.

Example:

Value ≈ 10411 | Trades: 23 | ema_fast=5 | ema_slow=15 | confidence=32 | atr_mult=3.8 | TP=6.5% | atr_len=28 | trend=100 | rsi=8

⚙️ Experiments

ATR Tuning:

High ATR (5.0–10.0) → fewer trades, larger risk, slightly higher peak values (~6.8%).

Low ATR (3.0–4.0) → more frequent trades (40–60), more consistent growth.

Extra Indicators:

Added CCI (cci_length) and Stochastic (stoch_k, stoch_d) into parameter grid.

Early tests show ~21 trades, results around $10.4k from $10k.

🚧 Next Steps

Expand analyzers:

Max Drawdown

Win Rate

CAGR

Smart parameter selection:

Progressive grid search (shortened param ranges).

Neural net prediction to reduce brute force.

Visualization:

Plot top 3 strategy equity curves.

Mark trade entry/exit points.

Reward System:

Use Sharpe ratio × Value for ranking.

TensorFlow Integration:

Train model on past optimizer runs.

Predict promising parameter sets before full backtest.
