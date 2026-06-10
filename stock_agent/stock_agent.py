"""
Main Stock Market Agent
Orchestrates data fetching, analysis, and alerts
"""

import logging
from datetime import datetime, time
import schedule
import time as time_module
from typing import Dict, List
import json
from data_fetcher import NSEDataFetcher
from analysis_engine import TechnicalAnalyzer, RiskManager
from alert_manager import AlertManager
from models import (
    Session, StockRecommendation, Trade, AlertLog, 
    add_recommendation, add_trade, close_trade, get_portfolio_performance, init_db
)
from config import (
    TOTAL_INVESTMENT, ALERT_INTERVAL_MINUTES, TRADING_START_TIME, 
    TRADING_END_TIME, LOG_DIR, LOG_LEVEL, MARKET_NAME
)
import os

# Setup logging
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{LOG_DIR}/stock_agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class StockMarketAgent:
    """Main agent for stock market analysis and alerts"""
    
    def __init__(self, investment: float = TOTAL_INVESTMENT):
        self.investment = investment
        self.fetcher = NSEDataFetcher()
        self.analyzer = TechnicalAnalyzer()
        self.risk_manager = RiskManager()
        self.alert_manager = AlertManager()
        self.session = Session()
        
        logger.info(f"StockMarketAgent initialized with {MARKET_NAME} analysis")
        logger.info(f"Total Investment: ₹{investment:,.2f}")
    
    def is_market_open(self) -> bool:
        """Check if market is open"""
        now = datetime.now().time()
        return TRADING_START_TIME <= now <= TRADING_END_TIME
    
    def analyze_stock(self, ticker: str) -> Dict:
        """
        Analyze a single stock
        
        Returns:
            Complete analysis with signal, prices, and recommendations
        """
        try:
            logger.info(f"Analyzing {ticker}...")
            
            # Fetch data
            data = self.fetcher.fetch_historical_data(ticker, period="3mo")
            latest_info = self.fetcher.fetch_latest_price(ticker)
            
            if data.empty or not latest_info:
                logger.warning(f"No data for {ticker}")
                return None
            
            # Generate signal
            signal_data = self.analyzer.generate_signal(data)
            
            # Calculate entry/exit prices
            current_price = latest_info['price']
            entry_exit = self.risk_manager.calculate_entry_exit(
                current_price,
                self.investment / 20  # Divide into 20 positions
            )
            
            # Combine analysis
            analysis = {
                'ticker': ticker,
                'signal': signal_data['signal'],
                'confidence': signal_data['confidence'],
                'current_price': current_price,
                'entry_price': entry_exit['entry_price'],
                'stop_loss': entry_exit['stop_loss'],
                'take_profit': entry_exit['take_profit'],
                'quantity': entry_exit['quantity'],
                'actual_investment': entry_exit['actual_investment'],
                'expected_profit': entry_exit['expected_profit'],
                'max_loss': entry_exit['max_loss_amount'],
                'reasons': signal_data['reasons'],
                'indicators': signal_data['indicators'],
                'latest_price_info': latest_info,
                'analysis_timestamp': datetime.now()
            }
            
            logger.info(f"✅ {ticker}: {signal_data['signal']} (Confidence: {signal_data['confidence']}%)")
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing {ticker}: {e}")
            return None
    
    def analyze_top_stocks(self, limit: int = 20) -> List[Dict]:
        """Analyze top stocks and return ranked by confidence"""
        try:
            logger.info(f"Analyzing top {limit} stocks...")
            
            analyses = []
            tickers = self.fetcher.nse_tickers[:limit]
            
            for ticker in tickers:
                analysis = self.analyze_stock(ticker)
                if analysis:
                    analyses.append(analysis)
            
            # Sort by confidence and signal strength
            def score_analysis(a):
                signal_score = {'BUY': 3, 'HOLD': 1, 'SELL': 0}.get(a['signal'], 0)
                return (signal_score, a['confidence'])
            
            ranked_analyses = sorted(analyses, key=score_analysis, reverse=True)
            
            logger.info(f"Analyzed {len(ranked_analyses)} stocks successfully")
            return ranked_analyses
            
        except Exception as e:
            logger.error(f"Error in batch analysis: {e}")
            return []
    
    def process_recommendations(self, analyses: List[Dict]) -> None:
        """Process and store recommendations, send alerts"""
        try:
            buy_signals = []
            sell_signals = []
            
            for analysis in analyses:
                if not analysis:
                    continue
                
                ticker = analysis['ticker']
                signal = analysis['signal']
                
                # Store recommendation
                try:
                    rec_id = add_recommendation(
                        ticker=ticker,
                        signal=signal,
                        confidence=analysis['confidence'],
                        current_price=analysis['current_price'],
                        entry_price=analysis['entry_price'],
                        stop_loss=analysis['stop_loss'],
                        take_profit=analysis['take_profit'],
                        expected_profit=analysis['expected_profit'],
                        quantity=analysis['quantity'],
                        reasons=json.dumps(analysis['reasons']),
                        indicators=json.dumps({k: float(v) if isinstance(v, (int, float)) else v 
                                             for k, v in analysis['indicators'].items()})
                    )
                    
                    # Categorize signals
                    if signal == 'BUY' and analysis['confidence'] >= 75:
                        buy_signals.append(analysis)
                    elif signal == 'SELL' and analysis['confidence'] >= 75:
                        sell_signals.append(analysis)
                    
                    # Send alert for high-confidence signals
                    if (signal in ['BUY', 'SELL']) and analysis['confidence'] >= 80:
                        alert_sent = AlertManager.send_stock_alert(analysis)
                        if alert_sent:
                            logger.info(f"✅ Alert sent for {ticker}")
                
                except Exception as e:
                    logger.error(f"Error processing {ticker}: {e}")
            
            # Send summary alert
            if len(analyses) > 0:
                top_pick = analyses[0] if analyses else None
                AlertManager.send_daily_summary(
                    stocks_analyzed=len(analyses),
                    buy_signals=len(buy_signals),
                    sell_signals=len(sell_signals),
                    top_pick=top_pick
                )
            
            logger.info(f"📊 Summary: {len(buy_signals)} BUY, {len(sell_signals)} SELL signals")
            
        except Exception as e:
            logger.error(f"Error processing recommendations: {e}")
    
    def hourly_analysis(self) -> None:
        """Run hourly analysis during market hours"""
        if not self.is_market_open():
            logger.info("⏰ Market is closed. Skipping analysis.")
            return
        
        logger.info("🔍 Starting hourly analysis...")
        
        # Analyze top stocks
        analyses = self.analyze_top_stocks(limit=30)
        
        # Process recommendations and send alerts
        self.process_recommendations(analyses)
        
        logger.info("✅ Hourly analysis complete")
    
    def start_monitoring(self) -> None:
        """Start the monitoring loop"""
        logger.info("=" * 50)
        logger.info("🚀 STOCK MARKET AGENT STARTED")
        logger.info(f"Investment: ₹{self.investment:,.2f}")
        logger.info(f"Market: {MARKET_NAME}")
        logger.info(f"Alert Interval: Every {ALERT_INTERVAL_MINUTES} minutes")
        logger.info(f"Trading Hours: {TRADING_START_TIME} - {TRADING_END_TIME}")
        logger.info("=" * 50)
        
        try:
            # Schedule hourly analysis
            schedule.every(ALERT_INTERVAL_MINUTES).minutes.do(self.hourly_analysis)
            
            # Run initial analysis
            self.hourly_analysis()
            
            # Keep running
            logger.info("📅 Scheduler started. Waiting for next scheduled time...")
            while True:
                schedule.run_pending()
                time_module.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            logger.info("⏹️ Agent stopped by user")
        except Exception as e:
            logger.error(f"Error in monitoring loop: {e}")
    
    def get_portfolio_status(self) -> Dict:
        """Get current portfolio status"""
        try:
            performance = get_portfolio_performance()
            return {
                'status': 'success',
                'portfolio': performance,
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"Error getting portfolio status: {e}")
            return {'status': 'error', 'message': str(e)}
    
    def display_recommendations(self, top_n: int = 10) -> None:
        """Display top recommendations in a formatted way"""
        try:
            analyses = self.analyze_top_stocks(limit=top_n * 2)
            
            print("\n" + "="*80)
            print(f"🔝 TOP {top_n} STOCK RECOMMENDATIONS")
            print("="*80)
            
            for i, analysis in enumerate(analyses[:top_n], 1):
                signal = analysis['signal']
                signal_emoji = {'BUY': '🟢', 'SELL': '🔴', 'HOLD': '🟡'}.get(signal, '❓')
                
                print(f"\n{i}. {signal_emoji} {analysis['ticker']}")
                print(f"   Signal: {signal} ({analysis['confidence']}% confidence)")
                print(f"   Current Price: ₹{analysis['current_price']:.2f}")
                print(f"   Entry: ₹{analysis['entry_price']:.2f} | SL: ₹{analysis['stop_loss']:.2f} | TP: ₹{analysis['take_profit']:.2f}")
                print(f"   Expected Profit: ₹{analysis['expected_profit']:.2f} | Risk: ₹{analysis['max_loss']:.2f}")
                print(f"   Reasons: {', '.join(analysis['reasons'][:2])}...")
            
            print("\n" + "="*80)
            
        except Exception as e:
            logger.error(f"Error displaying recommendations: {e}")


# Example usage and initialization
if __name__ == "__main__":
    # Initialize database
    init_db()
    
    # Create and run agent
    agent = StockMarketAgent(investment=500000)
    
    # Show recommendations
    agent.display_recommendations(top_n=10)
    
    # Start monitoring (will run hourly)
    # Uncomment to start live monitoring:
    # agent.start_monitoring()
