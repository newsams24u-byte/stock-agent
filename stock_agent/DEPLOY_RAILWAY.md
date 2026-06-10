# 🚀 Deploy to Railway.app (FREE - 5 Minutes)

Your Stock Market Agent is ready to deploy **for FREE**!

## 📊 What is Railway?

- **Free $5/month credit** (usually covers small projects)
- **Python Flask fully supported**
- **Background jobs work** (hourly analysis)
- **GitHub integration** (auto-deploy on push)
- **Database support** (PostgreSQL, MongoDB)
- **99.9% uptime**

## ✅ Prerequisites

Before deploying, you need:

1. **GitHub Account** (free at github.com)
2. **Railway Account** (free at railway.app)
3. **Code pushed to GitHub**

## 🔧 Step-by-Step Deployment

### Step 1: Push Code to GitHub

```bash
# Initialize git (if not already done)
cd /Users/yn00000/agent1/silver-agent
git init

# Add all files
git add .

# Commit
git commit -m "Stock Market Agent - Initial Release"

# Add remote (replace with your repo)
git remote add origin https://github.com/YOUR_USERNAME/stock-agent.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Create Railway Account

1. Go to **railway.app**
2. Click "Sign Up" (or Sign in with GitHub)
3. Authorize Railway to access GitHub
4. Create an account

### Step 3: Deploy from GitHub

**Option A: Web Dashboard (Easiest)**

1. Go to **railway.app/dashboard**
2. Click **"+ New Project"**
3. Select **"Deploy from GitHub repo"**
4. Select your **"stock-agent"** repo
5. Select the **"stock_agent"** directory as root
6. Click **"Deploy"**
7. Wait 2-3 minutes...
8. ✅ Done! Your app is live!

**Option B: CLI (If you prefer terminal)**

```bash
# Install Railway CLI
npm install -g @railway/cli

# Or with Homebrew
brew install railway

# Login
railway login

# Link to your GitHub repo
railway init

# Deploy
railway up

# View your app
railway open
```

### Step 4: Set Environment Variables

Railway needs your email/WhatsApp credentials.

**Via Web Dashboard:**

1. Go to your Railway project
2. Click the **"stock-agent"** service
3. Go to **"Variables"** tab
4. Add these variables:

```
EMAIL_SENDER = your-email@gmail.com
EMAIL_PASSWORD = your_gmail_app_password
EMAIL_RECEIVER = recipient@gmail.com
WHATSAPP_API_KEY = your_twilio_key (optional)
WHATSAPP_PHONE = +919999999999 (optional)
DATABASE_URL = leave empty (Railway handles)
```

**Via CLI:**

```bash
railway variables add EMAIL_SENDER=your@gmail.com
railway variables add EMAIL_PASSWORD=your_app_password
railway variables add WHATSAPP_API_KEY=your_key
railway up
```

### Step 5: Get Your Live URL

1. Go to Railway dashboard
2. Select your project
3. Click the **"stock-agent"** service
4. Copy the **Public URL** (looks like: `https://stock-agent.up.railway.app`)
5. Share it or open in browser!

## 🎉 Your App is Live!

Visit: `https://your-project.up.railway.app`

Features available:

- ✅ Web dashboard
- ✅ API endpoints
- ✅ Stock analysis
- ✅ Email alerts

## 📊 Pricing on Railway

**Free tier:**

- $5 monthly credit
- 100 GB bandwidth
- Unlimited compute

**What you'll pay:**

- Flask web app: ~$0.50-1.00/month
- Database (PostgreSQL): ~$2-3/month
- Typical total: **$2-5/month** (covered by free tier!)

## 🔄 Auto-Deploy on Code Changes

Any time you push to GitHub, Railway automatically redeploys:

```bash
# Make a change
echo "# Updated" >> README.md

# Commit and push
git add .
git commit -m "Update"
git push origin main

# Railway auto-deploys in 1-2 minutes!
```

## 🆘 Troubleshooting

### App won't start?

Check logs: `railway logs` or in dashboard → Logs tab

### Environment variables not working?

Make sure they're in Railway's **Variables** section, not `.env` file

### Port error?

Railway assigns port automatically, already configured in `Procfile`

### Database error?

Use SQLite initially (file-based), or add PostgreSQL service

## 💡 Next Steps

After deployment:

1. **Test it**: Visit your live URL
2. **Click "Analyze Now"**: Trigger first analysis
3. **Check recommendations**: View top stocks
4. **Monitor logs**: `railway logs -f` for real-time logs

## 📈 Scale Up Later

When you get more users:

- Add PostgreSQL database ($7/month)
- Increase web service size ($12-20/month)
- Add background worker ($7/month)

But for now, **free tier covers everything!**

## 🚀 Ready?

```bash
# 1. Make sure code is committed
git status

# 2. Push to GitHub
git push origin main

# 3. Go to railway.app
# 4. Deploy from GitHub
# 5. Set environment variables
# 6. Done! 🎉
```

---

**Your live URL**: `https://your-project.up.railway.app`

**Need help?** Check Railway docs: https://docs.railway.app

**Happy deploying!** 🚀📈
