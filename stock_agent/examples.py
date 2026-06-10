"""
Example Usage of Stock Market Agent
Shows different ways to use the agent
"""

from stock_agent import StockMarketAgent, init_db
import json

def example_1_quick_analysis():
    """Example 1: Get quick recommendations"""
    print("\n" + "="*60)
    print("📊 EXAMPLE 1: Quick Stock Analysis")
    print("="*60)
    
    agent = StockMarketAgent(investment=500000)
    agent.display_recommendations(top_n=5)


def example_2_single_stock():
    """Example 2: Analyze a single stock"""
    print("\n" + "="*60)
    print("🔍 EXAMPLE 2: Single Stock Analysis")
    print("="*60)
    
    agent = StockMarketAgent()
    
    ticker = "SBIN"  # Without .NS extension
    analysis = agent.analyze_stock(f"{ticker}.NS")
    
    if analysis:
        print(f"\n📈 {ticker} Analysis:")
        print(f"  Signal: {analysis['signal']} ({analysis['confidence']}% confidence)")
        print(f"  Current Price: ₹{analysis['current_price']:.2f}")
        print(f"  Entry Price: ₹{analysis['entry_price']:.2f}")
        print(f"  Stop Loss: ₹{analysis['stop_loss']:.2f}")
        print(f"  Take Profit: ₹{analysis['take_profit']:.2f}")
        print(f"  Expected Profit: ₹{analysis['expected_profit']:.2f}")
        print(f"  Max Loss: ₹{analysis['max_loss']:.2f}")
        print(f"\n  Reasons for signal:")
        for reason in analysis['reasons']:
            print(f"    ✓ {reason}")
        
        print(f"\n  Technical Indicators:")
        indicators = analysis['indicators']
        print(f"    RSI: {indicators.get('rsi', 0):.2f}")
        print(f"    MACD: {indicators.get('macd', 0):.4f}")
        print(f"    Volume: {int(indicators.get('volume', 0)):,}")


def example_3_batch_analysis():
    """Example 3: Analyze multiple stocks at once"""
    print("\n" + "="*60)
    print("📊 EXAMPLE 3: Batch Stock Analysis")
    print("="*60)
    
    agent = StockMarketAgent()
    
    tickers = ["SBIN", "RELIANCE", "INFY", "TCS", "HDFC"]
    print(f"\nAnalyzing {len(tickers)} stocks...")
    
    for ticker in tickers:
        try:
            analysis = agent.analyze_stock(f"{ticker}.NS")
            if analysis:
                emoji = "🟢" if analysis['signal'] == "BUY" else "🔴" if analysis['signal'] == "SELL" else "🟡"
                print(f"{emoji} {ticker:10} | Signal: {analysis['signal']:4} | Confidence: {analysis['confidence']:3.0f}% | Expected: ₹{analysis['expected_profit']:8.0f}")
        except Exception as e:
            print(f"❌ {ticker:10} | Error: {str(e)[:30]}")


def example_4_portfolio_status():
    """Example 4: Check portfolio performance"""
    print("\n" + "="*60)
    print("💼 EXAMPLE 4: Portfolio Performance")
    print("="*60)
    
    agent = StockMarketAgent()
    status = agent.get_portfolio_status()
    
    if status['status'] == 'success':
        p = status['portfolio']
        print(f"\nPortfolio Summary:")
        print(f"  Total Investment: ₹{p['total_investment']:,.2f}")
        print(f"  Total Profit/Loss: ₹{p['total_profit']:,.2f}")
        print(f"  Total Trades: {p['total_trades']}")
        print(f"  Open Trades: {p['open_trades']}")
        print(f"  Closed Trades: {p['closed_trades']}")
        print(f"  Win Rate: {p['win_rate']:.2f}%")
        print(f"  Avg Profit/Trade: ₹{p['avg_profit_per_trade']:,.2f}")
    else:
        print("No portfolio data yet. Make some trades first!")


def example_5_custom_analysis():
    """Example 5: Custom analysis with different parameters"""
    print("\n" + "="*60)
    print("⚙️ EXAMPLE 5: Custom Analysis")
    print("="*60)
    
    # Create agent with custom investment
    investment_amounts = [100000, 500000, 1000000]
    
    for investment in investment_amounts:
        agent = StockMarketAgent(investment=investment)
        print(f"\n💰 Investment: ₹{investment:,}")
        
        # Analyze a stock
        analysis = agent.analyze_stock("RELIANCE.NS")
        if analysis:
            print(f"  Quantity can buy: {analysis['quantity']} shares")
            print(f"  Actual Investment: ₹{analysis['actual_investment']:,.2f}")
            print(f"  Expected Profit: ₹{analysis['expected_profit']:,.2f}")
            print(f"  Return on Investment: {(analysis['expected_profit']/analysis['actual_investment']*100):.2f}%")


def example_6_alert_demo():
    """Example 6: Demo alert system (without sending)"""
    print("\n" + "="*60)
    print("🔔 EXAMPLE 6: Alert System Demo")
    print("="*60)
    
    from alert_manager import AlertManager
    
    # Create sample stock data
    sample_stock = {
        'ticker': 'SBIN.NS',
        'signal': 'BUY',
        'confidence': 87,
        'current_price': 500.50,
        'entry_price': 502.00,
        'stop_loss': 480.00,
        'take_profit': 530.00,
        'expected_profit': 1500.00,
        'reasons': ['RSI oversold at 25', 'MACD bullish crossover', 'Volume spike 2.5x average']
    }
    
    # Generate alert messages (don't actually send)
    whatsapp_msg, email_html = AlertManager.format_stock_alert(sample_stock)
    
    print("\n📱 WhatsApp Alert Preview:")
    print("-" * 40)
    print(whatsapp_msg)
    
    print("\n📧 Email Alert (HTML) - First 300 chars:")
    print("-" * 40)
    print(email_html[:300] + "...")


def example_7_market_status():
    """Example 7: Check market status"""
    print("\n" + "="*60)
    print("📅 EXAMPLE 7: Market Status")
    print("="*60)
    
    agent = StockMarketAgent()
    is_open = agent.is_market_open()
    
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    
    print(f"\nCurrent Time: {current_time}")
    print(f"Market Status: {'🟢 OPEN' if is_open else '🔴 CLOSED'}")
    print(f"\nMarket Hours: 9:15 AM - 3:30 PM (IST)")
    print(f"Holidays: Weekends + NSE holidays")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("🚀 STOCK MARKET AGENT - EXAMPLES")
    print("="*60)
    
    # Initialize database
    print("\n📦 Initializing database...")
    try:
        init_db()
    except:
        pass  # Database might already exist
    
    try:
        example_1_quick_analysis()
        example_2_single_stock()
        example_3_batch_analysis()
        example_4_portfolio_status()
        example_5_custom_analysis()
        example_6_alert_demo()
        example_7_market_status()
        
        print("\n" + "="*60)
        print("✅ Examples completed!")
        print("="*60)
        print("\nNext steps:")
        print("1. Run: python web_app.py (for web dashboard)")
        print("2. Or: python stock_agent.py (for terminal output)")
        print("3. Edit config.py to customize parameters")
        print("4. Setup .env for WhatsApp/Email alerts")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
