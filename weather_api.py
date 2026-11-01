import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("API key is missing.")
else:
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": "Tokyo",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])

    except requests.exceptions.RequestException as error:
        print("Error:", error)
