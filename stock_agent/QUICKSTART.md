# 🚀 Quick Start Guide - Stock Market Agent

Get your stock analysis agent running in **5 minutes**!

## Step 1: Install Dependencies (1 minute)

```bash
cd stock_agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 2: Setup Configuration (2 minutes)

### Option A: Basic Setup (No Alerts)

```bash
# Just skip alerts for now
# Edit config.py:
WHATSAPP_ENABLED = False
EMAIL_ENABLED = False
```

### Option B: Full Setup with Alerts

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials:
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password  # from myaccount.google.com/apppasswords
WHATSAPP_API_KEY=your_twilio_key
WHATSAPP_PHONE=+919999999999  # Your phone with +91
```

## Step 3: Run the Agent (2 minutes)

### Option 1: Web Dashboard (Recommended)

```bash
python web_app.py
# Open http://localhost:5000 in your browser
```

### Option 2: Quick Analysis

```bash
python stock_agent.py
# Shows top 10 recommendations in terminal
```

### Option 3: Continuous Monitoring

```bash
python -c "
from stock_agent import StockMarketAgent
agent = StockMarketAgent(investment=500000)
agent.start_monitoring()  # Runs hourly analysis
"
```

## ✅ What You'll See

### Web Dashboard Shows:

- ✅ Top 15 stock recommendations
- ✅ Entry, Stop Loss, Take Profit prices
- ✅ Expected profit & max risk
- ✅ Portfolio performance
- ✅ Real-time analysis

### Console Output Shows:

```
🟢 SBIN.NS
   Signal: BUY (85% confidence)
   Current: ₹500.50
   Entry: ₹502.00 | SL: ₹480.00 | TP: ₹530.00
   Expected Profit: ₹1,500 | Max Loss: ₹500

🟡 RELIANCE.NS
   Signal: HOLD (65% confidence)
   ...
```

## 🎯 First Trade Example

**Stock**: SBIN.NS  
**Signal**: BUY (85% confidence)  
**Investment**: ₹25,000 (5% of ₹5 lakh)

**Prices**:

- Entry: ₹502
- Stop Loss: ₹485 (Risk: ₹500)
- Take Profit: ₹530 (Profit: ₹1,400)

**Expected Outcome**:

- Best Case: +₹1,400 (5.6% return)
- Worst Case: -₹500 (2% loss)
- Break Even: ₹502

## 📊 Key Metrics Explained

| Metric              | Meaning                | Example |
| ------------------- | ---------------------- | ------- |
| **Signal**          | BUY/SELL/HOLD          | BUY     |
| **Confidence**      | Signal strength 0-100% | 85%     |
| **Entry Price**     | Where to buy           | ₹502    |
| **Stop Loss**       | Exit if price falls    | ₹485    |
| **Take Profit**     | Target selling price   | ₹530    |
| **Expected Profit** | Potential gain         | ₹1,400  |
| **Max Loss**        | Potential loss         | ₹500    |

## 🔄 Typical Trading Cycle

1. **Alert**: You get a WhatsApp/Email alert
2. **Analyze**: Check the web dashboard
3. **Execute**: Place buy order at suggested entry
4. **Monitor**: Set alerts for SL and TP
5. **Exit**: Sell at TP or SL (automatic in real system)
6. **Record**: Profit/loss is logged
7. **Repeat**: Next alert in 1 hour

## ⚙️ Customization

### Change Investment Amount

```python
agent = StockMarketAgent(investment=1000000)  # 10 lakhs
```

### Change Alert Interval

Edit `config.py`:

```python
ALERT_INTERVAL_MINUTES = 30  # Alert every 30 mins (instead of 60)
```

### Change Target Profit

Edit `config.py`:

```python
TARGET_PROFIT_PERCENT = 0.10  # 10% target (instead of 5%)
```

## 🐛 Troubleshooting

### "No data for SBIN.NS"

- Check internet connection
- Verify ticker symbol (ends with .NS for NSE)
- Try again in a few seconds

### "Email not sending"

- Check Gmail credentials in `.env`
- Ensure App Password is used (not regular password)
- Check if 2FA is enabled on Gmail

### "Port 5000 already in use"

```bash
python web_app.py --port 5001
```

### No alerts during market hours?

- Verify `WHATSAPP_ENABLED` or `EMAIL_ENABLED` is True
- Check `.env` credentials
- Run manual analysis: click "Analyze Now" button

## 📈 Sample Strategy

**Investment**: ₹5 lakhs  
**Per Trade**: ₹25,000 (5% position)  
**Risk**: ₹500 per trade (2% max)  
**Target**: ₹2,000-5,000/day

### Daily Targets

- 2 trades at TP = ₹2,800 profit
- 3 trades at TP = ₹4,200 profit
- 4 trades with 1 SL = ₹2,600 profit

**Win Rate Needed**: 60%+ to be profitable

## 🎓 Next Steps

1. ✅ Run analysis and review recommendations
2. ✅ Read individual stock reasons
3. ✅ Backtest on historical data
4. ✅ Paper trade (no real money) for 1 week
5. ✅ Start live trading with small positions
6. ✅ Scale up gradually

## 📞 Support

**Issue**: Agent crashing  
**Solution**: Check `logs/stock_agent.log`

**Issue**: Slow recommendations  
**Solution**: Reduce `limit` parameter or run during off-hours

**Issue**: Inaccurate signals  
**Solution**: Review `README.md` risk management section

---

**Ready?** Let's make some money! 💰📈

Next: Run `python web_app.py` and open http://localhost:5000
