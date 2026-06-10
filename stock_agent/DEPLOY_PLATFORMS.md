# Deploy to Multiple Platforms (All FREE)

Choose your platform and follow the steps!

---

## 🏆 Railway.app (BEST - Recommended)

**Cost**: FREE $5/month  
**Time**: 5 minutes  
**Rating**: ⭐⭐⭐⭐⭐

### Deploy:

1. Go to **railway.app**
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Choose your `stock-agent` repo
5. Add environment variables
6. Deploy!

📚 Full guide: [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)

---

## 🥈 Render.com (Easiest UI)

**Cost**: FREE (limited)  
**Time**: 10 minutes  
**Rating**: ⭐⭐⭐⭐

### Deploy:

1. Go to **render.com**
2. Click "New Web Service"
3. Connect GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn -w 1 -b 0.0.0.0:$PORT web_app:app`
6. Add environment variables
7. Deploy!

**Note**: Free tier spins down after 15 min inactivity

---

## 🥉 Google Cloud Run

**Cost**: ~$2-5/month (mostly free)  
**Time**: 15 minutes  
**Rating**: ⭐⭐⭐⭐

### Deploy:

```bash
# Install Google Cloud SDK
brew install --cask google-cloud-sdk

# Login
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Deploy
gcloud run deploy stock-agent \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars \
  EMAIL_SENDER=your@gmail.com,\
  EMAIL_PASSWORD=your_app_password
```

**Pros**: Excellent performance, 99.99% uptime  
**Cons**: Requires credit card (free tier limits apply)

---

## 🎯 Replit.com (Instant)

**Cost**: FREE  
**Time**: 2 minutes  
**Rating**: ⭐⭐⭐

### Deploy:

1. Go to **replit.com**
2. Click "Create Repl"
3. Choose "Import from GitHub"
4. Paste: `https://github.com/YOUR_USERNAME/stock-agent`
5. Click "Run"
6. Done!

**Pros**: No setup needed, instant  
**Cons**: Stops when idle (free tier)

---

## 💻 PythonAnywhere

**Cost**: $5/month  
**Time**: 10 minutes  
**Rating**: ⭐⭐⭐

### Deploy:

1. Go to **pythonanywhere.com**
2. Sign up (free account)
3. Upload files via FTP
4. Create web app (Flask)
5. Configure WSGI file
6. Reload

**Pros**: Great for beginners  
**Cons**: Manual file upload

---

## 🌐 Heroku (Legacy - No Free Tier)

**Note**: Heroku removed free tier in 2022

**Alternative**: Use Railway instead (very similar)

---

## 🚀 COMPARISON TABLE

```
┌──────────────┬──────────────┬──────────┬──────────────┬──────────┐
│ Platform     │ Cost/Month   │ Setup    │ Python Jobs  │ Uptime   │
├──────────────┼──────────────┼──────────┼──────────────┼──────────┤
│ Railway ⭐   │ $5 free      │ 5 min    │ Yes ✓        │ 99.9%    │
│ Render       │ Free Limited │ 10 min   │ Limited      │ 99%      │
│ Cloud Run    │ $2-5         │ 15 min   │ Yes ✓        │ 99.99%   │
│ Replit       │ Free         │ 2 min    │ Limited      │ ~95%     │
│ PythonAny.   │ $5           │ 10 min   │ Yes ✓        │ 99%      │
└──────────────┴──────────────┴──────────┴──────────────┴──────────┘
```

---

## 💡 QUICK DECISION GUIDE

**Want simplest setup?**  
→ Use **Replit** (just upload, click run)

**Want best free option?**  
→ Use **Railway** (best balance of free + features)

**Want production-grade?**  
→ Use **Cloud Run** or **Railway**

**Want to learn deployment?**  
→ Use **Render** (great UI, easy to understand)

**Want long-running jobs?**  
→ Use **Railway** or **Cloud Run**

---

## 📋 SETUP CHECKLIST

Before deploying, ensure:

- [ ] Code committed to GitHub
- [ ] `requirements.txt` updated
- [ ] `Dockerfile` present
- [ ] `Procfile` or `railway.toml` present
- [ ] `.env` NOT in git (add to `.gitignore`)
- [ ] Environment variables ready
- [ ] GitHub account created
- [ ] Platform account created

---

## 🔒 ENVIRONMENT VARIABLES NEEDED

All platforms require:

```
EMAIL_SENDER = your@gmail.com
EMAIL_PASSWORD = gmail_app_password (not regular password!)
EMAIL_RECEIVER = recipient@gmail.com
WHATSAPP_API_KEY = (optional) your_twilio_key
WHATSAPP_PHONE = (optional) +919999999999
DATABASE_URL = (optional) let platform handle
FLASK_ENV = production
```

---

## 🎯 RECOMMENDED FLOW

1. **Start Local**

   ```bash
   python3 web_app.py
   # Test at http://localhost:5000
   ```

2. **Deploy to Railway** (free)

   ```bash
   git push origin main
   # Deploy via railway.app
   ```

3. **Monitor & Scale** (as needed)
   - Check logs
   - Monitor performance
   - Scale up if needed ($7-20/month)

---

## 📊 LIVE URLS AFTER DEPLOYMENT

**Railway**: `https://stock-agent.up.railway.app`  
**Render**: `https://stock-agent.onrender.com`  
**Cloud Run**: `https://stock-agent-xxxxx.run.app`  
**Replit**: `https://stock-agent.replit.dev`

---

## 🆘 COMMON ISSUES

### "Port error"

✓ All config files handle this automatically

### "Module not found"

✓ Check `requirements.txt` is up to date

### "Database error"

✓ SQLite works on all platforms
✓ Or use PostgreSQL (free on Railway/Render)

### "Environment variables not loading"

✓ Set in platform, not in code
✓ Restart app after adding variables

---

## 🚀 NEXT STEPS

1. **Choose Platform** (Railway recommended)
2. **Push to GitHub**
3. **Deploy** (3-15 min depending on platform)
4. **Add Environment Variables**
5. **Open URL** and test!

---

## 📚 RESOURCES

- **Railway**: https://docs.railway.app
- **Render**: https://render.com/docs
- **Cloud Run**: https://cloud.google.com/run/docs
- **Replit**: https://docs.replit.com
- **PythonAnywhere**: https://help.pythonanywhere.com

---

## ✅ Ready to Deploy?

**Recommended**: Follow [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)

Or choose another platform above and deploy!

**Your app will be live in 5-15 minutes!** 🚀
