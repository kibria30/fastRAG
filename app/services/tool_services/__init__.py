from app.services.tool_services.weather_tools import get_weather

WEATHER_TOOLS = [
    get_weather,
]

TOOLS = [
    *WEATHER_TOOLS
]