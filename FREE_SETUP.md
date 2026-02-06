# 🎉 100% FREE Setup Guide

## All Services are FREE! No Credit Card Required!

This project works with **completely free APIs**. Here's how to get them:

---

## 1. LLM Provider (Choose ONE)

### Option A: GROQ (⭐ RECOMMENDED - Fastest & Easiest)

**Why Groq?**
- ✅ Completely FREE
- ✅ No credit card needed
- ✅ Very fast responses
- ✅ 14,400 requests per day free
- ✅ Easy to set up

**Steps:**
1. Go to: https://console.groq.com/keys
2. Sign up with Google/GitHub (free)
3. Click "Create API Key"
4. Copy the key (starts with `gsk_`)
5. Paste in `.env` file:
   ```
   GROQ_API_KEY=gsk_your_key_here
   ```

**That's it! Most people should use this.**

---

### Option B: Google Gemini (Good alternative)

**Why Gemini?**
- ✅ Completely FREE
- ✅ 15 requests per minute free
- ✅ 1 million tokens per day free
- ✅ No credit card required

**Steps:**
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key
5. Paste in `.env` file:
   ```
   GOOGLE_API_KEY=your_key_here
   ```

---

### Option C: Ollama (Most private - runs on your computer)

**Why Ollama?**
- ✅ 100% FREE forever
- ✅ Runs locally (no API calls)
- ✅ Complete privacy
- ✅ No rate limits
- ❌ Requires download (~4GB)
- ❌ Slower on older computers

**Steps:**
1. Download: https://ollama.ai/download
2. Install Ollama
3. Open terminal and run:
   ```bash
   ollama pull llama3.2
   ```
4. In `.env` file:
   ```
   OLLAMA_HOST=http://localhost:11434
   ```

---

## 2. Weather API (Required - FREE)

**OpenWeather - 1000 calls/day free**

**Steps:**
1. Go to: https://openweathermap.org/api
2. Click "Sign Up" (FREE)
3. Verify email
4. Go to: https://home.openweathermap.org/api_keys
5. Copy your API key
6. Paste in `.env` file:
   ```
   OPENWEATHER_API_KEY=your_key_here
   ```

**Note:** Key might take 10 minutes to activate after signup.

---

## 3. GitHub API (Optional - FREE)

**Increases rate limit from 60 to 5000 requests/hour**

**Steps:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "AI Assistant")
4. Select scope: ✅ `public_repo`
5. Click "Generate token"
6. Copy the token (starts with `ghp_`)
7. Paste in `.env` file:
   ```
   GITHUB_TOKEN=ghp_your_token_here
   ```

---

## Summary - What You Need

**Minimum (Required):**
1. ✅ GROQ API Key (FREE) → https://console.groq.com/keys
2. ✅ OpenWeather Key (FREE) → https://openweathermap.org/api

**Optional:**
3. ⭐ GitHub Token (FREE) → https://github.com/settings/tokens

**Total Cost: $0.00 💰**

---

## Your .env File Should Look Like:

```env
# LLM - Choose ONE (uncomment the one you want)
GROQ_API_KEY=gsk_abc123xyz...          # ⭐ RECOMMENDED

# Weather (Required)
OPENWEATHER_API_KEY=def456...

# GitHub (Optional but recommended)
GITHUB_TOKEN=ghp_xyz789...
```

---

## Quick Links Summary

| Service | Link | Cost |
|---------|------|------|
| **Groq** | https://console.groq.com/keys | FREE ✅ |
| **Google Gemini** | https://makersuite.google.com/app/apikey | FREE ✅ |
| **Ollama** | https://ollama.ai/download | FREE ✅ |
| **OpenWeather** | https://openweathermap.org/api | FREE ✅ |
| **GitHub** | https://github.com/settings/tokens | FREE ✅ |

---

## FAQ

**Q: Do I need a credit card?**
A: No! All services have free tiers with no credit card required.

**Q: Which LLM should I use?**
A: Use **Groq** - it's the fastest and easiest.

**Q: How much does this cost?**
A: $0.00 - Everything is free!

**Q: Are there rate limits?**
A: Yes, but very generous:
- Groq: 14,400 requests/day
- Gemini: 15 requests/minute
- OpenWeather: 1,000 calls/day
- GitHub: 5,000 requests/hour (with token)

**Q: What if I exceed limits?**
A: Very unlikely for personal use. You can also switch between LLM providers.

**Q: Is my data private?**
A: API calls go through the provider. For complete privacy, use Ollama (runs locally).

---

## Next Steps

After getting your keys:

1. **Edit .env file** - Paste your keys
2. **Run**: `python test_setup.py` - Verify everything works
3. **Start**: `python main.py` - Use the assistant!

**That's it! Enjoy your FREE AI assistant! 🎉**
