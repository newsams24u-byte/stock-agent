"""
Stock Agent Configuration
Indian Market Analysis & Trading Alerts
"""

import os
from datetime import time

# ===== MARKET SETTINGS =====
MARKET_NAME = "NSE"
TRADING_START_TIME = time(9, 15)  # 9:15 AM IST
TRADING_END_TIME = time(15, 30)   # 3:30 PM IST
ALERT_INTERVAL_MINUTES = 60  # Alert every hour

# ===== INVESTMENT SETTINGS =====
TOTAL_INVESTMENT = 500000  # 5 lakhs
MAX_LOSS_PER_TRADE = 0.03  # 3% max loss per trade
TARGET_PROFIT_PERCENT = 0.05  # 5% target profit (after charges)
BROKERAGE_PERCENT = 0.0005  # 0.05% brokerage
TRANSACTION_CHARGE = 0.0001  # 0.01% transaction charge
GST_PERCENT = 0.18  # 18% GST on brokerage

# ===== ANALYSIS SETTINGS =====
SHORT_TERM_ANALYSIS_DAYS = 5  # 3-5 day plays
INTRADAY_CUTOFF_MINUTES = 1440  # Consider as intraday if less than this
MIN_VOLUME = 100000  # Minimum daily volume
MIN_PRICE = 10  # Minimum stock price
MAX_PRICE = 500  # Maximum stock price for penny stocks
MIN_MARKET_CAP = 100  # Min market cap in crores

# ===== TECHNICAL INDICATORS =====
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
MACD_SIGNAL_THRESHOLD = 0.02
VOLUME_MA_PERIOD = 20
PRICE_MA_PERIOD = 20

# ===== NOTIFICATION SETTINGS =====
WHATSAPP_ENABLED = True
EMAIL_ENABLED = True

# WhatsApp Settings (using Twilio or similar)
WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY", "")
WHATSAPP_PHONE = os.getenv("WHATSAPP_PHONE", "+919999999999")  # Your phone with +91

# Email Settings
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your-email@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")  # Gmail App Password
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "your-email@gmail.com")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ===== DATABASE SETTINGS =====
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///stock_agent/data/trades.db")

# ===== API SETTINGS =====
FINAPI_KEY = os.getenv("FINAPI_KEY", "")  # Financial API key
TIMEOUT = 30  # API timeout in seconds

# ===== LOGGING =====
LOG_DIR = "stock_agent/logs"
LOG_LEVEL = "INFO"

print("✅ Configuration loaded successfully")
