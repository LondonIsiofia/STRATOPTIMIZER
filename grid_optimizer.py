from itertools import product
import backtrader as bt
import pandas as pd
from strategies.londonlogicv1 import LondonTradeV1
import datetime

class Analyzer:
    def __init__(self):
        self.results = []

    def run_backtest(self, strategy_class, paramset):
        cerebro = bt.Cerebro()
        cerebro.addstrategy(strategy_class, **paramset)

        data = bt.feeds.GenericCSVData(
            dataname='data/spy.csv',
            dtformat='%Y-%m-%d',
            timeframe=bt.TimeFrame.Days,
            compression=1,
            openinterest=-1,
            headers=True
        )
        cerebro.adddata(data)
        cerebro.broker.setcash(10000)
        cerebro.broker.setcommission(commission=0.001)
        cerebro.addsizer(bt.sizers.PercentSizer, percents=10)

        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trade_stats')
        cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name='sharpe_ratio')

        print(f"Testing parameters: {paramset}")
        results = cerebro.run()
        strat = results[0]

        final_value = cerebro.broker.getvalue()

        trade_analysis = strat.analyzers.trade_stats.get_analysis()
        sharpe_analysis = strat.analyzers.sharpe_ratio.get_analysis()

        total_trades = trade_analysis.total.closed if 'total' in trade_analysis and 'closed' in trade_analysis.total else 0
        sharpe = sharpe_analysis['sharperatio'] if 'sharperatio' in sharpe_analysis else None

        print(f"Final Value: {final_value:.2f} | Trades: {total_trades} | Sharpe Ratio: {sharpe}\n")

        self.results.append((paramset, final_value, total_trades, sharpe))

    def run_grid_search(self, strategy_class, param_grid):
        keys, values = zip(*param_grid.items())
        for combination in product(*values):
            params = dict(zip(keys, combination))
            self.run_backtest(strategy_class, params)

        self.results.sort(key=lambda x: x[1], reverse=True)
        self.report_results()

    def report_results(self):
        print("\nTop 3 Parameter Sets:")
        for i, (params, value, trades, sharpe) in enumerate(self.results[:3]):
            print(f"{i + 1}: Value: {value:.2f} | Trades: {trades} | Sharpe: {sharpe} | Params: {params}")

        df = pd.DataFrame([
            {"Value": v, "Trades": t, "Sharpe": s, **p}
            for p, v, t, s in self.results
        ])
        df.to_csv("results/optimization_results.csv", index=False)


param_grid = {
    'ema_fast': [5, 9],
    'ema_slow': [21, 30],
    'confidence_threshold': [60, 70],
    'atr_mult': [1.5, 2.0],
    'profit_target_pct': [0.03, 0.05],
    'atr_length': [7, 14],
    'ema_trend': [100, 200],
    'rsi_length': [10, 14]
}

if __name__ == '__main__':
    analyzer = Analyzer()
    analyzer.run_grid_search(LondonTradeV1, param_grid)
