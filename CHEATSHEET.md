# Command Cheat Sheet

## Quick Reference for Common Commands

### Initial Setup

| Task | Linux/Mac | Windows (PowerShell) | Windows (cmd) |
|------|-----------|---------------------|---------------|
| Run setup script | `./setup.sh` | `.\setup.bat` | `setup.bat` |
| Make script executable | `chmod +x setup.sh` | N/A | N/A |

### Virtual Environment

| Task | Linux/Mac | Windows (PowerShell) | Windows (cmd) |
|------|-----------|---------------------|---------------|
| Create venv | `python3 -m venv venv` | `python -m venv venv` | `python -m venv venv` |
| Activate venv | `source venv/bin/activate` | `.\venv\Scripts\Activate.ps1` | `venv\Scripts\activate.bat` |
| Deactivate venv | `deactivate` | `deactivate` | `deactivate` |

### Package Management

| Task | All Platforms |
|------|---------------|
| Install packages | `pip install -r requirements.txt` |
| Install single package | `pip install groq` |
| Upgrade pip | `pip install --upgrade pip` |
| List installed | `pip list` |

### Running the Application

| Task | All Platforms |
|------|---------------|
| Test setup | `python test_setup.py` |
| Run CLI | `python main.py` |
| Run API server | `python api_server.py` |
| Run API on different port | `python api_server.py --port 8001` |

### File Operations

| Task | Linux/Mac | Windows (PowerShell) | Windows (cmd) |
|------|-----------|---------------------|---------------|
| Copy .env file | `cp .env.example .env` | `Copy-Item .env.example .env` | `copy .env.example .env` |
| Edit .env | `nano .env` | `notepad .env` | `notepad .env` |
| View file | `cat .env` | `Get-Content .env` | `type .env` |

### Troubleshooting

| Task | All Platforms |
|------|---------------|
| Check Python version | `python --version` |
| Check pip version | `pip --version` |
| Check if venv active | Look for `(venv)` in prompt |
| Find Python path | `which python` (Mac/Linux) or `where python` (Windows) |

### API Testing

| Task | Command |
|------|---------|
| Test API endpoint | `curl -X POST http://localhost:8000/process -H "Content-Type: application/json" -d '{"task":"test"}'` |
| Check API health | `curl http://localhost:8000/health` |
| View API docs | Open browser: `http://localhost:8000/docs` |

### Git Operations (if using version control)

| Task | All Platforms |
|------|---------------|
| Check what will be uploaded | `git status` |
| Verify .env is ignored | `git check-ignore -v .env` |
| Initialize repo | `git init` |
| First commit | `git add . && git commit -m "Initial commit"` |
| Check .env NOT in commit | `git log --name-only` |

**🔒 IMPORTANT:** `.env` is in `.gitignore` - your API keys are PROTECTED!
See [SECURITY.md](SECURITY.md) for details.

## Common Paths

### Project Structure
```
ai_ops_assistant/
├── venv/                  # Virtual environment (don't commit)
├── .env                   # Your API keys (don't commit)
├── agents/                # Agent code
├── tools/                 # API integrations
├── llm/                   # LLM client
├── main.py               # CLI entry point
├── api_server.py         # API entry point
└── requirements.txt      # Dependencies
```

### Important Files
- `.env` - Your secret API keys
- `.env.example` - Template for .env
- `requirements.txt` - Python packages
- `README.md` - Full documentation
- `FREE_SETUP.md` - How to get free API keys
- `QUICKSTART.md` - Quick setup guide
- `WINDOWS_SETUP.md` - Windows-specific help

## Getting Help

| Issue | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| Python not found | Install Python 3.8+ from python.org |
| Permission denied (Mac/Linux) | `chmod +x setup.sh` |
| Can't run .bat in PowerShell | Use `.\setup.bat` or use cmd instead |
| API key error | Check .env file has correct keys |
| Port in use | Use `--port 8001` or kill other process |

## Quick Links

- **Groq API Keys**: https://console.groq.com/keys
- **Google Gemini Keys**: https://makersuite.google.com/app/apikey
- **OpenWeather Keys**: https://openweathermap.org/api
- **GitHub Tokens**: https://github.com/settings/tokens
- **Python Download**: https://www.python.org/downloads/
- **Ollama Download**: https://ollama.ai/download

## One-Line Setup (after extraction)

**Linux/Mac:**
```bash
chmod +x setup.sh && ./setup.sh
```

**Windows (cmd):**
```cmd
setup.bat
```

**Windows (PowerShell):**
```powershell
.\setup.bat
```

## Testing the System

```bash
# Activate venv first!
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Run tests
python test_setup.py

# Try a simple task
python main.py
# Type: "Get weather in London"
```

## Remember

1. ✅ Always activate venv before running commands
2. ✅ Never commit .env or venv/ to git (they're in .gitignore!)
3. ✅ All APIs are FREE - no credit card needed
4. ✅ Read FREE_SETUP.md for getting API keys
5. ✅ Read WINDOWS_SETUP.md if on Windows
6. 🔒 Read SECURITY.md to understand how your keys are protected
