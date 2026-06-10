# 📊 Stock Market Analysis & Trading Agent

A comprehensive AI-powered stock market analysis agent for the Indian market (NSE) that provides:

- **Deep Technical Analysis** using multiple indicators (RSI, MACD, Bollinger Bands, ATR, etc.)
- **Automated Hourly Alerts** via WhatsApp & Email
- **Risk Management** with automatic stop-loss and take-profit calculations
- **Portfolio Tracking** with performance metrics
- **Web Dashboard** for monitoring and control

## 🎯 Features

### Analysis Engine

- **RSI Analysis**: Overbought/oversold detection
- **MACD**: Trend confirmation
- **Bollinger Bands**: Volatility analysis
- **Volume Analysis**: Breakout detection
- **Support/Resistance**: Key price levels
- **ATR**: Volatility measurement

### Risk Management

- Automatic position sizing
- Stop-loss calculation (fixed % below entry)
- Take-profit targets (fixed % above entry)
- Brokerage & transaction charge accounting
- GST calculation on charges
- Max loss per trade limits

### Alerts System

- **WhatsApp**: Instant notifications (requires Twilio)
- **Email**: Detailed HTML reports
- **Hourly Scheduling**: Automatic analysis every hour
- **Summary Reports**: Daily trading summary

### Web Dashboard

- View top stock recommendations
- Portfolio performance tracking
- Manual analysis trigger
- Real-time market status
- Alert history
- Trade management

## 📋 Setup Instructions

### 1. Clone & Install Dependencies

```bash
cd stock_agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

#### Email Setup (Gmail)

1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Use this password in `EMAIL_PASSWORD`

#### WhatsApp Setup (Twilio)

1. Sign up for free trial: https://www.twilio.com/
2. Get your WhatsApp-enabled phone number
3. Add your API key and phone number to `.env`

### 3. Initialize Database

```bash
python -c "from models import init_db; init_db()"
```

## 🚀 Usage

### Option 1: Web Dashboard

```bash
python web_app.py
# Visit http://localhost:5000
```

Features:

- View recommendations in real-time
- Portfolio performance
- Manual analysis trigger
- Alert monitoring

### Option 2: Command Line (One-time Analysis)

```python
from stock_agent import StockMarketAgent

agent = StockMarketAgent(investment=500000)
agent.display_recommendations(top_n=10)
```

Output:

```
================================================================================
🔝 TOP 10 STOCK RECOMMENDATIONS
================================================================================

1. 🟢 SBIN.NS
   Signal: BUY (85% confidence)
   Current Price: ₹500.50
   Entry: ₹502.00 | SL: ₹480.00 | TP: ₹530.00
   Expected Profit: ₹1,500.00 | Risk: ₹500.00
   Reasons: RSI oversold, MACD bullish, Volume spike...

2. 🟡 RELIANCE.NS
   Signal: HOLD (65% confidence)
   ...
```

### Option 3: Automated Hourly Monitoring

```python
from stock_agent import StockMarketAgent

agent = StockMarketAgent(investment=500000)
agent.start_monitoring()
# Runs continuously, analyzes hourly during market hours
```

## 📊 Configuration

Edit `config.py` to customize:

```python
# Investment Settings
TOTAL_INVESTMENT = 500000  # 5 lakhs
MAX_LOSS_PER_TRADE = 0.03  # 3% max loss
TARGET_PROFIT_PERCENT = 0.05  # 5% target

# Alert Timing
ALERT_INTERVAL_MINUTES = 60  # Alert every hour
TRADING_START_TIME = time(9, 15)  # 9:15 AM IST
TRADING_END_TIME = time(15, 30)  # 3:30 PM IST

