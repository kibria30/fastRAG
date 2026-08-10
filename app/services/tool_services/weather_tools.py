from langchain_core.tools import tool
import requests

URL = "https://api.open-meteo.com/v1/forecast"


def get_latitude_and_longitude_from_location(location: str):
    """
    A placeholder function to convert a location string into latitude and longitude.
    In a real implementation, you would use a geocoding service like OpenCage, Google Maps API, etc.
    """
    # For demonstration purposes, let's assume the location is always "Dhaka" and return its coordinates.
    if location.lower() == "dhaka":
        return 23.8103, 90.4125
    else:
        raise ValueError("Location not recognized. Please provide a valid location.")


@tool
def get_weather(location: str = "Dhaka"):
    """
    Get the current weather for a given location (defaults to Dhaka) using the Open-Meteo API.
    """
    try:
        latitude, longitude = get_latitude_and_longitude_from_location(location)
    except ValueError as exc:
        return {"error": str(exc)}

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError as exc:
            return {
                "error": "Weather service returned invalid or empty JSON.",
                "details": response.text[:200],
            }

        current_weather = data.get("current")
        if not current_weather:
            return {"error": "Weather service returned no current weather data."}

        return {
            "temperature": current_weather.get("temperature_2m"),
            "humidity": current_weather.get("relative_humidity_2m"),
            "wind_speed": current_weather.get("wind_speed_10m")
        }
    except requests.exceptions.RequestException as exc:
        return {"error": f"Error fetching weather data: {exc}"}

    