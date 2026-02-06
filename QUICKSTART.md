# Quick Start Guide

## 🎉 Everything is 100% FREE!

No credit card needed! See [FREE_SETUP.md](FREE_SETUP.md) for details.

## Setup Steps (5 minutes)

### Option A: Automated Setup (Recommended)

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```cmd
.\setup.bat
```
*(Windows users: See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for troubleshooting)*

This will:
- Create virtual environment
- Install all dependencies
- Create .env file
- Run setup tests

### Option B: Manual Setup

### 1. Create Virtual Environment
```bash
# Create venv
python3 -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get API Keys (All FREE!)

**Full guide: [FREE_SETUP.md](FREE_SETUP.md)**

#### LLM Provider (Pick ONE - all free!)

**Groq (Recommended - Easiest)**
1. Go to https://console.groq.com/keys
2. Sign up (free, no credit card)
3. Create API key
4. Copy it

**Or Google Gemini**
1. Go to https://makersuite.google.com/app/apikey
2. Create API key (free)

**Or Ollama (Local)**
1. Download from https://ollama.ai
2. Run: `ollama pull llama3.2`

#### OpenWeather (Required - FREE)
1. Go to https://openweathermap.org/api
2. Sign up for free account
3. Get your API key

#### GitHub (Optional - FREE)
1. Go to https://github.com/settings/tokens
2. Generate token with `public_repo` scope

### 4. Create .env File
```bash
# Copy the example file
cp .env.example .env

# Edit .env and paste your keys
nano .env  # or use any text editor
```

Your `.env` should look like:
```env
GROQ_API_KEY=gsk-abc123...  # FREE
OPENWEATHER_API_KEY=def456...
GITHUB_TOKEN=ghp_xyz789...  # Optional
```

### 5. Test Setup
```bash
python test_setup.py
```

### 6. Run the Assistant

#### Option A: CLI
```bash
python main.py
```

#### Option B: API Server
```bash
python api_server.py
# Then visit http://localhost:8000/docs
```

## Example Usage

### CLI Example
```
Enter task: Find top 3 Python repos and weather in London
```

### API Example
```bash
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{"task": "Search for JavaScript repositories and get weather in Tokyo"}'
```

## Troubleshooting

### "Module not found"
```bash
# Make sure venv is activated
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Then install
pip install -r requirements.txt
```

### "API key not found"
Check your `.env` file exists and has the correct keys

### GitHub rate limit
Add a GitHub token to increase API limits from 60 to 5000 requests/hour

## Need Help?

Run the test script:
```bash
python test_setup.py
```

It will show exactly what's missing or broken.
