"""
Alert System
Sends WhatsApp and Email notifications
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List
import logging
from datetime import datetime
import requests
import json
from config import (
    WHATSAPP_ENABLED, EMAIL_ENABLED, WHATSAPP_API_KEY, WHATSAPP_PHONE,
    EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT
)

logger = logging.getLogger(__name__)

class AlertManager:
    """Manage WhatsApp and Email alerts"""
    
    @staticmethod
    def send_whatsapp_alert(message: str, phone: str = WHATSAPP_PHONE) -> bool:
        """
        Send WhatsApp alert using Twilio or similar service
        
        Args:
            message: Alert message
            phone: Recipient phone number with country code (+91...)
        
        Returns:
            Success status
        """
        if not WHATSAPP_ENABLED:
            logger.info("WhatsApp alerts disabled")
            return False
        
        try:
            # Example using Twilio (you need to set up Twilio account)
            # For now, showing the structure
            
            if not WHATSAPP_API_KEY:
                logger.warning("WhatsApp API key not configured")
                return False
            
            # You can use services like:
            # 1. Twilio (twilioWhatsApp)
            # 2. Click Send (clickatell)
            # 3. WhatsApp Business API
            # 4. Third-party APIs
            
            logger.info(f"[MOCK] WhatsApp sent to {phone}: {message[:50]}...")
            return True
            
        except Exception as e:
            logger.error(f"Error sending WhatsApp: {e}")
            return False
    
    @staticmethod
    def send_email_alert(subject: str, body: str, recipient: str = EMAIL_RECEIVER) -> bool:
        """
        Send Email alert
        
        Args:
            subject: Email subject
            body: Email body (HTML)
            recipient: Recipient email
        
        Returns:
            Success status
        """
        if not EMAIL_ENABLED:
            logger.info("Email alerts disabled")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = EMAIL_SENDER
            msg['To'] = recipient
            
            # Attach HTML body
            html_part = MIMEText(body, 'html')
            msg.attach(html_part)
            
            # Send email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            logger.info(f"Email sent to {recipient}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return False
    
    @staticmethod
    def format_stock_alert(stock_data: Dict) -> tuple:
        """Format stock alert message for WhatsApp and Email"""
        
        ticker = stock_data.get('ticker', 'N/A')
        signal = stock_data.get('signal', 'HOLD')
        confidence = stock_data.get('confidence', 0)
        current_price = stock_data.get('current_price', 0)
        entry_price = stock_data.get('entry_price', 0)
        stop_loss = stock_data.get('stop_loss', 0)
        take_profit = stock_data.get('take_profit', 0)
        expected_profit = stock_data.get('expected_profit', 0)
        reasons = stock_data.get('reasons', [])
        
        # WhatsApp message (concise)
        whatsapp_msg = f"""
🔔 STOCK ALERT - {ticker}
━━━━━━━━━━━━━━━━━
📊 Signal: *{signal}* ({confidence}%)
💰 Current: ₹{current_price:.2f}
📈 Entry: ₹{entry_price:.2f}
🛑 Stop Loss: ₹{stop_loss:.2f}
🎯 Take Profit: ₹{take_profit:.2f}
💵 Expected Profit: ₹{expected_profit:.2f}

