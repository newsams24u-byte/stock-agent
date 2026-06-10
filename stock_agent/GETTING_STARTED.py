#!/usr/bin/env python3
"""
🚀 STOCK MARKET ANALYSIS AGENT - GETTING STARTED

This script provides a guided tour through the stock agent setup.
Run this to understand what was created and get started.
"""

def print_header(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def print_section(title):
    print(f"\n📌 {title}")
    print("-" * 70)

def main():
    print("""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║     📊 STOCK MARKET ANALYSIS & TRADING ALERT AGENT                  ║
    ║                      Welcome! 🚀                                     ║
    ║                                                                      ║
    ║     Indian Market (NSE) | Real-time Alerts | Risk Management       ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    print_header("✅ WHAT'S BEEN CREATED FOR YOU")
    
    print("""
    🔧 CORE SYSTEM:
       • Technical Analysis Engine (RSI, MACD, Bollinger Bands, ATR)
       • Deep Signal Generation with Confidence Scoring
       • Risk Management (Stop Loss, Take Profit, Position Sizing)
       • WhatsApp + Email Alert System
       • Web Dashboard (Real-time Monitoring)
       • SQLite Database with Trade Tracking
       • Automatic Hourly Analysis
    
    📁 PROJECT FILES:
       stock_agent/
       ├── config.py              - Configuration & settings
       ├── data_fetcher.py         - Fetch NSE stock data
       ├── analysis_engine.py      - Technical analysis & signals
       ├── alert_manager.py        - WhatsApp & Email alerts
       ├── models.py               - Database & ORM
       ├── stock_agent.py          - Main agent orchestrator
       ├── web_app.py              - Flask web dashboard
       ├── examples.py             - Usage examples
       └── templates/dashboard.html - Web UI
    
    📚 DOCUMENTATION:
       ├── README.md               - Full feature documentation
       ├── QUICKSTART.md           - 5-minute setup guide
       ├── DEPLOYMENT.md           - Cloud deployment options
       ├── SETUP_SUMMARY.md        - Complete overview
       └── This file!
    """)
    
    print_header("🎯 KEY FEATURES")
    
    features = [
        ("Deep Analysis", "6+ technical indicators per stock"),
        ("Entry Signals", "Automatic BUY/SELL/HOLD recommendations"),
        ("Risk Calc", "Auto stop-loss, take-profit, position size"),
        ("Alerts", "WhatsApp + Email with all key metrics"),
        ("Tracking", "Portfolio performance & trade history"),
        ("Web UI", "Real-time dashboard with charts"),
        ("Hourly", "Automatic analysis every hour"),
        ("NSE", "30+ popular Indian stocks")
    ]
    
    for feature, desc in features:
        print(f"  ✓ {feature:15} → {desc}")
    
    print_header("🚀 QUICK START (Choose One)")
    
    print("""
    OPTION 1: WEB DASHBOARD (Recommended) ⭐
    ────────────────────────────────────
    $ python3 web_app.py
    Then open: http://localhost:5000
    
    Features:
    - See top 15 stock recommendations
    - Click "Analyze Now" for fresh analysis
    - View portfolio performance
    - Monitor alerts
    - Beautiful dark theme UI
    
    
    OPTION 2: COMMAND LINE ANALYSIS
    ──────────────────────────────
    $ python3 -c "
    from stock_agent import StockMarketAgent
    agent = StockMarketAgent()
    agent.display_recommendations(top_n=10)
    "
    
    Shows:
    - Top 10 stocks with signals
    - Entry, Stop Loss, Take Profit prices
    - Expected profit & max loss
    - Analysis reasons
    
    
    OPTION 3: AUTOMATED MONITORING
    ──────────────────────────────
    $ python3 -c "
    from stock_agent import StockMarketAgent
    agent = StockMarketAgent()
    agent.start_monitoring()
    "
    
    Does:
    - Runs hourly analysis (24/7)
    - Sends WhatsApp/Email alerts
    - Tracks all recommendations
    - Logs everything
    
    
    OPTION 4: INTERACTIVE SETUP
    ──────────────────────────
    $ bash run.sh
    
    Menu-driven setup:
    - Choose your preferred mode
    - Get guided configuration
    - Run agent with one click
    """)
    
    print_header("📊 EXAMPLE: FIRST TRADE")
    
    print("""
    Stock:                SBIN.NS
    Signal:               🟢 BUY (85% confidence)
    Current Price:        ₹500.50
    ────────────────────────────────
    Entry Price:          ₹502.00 (includes charges)
    Stop Loss:            ₹485.00 (3% loss limit)
    Take Profit:          ₹530.00 (5% profit target)
    ────────────────────────────────
    Your Investment:      ₹25,000 (5% of ₹5 lakh)
    Shares to Buy:        49 shares
    Max Loss:             ₹500 (2%)
    Max Profit:           ₹1,400 (5.6%)
    Risk:Reward:          1:2.8
    ────────────────────────────────
    
    📱 You'll get alert:
    
    🔔 STOCK ALERT - SBIN.NS
    ━━━━━━━━━━━━━━━━━━━━━
    📊 Signal: BUY (85%)
    💰 Current: ₹500.50
    📈 Entry: ₹502.00
    🛑 Stop Loss: ₹485.00
    🎯 Take Profit: ₹530.00
    💵 Expected Profit: ₹1,400.00
    
    ✓ RSI oversold (25)
    ✓ MACD bullish crossover
    ✓ Volume spike (2.5x)
    """)
    
    print_header("⚙️ SETUP & CONFIGURATION")
    
    print("""
    STEP 1: Install Dependencies
    ──────────────────────────
    cd stock_agent
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    
    STEP 2: Configure (Optional but Recommended)
    ────────────────────────────────────────
    cp .env.example .env
    
    Edit .env with:
    - EMAIL_SENDER=your@gmail.com
    - EMAIL_PASSWORD=google_app_password
    - WHATSAPP_PHONE=+919999999999
    - WHATSAPP_API_KEY=twilio_key
    
    
    STEP 3: Customize Settings (Optional)
    ──────────────────────────────────
    Edit config.py:
    - TOTAL_INVESTMENT = 500000  # Your capital
    - MAX_LOSS_PER_TRADE = 0.03  # 3% risk
    - TARGET_PROFIT_PERCENT = 0.05  # 5% target
    - ALERT_INTERVAL_MINUTES = 60  # Every hour
    
    
    STEP 4: Run Agent
    ───────────────
    python3 web_app.py
    # or any option from "Quick Start" section above
    """)
    
    print_header("💰 INVESTMENT STRATEGY")
    
    print("""
    CAPITAL ALLOCATION:
    ──────────────────
    Total Capital:        ₹5,00,000
    Per Trade:            ₹25,000 (5%)
    Max Loss Per Trade:   ₹500 (2%)
    Number of Trades:     20
    
    
    DAILY TRADING:
    ──────────────
    Morning (9:30):  Check alerts, enter at signal
    Afternoon (14:30): Exit at SL or TP
    Next Hour:       New alert comes
    Repeat:          5-8 trades per day
    
    
    PROFIT TARGETS:
    ──────────────
    2 trades at TP:    ₹2,800 profit
    3 trades at TP:    ₹4,200 profit
    4 trades at TP:    ₹5,600 profit
    1 trade SL:        -₹500
    
    Realistic Daily:   ₹1,500-2,500
    Monthly:           ₹30,000-50,000
    Annual:            ₹3-6 lakhs
    """)
    
    print_header("✅ BEFORE YOU START LIVE TRADING")
    
    checklist = [
        "✓ Run web dashboard or examples.py",
        "✓ Review 5-10 recommendations",
        "✓ Understand entry/SL/TP logic",
        "✓ Paper trade for 3-5 days",
        "✓ Check recommendation accuracy",
        "✓ Setup alerts (optional but recommended)",
        "✓ Start with small position size",
        "✓ Monitor first 10 trades carefully",
        "✓ Keep detailed records",
        "✓ Never override stop-losses"
    ]
    
    for item in checklist:
        print(f"  {item}")
    
    print_header("📚 DOCUMENTATION & EXAMPLES")
    
    print("""
    README.md
    ─────────
    - Complete feature list
    - All API endpoints
    - Advanced configuration
    - Troubleshooting guide
    
    
    QUICKSTART.md
    ─────────────
    - 5-minute setup
    - First trade example
    - Common issues
    
    
    DEPLOYMENT.md
    ─────────────
    - Deploy to Heroku
    - Deploy to AWS
    - Docker deployment
    - Production setup
    
    
    examples.py
    ───────────
    Run to see:
    - Quick analysis
    - Single stock analysis
    - Batch analysis
    - Portfolio status
    - Custom analysis
    - Alert formatting
    - Market status
    
    $ python3 examples.py
    """)
    
    print_header("⚠️ IMPORTANT REMINDERS")
    
    print("""
    DO'S:
    ────
    ✓ Use stop-losses on ALL trades
    ✓ Scale up gradually
    ✓ Keep detailed records
    ✓ Review signals before trading
    ✓ Take profits at targets
    ✓ Diversify across 10-20 stocks
    
    
    DON'Ts:
    ───────
    ✗ Override system recommendations
    ✗ Add to losing trades
    ✗ Trade all capital at once
    ✗ Use leverage/margin
    ✗ Ignore risk management
    ✗ Trade during illiquid hours
    
    
    RISK DISCLAIMER:
    ────────────────
    This is NOT investment advice. Markets can go down.
    You can lose money. Do your own research.
    Start small. Scale gradually. Manage risk.
    """)
    
    print_header("🚀 NEXT STEPS")
    
    print("""
    IMMEDIATE (Right Now):
    ─────────────────────
    1. Run: python3 web_app.py
    2. Open: http://localhost:5000
    3. Click: "Analyze Now"
    4. Review: Top 10 recommendations
    
    
    TODAY:
    ──────
    1. Read: QUICKSTART.md (5 mins)
    2. Understand: Example trade logic
    3. Test: Analyze 2-3 stocks manually
    4. Setup: Email credentials (optional)
    
    
    THIS WEEK:
    ──────────
    1. Paper trade for 3-5 days
    2. Check recommendation accuracy
    3. Monitor wins vs losses
    4. Refine parameters if needed
    
    
    THEN:
    ─────
    1. Start live trading (small positions)
    2. Scale up gradually
    3. Keep detailed records
    4. Review results weekly
    """)
    
    print_header("📞 HELP & SUPPORT")
    
    print("""
    Can't find something?
    ──────────────────
    1. Check README.md (most detailed)
    2. Check QUICKSTART.md (quick help)
    3. Check examples.py (see it in action)
    4. Check logs/stock_agent.log (error messages)
    
    
    Common Issues:
    ──────────────
    "Port 5000 already in use"
    → python3 web_app.py --port 5001
    
    "No data for stock"
    → Check internet, wait, try again
    
    "Email not sending"
    → Use Gmail App Password, not regular password
    
    "Slow analysis"
    → Reduce limit or run during off-hours
    """)
    
    print("""
    
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║                    YOU'RE ALL SET! 🎉                               ║
    ║                                                                      ║
    ║              Ready to analyze the market?                           ║
    ║                                                                      ║
    ║              Next command:                                          ║
    ║              $ python3 web_app.py                                   ║
    ║                                                                      ║
    ║              Then open: http://localhost:5000                      ║
    ║                                                                      ║
    ║              Happy Trading! 📈💰                                    ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    
    """)

if __name__ == "__main__":
    main()
