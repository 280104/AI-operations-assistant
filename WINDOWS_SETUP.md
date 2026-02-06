# Windows Setup Guide

## Quick Setup for Windows Users

### Step 1: Extract the ZIP
1. Right-click `ai_ops_assistant.zip`
2. Click "Extract All..."
3. Choose a location
4. Click "Extract"

### Step 2: Open PowerShell in the folder
1. Open the extracted `ai_ops_assistant` folder
2. Hold **Shift** and **right-click** in the folder
3. Select "Open PowerShell window here" or "Open in Terminal"

### Step 3: Run Setup Script

**If using PowerShell:**
```powershell
.\setup.bat
```

**If using Command Prompt (cmd):**
```cmd
setup.bat
```

**Note:** In PowerShell, you need the `.\` prefix to run scripts in the current folder.

### Step 4: If You Get "Execution Policy" Error

If you see an error about execution policy, you have two options:

**Option A: Use Command Prompt instead**
1. In the folder, type `cmd` in the address bar
2. Press Enter
3. Run: `setup.bat`

**Option B: Allow PowerShell scripts**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.bat
```

### Step 5: Get FREE API Keys

See [FREE_SETUP.md](FREE_SETUP.md) for links to get free keys:
- **Groq**: https://console.groq.com/keys (2 minutes)
- **OpenWeather**: https://openweathermap.org/api (2 minutes)

### Step 6: Edit .env File

1. Open `.env` file with Notepad
2. Paste your API keys:
```env
GROQ_API_KEY=gsk_your_actual_key_here
OPENWEATHER_API_KEY=your_actual_key_here
```
3. Save and close

### Step 7: Activate Virtual Environment

**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

You'll see `(venv)` appear in your prompt.

### Step 8: Test Setup

```cmd
python test_setup.py
```

### Step 9: Run the Assistant!

```cmd
python main.py
```

## Common Windows Issues

### Issue: "python is not recognized"

**Solution:** Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or newer
3. **Important:** Check "Add Python to PATH" during installation
4. Restart PowerShell/cmd

### Issue: "pip is not recognized"

**Solution:** 
```cmd
python -m pip install --upgrade pip
```

### Issue: Can't run .bat files in PowerShell

**Solution:** Use Command Prompt instead
1. Type `cmd` in the folder address bar
2. Press Enter
3. Run: `setup.bat`

### Issue: "Module not found" errors

**Solution:** Make sure virtual environment is activated
```cmd
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Issue: Port already in use (when running API server)

**Solution:** 
```cmd
python api_server.py --port 8001
```

## Alternative: Manual Setup on Windows

If the automated script doesn't work:

```cmd
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
venv\Scripts\activate.bat

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install packages
pip install -r requirements.txt

# 5. Copy .env.example to .env
copy .env.example .env

# 6. Edit .env with your API keys (use Notepad)
notepad .env

# 7. Test setup
python test_setup.py

# 8. Run!
python main.py
```

## Need More Help?

- Check [FREE_SETUP.md](FREE_SETUP.md) for getting API keys
- Check [README.md](README.md) for full documentation
- Check [QUICKSTART.md](QUICKSTART.md) for quick reference
