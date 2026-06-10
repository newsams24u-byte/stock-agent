#!/bin/bash

# Stock Market Agent Startup Script

echo "🚀 Starting Stock Market Analysis Agent..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt -q

# Initialize database
echo "🗄️  Initializing database..."
python -c "from models import init_db; init_db()" 2>/dev/null || true

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "📝 Creating .env from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your WhatsApp and Email credentials"
    echo "   Then run this script again"
    exit 1
fi

# Menu
echo ""
echo "================================"
echo "📊 Stock Market Agent"
echo "================================"
echo "1. Run Web Dashboard (http://localhost:5000)"
echo "2. Show Recommendations (CLI)"
echo "3. Start Hourly Monitoring"
echo "4. Analyze Single Stock"
echo "5. Exit"
echo "================================"
echo ""
read -p "Choose an option (1-5): " choice

case $choice in
    1)
        echo "🌐 Starting web dashboard..."
        python web_app.py
        ;;
    2)
        echo "📈 Displaying top recommendations..."
        python -c "
from stock_agent import StockMarketAgent
agent = StockMarketAgent()
agent.display_recommendations(top_n=15)
"
        ;;
    3)
        echo "📅 Starting hourly monitoring (Ctrl+C to stop)..."
        python -c "
from stock_agent import StockMarketAgent
agent = StockMarketAgent()
agent.start_monitoring()
"
        ;;
    4)
        read -p "Enter stock ticker (e.g., SBIN): " ticker
        echo "🔍 Analyzing $ticker..."
        python -c "
from stock_agent import StockMarketAgent
agent = StockMarketAgent()
analysis = agent.analyze_stock('${ticker}.NS')
if analysis:
    print(f\"Signal: {analysis['signal']} ({analysis['confidence']}%)\")
    print(f\"Current: ₹{analysis['current_price']:.2f}\")
    print(f\"Entry: ₹{analysis['entry_price']:.2f}\")
    print(f\"SL: ₹{analysis['stop_loss']:.2f}\")
    print(f\"TP: ₹{analysis['take_profit']:.2f}\")
    print(f\"Expected Profit: ₹{analysis['expected_profit']:.2f}\")
else:
    print('No data found for this stock')
"
        ;;
    5)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac

deactivate
