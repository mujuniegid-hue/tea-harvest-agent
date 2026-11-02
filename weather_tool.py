import requests

BUSHENYI_LAT = -0.54
BUSHENYI_LON = 30.19


def get_weather():
    """Get current weather and the next 6 hours of rain for Bushenyi."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": BUSHENYI_LAT,
        "longitude": BUSHENYI_LON,
        "current": "temperature_2m,relative_humidity_2m,precipitation",
        "hourly": "precipitation_probability,precipitation",
        "forecast_hours": 6,
        "timezone": "Africa/Kampala",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data["current"]
        hourly = data["hourly"]

        return {
            "location": "Bushenyi, Uganda",
            "temperature_c": current["temperature_2m"],
            "humidity_percent": current["relative_humidity_2m"],
            "raining_now": current["precipitation"] > 0,
            "rain_next_6h_mm": round(sum(hourly["precipitation"]), 1),
            "max_rain_chance_next_6h_percent": max(hourly["precipitation_probability"]),
        }
    except Exception as error:
        return {"error": f"Could not get weather data: {error}"}


if __name__ == "__main__":
    print(get_weather())