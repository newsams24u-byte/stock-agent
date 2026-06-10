# 🚀 Instagram Agent - Quick Start Guide

## What's Built

✅ **Fully Automated AI Agent** that:

- Fetches Bangalore news every 30 minutes
- Falls back to India news if needed
- Generates viral captions with hashtags using Claude AI
- Creates stunning Instagram images automatically
- Posts directly to Instagram via API

## 3 Easy Steps to Start

### Step 1: Get Your API Keys (5 minutes)

1. **NewsAPI** - https://newsapi.org/ (Free)
   - Sign up → Get API key

2. **Anthropic** - https://console.anthropic.com/ (Claude AI)
   - Sign up → Create API key
   - Cost: ~$0.001 per post (~$0.03/day)

3. **Instagram** - Choose ONE:
   - **Business Account** (Recommended): Get from Meta Developers
   - **Personal Account**: Just use your username/password

### Step 2: Configure Credentials

```bash
cd instagram_agent
cp .env.example .env
```

Edit `.env` with your keys:

```env
NEWSAPI_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
INSTAGRAM_ACCESS_TOKEN=your_token_here
INSTAGRAM_BUSINESS_ACCOUNT_ID=your_id_here
POST_INTERVAL_MINUTES=30
```

### Step 3: Run the Agent

**Option A: Using bash script (Easiest)**

```bash
cd instagram_agent
chmod +x run.sh
./run.sh
```

**Option B: Manual**

```bash
cd instagram_agent
pip install -r requirements.txt
python main_agent.py
```

## What Happens

✅ **First Run**: Immediately creates and posts your first news story  
🔄 **Every 30 mins**: Automatically fetches, generates caption, creates image, posts

The agent will:

1. Fetch Bangalore/India news
2. Generate AI caption + viral hashtags (e.g., #BangaloreNews, #IndiaUpdates)
3. Add engagement hook ("What do you think?")
4. Create beautiful Instagram image
5. Post to your Instagram account

## Example Output

```
============================================================
🤖 Instagram News Agent - Creating Post
============================================================
📰 Fetching news...
✅ Found bangalore news: "New Tech Hub Opens in Bangalore..."
✍️ Generating caption and hashtags...
✅ Caption generated:
"New Tech Hub Opens in Bangalore! 🚀 What do you think? #BangaloreNews..."
🖼️ Creating image...
✅ Image created: instagram_agent/posts/post_1717584000.png
📤 Posting to Instagram...
✅ Posted successfully to Instagram!
```

## File Structure

```
instagram_agent/
├── main_agent.py          ← Main orchestrator
├── news_fetcher.py        ← Fetches Bangalore/India news
├── content_generator.py   ← AI captions + hashtags
├── image_creator.py       ← Creates images
├── instagram_poster.py    ← Posts to Instagram
├── requirements.txt       ← Dependencies
├── .env                   ← Your credentials
├── README.md              ← Full documentation
├── run.sh                 ← Easy launcher
└── posts/                 ← Generated images
```

## How It's Automated (Using APIs)

- **News Fetching**: NewsAPI (not web scraping)
- **AI Captions**: Claude API (not templates)
- **Image Creation**: PIL library (local)
- **Posting**: Instagram Graph API (not bot automation)
- **Scheduling**: APScheduler (background daemon)

**No browser automation, no manual work, fully API-driven!**

## Customization Ideas

- Change interval from 30 to 15 minutes
- Add your logo to images
- Use different hashtag strategies
- Add more cities (Mumbai, Delhi, etc.)
- Fetch from multiple news sources

## Stop the Agent

Press `Ctrl+C` in terminal

## Support

- Check `.env` file is configured correctly
- Ensure all API keys are valid
- Verify Instagram credentials work
- Check `posts/` folder for generated images

---

🎉 **You're all set! Your Instagram news agent is ready to go live!**
