"""
Weather Tool for fetching current weather information
"""
import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


class WeatherTool:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city: str, units: str = "metric") -> Dict[str, Any]:
        """
        Get current weather for a city
        
        Args:
            city: City name (e.g., "San Francisco" or "London,UK")
            units: Temperature units (metric, imperial, standard)
        
        Returns:
            Weather information dictionary
        """
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant information
            weather_info = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "temp_min": data["main"]["temp_min"],
                "temp_max": data["main"]["temp_max"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "weather": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "clouds": data["clouds"]["all"],
                "units": "°C" if units == "metric" else "°F" if units == "imperial" else "K"
            }
            
            return weather_info
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Weather API Error: {str(e)}")
    
    def get_forecast(self, city: str, units: str = "metric") -> Dict[str, Any]:
        """
        Get 5-day weather forecast for a city
        
        Args:
            city: City name
            units: Temperature units
        
        Returns:
            Forecast information
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract forecast for next 5 days (taking one per day)
            forecasts = []
            seen_dates = set()
            
            for item in data["list"]:
                date = item["dt_txt"].split()[0]
                if date not in seen_dates and len(forecasts) < 5:
                    seen_dates.add(date)
                    forecasts.append({
                        "date": date,
                        "temperature": item["main"]["temp"],
                        "weather": item["weather"][0]["main"],
                        "description": item["weather"][0]["description"]
                    })
            
            return {
                "city": data["city"]["name"],
                "country": data["city"]["country"],
                "forecasts": forecasts,
                "units": "°C" if units == "metric" else "°F" if units == "imperial" else "K"
            }
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Weather API Error: {str(e)}")


# Singleton instance
weather_tool = WeatherTool()
