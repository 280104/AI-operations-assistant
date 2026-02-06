@echo off
REM AI Operations Assistant - Setup Script for Windows

echo ╔═══════════════════════════════════════════════╗
echo ║   AI Operations Assistant Setup               ║
echo ╚═══════════════════════════════════════════════╝
echo.

REM Check Python version
echo 1️⃣  Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+
    exit /b 1
)
echo ✅ Python found
echo.

REM Create virtual environment
echo 2️⃣  Creating virtual environment...
python -m venv venv
echo ✅ Virtual environment created
echo.

REM Activate virtual environment
echo 3️⃣  Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Upgrade pip
echo 4️⃣  Upgrading pip...
python -m pip install --upgrade pip
echo ✅ pip upgraded
echo.

REM Install dependencies
echo 5️⃣  Installing dependencies...
pip install -r requirements.txt
echo ✅ Dependencies installed
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo 6️⃣  Creating .env file...
    copy .env.example .env
    echo ✅ .env file created
    echo.
    echo ⚠️  IMPORTANT: Edit .env file and add your API keys!
    echo.
) else (
    echo 6️⃣  .env file already exists
    echo.
)

REM Run setup test
echo 7️⃣  Running setup tests...
python test_setup.py
echo.

echo ╔═══════════════════════════════════════════════╗
echo ║   Setup Complete!                             ║
echo ╚═══════════════════════════════════════════════╝
echo.
echo Next steps:
echo 1. Edit .env file with your API keys
echo 2. Run: venv\Scripts\activate  (to activate venv)
echo 3. Run: python main.py  (to start CLI)
echo.
echo To deactivate virtual environment later:
echo    deactivate
echo.
pause
