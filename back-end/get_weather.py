'''
get_weather.py: get local weather from weather API (e.g., OpenWeather API)
'''

import os
import requests
import pycountry
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')


# get the current location of the user by using geolocation API
def getUserLocation():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception("Failed to get user location")

    return {
        "lat": data["lat"],
        "lon": data["lon"]
    }

# the function to get current weather data based on user's location
def getCurrentWeather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "imperial"
    }
    # get the response from API call
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        raise Exception("Failed to get weather data")

    return {
        "city": data["name"],
        "country": pycountry.countries.get(alpha_2=data["sys"]["country"]).name,
        "weather": data["weather"][0]["main"],
        "weather_desc": data["weather"][0]["main"],
        "temperature": data["main"]["temp"]
    }


if __name__ == "__main__":
    user_location = getUserLocation()
    data = getCurrentWeather(user_location["lat"], user_location["lon"])
    # data = getCurrentWeather(13.74, 100.49)
    print(data)
