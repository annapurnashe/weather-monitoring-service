import requests
from app.config import Config

def fetch_weather(latitude, longitude):
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true'
    }
    
    try:
        response = requests.get(Config.WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current_weather = data.get('current_weather', {})
        
        return {
            'temperature': current_weather.get('temperature'),
            'wind_speed': current_weather.get('windspeed'),
            'weather_code': current_weather.get('weathercode')
        }
    except:
        return None