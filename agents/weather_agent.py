import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Read from .env
    if not api_key:
        return "❌ Missing API key. Please set OPENWEATHER_API_KEY in .env file."

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url).json()

        # Handle invalid city or errors
        if res.get("cod") != 200:
            return f"❌ Error: {res.get('message', 'Unable to fetch weather data.')}"
        
        temp = res["main"]["temp"]
        condition = res["weather"][0]["description"].title()
        return f"🌦 Weather in {city.title()}: {temp}°C, {condition}"

    except Exception as e:
        return f"❌ Unable to fetch weather data. ({str(e)})"
