'''
recommender.py: This is where we map current weather to song mood/genre
'''

import get_music
import get_weather
import pandas as pd
import joblib

#testing - getMusic function 
#needs one argument - mood
# print(getMusic.get_songs('Sad'))





#uses trained decision tree model to predict user's mood using location weather
def map_weather_to_mood(user_weather_data):
    loaded_pipeline = joblib.load('dt_pipeline.pkl')

    input_df = pd.DataFrame([{
        "weather": user_weather_data["weather"],
        "weather_desc": user_weather_data["weather_desc"],
        "temperature": user_weather_data["temperature"]
    }])
    mood_prediction = loaded_pipeline.predict(input_df)
    return mood_prediction

#uses the music and weather functions to give song recs based on predicted mood
def recommend_music(user_location):
    # call get weather
    lat, lon = user_location['lat'], user_location['lon']
    weather_data = get_weather.getCurrentWeather(lat, lon)

    #calling the mapping - returns a numpy array need to access string with mood[0]
    mood = map_weather_to_mood(weather_data)

    #calling music
    songs_recommendations = get_music.get_songs(mood[0])
    return weather_data, mood[0], songs_recommendations


if __name__ == "__main__":

    #user location weather data
    loc = get_weather.getUserLocation()
    lat, lon = loc['lat'], loc['lon']
    weather_data = get_weather.getCurrentWeather(lat, lon)


    weather, user_mood, recommendations = recommend_music(loc)
    # print(weather)
    # print(user_mood)
    # print(recommendations)
    print("Predicted mood:", user_mood)
    print("Location:", weather['city'],',', weather['country'])
    print("Temperature:", weather['temperature'])
    print("Weather: ", weather['weather'],'\n')
    print("Song Recommendations: ", recommendations)
    # print("Song Recommednations: ", recommendations[0], '- ', recommendations['artist'], ': ', recommendations['link'])


#     #city, country, weather, weather_desc, temperature
#     #example output
#     #{'city': 'Rossmoor', 'country': 'United States', 'weather': 'Clouds', 'weather_desc': 'Clouds', 'temperature': 64.22}
   

