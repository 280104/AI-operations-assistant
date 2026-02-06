"""
LLM Client supporting multiple FREE providers:
- Groq (FREE, fast)
- Google Gemini (FREE tier)
- Ollama (FREE, local)
- OpenAI (paid backup)
"""
import os
import json
import requests
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        # Choose provider based on available API keys
        self.provider = self._detect_provider()
        self._setup_client()
    
    def _detect_provider(self) -> str:
        """Detect which LLM provider to use based on environment variables"""
        if os.getenv("GROQ_API_KEY"):
            return "groq"  # FREE and fast!
        elif os.getenv("GOOGLE_API_KEY"):
            return "gemini"  # FREE tier available
        elif os.getenv("OLLAMA_HOST"):
            return "ollama"  # FREE, runs locally
        elif os.getenv("OPENAI_API_KEY"):
            return "openai"  # Paid
        else:
            # Default to Groq with placeholder (user needs to get free key)
            return "groq"
    
    def _setup_client(self):
        """Setup client based on provider"""
        if self.provider == "groq":
            from groq import Groq
            self.client = Groq(api_key=os.getenv("GROQ_API_KEY", ""))
            self.model = "llama-3.3-70b-versatile" # FREE Groq model
        elif self.provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY", ""))
            self.client = genai.GenerativeModel('gemini-1.5-flash')  # FREE tier
            self.model = "gemini-1.5-flash"
        elif self.provider == "ollama":
            self.base_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
            self.model = "llama3.2"  # FREE local model
        elif self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = "gpt-4o-mini"
    
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        json_mode: bool = False,
        temperature: float = 0.7
    ) -> str:
        """
        Generate a response from the LLM
        
        Args:
            prompt: User prompt
            system_prompt: System instructions
            json_mode: Enable JSON response format
            temperature: Sampling temperature
        
        Returns:
            LLM response as string
        """
        try:
            if self.provider == "groq":
                return self._generate_groq(prompt, system_prompt, json_mode, temperature)
            elif self.provider == "gemini":
                return self._generate_gemini(prompt, system_prompt, json_mode, temperature)
            elif self.provider == "ollama":
                return self._generate_ollama(prompt, system_prompt, json_mode, temperature)
            elif self.provider == "openai":
                return self._generate_openai(prompt, system_prompt, json_mode, temperature)
        except Exception as e:
            raise Exception(f"LLM API Error ({self.provider}): {str(e)}")
    
    def _generate_groq(self, prompt, system_prompt, json_mode, temperature) -> str:
        """Generate using Groq (FREE)"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        
        response = self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content
    
    def _generate_gemini(self, prompt, system_prompt, json_mode, temperature) -> str:
        """Generate using Google Gemini (FREE)"""
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        if json_mode:
            full_prompt += "\n\nRespond ONLY with valid JSON."
        
        response = self.client.generate_content(
            full_prompt,
            generation_config={"temperature": temperature}
        )
        return response.text
    
    def _generate_ollama(self, prompt, system_prompt, json_mode, temperature) -> str:
        """Generate using Ollama (FREE, local)"""
        url = f"{self.base_url}/api/generate"
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        if json_mode:
            full_prompt += "\n\nRespond ONLY with valid JSON."
        
        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
            "temperature": temperature
        }
        
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()["response"]
    
    def _generate_openai(self, prompt, system_prompt, json_mode, temperature) -> str:
        """Generate using OpenAI (paid)"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        
        response = self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content
    
    def generate_json(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate and parse JSON response from LLM
        
        Args:
            prompt: User prompt
            system_prompt: System instructions
        
        Returns:
            Parsed JSON as dictionary
        """
        response = self.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            json_mode=True,
            temperature=0.3  # Lower temperature for structured output
        )
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            raise Exception(f"Failed to parse LLM response as JSON: {response}")


# Singleton instance
llm_client = LLMClient()
