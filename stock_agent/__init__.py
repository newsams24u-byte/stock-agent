"""
Stock Agent Package
"""

__version__ = "1.0.0"
__author__ = "Stock Market Analysis Team"
__description__ = "AI-powered stock market analysis and trading agent for Indian markets"

from .stock_agent import StockMarketAgent
from .data_fetcher import NSEDataFetcher
from .analysis_engine import TechnicalAnalyzer, RiskManager
from .alert_manager import AlertManager
from .models import init_db

__all__ = [
    'StockMarketAgent',
    'NSEDataFetcher',
    'TechnicalAnalyzer',
    'RiskManager',
    'AlertManager',
    'init_db'
]