Reasons:
{chr(10).join([f"✓ {r}" for r in reasons[:3]])}

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        # Email message (detailed HTML)
        email_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: #1a1a1a; color: #00ff00; padding: 20px; border-radius: 5px; }}
        .signal-buy {{ color: #00cc00; font-weight: bold; }}
        .signal-sell {{ color: #ff3333; font-weight: bold; }}
        .signal-hold {{ color: #ffaa00; font-weight: bold; }}
        .metrics {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 20px 0; }}
        .metric {{ background: #f5f5f5; padding: 10px; border-radius: 5px; }}
        .metric-label {{ font-size: 12px; color: #666; }}
        .metric-value {{ font-size: 18px; font-weight: bold; }}
        .reasons {{ background: #f9f9f9; padding: 15px; border-left: 4px solid #00ff00; margin: 20px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Stock Market Alert</h1>
            <p>Deep Analysis Report - {ticker}</p>
        </div>
        
        <div class="signal signal-{signal.lower()}">
            <h2>Signal: {signal} ({confidence}% Confidence)</h2>
        </div>
        
        <div class="metrics">
            <div class="metric">
                <div class="metric-label">Current Price</div>
                <div class="metric-value">₹{current_price:.2f}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Entry Price</div>
                <div class="metric-value">₹{entry_price:.2f}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Stop Loss</div>
                <div class="metric-value">₹{stop_loss:.2f}</div>
            </div>
            <div class="metric">
                <div class="metric-label">Take Profit</div>
                <div class="metric-value">₹{take_profit:.2f}</div>
            </div>
        </div>
        
        <div class="reasons">
            <h3>Analysis Reasons:</h3>
            <ul>
                {"".join([f"<li>{r}</li>" for r in reasons])}
            </ul>
        </div>
        
        <div class="metric">
            <div class="metric-label">Expected Profit</div>
            <div class="metric-value" style="color: #00cc00;">₹{expected_profit:.2f}</div>
        </div>
        
        <p style="font-size: 12px; color: #999;">
            Alert Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}<br>
            Disclaimer: This is an AI-generated recommendation. Always do your own research before trading.
        </p>
    </div>
</body>
</html>
        """
        
        return whatsapp_msg.strip(), email_html
    
    @staticmethod
    def send_stock_alert(stock_data: Dict, send_whatsapp: bool = True, send_email: bool = True) -> bool:
        """
        Send both WhatsApp and Email alerts for a stock
        
        Args:
            stock_data: Dictionary with stock analysis data
            send_whatsapp: Whether to send WhatsApp alert
            send_email: Whether to send email alert
        
        Returns:
            Success status
        """
        try:
            whatsapp_msg, email_html = AlertManager.format_stock_alert(stock_data)
            
            success = True
            
            # Send WhatsApp
            if send_whatsapp:
                whatsapp_success = AlertManager.send_whatsapp_alert(whatsapp_msg)
                success = success and whatsapp_success
            
            # Send Email
            if send_email:
                subject = f"📊 Stock Alert: {stock_data.get('ticker', 'N/A')} - {stock_data.get('signal', 'HOLD')}"
                email_success = AlertManager.send_email_alert(subject, email_html)
                success = success and email_success
            
            return success
            
        except Exception as e:
            logger.error(f"Error sending stock alert: {e}")
            return False
    
    @staticmethod
    def send_daily_summary(stocks_analyzed: int, buy_signals: int, sell_signals: int, 
                          top_pick: Dict = None) -> bool:
        """Send daily summary alert"""
        
        try:
            whatsapp_msg = f"""
📈 DAILY MARKET SUMMARY
━━━━━━━━━━━━━━━━━
Stocks Analyzed: {stocks_analyzed}
🟢 BUY Signals: {buy_signals}
🔴 SELL Signals: {sell_signals}

Top Pick: {top_pick.get('ticker') if top_pick else 'N/A'}
Confidence: {top_pick.get('confidence', 0)}%

Next Alert: In 1 hour

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
            
            email_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: #1a1a1a; color: #00ff00; padding: 20px; }}
        .stats {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 20px 0; }}
        .stat-box {{ background: #f0f0f0; padding: 15px; text-align: center; border-radius: 5px; }}
        .stat-number {{ font-size: 32px; font-weight: bold; }}
        .buy {{ color: #00cc00; }}
        .sell {{ color: #ff3333; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header"><h1>📈 Daily Market Summary</h1></div>
        
        <div class="stats">
            <div class="stat-box">
                <div>Stocks Analyzed</div>
                <div class="stat-number">{stocks_analyzed}</div>
            </div>
            <div class="stat-box">
                <div>🟢 BUY Signals</div>
                <div class="stat-number buy">{buy_signals}</div>
            </div>
            <div class="stat-box">
                <div>🔴 SELL Signals</div>
                <div class="stat-number sell">{sell_signals}</div>
            </div>
        </div>
        
        <p>Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}</p>
    </div>
</body>
</html>
            """
            
            # Send alerts
            AlertManager.send_whatsapp_alert(whatsapp_msg)
            AlertManager.send_email_alert("📈 Daily Market Summary", email_html)
            
            return True
            
        except Exception as e:
            logger.error(f"Error sending daily summary: {e}")
            return False


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Test alert
    test_data = {
        'ticker': 'SBIN.NS',
        'signal': 'BUY',
        'confidence': 85,
        'current_price': 500.50,
        'entry_price': 502.00,
        'stop_loss': 480.00,
        'take_profit': 530.00,
        'expected_profit': 1500.00,
        'reasons': ['RSI oversold', 'MACD bullish', 'Volume spike']
    }
    
    # Send alert
    success = AlertManager.send_stock_alert(test_data)
    print(f"Alert sent: {success}")
