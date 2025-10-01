import backtrader as bt

class LondonTradeV1(bt.Strategy):
    params = (
        ("ema_fast", 9),
        ("ema_slow", 21),
        ("ema_trend", 200),
        ("rsi_length", 14),
        ("atr_length", 14),
        ("atr_mult", 2.0),
        ("profit_target_pct", 0.05),
        ("confidence_threshold", 70), 
    )

    def __init__(self):
        self.ema_fast = bt.ind.EMA(period=self.p.ema_fast)
        self.ema_slow = bt.ind.EMA(period=self.p.ema_slow)
        self.ema_trend = bt.ind.EMA(period=self.p.ema_trend)
        self.rsi = bt.ind.RSI(period=self.p.rsi_length)
        self.atr = bt.ind.ATR(period=self.p.atr_length)

        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f"{dt} | {txt}")

    def next(self):
        if self.position:
            if self.data.close[0] <= self.stop_loss:
                self.log(f"STOP LOSS HIT @ {self.data.close[0]:.2f}")
                self.close()
            elif self.data.close[0] >= self.take_profit:
                self.log(f"PROFIT TARGET HIT @ {self.data.close[0]:.2f}")
                self.close()
            return

        confidence = 0
        if self.ema_fast[0] > self.ema_slow[0]:
            confidence += 30
        if self.data.close[0] > self.ema_trend[0]:
            confidence += 30
        if self.rsi[0] > 50:
            confidence += 20
        if self.ema_fast[0] > self.ema_trend[0]:
            confidence += 20

        if confidence >= self.p.confidence_threshold:
            self.log(f"BUY SIGNAL | Confidence={confidence}")
            size = self.broker.get_cash() * 0.1 / self.data.close[0]  # 10% cash per trade
            self.buy(size=size)

            self.entry_price = self.data.close[0]
            self.stop_loss = self.entry_price - (self.atr[0] * self.p.atr_mult)
            self.take_profit = self.entry_price * (1 + self.p.profit_target_pct)
            self.log(
                f"ENTRY @ {self.entry_price:.2f} | SL={self.stop_loss:.2f} | TP={self.take_profit:.2f}"
            )
