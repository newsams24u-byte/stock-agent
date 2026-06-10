# 🚀 Deployment Guide - Stock Market Agent

Deploy your stock market agent to production on various cloud platforms.

## 🐳 Docker Deployment

### Local Docker

```bash
# Build image
docker build -t stock-agent .

# Run container
docker run -p 5000:5000 \
  -e EMAIL_SENDER=your@email.com \
  -e EMAIL_PASSWORD=app_password \
  -e WHATSAPP_API_KEY=your_key \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  stock-agent
```

### Docker Compose

```bash
# Update .env with your credentials
cp .env.example .env
# Edit .env

# Start services
docker-compose up -d

# View logs
docker-compose logs -f web

# Stop services
docker-compose down
```

## ☁️ Cloud Deployment Options

### Option 1: Heroku (Recommended for Free Tier)

```bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login
heroku login

# Create app
heroku create your-stock-agent

# Set environment variables
heroku config:set EMAIL_SENDER=your@email.com
heroku config:set EMAIL_PASSWORD=your_app_password
heroku config:set WHATSAPP_API_KEY=your_key

# Deploy
git push heroku main

# View logs
heroku logs -t
```

**Procfile** (already included):

```
web: python web_app.py
worker: python -c "from stock_agent import StockMarketAgent; StockMarketAgent().start_monitoring()"
```

### Option 2: AWS (EC2)

```bash
# Launch EC2 instance (Ubuntu 22.04)
# SSH into instance

# Install dependencies
sudo apt update && sudo apt install -y python3 python3-pip git

# Clone repository
git clone your-repo-url
cd stock_agent

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup supervisor for background job
sudo apt install supervisor

# Create supervisor config
sudo nano /etc/supervisor/conf.d/stock-agent.conf
```

**supervisor config**:

```
[program:stock-agent]
command=/home/ubuntu/stock_agent/venv/bin/python /home/ubuntu/stock_agent/stock_agent.py
autostart=true
autorestart=true
stderr_logfile=/var/log/stock-agent.err.log
stdout_logfile=/var/log/stock-agent.out.log
```

```bash
# Start supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start stock-agent
```

### Option 3: Railway.app

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Create project
railway init

# Add services
railway add

# Set environment variables in dashboard

# Deploy
railway up
```

### Option 4: Render

1. Push code to GitHub
2. Go to render.com/dashboard
3. Create new Web Service
4. Connect GitHub repository
5. Set environment variables
6. Deploy

### Option 5: Google Cloud Run

```bash
# Install gcloud CLI
brew install --cask google-cloud-sdk

# Authenticate
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy stock-agent \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars EMAIL_SENDER=your@email.com \
  --set-env-vars EMAIL_PASSWORD=your_app_password
```

## 🔧 Production Configuration

### Environment Variables

```
# Flask
FLASK_ENV=production
FLASK_DEBUG=False

# Email
EMAIL_SENDER=your@gmail.com
EMAIL_PASSWORD=your_app_password  # Google App Password
EMAIL_RECEIVER=recipient@gmail.com

# WhatsApp
WHATSAPP_API_KEY=your_twilio_key
WHATSAPP_PHONE=+919999999999

# Database
DATABASE_URL=sqlite:///data/trades.db

# Logging
LOG_LEVEL=INFO
```

### Performance Tuning

**For better performance**:

1. **Database**: Use PostgreSQL instead of SQLite

   ```
   DATABASE_URL=postgresql://user:pass@host/dbname
   ```

2. **Caching**: Enable Redis caching

   ```
   pip install redis
   ```

3. **Worker**: Use Gunicorn

   ```
   pip install gunicorn
   gunicorn -w 4 web_app:app
   ```

4. **SSL**: Enable HTTPS
   ```
   # On Heroku/Railway: Automatic
   # On AWS: Use ALB with ACM certificate
   ```

## 📊 Monitoring

### Health Checks

```bash
# Check if app is running
curl http://localhost:5000/api/status

# Check database
curl http://localhost:5000/api/portfolio

# Check recommendations
curl http://localhost:5000/api/recommendations
```

### Logging

```bash
# View logs in production
# Heroku
heroku logs -t

# AWS EC2
tail -f /var/log/stock-agent.out.log

# Docker
docker logs -f container_id

# Railway
railway logs
```

### Alerts

Monitor using:

- **Sentry** (error tracking)
- **New Relic** (performance)
- **DataDog** (monitoring)
- **PagerDuty** (on-call)

## 🔐 Security Best Practices

1. **Environment Variables**: Never commit `.env`

   ```bash
   echo ".env" >> .gitignore
   ```

2. **API Keys**: Use secret management
   - AWS Secrets Manager
   - HashiCorp Vault
   - Railway Secrets

3. **Database**: Use managed databases
   - AWS RDS
   - Google Cloud SQL
   - Render Postgres

4. **HTTPS**: Always use SSL/TLS
   - Automatic on most platforms
   - Use Let's Encrypt if self-hosted

5. **Rate Limiting**: Protect endpoints
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, key_func=lambda: 'global')
   @app.route('/api/analysis')
   @limiter.limit("10/minute")
   def api_analysis():
       ...
   ```

## 📈 Scaling

### Horizontal Scaling

For high volume:

1. **Load Balancer**: Distribute traffic
   - AWS ALB
   - nginx
   - Cloudflare

2. **Multiple Workers**: Run multiple instances
   - Docker Swarm
   - Kubernetes
   - Docker Compose (dev only)

3. **Caching**: Reduce database hits
   - Redis
   - Memcached
   - Cloudflare Cache

### Vertical Scaling

For high latency:

1. **Database Optimization**: Add indexes
2. **Query Optimization**: Cache results
3. **Bigger Machines**: More CPU/RAM

## 🚨 Troubleshooting Deployment

### App won't start?

```
# Check logs
# Check environment variables
# Check database connectivity
# Check port availability
```

### Alerts not sending?

```
# Verify email/WhatsApp credentials
# Check SMTP/API status
# Test with manual analysis
```

### Slow performance?

```
# Check CPU/Memory usage
# Look for slow queries
# Check network latency
# Review logs for errors
```

### Database issues?

```
# Backup data
# Migrate to managed database
# Check file permissions (if SQLite)
# Monitor disk space
```

## 📚 Additional Resources

- [Heroku Deployment](https://devcenter.heroku.com/)
- [AWS EC2 Guide](https://docs.aws.amazon.com/ec2/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Railway.app Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)

## 💡 Production Checklist

- [ ] Environment variables configured
- [ ] Database backup strategy
- [ ] Error monitoring setup (Sentry)
- [ ] Performance monitoring (New Relic)
- [ ] SSL/HTTPS enabled
- [ ] Rate limiting enabled
- [ ] Logging configured
- [ ] Health checks working
- [ ] Alerts configured
- [ ] Disaster recovery plan
- [ ] Load testing completed
- [ ] Security audit done

---

**Happy deploying!** 🚀