# Technical Indicators
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
```

## 📈 How It Works

### 1. Data Fetching

- Fetches historical OHLCV data from Yahoo Finance
- Covers 3-month history for analysis
- Supports 30+ popular NSE stocks

### 2. Technical Analysis

- Calculates 6+ technical indicators
- Generates BUY/SELL/HOLD signals
- Confidence score 0-100%

### 3. Risk Calculation

```
Entry Price = Current Price × (1 + charges%)
Stop Loss = Entry × (1 - 3%)
Take Profit = Entry × (1 + 5% + charges%)
Expected Profit = (TP - Entry) × Quantity
```

### 4. Alert Generation

Sends alerts when:

- Signal confidence ≥ 80%
- High conviction opportunities found
- Includes all key metrics & recommendations

### 5. Portfolio Tracking

Records:

- Entry/exit prices
- Actual P&L
- Return %
- Win rate

## 💡 Investment Strategy

### Recommended Approach

1. **Capital Allocation**: Divide ₹5 lakhs into 20 positions
   - ₹25,000 per trade
   - Max loss per trade: ₹750 (3%)

2. **Trade Duration**: 3-5 days
   - Entry: After signal confirmation
   - Exit: At TP or SL (automated in real trading)
   - Total portfolio P&L: ₹750-5000/day potential

3. **Daily Profit Target**: ₹2,000-5,000
   - Realistic on ₹5 lakh capital
   - Requires 4-6% daily portfolio movement

### Risk Management

✅ **DO:**

- Follow stop-losses religiously
- Take profits at targets
- Diversify across 10-20 stocks
- Scale out gradually
- Keep detailed records

❌ **DON'T:**

- Override system recommendations
- Add to losing trades
- Ignore stop-losses
- Trade all capital at once
- Use leverage (margin)

## 📊 API Endpoints

| Endpoint                 | Method | Purpose                   |
| ------------------------ | ------ | ------------------------- |
| `/`                      | GET    | Dashboard                 |
| `/api/recommendations`   | GET    | Get stock recommendations |
| `/api/portfolio`         | GET    | Portfolio performance     |
| `/api/trades`            | GET    | Trade history             |
| `/api/analysis/<ticker>` | GET    | Single stock analysis     |
| `/api/alerts`            | GET    | Alert history             |
| `/api/run-analysis`      | POST   | Manual analysis           |
| `/api/status`            | GET    | Agent status              |

## 📝 Examples

### Get Top 10 Recommendations

```bash
curl http://localhost:5000/api/recommendations?limit=10
```

Response:

```json
{
  "status": "success",
  "count": 10,
  "recommendations": [
    {
      "ticker": "SBIN.NS",
      "signal": "BUY",
      "confidence": 85,
      "current_price": 500.5,
      "entry_price": 502.0,
      "stop_loss": 480.0,
      "take_profit": 530.0,
      "expected_profit": 1500.0,
      "reasons": ["RSI oversold", "MACD bullish"]
    }
  ]
}
```

### Get Portfolio Status

```bash
curl http://localhost:5000/api/portfolio
```

## 🔧 Troubleshooting

### No WhatsApp Alerts?

- Check `.env` has valid `WHATSAPP_API_KEY`
- Verify Twilio account is active
- Check phone number format: `+919999999999`

### No Email Alerts?

- Generate Gmail App Password (not regular password)
- Enable "Less secure app access" if needed
- Check email credentials in `.env`

### Slow Analysis?

- Reduce `limit` in `analyze_top_stocks()`
- Increase `ALERT_INTERVAL_MINUTES`
- Use caching for faster results

### Database Issues?

- Delete `data/trades.db` to reset
- Run `init_db()` again
- Check database path in `config.py`

## ⚠️ Important Disclaimers

1. **No Guarantee**: Past performance ≠ future results
2. **Market Risk**: Stocks can go down, you can lose money
3. **AI Generated**: Not a financial advisor, do your research
4. **Backtest First**: Test on historical data before live trading
5. **Position Size**: Start small, scale up gradually
6. **Stop Losses**: Always use, don't override

## 📚 Additional Resources

- [Technical Analysis Guide](https://www.investopedia.com/terms/t/technicalanalysis.asp)
- [Risk Management](https://www.moneycontrol.com/)
- [NSE Market Hours](https://www.nseindia.com/)
- [Trading Psychology](https://www.tradingview.com/)

## 🤝 Support

For issues or feature requests:

1. Check logs in `logs/stock_agent.log`
2. Review this README
3. Run `python -m pytest` for tests

## 📄 License

MIT License - Use freely, modify as needed

---

**Happy Trading!** 🚀📈

Remember: Small consistent profits beat risky big trades.
