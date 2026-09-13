import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
           print("Unable to get weather information.")
           print("Status Code:", response.status_code)
           print("Error:", data)
           return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n=== Weather Information ===")
        print(f"City: {city}")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
    except (KeyError, ValueError):
        print("Unable to process weather data.")


print("=== Basic Weather App ===")

city = input("Enter city name or ZIP code: ").strip()

if not city:
    print("City or ZIP code cannot be empty.")
elif not API_KEY:
    print("API key not found. Please check your .env file.")
else:
    get_weather(city)