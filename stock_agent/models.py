"""
Database Models for Trade Tracking
Using SQLite with SQLAlchemy
"""

from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

# Create engine and session
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class StockRecommendation(Base):
    """Store stock recommendations"""
    __tablename__ = 'stock_recommendations'
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(20), nullable=False)
    signal = Column(String(10), nullable=False)  # BUY, SELL, HOLD
    confidence = Column(Float, nullable=False)
    current_price = Column(Float, nullable=False)
    entry_price = Column(Float, nullable=False)
    stop_loss = Column(Float, nullable=False)
    take_profit = Column(Float, nullable=False)
    expected_profit = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    reasons = Column(Text, nullable=True)  # JSON formatted
    indicators = Column(Text, nullable=True)  # JSON formatted
    created_at = Column(DateTime, default=datetime.now)
    alert_sent = Column(Boolean, default=False)
    
    def __repr__(self):
        return f"<StockRecommendation {self.ticker} {self.signal}>"


class Trade(Base):
    """Track actual trades taken"""
    __tablename__ = 'trades'
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(20), nullable=False)
    entry_price = Column(Float, nullable=False)
    entry_date = Column(DateTime, nullable=False)
    quantity = Column(Integer, nullable=False)
    investment_amount = Column(Float, nullable=False)
    stop_loss = Column(Float, nullable=False)
    take_profit = Column(Float, nullable=False)
    exit_price = Column(Float, nullable=True)
    exit_date = Column(DateTime, nullable=True)
    status = Column(String(20), default="OPEN")  # OPEN, CLOSED, STOPPED_OUT
    profit_loss = Column(Float, nullable=True)
    return_percent = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Trade {self.ticker} {self.status}>"


class MarketData(Base):
    """Cache market data for analysis"""
    __tablename__ = 'market_data'
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(20), nullable=False)
    date = Column(DateTime, nullable=False)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<MarketData {self.ticker} {self.date}>"


class AlertLog(Base):
    """Log all alerts sent"""
    __tablename__ = 'alert_logs'
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(20), nullable=False)
    alert_type = Column(String(20), nullable=False)  # WHATSAPP, EMAIL, BOTH
    signal = Column(String(10), nullable=False)
    message = Column(Text, nullable=True)
    sent_successfully = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<AlertLog {self.ticker} {self.alert_type}>"


class PortfolioMetrics(Base):
    """Track portfolio performance"""
    __tablename__ = 'portfolio_metrics'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    total_investment = Column(Float, nullable=False)
    current_portfolio_value = Column(Float, nullable=False)
    total_profit_loss = Column(Float, nullable=False)
    profit_loss_percent = Column(Float, nullable=False)
    open_trades = Column(Integer, nullable=False)
    closed_trades = Column(Integer, nullable=False)
    win_rate = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<PortfolioMetrics {self.date}>"


# Create tables
def init_db():
    """Initialize database"""
    Base.metadata.create_all(engine)
    print("✅ Database initialized successfully")


# Helper functions
def add_recommendation(ticker, signal, confidence, current_price, entry_price, 
                       stop_loss, take_profit, expected_profit, quantity, reasons, indicators):
    """Add a stock recommendation"""
    session = Session()
    try:
        rec = StockRecommendation(
            ticker=ticker,
            signal=signal,
            confidence=confidence,
            current_price=current_price,
            entry_price=entry_price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            expected_profit=expected_profit,
            quantity=quantity,
            reasons=reasons,
            indicators=indicators
        )
        session.add(rec)
        session.commit()
        return rec.id
    finally:
        session.close()


def add_trade(ticker, entry_price, entry_date, quantity, investment_amount, 
              stop_loss, take_profit):
    """Add a new trade"""
    session = Session()
    try:
        trade = Trade(
            ticker=ticker,
            entry_price=entry_price,
            entry_date=entry_date,
            quantity=quantity,
            investment_amount=investment_amount,
            stop_loss=stop_loss,
            take_profit=take_profit
        )
        session.add(trade)
        session.commit()
        return trade.id
    finally:
        session.close()


def close_trade(trade_id, exit_price, exit_date):
    """Close an open trade"""
    session = Session()
    try:
        trade = session.query(Trade).filter(Trade.id == trade_id).first()
        if trade:
            trade.exit_price = exit_price
            trade.exit_date = exit_date
            trade.status = "CLOSED"
            trade.profit_loss = (exit_price - trade.entry_price) * trade.quantity
            trade.return_percent = ((exit_price - trade.entry_price) / trade.entry_price) * 100
            session.commit()
        return trade
    finally:
        session.close()


def get_open_trades():
    """Get all open trades"""
    session = Session()
    try:
        trades = session.query(Trade).filter(Trade.status == "OPEN").all()
        return trades
    finally:
        session.close()


def get_portfolio_performance():
    """Get portfolio performance summary"""
    session = Session()
    try:
        trades = session.query(Trade).all()
        
        total_profit = sum([t.profit_loss for t in trades if t.profit_loss])
        total_investment = sum([t.investment_amount for t in trades])
        closed_trades = len([t for t in trades if t.status == "CLOSED"])
        winning_trades = len([t for t in trades if t.status == "CLOSED" and t.profit_loss > 0])
        
        win_rate = (winning_trades / closed_trades * 100) if closed_trades > 0 else 0
        
        return {
            'total_investment': total_investment,
            'total_profit': total_profit,
            'total_trades': len(trades),
            'open_trades': len([t for t in trades if t.status == "OPEN"]),
            'closed_trades': closed_trades,
            'win_rate': win_rate,
            'avg_profit_per_trade': total_profit / closed_trades if closed_trades > 0 else 0
        }
    finally:
        session.close()


# Example usage
if __name__ == "__main__":
    init_db()
    print("✅ Database setup complete")
