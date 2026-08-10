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
    Get the current weather for a given location(keep it by default dhaka as latitude and longitude are only given Dhaka only) using the Open-Meteo API.
    """
    latitude, longitude = get_latitude_and_longitude_from_location(location)
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }
    
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        current_weather = data["current"]
        
        return {
            "temperature": current_weather["temperature_2m"],
            "humidity": current_weather["relative_humidity_2m"],
            "wind_speed": current_weather["wind_speed_10m"]
        }
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching weather data: {e}")

    