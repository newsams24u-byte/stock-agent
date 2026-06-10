#!/bin/sh
set -eu

# Install dependencies from root declaration, then run app from stock_agent.
pip install --no-cache-dir -r requirements.txt
cd stock_agent
exec gunicorn -w 1 -b 0.0.0.0:${PORT:-5000} web_app:app