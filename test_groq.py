# Create a test file: test_groq.py
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

try:
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": "Say hello"}],
        temperature=0.7
    )
    print("✅ Groq working!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ Error: {e}")