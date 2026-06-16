import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    try:

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={WEATHER_API_KEY}"
            "&units=metric"
        )

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return {
                "success": False,
                "message": "City not found"
            }

        weather_info = {
            "success": True,
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }


def get_farming_advice(weather_data):

    if not weather_data.get("success"):
        return "Weather information unavailable."

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]

    advice = []

    if temperature > 35:
        advice.append(
            "High temperature detected. Increase irrigation if required."
        )

    elif temperature < 15:
        advice.append(
            "Low temperature detected. Protect sensitive crops."
        )

    if humidity > 80:
        advice.append(
            "High humidity may increase fungal disease risk."
        )

    elif humidity < 30:
        advice.append(
            "Low humidity detected. Monitor soil moisture."
        )

    if not advice:
        advice.append(
            "Current weather conditions appear suitable for most field activities."
        )

    return " ".join(advice)