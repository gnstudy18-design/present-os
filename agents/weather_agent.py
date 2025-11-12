import requests

def get_weather(city):
    api_key = "your_openweather_api_key"
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url).json()
        temp = res["main"]["temp"]
        condition = res["weather"][0]["description"].title()
        return f"🌦 Weather in {city.title()}: {temp}°C, {condition}"
    except:
        return "❌ Unable to fetch weather data."
