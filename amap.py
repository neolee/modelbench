import os
import requests


api_key = os.getenv('AMAP_API_KEY')

if not api_key:
    raise ValueError("missing environment var AMAP_API_KEY")

base_url = "https://restapi.amap.com/v3/weather/weatherInfo"

def weather_info(city: str) -> dict | None:
    """
    get weather info for city

    :param city: city name or adcode
    :return: a `dict` containing weather info
    """
    params = {
        'key': api_key,
        'city': city
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    try:
        data = weather_info("浦东新区")
        print(data)
    except Exception as e:
        print(f"Error: {e}")
