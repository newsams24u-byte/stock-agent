"""
Stock Data Fetcher for Indian Markets (NSE)
Fetches real-time and historical data
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)

class NSEDataFetcher:
    """Fetch stock data from NSE India"""
    
    def __init__(self):
        self.nse_tickers = self._get_popular_nse_stocks()
    
    def _get_popular_nse_stocks(self) -> List[str]:
        """Get list of popular NSE stocks for analysis"""
        # Popular penny stocks and mid-cap stocks in India
        penny_stocks = [
            "SBIN.NS", "BAJAJFINSV.NS", "MARUTI.NS", "RELIANCE.NS", 
            "TATASTEEL.NS", "INDIGO.NS", "ADANIPORTS.NS", "ASIANPAINT.NS",
            "WIPRO.NS", "TECHM.NS", "INFY.NS", "ICICIBANK.NS", "HDFC.NS",
            "LT.NS", "SUNPHARMA.NS", "TITAN.NS", "BRITANNIA.NS", "NESTLEIND.NS",
            "BAJAJFINSV.NS", "HDFCLIFE.NS", "SBILIFE.NS", "IRCTC.NS", 
            "NYKAA.NS", "FSL.NS", "PAYTM.NS", "ZEEL.NS", "IDEA.NS",
            "INDUSINDBK.NS", "AXISBANK.NS", "KOTAKBANK.NS", "HDFCBANK.NS"
        ]
        return penny_stocks
    
    def fetch_historical_data(self, ticker: str, period: str = "1mo") -> pd.DataFrame:
        """
        Fetch historical OHLCV data
        
        Args:
            ticker: Stock ticker (e.g., "SBIN.NS")
            period: "1mo", "3mo", "1y", etc.
        
        Returns:
            DataFrame with OHLCV data
        """
        try:
            data = yf.download(ticker, period=period, progress=False)
            if data.empty:
                logger.warning(f"No data fetched for {ticker}")
                return pd.DataFrame()
            data['Ticker'] = ticker
            return data
        except Exception as e:
            logger.error(f"Error fetching data for {ticker}: {e}")
            return pd.DataFrame()
    
    def fetch_latest_price(self, ticker: str) -> Dict:
        """Get latest price and info"""
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            history = stock.history(period="1d")
            
            if history.empty:
                return {}
            
            latest = history.iloc[-1]
            return {
                'ticker': ticker,
                'price': latest['Close'],
                'open': latest['Open'],
                'high': latest['High'],
                'low': latest['Low'],
                'volume': latest['Volume'],
                'market_cap': info.get('marketCap', 0),
                'pe_ratio': info.get('trailingPE', 0),
                'dividend_yield': info.get('dividendYield', 0),
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"Error fetching latest price for {ticker}: {e}")
            return {}
    
    def fetch_batch_stocks(self, tickers: List[str], period: str = "1mo") -> Dict[str, pd.DataFrame]:
        """Fetch data for multiple stocks"""
        data_dict = {}
        for ticker in tickers:
            data = self.fetch_historical_data(ticker, period)
            if not data.empty:
                data_dict[ticker] = data
        return data_dict
    
    def get_top_gainers(self, limit: int = 10) -> List[Dict]:
        """Get top gaining stocks (dummy for now, needs integration with scraper)"""
        # This would typically scrape NSE website or use a paid API
        # For now, return popular stocks
        gainers = []
        for ticker in self.nse_tickers[:limit]:
            data = self.fetch_latest_price(ticker)
            if data:
                gainers.append(data)
        return gainers
    
    def get_volume_spikes(self, ticker: str, days: int = 5, spike_threshold: float = 1.5) -> bool:
        """Detect volume spikes (potential breakout)"""
        try:
            data = self.fetch_historical_data(ticker, period="3mo")
            if len(data) < days:
                return False
            
            recent_volume = data['Volume'].iloc[-1]
            avg_volume = data['Volume'].iloc[-days:-1].mean()
            
            return recent_volume > (avg_volume * spike_threshold)
        except Exception as e:
            logger.error(f"Error detecting volume spikes for {ticker}: {e}")
            return False


# Example usage
if __name__ == "__main__":
    fetcher = NSEDataFetcher()
    
    # Test fetch
    data = fetcher.fetch_historical_data("SBIN.NS", period="1mo")
    print(f"Fetched {len(data)} records for SBIN.NS")
    
    # Test latest price
    latest = fetcher.fetch_latest_price("RELIANCE.NS")
    print(f"Latest RELIANCE price: ₹{latest.get('price', 0):.2f}")
