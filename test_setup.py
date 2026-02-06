"""
Test script to verify AI Operations Assistant setup
"""
import os
from dotenv import load_dotenv

load_dotenv()


def test_environment():
    """Test environment variables"""
    print("🔍 Testing Environment Variables...\n")
    
    # Check for at least ONE LLM provider
    llm_providers = {
        "GROQ_API_KEY": "Groq API Key (FREE - Recommended)",
        "GOOGLE_API_KEY": "Google Gemini API Key (FREE)",
        "OLLAMA_HOST": "Ollama Host (FREE - Local)",
        "OPENAI_API_KEY": "OpenAI API Key (Paid)"
    }
    
    llm_configured = False
    print("LLM Providers (need at least ONE):")
    for var, description in llm_providers.items():
        value = os.getenv(var)
        if value and value != f"your_{var.lower()}":
            print(f"✅ {description}: Configured")
            llm_configured = True
        else:
            print(f"⚪ {description}: Not configured")
    
    if not llm_configured:
        print("\n❌ No LLM provider configured!")
        print("   Get a FREE Groq key: https://console.groq.com/keys")
        print("   Or see FREE_SETUP.md for all options\n")
        return False
    
    print()
    
    # Required APIs
    required_vars = {
        "OPENWEATHER_API_KEY": "OpenWeather API Key (FREE)"
    }
    
    optional_vars = {
        "GITHUB_TOKEN": "GitHub Token (FREE - increases rate limits)"
    }
    
    all_good = True
    
    print("Required APIs:")
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value and value != f"your_{var.lower()}":
            print(f"✅ {description}: Configured")
        else:
            print(f"❌ {description}: Missing")
            all_good = False
    
    print("\nOptional APIs:")
    for var, description in optional_vars.items():
        value = os.getenv(var)
        if value and value != f"your_{var.lower()}":
            print(f"✅ {description}: Configured")
        else:
            print(f"⚪ {description}: Not configured (optional)")
    
    print()
    return all_good and llm_configured


def test_imports():
    """Test required imports"""
    print("📦 Testing Package Imports...\n")
    
    required_packages = [
        ("requests", "Requests"),
        ("dotenv", "Python-dotenv"),
        ("pydantic", "Pydantic"),
        ("fastapi", "FastAPI"),
        ("uvicorn", "Uvicorn")
    ]
    
    optional_packages = [
        ("groq", "Groq (FREE LLM)"),
        ("google.generativeai", "Google Gemini (FREE LLM)"),
        ("openai", "OpenAI (Paid LLM)")
    ]
    
    all_good = True
    
    print("Required packages:")
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name}: Installed")
        except ImportError:
            print(f"❌ {name}: Not installed")
            all_good = False
    
    print("\nLLM Provider packages (need at least ONE):")
    llm_found = False
    for package, name in optional_packages:
        try:
            __import__(package)
            print(f"✅ {name}: Installed")
            llm_found = True
        except ImportError:
            print(f"⚪ {name}: Not installed")
    
    if not llm_found:
        print("\n⚠️  No LLM provider package found!")
        print("   Install one: pip install groq  (recommended - FREE)")
    
    print()
    return all_good and llm_found


def test_agents():
    """Test agent imports"""
    print("🤖 Testing Agent Modules...\n")
    
    try:
        from agents.planner import planner_agent
        print("✅ Planner Agent: Ready")
    except Exception as e:
        print(f"❌ Planner Agent: Error - {e}")
        return False
    
    try:
        from agents.executor import executor_agent
        print("✅ Executor Agent: Ready")
    except Exception as e:
        print(f"❌ Executor Agent: Error - {e}")
        return False
    
    try:
        from agents.verifier import verifier_agent
        print("✅ Verifier Agent: Ready")
    except Exception as e:
        print(f"❌ Verifier Agent: Error - {e}")
        return False
    
    print()
    return True


def test_tools():
    """Test tool modules"""
    print("🔧 Testing Tool Modules...\n")
    
    try:
        from tools.github_tool import github_tool
        print("✅ GitHub Tool: Ready")
    except Exception as e:
        print(f"❌ GitHub Tool: Error - {e}")
        return False
    
    try:
        from tools.weather_tool import weather_tool
        print("✅ Weather Tool: Ready")
    except Exception as e:
        print(f"❌ Weather Tool: Error - {e}")
        return False
    
    print()
    return True


def test_llm():
    """Test LLM client"""
    print("🧠 Testing LLM Client...\n")
    
    try:
        from llm.llm_client import llm_client
        print(f"✅ LLM Client: Initialized (using {llm_client.provider})")
        
        # Check if API key is configured
        if llm_client.provider == "groq":
            if os.getenv("GROQ_API_KEY") and os.getenv("GROQ_API_KEY") != "your_groq_api_key_here":
                print("✅ Groq API Key: Configured")
                try:
                    response = llm_client.generate("Say 'test' in one word")
                    print("✅ LLM Client: Connection successful")
                except Exception as e:
                    print(f"⚠️  LLM Client: API call failed - {e}")
            else:
                print("⚠️  Groq API Key: Not configured")
                print("   Get FREE key: https://console.groq.com/keys")
        
        elif llm_client.provider == "gemini":
            if os.getenv("GOOGLE_API_KEY"):
                print("✅ Google Gemini API Key: Configured")
                try:
                    response = llm_client.generate("Say 'test' in one word")
                    print("✅ LLM Client: Connection successful")
                except Exception as e:
                    print(f"⚠️  LLM Client: API call failed - {e}")
            else:
                print("⚠️  Google API Key: Not configured")
        
        elif llm_client.provider == "ollama":
            print("✅ Ollama: Configured (local)")
            try:
                response = llm_client.generate("Say 'test' in one word")
                print("✅ LLM Client: Connection successful")
            except Exception as e:
                print(f"⚠️  Ollama: Not running or model not downloaded")
                print("   Run: ollama pull llama3.2")
        
        elif llm_client.provider == "openai":
            if os.getenv("OPENAI_API_KEY"):
                print("✅ OpenAI API Key: Configured")
            else:
                print("⚠️  OpenAI API Key: Not configured")
    
    except Exception as e:
        print(f"❌ LLM Client: Error - {e}")
        return False
    
    print()
    return True


def main():
    """Run all tests"""
    print("""
    ╔═══════════════════════════════════════════════╗
    ║   AI Operations Assistant - Setup Test        ║
    ╚═══════════════════════════════════════════════╝
    """)
    
    results = []
    
    results.append(("Environment", test_environment()))
    results.append(("Imports", test_imports()))
    results.append(("Agents", test_agents()))
    results.append(("Tools", test_tools()))
    results.append(("LLM", test_llm()))
    
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! System is ready to use.")
        print("\nRun 'python main.py' to start the CLI")
        print("or 'python api_server.py' to start the API server")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("1. Run: pip install groq  (for FREE LLM)")
        print("2. Get FREE Groq key: https://console.groq.com/keys")
        print("3. Create .env file with your API keys")
        print("4. See FREE_SETUP.md for detailed instructions")
    print("=" * 60)


if __name__ == "__main__":
    main()
