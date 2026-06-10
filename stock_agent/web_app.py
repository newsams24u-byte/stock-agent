"""
Stock Agent Web Dashboard
Flask app for monitoring and managing recommendations
"""

from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import logging
from stock_agent import StockMarketAgent
from models import (
    Session, StockRecommendation, Trade, AlertLog, get_portfolio_performance
)
import os

# Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'stock-agent-secret'
agent = StockMarketAgent(investment=500000)

logger = logging.getLogger(__name__)

# ===== ROUTES =====

@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template('dashboard.html')


@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    """Get stock recommendations"""
    try:
        top_n = request.args.get('limit', default=15, type=int)
        analyses = agent.analyze_top_stocks(limit=top_n * 2)
        
        recommendations = []
        for analysis in analyses[:top_n]:
            if analysis:
                recommendations.append({
                    'ticker': analysis['ticker'],
                    'signal': analysis['signal'],
                    'confidence': analysis['confidence'],
                    'current_price': round(analysis['current_price'], 2),
                    'entry_price': round(analysis['entry_price'], 2),
                    'stop_loss': round(analysis['stop_loss'], 2),
                    'take_profit': round(analysis['take_profit'], 2),
                    'expected_profit': round(analysis['expected_profit'], 2),
                    'max_loss': round(analysis['max_loss'], 2),
                    'quantity': analysis['quantity'],
                    'reasons': analysis['reasons'][:3],
                    'rsi': round(analysis['indicators'].get('rsi', 0), 2),
                    'timestamp': analysis['analysis_timestamp'].isoformat()
                })
        
        return jsonify({
            'status': 'success',
            'count': len(recommendations),
            'recommendations': recommendations
        })
    except Exception as e:
        logger.error(f"Error fetching recommendations: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    """Get portfolio performance"""
    try:
        performance = get_portfolio_performance()
        
        return jsonify({
            'status': 'success',
            'portfolio': {
                'total_investment': round(performance['total_investment'], 2),
                'total_profit': round(performance['total_profit'], 2),
                'total_trades': performance['total_trades'],
                'open_trades': performance['open_trades'],
                'closed_trades': performance['closed_trades'],
                'win_rate': round(performance['win_rate'], 2),
                'avg_profit_per_trade': round(performance['avg_profit_per_trade'], 2)
            }
        })
    except Exception as e:
        logger.error(f"Error fetching portfolio: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/trades', methods=['GET'])
def get_trades():
    """Get all trades"""
    try:
        session = Session()
        trades = session.query(Trade).all()
        
        trades_data = []
        for trade in trades:
            trades_data.append({
                'id': trade.id,
                'ticker': trade.ticker,
                'status': trade.status,
                'entry_price': round(trade.entry_price, 2),
                'entry_date': trade.entry_date.isoformat(),
                'exit_price': round(trade.exit_price, 2) if trade.exit_price else None,
                'exit_date': trade.exit_date.isoformat() if trade.exit_date else None,
                'quantity': trade.quantity,
                'investment': round(trade.investment_amount, 2),
                'profit_loss': round(trade.profit_loss, 2) if trade.profit_loss else None,
                'return_percent': round(trade.return_percent, 2) if trade.return_percent else None
            })
        
        session.close()
        
        return jsonify({
            'status': 'success',
            'trades': trades_data
        })
    except Exception as e:
        logger.error(f"Error fetching trades: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/analysis/<ticker>', methods=['GET'])
def analyze_single_stock(ticker):
    """Get detailed analysis for a single stock"""
    try:
        analysis = agent.analyze_stock(ticker.upper() + ".NS")
        
        if not analysis:
            return jsonify({'status': 'error', 'message': 'No data found'}), 404
        
        return jsonify({
            'status': 'success',
            'analysis': {
                'ticker': analysis['ticker'],
                'signal': analysis['signal'],
                'confidence': analysis['confidence'],
                'current_price': round(analysis['current_price'], 2),
                'entry_price': round(analysis['entry_price'], 2),
                'stop_loss': round(analysis['stop_loss'], 2),
                'take_profit': round(analysis['take_profit'], 2),
                'expected_profit': round(analysis['expected_profit'], 2),
                'reasons': analysis['reasons'],
                'indicators': {
                    'rsi': round(analysis['indicators'].get('rsi', 0), 2),
                    'macd': round(analysis['indicators'].get('macd', 0), 4),
                    'volume': int(analysis['indicators'].get('volume', 0))
                }
            }
        })
    except Exception as e:
        logger.error(f"Error analyzing {ticker}: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Get recent alerts"""
    try:
        session = Session()
        alerts = session.query(AlertLog).order_by(AlertLog.created_at.desc()).limit(20).all()
        
        alerts_data = []
        for alert in alerts:
            alerts_data.append({
                'id': alert.id,
                'ticker': alert.ticker,
                'type': alert.alert_type,
                'signal': alert.signal,
                'sent': alert.sent_successfully,
                'created_at': alert.created_at.isoformat()
            })
        
        session.close()
        
        return jsonify({
            'status': 'success',
            'alerts': alerts_data
        })
    except Exception as e:
        logger.error(f"Error fetching alerts: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/run-analysis', methods=['POST'])
def run_analysis():
    """Manually run analysis"""
    try:
        logger.info("Manual analysis requested")
        
        # Run analysis
        analyses = agent.analyze_top_stocks(limit=30)
        
        # Process recommendations
        agent.process_recommendations(analyses)
        
        return jsonify({
            'status': 'success',
            'message': f'Analysis complete. {len(analyses)} stocks analyzed.',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Error running analysis: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get agent status"""
    try:
        is_market_open = agent.is_market_open()
        portfolio = get_portfolio_performance()
        
        return jsonify({
            'status': 'success',
            'agent_status': {
                'market_open': is_market_open,
                'investment_amount': agent.investment,
                'last_analysis': datetime.now().isoformat(),
                'portfolio': portfolio
            }
        })
    except Exception as e:
        logger.error(f"Error getting status: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'message': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({'status': 'error', 'message': 'Server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
