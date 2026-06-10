# Free Deployment Guide - Stock Market Agent

Choose one of these FREE options:

## 🏆 OPTION 1: Railway.app (BEST - Free $5/month)

### Why Railway?

✅ Free $5 credit/month  
✅ Python Flask 100% supported  
✅ Background jobs work  
✅ Super easy GitHub deployment  
✅ Perfect for this project

### Deploy in 3 Steps:

**Step 1: Push to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/stock-agent.git
git push -u origin main
```

**Step 2: Deploy via Railway**

```bash
npm i -g @railway/cli
railway login
railway init
railway add
```

**Step 3: Set Environment Variables**

```bash
railway variables add EMAIL_SENDER=your@gmail.com
railway variables add EMAIL_PASSWORD=your_app_password
railway variables add WHATSAPP_API_KEY=your_key
railway up
```

Your app will be at: `https://your-project.up.railway.app`

---

## 🥈 OPTION 2: Render.com (Free - Limited)

### Deploy Steps:

1. Go to **render.com**
2. Click **"New + → Web Service"**
3. Connect your GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python web_app.py`
6. Add environment variables
7. Deploy!

Free tier limited to:

- 0.5 GB RAM
- Spins down after 15 min inactivity
- Good for testing

---

## 🥉 OPTION 3: Heroku (Free Alternative - Needs Credit Card)

Heroku's free tier ended, but alternatives:

- Railway (recommended)
- Render
- PythonAnywhere

---

## 🎯 OPTION 4: Google Cloud Run (Free - Pay Per Use)

### Free Tier: $0-2.50/month typically

- 2 million requests/month free
- Very affordable

### Deploy:

```bash
# Install Google Cloud SDK
brew install --cask google-cloud-sdk

# Login
gcloud auth login
gcloud config set project your-project-id

# Deploy
gcloud run deploy stock-agent \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars EMAIL_SENDER=your@gmail.com
```

---

## ⚡ OPTION 5: Replit.com (Instant - Free)

### Fastest option - No deployment needed!

1. Go to **replit.com**
2. Click **"Create"**
3. Upload this folder
4. Click **"Run"**
5. Done! Live in seconds

Benefits:

- No setup needed
- Works immediately
- Free tier available
- Good for testing

Drawback: Server stops if idle for a while (free tier)

---

## 🚀 RECOMMENDED PATH: Railway.app

Why Railway is best for you:

| Aspect              | Railway  | Render  | Cloud Run   |
| ------------------- | -------- | ------- | ----------- |
| **Free Cost**       | $5/month | Limited | Pay per use |
| **Setup Time**      | 5 min    | 10 min  | 15 min      |
| **Python Support**  | ⭐⭐⭐   | ⭐⭐⭐  | ⭐⭐⭐      |
| **Background Jobs** | ✓        | Limited | ✓           |
| **Uptime**          | 99.9%    | 99%     | 99.99%      |
| **Recommended**     | **YES**  | OK      | Advanced    |

---

## 📊 Quick Comparison Table

```
┌─────────────────┬──────────────┬─────────┬─────────────┐
│ Platform        │ Cost/Month   │ Setup   │ Python Jobs │
├─────────────────┼──────────────┼─────────┼─────────────┤
│ Railway.app     │ $5 free      │ 5 min   │ Yes ✓       │
│ Render.com      │ Limited Free │ 10 min  │ Limited     │
│ Cloud Run       │ Pay/Use      │ 15 min  │ Yes ✓       │
│ Replit.com      │ Free         │ 2 min   │ Limited     │
│ PythonAnywhere  │ $5/month     │ 10 min  │ Yes ✓       │
└─────────────────┴──────────────┴─────────┴─────────────┘
```

---

## 🔧 Ready to Deploy?

### Railway (Recommended):

```bash
# Install CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up

# Get your URL
railway open
```

### Or Use Web Dashboard:

1. Visit **railway.app**
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub"
5. Choose this repository
6. Add environment variables
7. Auto-deploys!

---

## 💾 Database Considerations

**Current**: SQLite (file-based)

- ✓ Works on Railway
- ✓ Works on Render
- ✓ Works on Cloud Run
- ⚠️ Data lost on server restart (free tiers)

**Better for Production**: Use managed database

- PostgreSQL (free tier on Railway/Render)
- MongoDB (free tier available)

---

## ✅ NEXT STEPS

1. **Choose Platform**: Railway recommended ⭐
2. **Push to GitHub**: Your code needs to be on GitHub
3. **Connect Repository**: Link to deployment platform
4. **Add Environment Variables**: Email, WhatsApp keys
5. **Deploy**: One click!
6. **Share URL**: Your live app!

---

## 📚 Need Help?

**Railway Docs**: https://docs.railway.app/  
**Render Docs**: https://render.com/docs  
**Google Cloud**: https://cloud.google.com/docs

---

**Let me know which platform you want to use, and I'll help set it up!** 🚀
