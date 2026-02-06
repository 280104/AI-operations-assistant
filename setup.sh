#!/bin/bash

# AI Operations Assistant - Setup Script with Virtual Environment

echo "╔═══════════════════════════════════════════════╗"
echo "║   AI Operations Assistant Setup               ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "1️⃣  Checking Python version..."
python3 --version || { echo "❌ Python 3 not found. Please install Python 3.8+"; exit 1; }
echo "✅ Python found"
echo ""

# Create virtual environment
echo "2️⃣  Creating virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created"
echo ""

# Activate virtual environment
echo "3️⃣  Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "4️⃣  Upgrading pip..."
pip install --upgrade pip
echo "✅ pip upgraded"
echo ""

# Install dependencies
echo "5️⃣  Installing dependencies..."
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "6️⃣  Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys!"
    echo ""
else
    echo "6️⃣  .env file already exists"
    echo ""
fi

# Run setup test
echo "7️⃣  Running setup tests..."
python test_setup.py
echo ""

echo "╔═══════════════════════════════════════════════╗"
echo "║   Setup Complete!                             ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Run: source venv/bin/activate  (to activate venv)"
echo "3. Run: python main.py  (to start CLI)"
echo ""
echo "To deactivate virtual environment later:"
echo "   deactivate"
echo ""
