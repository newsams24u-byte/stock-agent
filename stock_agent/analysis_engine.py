"""
Technical Analysis Engine
Calculates indicators and generates trading signals
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, List
import logging
from config import (
    RSI_OVERBOUGHT, RSI_OVERSOLD, MAX_LOSS_PER_TRADE, 
    TARGET_PROFIT_PERCENT, BROKERAGE_PERCENT, TRANSACTION_CHARGE, GST_PERCENT
)

logger = logging.getLogger(__name__)

class TechnicalAnalyzer:
    """Perform technical analysis on stock data"""
    
    @staticmethod
    def calculate_rsi(data: pd.DataFrame, period: int = 14) -> pd.Series:
        """Calculate Relative Strength Index"""
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    @staticmethod
    def calculate_macd(data: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """Calculate MACD"""
        ema_fast = data['Close'].ewm(span=fast).mean()
        ema_slow = data['Close'].ewm(span=slow).mean()
        
        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal).mean()
        histogram = macd - signal_line
        
        return macd, signal_line, histogram
    
    @staticmethod
    def calculate_bollinger_bands(data: pd.DataFrame, period: int = 20, std_dev: int = 2) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """Calculate Bollinger Bands"""
        sma = data['Close'].rolling(window=period).mean()
        std = data['Close'].rolling(window=period).std()
        
        upper_band = sma + (std_dev * std)
        lower_band = sma - (std_dev * std)
        
        return upper_band, sma, lower_band
    
    @staticmethod
    def calculate_atr(data: pd.DataFrame, period: int = 14) -> pd.Series:
        """Calculate Average True Range (for volatility)"""
        high_low = data['High'] - data['Low']
        high_close = abs(data['High'] - data['Close'].shift())
        low_close = abs(data['Low'] - data['Close'].shift())
        
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        atr = true_range.rolling(period).mean()
        
        return atr
    
    @staticmethod
    def calculate_volume_ma(data: pd.DataFrame, period: int = 20) -> pd.Series:
        """Calculate Volume Moving Average"""
        return data['Volume'].rolling(window=period).mean()
    
    @staticmethod
    def detect_support_resistance(data: pd.DataFrame, window: int = 14) -> Tuple[float, float]:
        """Detect recent support and resistance levels"""
        high = data['High'].rolling(window=window).max()
        low = data['Low'].rolling(window=window).min()
        
        resistance = high.iloc[-1]
        support = low.iloc[-1]
        
        return support, resistance
    
    @staticmethod
    def generate_signal(data: pd.DataFrame) -> Dict:
        """
        Generate comprehensive trading signal
        
        Returns:
            {
                'signal': 'BUY', 'SELL', or 'HOLD',
                'confidence': 0-100,
                'reasons': [list of reasons],
                'indicators': {indicator data}
            }
        """
        if len(data) < 30:
            return {'signal': 'HOLD', 'confidence': 0, 'reasons': ['Insufficient data']}
        
        # Calculate all indicators
        rsi = TechnicalAnalyzer.calculate_rsi(data)
        macd, signal_line, histogram = TechnicalAnalyzer.calculate_macd(data)
        upper_bb, middle_bb, lower_bb = TechnicalAnalyzer.calculate_bollinger_bands(data)
        atr = TechnicalAnalyzer.calculate_atr(data)
        vol_ma = TechnicalAnalyzer.calculate_volume_ma(data)
        support, resistance = TechnicalAnalyzer.detect_support_resistance(data)
        
        latest_close = data['Close'].iloc[-1]
        latest_rsi = rsi.iloc[-1]
        latest_macd = macd.iloc[-1]
        latest_signal = signal_line.iloc[-1]
        latest_volume = data['Volume'].iloc[-1]
        
        signal_score = 0
        reasons = []
        
        # RSI Analysis
        if latest_rsi < RSI_OVERSOLD:
            signal_score += 2
            reasons.append(f"RSI oversold ({latest_rsi:.1f})")
        elif latest_rsi > RSI_OVERBOUGHT:
            signal_score -= 2
            reasons.append(f"RSI overbought ({latest_rsi:.1f})")
        
        # MACD Analysis
        if latest_macd > latest_signal and histogram.iloc[-1] > 0:
            signal_score += 2
            reasons.append("MACD bullish crossover")
        elif latest_macd < latest_signal and histogram.iloc[-1] < 0:
            signal_score -= 2
            reasons.append("MACD bearish crossover")
        
        # Bollinger Bands Analysis
        if latest_close < lower_bb.iloc[-1]:
            signal_score += 1
            reasons.append("Price below lower Bollinger Band")
        elif latest_close > upper_bb.iloc[-1]:
            signal_score -= 1
            reasons.append("Price above upper Bollinger Band")
        
        # Volume Analysis
        if latest_volume > vol_ma.iloc[-1]:
            signal_score += 1
            reasons.append("Volume spike detected")
        
        # Price near support
        if support > 0 and abs(latest_close - support) / support < 0.02:
            signal_score += 1
            reasons.append(f"Price near support (₹{support:.2f})")
        
        # Determine signal
        if signal_score >= 3:
            final_signal = 'BUY'
            confidence = min(90, 50 + (signal_score * 10))
        elif signal_score <= -2:
            final_signal = 'SELL'
            confidence = min(90, 50 + (abs(signal_score) * 10))
        else:
            final_signal = 'HOLD'
            confidence = 50
        
        return {
            'signal': final_signal,
            'confidence': confidence,
            'reasons': reasons,
            'indicators': {
                'rsi': latest_rsi,
                'macd': latest_macd,
                'signal_line': latest_signal,
                'volume': latest_volume,
                'support': support,
                'resistance': resistance,
                'atr': atr.iloc[-1]
            }
        }


class RiskManager:
    """Calculate risk metrics and pricing"""
    
    @staticmethod
    def calculate_position_size(investment: float, risk_percent: float = MAX_LOSS_PER_TRADE) -> float:
        """Calculate position size based on risk"""
        max_loss = investment * risk_percent
        return max_loss
    
    @staticmethod
    def calculate_entry_exit(current_price: float, investment: float, 
                            max_loss_percent: float = MAX_LOSS_PER_TRADE,
                            target_profit_percent: float = TARGET_PROFIT_PERCENT) -> Dict:
        """
        Calculate entry, stop loss, and take profit prices
        
        Accounts for:
        - Brokerage
        - Transaction charges
        - GST
        """
        
        # Total charges per transaction (entry + exit)
        total_brokerage = (BROKERAGE_PERCENT + TRANSACTION_CHARGE) * 2  # Entry and exit
        gst_on_charges = total_brokerage * GST_PERCENT
        total_charges_percent = total_brokerage + gst_on_charges
        
        # Adjusted entry price (includes charges)
        entry_price = current_price * (1 + total_charges_percent)
        
        # Stop loss (max loss)
        stop_loss = entry_price * (1 - max_loss_percent)
        
        # Take profit (target)
        take_profit = entry_price * (1 + target_profit_percent + total_charges_percent)
        
        # Quantity can buy
        quantity = int(investment / entry_price)
        
        # Actual investment
        actual_investment = quantity * entry_price
        
        return {
            'entry_price': entry_price,
            'stop_loss': stop_loss,
            'take_profit': take_profit,
            'quantity': quantity,
            'actual_investment': actual_investment,
            'max_loss_amount': actual_investment * max_loss_percent,
            'expected_profit': (take_profit - entry_price) * quantity,
            'charges_percent': total_charges_percent * 100
        }
    
    @staticmethod
    def calculate_return_on_investment(entry: float, exit_price: float, 
                                       investment: float) -> Dict:
        """Calculate ROI and returns"""
        total_charges_percent = (BROKERAGE_PERCENT + TRANSACTION_CHARGE) * 2 * (1 + GST_PERCENT)
        
        gross_return = ((exit_price - entry) / entry) * 100
        net_return = gross_return - (total_charges_percent * 100)
        profit = investment * (net_return / 100)
        
        return {
            'gross_return_percent': gross_return,
            'net_return_percent': net_return,
            'profit_amount': profit,
            'charges_amount': investment * (total_charges_percent * 100 / 100)
        }


# Example usage
if __name__ == "__main__":
    import yfinance as yf
    
    # Fetch sample data
    data = yf.download("SBIN.NS", period="3mo", progress=False)
    
    # Generate signal
    analyzer = TechnicalAnalyzer()
    signal = analyzer.generate_signal(data)
    
    print(f"Signal: {signal['signal']}")
    print(f"Confidence: {signal['confidence']}%")
    print(f"Reasons: {signal['reasons']}")
    
    # Risk management
    rm = RiskManager()
    current_price = data['Close'].iloc[-1]
    entry_exit = rm.calculate_entry_exit(current_price, 50000)
    
    print(f"\nEntry Price: ₹{entry_exit['entry_price']:.2f}")
    print(f"Stop Loss: ₹{entry_exit['stop_loss']:.2f}")
    print(f"Take Profit: ₹{entry_exit['take_profit']:.2f}")
    print(f"Expected Profit: ₹{entry_exit['expected_profit']:.2f}")
